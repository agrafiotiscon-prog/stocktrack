import unittest
from unittest import mock

from stocktrack import history
from stocktrack.history import TickerMap, parse_chart

DAY = 86400
T0 = 1_600_000_000  # a timestamp; dates are derived from it


def chart(n=6, splits=None, period=None):
    closes = [10.0 * (k + 1) for k in range(n)]
    return {"chart": {"result": [{
        "meta": {"gmtoffset": 0, **({"currentTradingPeriod": {"regular": period}} if period else {})},
        "timestamp": [T0 + k * DAY for k in range(n)],
        "indicators": {"quote": [{"open": closes, "close": closes, "volume": [100] * n}],
                       "adjclose": [{"adjclose": closes}]},
        "events": {"splits": splits or {}},
    }]}}


class ParseChartTest(unittest.TestCase):
    def test_duplicate_split_counted_once(self):
        split = {"numerator": 2, "denominator": 1}
        dup = {"a": {**split, "date": T0 + 3 * DAY}, "b": {**split, "date": T0 + 5 * DAY}}
        h = parse_chart("X", chart(splits=dup))
        self.assertEqual(h.raw_close[0], 10.0 * 2)  # one 2:1 split, not 4:1

    def test_open_session_bar_dropped(self):
        last = T0 + 5 * DAY
        with mock.patch.object(history, "_now", return_value=last + 3600):
            h = parse_chart("X", chart(period={"start": last, "end": last + 6 * 3600}))
        self.assertEqual(len(h.dates), 5)
        with mock.patch.object(history, "_now", return_value=last + 7 * 3600):  # after the close
            h = parse_chart("X", chart(period={"start": last, "end": last + 6 * 3600}))
        self.assertEqual(len(h.dates), 6)


class TickerMapTest(unittest.TestCase):
    def setUp(self):
        self.tm = TickerMap([
            [100, "Acme", "ACME", "NYSE"],
            [200, "Bank", "BNK-PA", "NYSE"],  # only a preferred line is listed
            [300, "NewCo", "OLD", "Nasdaq"],  # ticker taken over by another company
            [400, "Spac", "SPACW", "Nasdaq"],
            [400, "Spac", "SPAC", "Nasdaq"],
        ])

    def test_resolution(self):
        self.assertEqual(self.tm.resolve("100", "ACME"), ("ACME", "filing"))
        self.assertEqual(self.tm.resolve("100", "ACMEQ"), ("ACME", "current"))
        self.assertEqual(self.tm.resolve("200", "BNK"), (None, "class_gone"))
        self.assertEqual(self.tm.resolve("999", "OLD"), ("OLD", "reused"))  # priced only if the price check passes
        self.assertEqual(self.tm.resolve("999", "GONE"), (None, "unlisted"))
        self.assertEqual(self.tm.resolve("400", ""), ("SPAC", "current"))  # skips the warrant line


if __name__ == "__main__":
    unittest.main()
