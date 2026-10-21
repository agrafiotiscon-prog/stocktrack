import datetime as dt
import math
import unittest
from array import array

from stocktrack.backtest import (
    MAX_STALE,
    PRIMARY,
    Calendar,
    Ev,
    add_pit_features,
    align,
    attach_market_data,
    block_bootstrap,
    calendar_time,
    event_stats,
    holm,
    newey_west_t,
    simulate,
    unique_signals,
    walk_forward,
)
from stocktrack.history import PriceHistory
from tests.test_signals import make_buy


def business_days(start: str, n: int) -> list[str]:
    d, out = dt.date.fromisoformat(start), []
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d += dt.timedelta(days=1)
    return out


DAYS = business_days("2020-01-01", 400)


def flat_spy(days=DAYS, price=100.0) -> PriceHistory:
    n = len(days)
    return PriceHistory("SPY", list(days), [price] * n, [price] * n, [1e9] * n, [price] * n)


def stock(days, opens, closes, raw=None, dollar_volume=5e6) -> PriceHistory:
    raw = raw or closes
    return PriceHistory("ACME", list(days), list(opens), list(closes), [dollar_volume] * len(days), list(raw))


def ev_for(filed: str, **buy_kw) -> Ev:
    buy_kw.setdefault("last_date", filed)
    buy_kw.setdefault("avg_price", 10.0)
    return Ev(buy=make_buy(filed_at=filed, **buy_kw), filed=filed)


class MarketDataTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calendar(flat_spy())

    def test_entry_is_next_open_after_filing(self):
        closes = [10 + k for k in range(len(DAYS))]
        opens = [c - 0.5 for c in closes]
        h = stock(DAYS, opens, closes)
        ev = ev_for(DAYS[10], last_date=DAYS[8], avg_price=18.0, shares=100)
        attach_market_data(ev, h, self.cal)
        self.assertEqual(ev.status, "priced")
        self.assertEqual((ev.entry_date, ev.entry_cal), (DAYS[11], 11))
        self.assertAlmostEqual(ev.ret[1], closes[11] / opens[11] - 1)
        self.assertAlmostEqual(ev.ret[5], closes[15] / opens[11] - 1)
        self.assertAlmostEqual(ev.ret[63], closes[11 + 62] / opens[11] - 1)
        self.assertEqual(ev.exit_cal[5], 15)
        self.assertAlmostEqual(ev.abn[63], ev.ret[63])  # flat SPY
        self.assertAlmostEqual(ev.abn_c[63], closes[73] / closes[11] - 1)  # variant C: entry at day-e close
        self.assertAlmostEqual(ev.price, closes[10])
        self.assertAlmostEqual(ev.price_ratio, 1.0)
        self.assertAlmostEqual(ev.pre_drift, opens[11] / closes[8] - 1)

    def test_price_mismatch_is_rejected(self):
        h = stock(DAYS, [10.0] * 400, [10.0] * 400)
        ev = ev_for(DAYS[10], avg_price=40.0)  # 4x the market: wrong security or a typo
        attach_market_data(ev, h, self.cal)
        self.assertEqual(ev.status, "price_mismatch")
        self.assertEqual(ev.ret, {})
        unpriced = ev_for(DAYS[10], avg_price=None)
        attach_market_data(unpriced, h, self.cal)
        self.assertEqual(unpriced.status, "unverified")
        typo = ev_for(DAYS[10], last_date=DAYS[200])  # trade dated after its own filing
        attach_market_data(typo, h, self.cal)
        self.assertEqual(typo.status, "bad_trade_date")

    def test_survivor_index_membership(self):
        from stocktrack.backtest import EWAccumulator, _add_to_ew

        closes = [10 * 1.01 ** k for k in range(200)]
        h = stock(DAYS[:200], closes, closes)
        acc = EWAccumulator(400)
        _add_to_ew(h, self.cal, acc, start_cal=40, own_entries=[40, 120])
        member = [c for c in range(400) if acc.count[c]]
        self.assertEqual(member[0], 103)  # joins only after its first filing is public...
        self.assertNotIn(120, member)  # ...and its own post-signal windows are left out
        self.assertNotIn(182, member)
        self.assertIn(183, member)  # until 63 sessions after entry
        self.assertEqual(member[-1], 199)
        # Point in time: a member is held overnight into its own entry session and sold at the open...
        self.assertAlmostEqual(acc.num[120] / acc.den[120], closes[120] / closes[119] - 1)
        self.assertEqual(acc.intra[120], 0.0)
        # ...but a stock that wasn't a member the day before (its first filing) earns nothing that night.
        self.assertEqual(acc.den[40], 0.0)

    def test_thin_survivor_index_is_not_a_benchmark(self):
        from stocktrack.backtest import EWAccumulator, _add_to_ew

        acc = EWAccumulator(400)
        for k in range(3):
            closes = [10 * (1 + 0.001 * k) ** i for i in range(400)]
            start = 0 if k < 2 else 100  # three stocks from session 100, two before
            _add_to_ew(stock(DAYS, closes, closes), self.cal, acc, start, [])
        self.cal.finish_ew(acc, min_members=3)
        self.assertFalse(self.cal.ew_usable(30, 92))
        self.assertTrue(self.cal.ew_usable(130, 192))
        self.assertIn(DAYS[30][:7], self.cal.ew_thin_months)
        self.assertNotIn(DAYS[130][:7], self.cal.ew_thin_months)
        evs = []
        for k in range(0, 300, 7):
            e = ev_for(DAYS[k], avg_price=10.0)
            e.buy.issuer_cik = str(k)
            attach_market_data(e, stock(DAYS, [10.0] * 400, [10.0] * 400), self.cal)
            evs.append(e)
        months = {m for m, _, _ in calendar_time(evs, self.cal, min_positions=1, bench="ew")["series"]}
        self.assertTrue(months)
        self.assertFalse(months & self.cal.ew_thin_months)

    def test_survivor_index_is_buy_and_hold(self):
        from stocktrack.backtest import EWAccumulator, _add_to_ew

        n = 60  # one stock bouncing 10 -> 11 -> 10, one flat: no buy-and-hold gain
        bounce = [10.0 if k % 2 == 0 else 11.0 for k in range(n)]
        acc = EWAccumulator(400)
        _add_to_ew(stock(DAYS[:n], bounce, bounce), self.cal, acc, 0, [])
        _add_to_ew(stock(DAYS[:n], [10.0] * n, [10.0] * n), self.cal, acc, 0, [])
        self.cal.finish_ew(acc)
        month = [c for c in range(n) if DAYS[c][:7] == "2020-02" and acc.count[c]]
        level = 1.0
        for c in month:
            level *= 1 + self.cal.ew_daily[c]
        self.assertLess(abs(level - 1), 0.03)  # a daily-rebalanced average would compound to ~+50%

    def test_data_break_censors_returns(self):
        closes = [2.0] * 30 + [16.0] * 370  # an 8x step on normal volume: an unadjusted reverse split
        h, _ = align(stock(DAYS, closes, closes), self.cal)
        self.assertEqual(h.breaks, [DAYS[30]])
        ev = ev_for(DAYS[10], avg_price=2.0)
        attach_market_data(ev, h, self.cal)
        self.assertIn(5, ev.ret)
        self.assertNotIn(21, ev.ret)  # the window would span the break
        self.assertEqual(len(ev.path), 30 - 11)

    def test_news_jump_is_kept(self):
        closes = [2.0] * 30 + [16.0] * 370
        h = stock(DAYS, closes, closes)
        h.dollar_volume_day[30] = 5e8  # a real 8x move trades heavily
        self.assertEqual(align(h, self.cal)[0].breaks, [])

    def test_crash_is_kept_but_missed_split_is_a_break(self):
        # A real crash: opens down, keeps falling during the day; dollar volume ends near normal.
        closes = [8.0] * 30 + [2.2] * 370
        opens = [8.0] * 30 + [5.4] + [2.2] * 369
        crash = stock(DAYS, opens, closes)
        crash.dollar_volume_day[30] = 7e6  # 1.4x normal dollar volume, about 5x the shares
        h, _ = align(crash, self.cal)
        self.assertEqual(h.breaks, [])
        ev = ev_for(DAYS[10], avg_price=8.0)
        attach_market_data(ev, h, self.cal)
        self.assertAlmostEqual(ev.ret[63], 2.2 / 8.0 - 1)  # the loss is recorded, not censored
        # A missed 4:1 split: the whole step in the opening gap, flat after, ordinary dollar volume.
        closes = [40.0] * 30 + [10.0] * 370
        self.assertEqual(align(stock(DAYS, closes, closes), self.cal)[0].breaks, [DAYS[30]])

    def test_heavily_traded_spike_is_kept(self):
        closes = [10.0, 10.0, 50.0, 10.0, 10.0]
        h = stock(DAYS[:5], closes, closes)
        h.dollar_volume_day[2] = 5e8  # a real squeeze, 100x normal dollar volume
        h, repaired = align(h, self.cal)
        self.assertEqual(repaired, 0)
        self.assertEqual(h.close, closes)

    def test_placebo_is_censored_at_a_break(self):
        from stocktrack.backtest import placebo_ar

        closes = [2.0] * 30 + [16.0] * 370
        h, _ = align(stock(DAYS, closes, closes), self.cal)
        self.assertIsNone(placebo_ar(h, self.cal, 10))  # the window spans the unadjusted split
        self.assertIsNotNone(placebo_ar(h, self.cal, 40))

    def test_multi_bar_bad_tick(self):
        closes = [10.0, 10.0, 1.0, 1.1, 10.0, 10.0]  # two-bar dip to a tenth
        h, dropped = align(stock(DAYS[:6], closes, closes), self.cal)
        self.assertEqual(dropped, 2)
        self.assertEqual(h.close, [10.0] * 4)

    def test_abnormal_subtracts_spy_same_window(self):
        spy_close = [100 * 1.001 ** k for k in range(len(DAYS))]
        cal = Calendar(PriceHistory("SPY", DAYS, spy_close, spy_close, [1e9] * len(DAYS), spy_close))
        h = stock(DAYS, [10.0] * len(DAYS), [11.0] * len(DAYS), raw=[10.0] * len(DAYS))
        ev = ev_for(DAYS[0])
        attach_market_data(ev, h, cal)
        self.assertAlmostEqual(ev.abn[21], 0.1 - (spy_close[21] / spy_close[1] - 1))

    def test_immature_and_delisted_horizons_are_missing(self):
        h = stock(DAYS[:40], [10.0] * 40, [10.0] * 40)
        ev = ev_for(DAYS[0])
        attach_market_data(ev, h, self.cal)
        self.assertIn(21, ev.ret)
        self.assertNotIn(63, ev.ret)
        late = ev_for(DAYS[-3])
        attach_market_data(late, stock(DAYS, [10.0] * 400, [10.0] * 400), self.cal)
        self.assertIn(1, late.ret)
        self.assertNotIn(5, late.ret)

    def test_stale_entry_is_skipped(self):
        days = DAYS[:5] + DAYS[12:]  # no bars for 7 sessions after filing
        h, _ = align(stock(days, [10.0] * len(days), [10.0] * len(days)), self.cal)
        ev = ev_for(DAYS[4])
        attach_market_data(ev, h, self.cal)
        self.assertEqual(ev.status, "no_entry_bar")

    def test_path_fills_missing_days_and_stops_when_stale(self):
        days = DAYS[:12] + DAYS[14:20]
        closes = [10.0] * 12 + [12.0] * 6
        ev = ev_for(DAYS[9])
        attach_market_data(ev, stock(days, closes, closes), self.cal)
        p = list(ev.path)
        self.assertEqual(p[:4], [0.0, 0.0, 0.0, 0.0])
        self.assertAlmostEqual(p[4], 0.2)
        self.assertEqual(len(p), 10 + MAX_STALE)

    def test_bad_ticks_are_repaired(self):
        closes = [10.0, 10.0, 50.0, 10.0, 10.0]  # one-day 5x spike
        h, repaired = align(stock(DAYS[:5], closes, closes), self.cal)
        self.assertEqual(repaired, 1)
        self.assertEqual(h.close, [10.0] * 4)


