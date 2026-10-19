import datetime as dt
import math
import unittest
from dataclasses import replace

from stocktrack.backtest import (
    MAX_STALE,
    PRIMARY,
    Calendar,
    Ev,
    add_pit_features,
    align,
    attach_market_data,
    holm,
    simulate,
    summarize,
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


def stock(days, opens, closes, raw=None) -> PriceHistory:
    raw = raw or closes
    return PriceHistory("ACME", list(days), list(opens), list(closes), [5e6] * len(days), list(raw))


def ev_for(filed: str, **buy_kw) -> Ev:
    return Ev(buy=make_buy(filed_at=filed, **buy_kw), filed=filed)


class MarketDataTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calendar(flat_spy())

    def test_entry_is_next_open_after_filing(self):
        # price climbs 1 per day; open = close - 0.5
        closes = [10 + k for k in range(len(DAYS))]
        opens = [c - 0.5 for c in closes]
        h = stock(DAYS, opens, closes)
        ev = ev_for(DAYS[10], last_date=DAYS[8], avg_price=18.0, shares=100)
        attach_market_data(ev, h, self.cal)
        self.assertEqual(ev.entry_date, DAYS[11])
        self.assertEqual(ev.entry_cal, 11)
        self.assertAlmostEqual(ev.ret[1], closes[11] / opens[11] - 1)
        self.assertAlmostEqual(ev.ret[5], closes[15] / opens[11] - 1)
        self.assertAlmostEqual(ev.ret[63], closes[11 + 62] / opens[11] - 1)
        self.assertEqual(ev.exit_date[5], DAYS[15])
        # flat SPY: abnormal equals raw
        self.assertAlmostEqual(ev.abn[63], ev.ret[63])
        self.assertAlmostEqual(ev.price, closes[10])  # day before entry
        self.assertAlmostEqual(ev.price_ratio, 18.0 / closes[8])
        self.assertAlmostEqual(ev.mkt_value, 100 * closes[8])

    def test_abnormal_subtracts_spy_same_window(self):
        spy_close = [100 * 1.001 ** k for k in range(len(DAYS))]
        spy = PriceHistory("SPY", DAYS, spy_close, spy_close, [1e9] * len(DAYS), spy_close)
        cal = Calendar(spy)
        h = stock(DAYS, [10.0] * len(DAYS), [11.0] * len(DAYS))
        ev = ev_for(DAYS[0])
        attach_market_data(ev, h, cal)
        spy_r = spy_close[1 + 20] / spy_close[1] - 1
        self.assertAlmostEqual(ev.abn[21], 0.1 - spy_r)

    def test_immature_and_delisted_horizons_are_missing(self):
        h = stock(DAYS[:40], [10.0] * 40, [10.0] * 40)  # stock stops trading after 40 sessions
        ev = ev_for(DAYS[0])
        attach_market_data(ev, h, self.cal)
        self.assertIn(21, ev.ret)
        self.assertNotIn(63, ev.ret)
        late = ev_for(DAYS[-3])
        attach_market_data(late, stock(DAYS, [10.0] * 400, [10.0] * 400), self.cal)
        self.assertIn(1, late.ret)
        self.assertNotIn(5, late.ret)

    def test_stale_entry_is_skipped(self):
        days = DAYS[:5] + DAYS[10:]  # no bars for 5 sessions after filing
        h = stock(days, [10.0] * len(days), [10.0] * len(days))
        ev = ev_for(DAYS[4])
        attach_market_data(ev, align(h, self.cal), self.cal)
        self.assertIsNone(ev.entry_date)

    def test_path_fills_missing_days_and_stops_when_stale(self):
        days = DAYS[:12] + DAYS[14:20]  # 2-day gap, then the stock ends
        closes = [10.0] * 12 + [12.0] * 6
        h = stock(days, closes, closes)
        ev = ev_for(DAYS[9])
        attach_market_data(ev, h, self.cal)
        p = list(ev.path)
        self.assertEqual(p[:2], [0.0, 0.0])  # entry day 10 and day 11: flat
        self.assertEqual(p[2:4], [0.0, 0.0])  # sessions 12-13: no bars
        self.assertAlmostEqual(p[4], 0.2)  # session 14: 10 -> 12
        # sessions 10-19, then up to MAX_STALE flat sessions after the last bar
        self.assertEqual(len(p), 10 + MAX_STALE)


class PitTest(unittest.TestCase):
    def test_cluster_counts_only_public_filings(self):
        a = ev_for("2021-03-01", accession="a", owner_cik="1", last_date="2021-02-26", shares=100)
        b = ev_for("2021-03-03", accession="b", owner_cik="2", last_date="2021-03-01", shares=200)
        c = ev_for("2021-03-05", accession="c", owner_cik="3", last_date="2021-02-25", shares=300)
        add_pit_features([a, b, c])
        self.assertEqual((a.cluster, b.cluster, c.cluster), (1, 2, 3))

    def test_track_record_uses_only_known_outcomes(self):
        old = ev_for("2021-01-04", accession="o", owner_cik="9")
        old.abn[PRIMARY], old.exit_date[PRIMARY], old.entry_date = 0.30, "2021-04-06", "2021-01-05"
        early = ev_for("2021-03-01", accession="e", owner_cik="9")
        early.entry_date = "2021-03-02"
        later = ev_for("2021-05-03", accession="l", owner_cik="9")
        later.entry_date = "2021-05-04"
        add_pit_features([old, early, later])
        self.assertEqual(early.track_n, 0)  # old buy's 63d outcome wasn't known yet
        self.assertEqual(later.track_n, 1)
        self.assertAlmostEqual(later.track_mean, 0.30)

    def test_routine_vs_opportunistic(self):
        evs = [ev_for(f"{y}-03-10", accession=f"r{y}", owner_cik="7", first_date=f"{y}-03-05",
                      last_date=f"{y}-03-05", shares=100 + y) for y in (2016, 2017, 2018, 2019)]
        evs.append(ev_for("2019-09-10", accession="x", owner_cik="7", first_date="2019-09-05",
                          last_date="2019-09-05", shares=5))
        add_pit_features(evs)
        self.assertEqual(evs[0].kind, "unknown")
        self.assertEqual(evs[3].kind, "routine")  # March in each of 2016-2018
        self.assertEqual(evs[4].kind, "opportunistic")  # September breaks the pattern

    def test_novelty_and_score(self):
        a = ev_for("2021-01-04", accession="a", owner_cik="1")
        b = ev_for("2021-06-01", accession="b", owner_cik="1", shares=7)
        add_pit_features([a, b])
        self.assertTrue(a.first_in_year_insider)
        self.assertFalse(b.first_in_year_insider)
        self.assertGreater(a.score, 0)


class StatsTest(unittest.TestCase):
    def test_summarize_weights_months_equally(self):
        evs = []
        for k in range(10):  # January: ten +10% events
            e = ev_for("2021-01-04")
            e.entry_date, e.abn[21], e.ret[21] = "2021-01-05", 0.10, 0.12
            evs.append(e)
        for m in ("02", "03"):
            e = ev_for(f"2021-{m}-01")
            e.entry_date, e.abn[21], e.ret[21] = f"2021-{m}-02", -0.10, -0.08
            evs.append(e)
        s = summarize(evs, 21, (-1.0, 1.0))
        self.assertEqual((s["n"], s["months"]), (12, 3))
        self.assertAlmostEqual(s["mean"], (1.0 - 0.2) / 12)
        self.assertAlmostEqual(s["monthly_mean"], (0.10 - 0.20) / 3)
        self.assertAlmostEqual(s["hit"], 10 / 12)

    def test_winsorizing(self):
        e = ev_for("2021-01-04")
        e.entry_date, e.abn[21], e.ret[21] = "2021-01-05", 5.0, 5.0
        self.assertAlmostEqual(summarize([e], 21, (-0.5, 0.5))["mean"], 0.5)

    def test_holm(self):
        adj = holm({"a": 0.01, "b": 0.04, "c": 0.03})
        self.assertAlmostEqual(adj["a"], 0.03)
        self.assertAlmostEqual(adj["c"], 0.06)
        self.assertAlmostEqual(adj["b"], 0.06)


class SimulateTest(unittest.TestCase):
    def test_single_position_with_slots_and_costs(self):
        cal = Calendar(flat_spy(DAYS[:30]))
        e = ev_for(DAYS[0], avg_price=20.0)
        e.entry_cal, e.price = 1, 20.0
        from array import array

        e.path = array("f", [0.10] * 5)
        res = simulate([e], cal, hold=5, slots=2, costs=False)
        self.assertEqual(res["trades"], 1)
        self.assertAlmostEqual(res["strategy_total"], 1.05 ** 5 - 1, places=5)  # half the capital in the trade
        self.assertAlmostEqual(res["exposure"], 5 / 2 / 29, places=6)
        with_costs = simulate([e], cal, hold=5, slots=1, costs=True)
        self.assertLess(with_costs["strategy_total"], 1.10 ** 5 - 1)


class WalkForwardTest(unittest.TestCase):
    def test_threshold_chosen_from_past_only(self):
        evs = []
        for year in (2010, 2011):
            for k in range(250):
                for score, abn in ((70, 0.05), (10, -0.05)):
                    e = ev_for(f"{year}-03-01")
                    e.entry_date, e.score, e.price, e.adv = f"{year}-03-02", score, 10.0, 5e6
                    e.abn[PRIMARY], e.ret[PRIMARY] = abn, abn
                    e.exit_date[PRIMARY] = f"{year}-06-01"
                    evs.append(e)
        wf = walk_forward(evs, (-1, 1), start_year=2010)
        self.assertEqual(wf["thresholds"]["2010"], 0)  # nothing known yet
        self.assertEqual(wf["thresholds"]["2011"], 20)  # lowest threshold that drops the losers
        self.assertEqual(wf["stats"]["n"], 500 + 250)


if __name__ == "__main__":
    unittest.main()
