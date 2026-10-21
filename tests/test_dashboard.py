import json
import re
import tempfile
import unittest
from pathlib import Path

from stocktrack import dashboard as dash
from stocktrack import ledger as led
from tests.test_research import PipelineTest


class DashboardTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PipelineTest.setUpClass()
        cls.res, cls.evs = PipelineTest.res, PipelineTest.evs
        ev = next(e for e in cls.evs if e.priced)
        cls.row = led.new_row(ev, logged=ev.filed)
        cls.today = ev.filed
        cls.hyp = {"registered": "2000-01-01", "hypotheses": [
            {"strategy": "cfo_exec_25k", "claim": "CFOs beat SPY.", "expected": "+1%"},
            {"strategy": "avoid: role Other and routine insiders", "claim": "They lag.", "expected": "below average"}]}

    def data(self, rows=None):
        return dash.dashboard_data(self.res, rows if rows is not None else [self.row], self.hyp, today=self.today,
                                   generated="2026-10-21T12:00Z")

    def test_data_mirrors_the_backtest(self):
        d = self.data()
        o = self.res["overall"]
        self.assertEqual(d["overall"]["spy"]["ann"], dash._r(o["ctp"].get("annualized")))
        self.assertEqual(d["overall"]["spy"]["months"], o["ctp"].get("months"))
        self.assertEqual(d["overall"]["event"]["n"], o["events"]["63"]["n"])
        self.assertEqual(len(d["kinds"]), sum(len(b) for b in self.res["slices"].values()))
        self.assertEqual({s["key"] for s in d["strategies"]}, set(self.res["strategies"]))
        curve = d["strategies"][0]["holds"]["63d"]["curve"]
        self.assertEqual(len(curve), len(self.res["strategies"][d["strategies"][0]["key"]]["portfolio"]["63d"]["curve"]))
        self.assertTrue(all(len(p) == 3 for p in curve))
        self.assertEqual([h["needed"] for h in d["live"]["hypotheses"]], [100, 100])
        self.assertEqual(d["live"]["logged"], 1)
        json.dumps(d, allow_nan=False)  # the page needs strict JSON

    def test_live_rows_are_recent_and_newest_first(self):
        old = dict(self.row, accession="old", filed_at="1990-01-01")
        newer = dict(self.row, accession="new", filed_at=self.row["filed_at"][:10] + "T23:00:00")
        rows = self.data([old, self.row, newer])["live"]["rows"]
        self.assertEqual(len(rows), 2)  # the 1990 filing is outside the window
        self.assertGreaterEqual(rows[0]["filed"], rows[1]["filed"])

    def test_untrusted_text_cannot_break_out_of_the_data_script(self):
        evil = dict(self.row, owner_name="</script><script>alert(1)</script>", issuer_name="<!-- x")
        html = dash.render(self.data([evil]))
        payload = re.search(r'<script id="dashboard-data" type="application/json">(.*?)</script>', html, re.S).group(1)
        self.assertNotIn("<", payload)
        decoded = json.loads(payload)
        self.assertEqual(decoded["live"]["rows"][0]["insider"], "</script><script>alert(1)</script>")

    def test_nan_becomes_null(self):
        self.assertIsNone(dash._r(float("nan")))
        self.assertIsNone(dash._r(float("inf")))
        self.assertEqual(dash._r(0.123456789), 0.12346)

    def test_build_writes_a_self_contained_page(self):
        with tempfile.TemporaryDirectory() as d:
            path = dash.build_dashboard(d, self.res, [self.row], self.hyp, today=self.today)
            html = Path(path).read_text()
        self.assertIn("<title>Insider Edge</title>", html)
        self.assertNotIn("/*__DASHBOARD_DATA__*/", html)
        self.assertEqual(re.findall(r'<script[^>]+src=', html), [])  # no external scripts


if __name__ == "__main__":
    unittest.main()