class PitTest(unittest.TestCase):
    def test_cluster_counts_only_public_filings(self):
        a = ev_for("2021-03-01", accession="a", owner_cik="1", last_date="2021-02-26", shares=100)
        b = ev_for("2021-03-03", accession="b", owner_cik="2", last_date="2021-03-01", shares=200)
        c = ev_for("2021-03-05", accession="c", owner_cik="3", last_date="2021-02-25", shares=300)
        add_pit_features([a, b, c])
        self.assertEqual((a.cluster, b.cluster, c.cluster), (1, 2, 3))

    def test_track_record_uses_only_known_outcomes(self):
        old = ev_for("2021-01-04", accession="o", owner_cik="9")
        old.entry_cal, old.abn[PRIMARY], old.exit_cal[PRIMARY] = 1, 0.30, 63
        early = ev_for("2021-03-01", accession="e", owner_cik="9")
        early.entry_cal = 40  # before the old buy's outcome closed
        later = ev_for("2021-05-03", accession="l", owner_cik="9")
        later.entry_cal = 85
        add_pit_features([old, early, later])
        self.assertEqual(early.track_n, 0)
        self.assertEqual(later.track_n, 1)
        self.assertAlmostEqual(later.track, 0.30 / 6)  # shrunk: n/(n+5) * mean

    def test_routine_vs_opportunistic(self):
        evs = [ev_for(f"{y}-03-10", accession=f"r{y}", owner_cik="7", first_date=f"{y}-03-05",
                      last_date=f"{y}-03-05", shares=100 + y) for y in (2016, 2017, 2018, 2019)]
        evs.append(ev_for("2019-09-10", accession="x", owner_cik="7", first_date="2019-09-05",
                          last_date="2019-09-05", shares=5))
        add_pit_features(evs)
        self.assertEqual(evs[0].kind, "unclassified")
        self.assertEqual(evs[3].kind, "routine")
        self.assertEqual(evs[4].kind, "opportunistic")

    def test_track_record_skips_plan_purchases(self):
        old = ev_for("2021-01-04", accession="o", owner_cik="9", plan_purchase=True)
        old.entry_cal, old.abn[PRIMARY], old.exit_cal[PRIMARY] = 1, 0.30, 63
        later = ev_for("2021-05-03", accession="l", owner_cik="9")
        later.entry_cal = 85
        add_pit_features([old, later])
        self.assertEqual(later.track_n, 0)

    def test_novelty_unknown_in_first_year_of_data(self):
        a = ev_for("2006-01-10", accession="a", owner_cik="1")
        b = ev_for("2007-03-01", accession="b", owner_cik="1", shares=7)
        add_pit_features([a, b])
        self.assertIsNone(a.first_in_year_insider)  # an earlier buy may predate the data
        self.assertTrue(b.first_in_year_insider)

    def test_features_ignore_later_filings(self):
        """Deleting everything filed after a signal must not change its features."""
        evs = [ev_for(f"2021-03-{d:02d}", accession=f"a{d}", owner_cik=str(d % 3), shares=d,
                      last_date=f"2021-03-{d:02d}") for d in range(1, 20)]
        add_pit_features(evs)
        full = [(e.cluster, e.kind, e.track_n, e.first_in_year_insider, e.score) for e in evs]
        for cut in (5, 10, 15):
            prefix = [ev_for(e.filed, accession=e.buy.accession, owner_cik=e.buy.owner_cik, shares=e.buy.shares,
                             last_date=e.buy.last_date) for e in evs[:cut]]
            add_pit_features(prefix)
            self.assertEqual([(e.cluster, e.kind, e.track_n, e.first_in_year_insider, e.score) for e in prefix],
                             full[:cut])


