import math
import tempfile
import unittest
from pathlib import Path

from stocktrack import ledger as led
from stocktrack import vault as vlt
from stocktrack.backtest import Calendar, Ev, build_events, run_backtest
from stocktrack.history import PriceHistory
from tests.test_backtest import business_days
from tests.test_signals import make_buy

DAYS = business_days("2014-01-01", 900)  # spans the 2015/2016 discovery-holdout split


def series(k: int) -> PriceHistory:
    """A deterministic wiggly price series per company."""
    closes = [20 * (1 + 0.0004 * k) ** i * (1 + 0.02 * math.sin(i / (5 + k))) for i in range(len(DAYS))]
    opens = [c * 0.999 for c in closes]
    return PriceHistory(f"T{k}", list(DAYS), opens, closes, [5e7] * len(DAYS), list(closes))


class FakeStore:
    def __init__(self):
        self.hist = {f"T{k}": series(k) for k in range(6)}
        flat = [100 * 1.0002 ** i for i in range(len(DAYS))]
        self.hist["SPY"] = PriceHistory("SPY", list(DAYS), flat, flat, [1e10] * len(DAYS), flat)

    def load(self, sym):
        return self.hist.get(sym)

    def get(self, sym, refresh=False):
        return self.hist.get(sym)


class FakeTickers:
    def resolve(self, cik, ticker):
        return (ticker, "filing") if ticker else (None, "unlisted")

    def exchange(self, cik):
        return "NYSE"


def synthetic_buys():
    store = FakeStore()
    buys, n = [], 0
    for i in range(5, len(DAYS) - 300, 3):
        k = i % 6
        n += 1
        price = store.hist[f"T{k}"].close[i - 1]
        buys.append(make_buy(accession=f"acc{n}", issuer_cik=str(100 + k), ticker=f"T{k}", owner_cik=str(n % 40),
                             owner_name=f"Insider {n % 40}", role=["CEO", "Director", "CFO"][n % 3],
                             last_date=DAYS[i - 1], first_date=DAYS[i - 1], filed_at=DAYS[i], avg_price=price,
                             shares=1000 + n, value=(1000 + n) * price))
    return buys, store


class PipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        buys, cls.store = synthetic_buys()
        cls.evs, cls.cal, cls.meta = build_events(buys, cls.store, FakeTickers())
        cls.res = run_backtest(cls.evs, cls.cal, echo=lambda *a: None)
        cls.res["meta"] = {"run_date": DAYS[-1], "git_commit": "test", "config_hash": "x", "seed": 1, **cls.meta}

    def test_backtest_shape(self):
        r = self.res
        self.assertEqual(r["coverage"]["status"].get("priced"), len(self.evs))
        self.assertGreater(r["overall"]["events"]["63"]["n"], 100)
        self.assertIn("role", r["slices"])
        self.assertIn("verdict", next(iter(r["slices"]["role"].values())))
        self.assertGreater(r["strategies"]["all_liquid"]["portfolio"]["63d"]["trades"], 0)

    def test_no_survivor_benchmark_while_the_index_is_thin(self):
        self.assertFalse(any(e.abn_ew for e in self.evs))  # six stocks never make a 100-stock index
        buys, store = synthetic_buys()
        evs, _, _ = build_events(buys, store, FakeTickers(), min_members=0)
        self.assertTrue(any(e.abn_ew for e in evs))

    def test_ledger_roundtrip_and_outcomes(self):
        ev = next(e for e in self.evs if e.priced)
        row = led.new_row(ev, logged=ev.filed)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "picks.csv"
            led.save(path, [row])
            rows = led.load(path)
        self.assertEqual(rows[0]["accession"], ev.buy.accession)
        self.assertEqual(led.to_buy(rows[0]).shares, ev.buy.shares)
        changed, matured = led.update_outcomes(rows, self.store, self.cal, refresh=False)
        self.assertEqual(changed, 1)
        self.assertEqual(rows[0]["entry_date"], ev.entry_date)
        self.assertEqual(rows[0]["status"], "closed")  # a year of data after entry
        self.assertEqual({h for h, _ in matured}, set(led.LEDGER_HORIZONS))
        self.assertAlmostEqual(rows[0]["abn_63"], ev.abn[63], places=6)
        self.assertEqual(led.update_outcomes(rows, self.store, self.cal, refresh=False), (0, []))

    def test_forward_means_logged_before_the_entry_open(self):
        def row(logged, entry):
            return {"logged": logged, "entry_date": entry}

        self.assertTrue(led.is_forward(row("2026-10-20T11:00:00Z", "2026-10-20")))  # morning run, before 9:30 ET
        self.assertFalse(led.is_forward(row("2026-10-20T20:05:00Z", "2026-10-20")))  # evening run, after the open
        self.assertTrue(led.is_forward(row("2026-10-20T20:05:00Z", "2026-10-21")))
        self.assertFalse(led.is_forward(row("2026-10-20T11:00:00Z", "")))  # not entered yet
        self.assertFalse(led.is_forward(row("2026-10-20", "2026-10-20")))  # date only: assume end of day
        self.assertTrue(led.is_forward(row("2026-10-19", "2026-10-20")))

    def test_forward_test_excludes_late_logged_rows(self):
        ev = next(e for e in self.evs if e.priced)
        on_time = dict(led.new_row(ev, logged=ev.filed), entry_date=ev.entry_date, abn_21=0.05)
        late = dict(led.new_row(ev, logged="2099-01-01"), entry_date=ev.entry_date, abn_21=-0.5)
        stats = vlt.forward_by_strategy([on_time, late])["all"]
        self.assertEqual(stats["rows"], 1)
        self.assertAlmostEqual(stats["21"]["mean"], 0.05)

    def test_forward_test_counts_one_signal_per_company_day(self):
        ev = next(e for e in self.evs if e.priced)
        first = dict(led.new_row(ev, logged=ev.filed), entry_date=ev.entry_date, abn_21=0.05)
        same_day = dict(first, accession="other", owner_cik="999", owner_name="Another Insider")
        next_day = dict(first, accession="later", entry_date=DAYS[DAYS.index(ev.entry_date) + 1], abn_21=-0.01)
        stats = vlt.forward_by_strategy([first, same_day, next_day])["all"]
        self.assertEqual(stats["rows"], 2)
        self.assertAlmostEqual(stats["21"]["mean"], 0.02)

    def test_vault_build(self):
        ev = [e for e in self.evs if e.priced and e.score >= 40][-1]
        today = ev.filed  # signal notes cover the last 400 days
        row = led.new_row(ev, logged=ev.filed)
        led.update_outcomes([row], self.store, self.cal, refresh=False)
        with tempfile.TemporaryDirectory() as d:
            n = vlt.build_vault(d, self.res, [row], {}, today=today)
            root = Path(d)
            self.assertGreater(n, 20)
            for rel in ("Home.md", "What Works.md", "Methodology.md", f"Backtests/{DAYS[-1]} Backtest.md",
                        f"Research Log/{today}.md", f"Tickers/{ev.symbol}.md"):
                self.assertTrue((root / rel).exists(), rel)
            works = (root / "What Works.md").read_text()
            self.assertTrue(works.startswith("---\ntype: \"scoreboard\""))
            self.assertIn("## Kinds of insider buy", works)
            signals = list((root / "Signals").glob("*.md"))
            self.assertEqual(len(signals), 1)
            self.assertIn(f"ticker: \"{ev.symbol}\"", signals[0].read_text())

            # Notes written under "## Notes" in a log survive regeneration
            log = root / "Research Log" / f"{today}.md"
            log.write_text(log.read_text() + "My observation.\n")
            vlt.build_vault(d, self.res, [row], {}, today=today)
            self.assertIn("My observation.", log.read_text())

            # Rebuilding without a run (the `research vault` action) keeps the day's run summary
            vlt.build_vault(d, self.res, [row], {}, today=today, run_summary={"new insider buys": 7})
            vlt.build_vault(d, self.res, [row], {}, today=today)
            self.assertIn("- new insider buys: 7", log.read_text())
            self.assertIn("My observation.", log.read_text())


class ReusedTickers:
    """Issuer 900 once used ticker T1 (its filings don't match T1's prices); issuer 901 trades as T1 now."""

    def resolve(self, cik, ticker):
        return ("T1", "reused") if cik == "900" else ("T1", "filing")

    def exchange(self, cik):
        return "NYSE"


