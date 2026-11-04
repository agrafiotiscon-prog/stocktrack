import tempfile
import unittest
from pathlib import Path

from stocktrack import advisor as adv
from stocktrack import ledger as led
from stocktrack import paper
from tests.test_research import PipelineTest


def matured(row: dict, entry: str, abn: float, ret: float, **kw) -> dict:
    """A ledger row logged before its entry open, with a completed first week."""
    return dict(row, logged=entry + "T05:00:00Z", entry_date=entry, entry_price=10.0,
                last_seen=adv.add_market_days(entry, 5), last_price=10.0, status="open", abn_5=abn, ret_5=ret,
                abn_now=abn, ret_now=ret, **kw)


class StatsTest(unittest.TestCase):
    def test_stats(self):
        s = paper._stats([0.03, -0.01, 0.02, 0.0])
        self.assertAlmostEqual(s["mean"], 0.01)
        self.assertAlmostEqual(s["median"], 0.01)
        self.assertEqual(s["hit"], 0.5)
        self.assertNotIn("ci", s)  # too few for an interval
        self.assertIn("ci", paper._stats([0.01 * i for i in range(20)]))
        self.assertEqual(paper._stats([]), {"n": 0})

    def test_day_bootstrap_resamples_days(self):
        rows = [{"entry_date": f"2026-10-{d:02d}", "x": v} for d in range(19, 26) for v in (d / 100, d / 100 + 0.01)]
        lo, hi = paper.day_bootstrap(rows, "x", reps=2000)
        mean = sum(r["x"] for r in rows) / len(rows)
        self.assertLess(lo, mean)
        self.assertGreater(hi, mean)
        self.assertEqual(paper.day_bootstrap(rows, "x", reps=2000), (lo, hi))  # seeded
        self.assertIsNone(paper.day_bootstrap(rows[:4], "x"))  # fewer than 5 days

    def test_market_days(self):
        self.assertEqual(paper._market_days("2026-11-25", "2026-11-30"), 2)  # Thanksgiving and a weekend
        self.assertEqual(paper._market_days("2026-11-02", "2026-11-02"), 0)

    def test_formatting(self):
        self.assertEqual(paper.pct(-0.0123), "−1.2%")
        self.assertEqual(paper.pct(0.0), "0.0%")
        self.assertEqual(paper.pct(None), "–")
        self.assertEqual(paper.money(999_600), "$1.0M")


class PaperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PipelineTest.setUpClass()
        ev = next(e for e in PipelineTest.evs if e.liquid)
        base = led.new_row(ev, logged=ev.filed)
        days = ["2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-26", "2026-10-27"]
        cls.rows = [matured(dict(base, accession=f"a{i}", issuer_cik=str(1000 + i)), days[i % len(days)],
                           abn=(i % 7 - 3) / 100, ret=(i % 5 - 2) / 100) for i in range(30)]
        late = dict(base, accession="late", issuer_cik="9", logged="2026-10-30T15:00:00Z", entry_date="2026-10-28",
                    status="open", abn_5=0.5, ret_5=0.5)  # logged after its entry: must not count
        cls.ledger = cls.rows + [late, dict(base, accession="pend", status="pending")]
        hyp = {"registered": "2026-10-19", "hypotheses": [{"strategy": "cfo_exec_25k", "claim": "x", "expected": "+1%"}]}
        cls.data = paper.paper_data(cls.ledger, PipelineTest.res, hyp, "2026-11-04", "abc123")

    def test_counts_only_rows_logged_before_entry(self):
        d = self.data
        self.assertEqual(d["company_days"], 30)
        self.assertEqual(d["week"]["n"], 30)
        self.assertAlmostEqual(d["week"]["mean"], sum(r["abn_5"] for r in self.rows) / 30)
        self.assertEqual(d["late"]["n"], 1)
        self.assertEqual(d["pending"], 1)
        self.assertEqual(d["week_days"], 6)
        self.assertIsNotNone(d["week_boot"])

    def test_renders_a_complete_paper(self):
        doc = paper.render(self.data)
        for part in ("<h2>1. Introduction", "Table 2.", "Figure 3.", "<h2>References", "commit abc123"):
            self.assertIn(part, doc)
        text = doc.split("<style>")[0] + doc.split("</style>")[1]
        for bad in (">None<", "None%", "(None", "None)", "nan%", "{", "}"):
            self.assertNotIn(bad, text)

    def test_build_without_pdf(self):
        with tempfile.TemporaryDirectory() as d:
            out = paper.build_paper(d, self.ledger, PipelineTest.res, None, "2026-11-04", pdf=False)
            self.assertEqual([p.name for p in out], ["forward-test.html"])
            self.assertTrue(Path(out[0]).read_text().startswith("<!doctype html>"))

    def test_empty_ledger_still_renders(self):
        doc = paper.render(paper.paper_data([], PipelineTest.res, None, "2026-11-04"))
        self.assertIn("No logged buy has completed its first week yet.", doc)


if __name__ == "__main__":
    unittest.main()