class StatsTest(unittest.TestCase):
    def test_one_signal_per_company_day(self):
        a = ev_for("2021-01-04", accession="a", owner_cik="1")
        b = ev_for("2021-01-04", accession="b", owner_cik="2")
        a.entry_date = b.entry_date = "2021-01-05"
        self.assertEqual(unique_signals([a, b]), [a])

    def test_event_stats(self):
        evs = []
        for k, abn in enumerate([0.10, 0.10, -0.05, 5.0]):
            e = ev_for("2021-01-04", accession=str(k), issuer_cik=str(k))
            e.entry_date, e.abn[21], e.ret[21] = "2021-01-05", abn, abn
            evs.append(e)
        s = event_stats(evs, 21, (-0.5, 0.5))
        self.assertEqual(s["n"], 4)
        self.assertAlmostEqual(s["mean"], (0.10 + 0.10 - 0.05 + 0.5) / 4)  # winsorized
        self.assertAlmostEqual(s["hit"], 0.75)

    def test_newey_west_and_bootstrap(self):
        mean, t = newey_west_t([0.01, 0.02, 0.0, 0.015, 0.01, 0.02, 0.005, 0.01])
        self.assertAlmostEqual(mean, 0.01125)
        self.assertGreater(t, 3)
        bb = block_bootstrap([0.01] * 30, draws=200)
        self.assertEqual(bb["ci"], [0.01, 0.01])
        self.assertEqual(bb["p_boot"], 0.0)
        self.assertEqual(block_bootstrap([0.0] * 30, draws=200)["p_boot"], 1.0)  # mid-p for an all-zero series
        self.assertEqual(block_bootstrap([0.01] * 30, draws=0), {})

    def test_holm(self):
        adj = holm({"a": 0.01, "b": 0.04, "c": 0.03})
        self.assertAlmostEqual(adj["a"], 0.03)
        self.assertAlmostEqual(adj["c"], 0.06)
        self.assertAlmostEqual(adj["b"], 0.06)