class EdgeCaseTest(unittest.TestCase):
    def test_placebo_event_side_uses_every_eligible_event(self):
        from stocktrack.backtest import _placebo

        evs = [Ev(buy=make_buy(), filed=DAYS[0]) for _ in range(3)]
        evs[0].abn, evs[0].placebo_all, evs[0].placebo = {63: 0.10}, 0.0, None  # placebo window overlapped
        evs[1].abn, evs[1].placebo_all, evs[1].placebo = {63: -0.10}, 0.02, 0.02
        evs[2].abn = {63: 0.5}  # no placebo window in the data: not eligible
        p = _placebo(evs, (-1, 1))
        self.assertEqual((p["n"], p["n_placebo"]), (2, 1))
        self.assertAlmostEqual(p["event_mean"], 0.0)
        self.assertAlmostEqual(p["difference"], -0.02)
        self.assertAlmostEqual(p["difference_no_exclusion"], (0.10 - 0.0 + -0.10 - 0.02) / 2)

    def test_reused_ticker_needs_consistent_matches_and_starts_index_at_own_filings(self):
        store = FakeStore()
        hist = store.hist["T1"]
        buys = []
        for n, i in enumerate(range(20, 120, 20)):  # the old company: 1 of 5 filings matches by chance
            price = hist.close[i - 1] * (1.0 if n == 0 else 5.0)
            buys.append(make_buy(accession=f"old{n}", issuer_cik="900", ticker="T1", last_date=DAYS[i - 1],
                                 first_date=DAYS[i - 1], filed_at=DAYS[i], avg_price=price))
        buys.append(make_buy(accession="old-unverified", issuer_cik="900", ticker="T1", last_date=DAYS[130],
                             first_date=DAYS[130], filed_at=DAYS[131], avg_price=None))
        buys.append(make_buy(accession="new", issuer_cik="901", ticker="T1", last_date=DAYS[399],
                             first_date=DAYS[399], filed_at=DAYS[400], avg_price=hist.close[399]))
        evs, cal, _ = build_events(buys, store, ReusedTickers(), min_members=1)
        status = {e.buy.accession: e.status for e in evs}
        self.assertTrue(all(status[f"old{n}"] == "price_mismatch" for n in range(5)))
        self.assertEqual(status["old-unverified"], "unverified")  # never compared, so not relabelled
        self.assertEqual(status["new"], "priced")
        # The index holds T1 only from the current company's first filing, not the old company's.
        self.assertEqual(sum(cal.ew_count[:401]), 0)

    def test_ledger_row_stopped_by_a_data_break(self):
        store = FakeStore()
        h = store.hist["T2"]
        closes = list(h.close[:300]) + [c * 4 for c in h.close[300:]]  # a missed 1:4 reverse split
        store.hist["T2"] = PriceHistory("T2", list(DAYS), closes, closes, [5e7] * len(DAYS), closes)
        cal = Calendar(store.hist["SPY"])
        buy = make_buy(accession="x", issuer_cik="102", ticker="T2", last_date=DAYS[249], first_date=DAYS[249],
                       filed_at=DAYS[250], avg_price=closes[249])
        ev = Ev(buy=buy, filed=DAYS[250], symbol="T2")
        row = led.new_row(ev, logged=DAYS[250])
        led.update_outcomes([row], store, cal, refresh=False)
        self.assertEqual(row["status"], "break")
        self.assertEqual(row["last_seen"], DAYS[299])  # marked to the bar before the break
        self.assertIsNotNone(row["abn_21"])
        self.assertIsNone(row["abn_63"])
        self.assertEqual(led.update_outcomes([row], store, cal, refresh=False), (0, []))

    def test_failed_price_download_leaves_the_row_alone(self):
        class Failing(FakeStore):
            def get(self, sym, refresh=False):
                raise OSError("network down")

        store = Failing()
        ev = Ev(buy=make_buy(ticker="T0", filed_at=DAYS[10]), filed=DAYS[10], symbol="T0")
        row = led.new_row(ev, logged=DAYS[10])
        before = dict(row)
        self.assertEqual(led.update_outcomes([row], store, Calendar(store.hist["SPY"]), refresh=False), (0, []))
        self.assertEqual(row, before)


class FormatTest(unittest.TestCase):
    def test_helpers(self):
        self.assertEqual(vlt.safe('A/B: "C"?'), "A-B- -C--")
        self.assertEqual(vlt.yaml_value(['a', 1, None]), '["a", 1, ]')
        self.assertEqual(vlt.pct(0.1234), "+12.3%")
        self.assertEqual(vlt.pct(None), "–")
        self.assertEqual(vlt.pval(0.0001), "<0.001")


if __name__ == "__main__":
    unittest.main()