def priced_ev(entry_cal: int, path: list[float], score: int = 50, issuer: str = "1", acc: str = "x") -> Ev:
    e = ev_for(DAYS[entry_cal - 1], issuer_cik=issuer, accession=acc)
    e.status, e.entry_cal, e.entry_date = "priced", entry_cal, DAYS[entry_cal]
    e.price, e.adv, e.score = 20.0, 5e7, score
    e.path = array("f", path)
    return e


class PortfolioTest(unittest.TestCase):
    def test_calendar_time_buy_and_hold_weights(self):
        cal = Calendar(flat_spy(DAYS[:60]))
        evs = [priced_ev(1, [0.10] + [0.0] * 20, issuer=str(k), acc=str(k)) for k in range(5)]
        ct = calendar_time(evs, cal, hold=21, min_positions=5)
        self.assertEqual(len(ct["series"]), 1)  # January only; February is the last, incomplete month
        m, port, spy = ct["series"][0]
        self.assertAlmostEqual(port, 0.10, places=6)
        self.assertEqual(spy, 0.0)

    def test_company_held_once(self):
        cal = Calendar(flat_spy(DAYS[:60]))
        evs = [priced_ev(1, [0.0] * 21, issuer="1", acc="a"), priced_ev(3, [0.5] * 21, issuer="1", acc="b")]
        evs += [priced_ev(1, [0.0] * 21, issuer=str(k), acc=str(k)) for k in range(2, 6)]
        ct = calendar_time(evs, cal, hold=21, min_positions=1)
        self.assertAlmostEqual(ct["series"][0][1], 0.0)  # the second ACME signal is ignored

    def test_simulation_slots_and_costs(self):
        cal = Calendar(flat_spy(DAYS[:30]))
        e = priced_ev(1, [0.10] * 5)
        res = simulate([e], cal, hold=5, slots=2, cost_mult=0)
        self.assertEqual(res["trades"], 1)
        self.assertAlmostEqual(res["strategy_total"], (1 + (1.1 ** 5 - 1) / 2) - 1, places=4)
        costly = simulate([e], cal, hold=5, slots=2, cost_mult=1)
        self.assertLess(costly["strategy_total"], res["strategy_total"])

    def test_simulation_prefers_higher_scores_when_full(self):
        cal = Calendar(flat_spy(DAYS[:30]))
        lo = priced_ev(1, [0.0] * 5, score=10, issuer="1", acc="a")
        hi = priced_ev(1, [0.10] * 5, score=90, issuer="2", acc="b")
        res = simulate([lo, hi], cal, hold=5, slots=1, cost_mult=0)
        self.assertEqual((res["trades"], res["skipped"]), (1, 1))
        self.assertGreater(res["strategy_total"], 0.5)


class WalkForwardTest(unittest.TestCase):
    def test_threshold_uses_only_earlier_months(self):
        days = business_days("2009-01-01", 1300)
        cal = Calendar(flat_spy(days))
        evs, k = [], 0
        for c in range(1, len(days) - 70, 5):
            for score, r in ((70, 0.001), (45, -0.001)):
                for j in range(3):
                    k += 1
                    e = ev_for(days[c - 1], issuer_cik=f"{score}-{j}-{c}", accession=str(k))
                    e.status, e.entry_cal, e.entry_date = "priced", c, days[c]
                    e.price, e.adv, e.score = 20.0, 5e7, score
                    e.path = array("f", [r] * 63)
                    evs.append(e)
        wf = walk_forward(evs, cal, start_year=2011)
        self.assertEqual(wf["thresholds"]["2011"], 50)  # 2009-2010 showed the 45-score buys losing
        self.assertTrue(all(e.score >= 50 for e in evs if e.year >= 2011 and e.score >= 50))


if __name__ == "__main__":
    unittest.main()
