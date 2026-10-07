import datetime as dt
import io
import unittest
import urllib.error

from stocktrack.db import Database
from stocktrack.feeds import daily_index_url, latest_feed_url
from stocktrack.tracker import Tracker
from tests.helpers import atom_feed, form4_xml, owner_xml, submission, tx_xml


class FakeClient:
    """Serves canned responses by URL; anything else is a 404."""

    def __init__(self, pages: dict[str, str]) -> None:
        self.pages = pages
        self.requests: list[str] = []

    def get(self, url: str) -> bytes:
        self.requests.append(url)
        if url not in self.pages:
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO())
        return self.pages[url].encode("utf-8")

    def get_text(self, url: str) -> str:
        return self.get(url).decode("utf-8")


def sub_url(cik: str, acc: str) -> str:
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}.txt"


def buy_filing(acc: str, owner_cik: str, name: str, title: str = "", director: bool = True,
               shares: int = 10_000, price: float = 20.0, date: str = "2026-10-05", ticker: str = "ACME",
               issuer_cik: str = "0000320193") -> str:
    xml = form4_xml(
        owners=[owner_xml(cik=owner_cik, name=name, director=director, officer=bool(title), title=title)],
        txs=[tx_xml(date=date, shares=shares, price=price, after=shares * 3)],
        ticker=ticker,
        issuer_cik=issuer_cik,
    )
    return submission(xml, accession=acc, accepted=date.replace("-", "") + "170000")


class TrackerTest(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_scan_latest_ingests_buys_and_skips_seen(self):
        feed = atom_feed(
            [
                ("4", "0000000001-26-000001", "320193", "Issuer"),
                ("4", "0000000001-26-000002", "320193", "Issuer"),
                ("425", "0000000001-26-000003", "320193", "Subject"),
            ]
        )
        sale = submission(form4_xml(txs=[tx_xml(code="S", ad="D")]), accession="0000000001-26-000002")
        client = FakeClient(
            {
                latest_feed_url(0, 100): feed,
                latest_feed_url(100, 100): atom_feed([]),
                sub_url("320193", "0000000001-26-000001"): buy_filing("0000000001-26-000001", "11", "Ceo Carl", "CEO"),
                sub_url("320193", "0000000001-26-000002"): sale,
            }
        )
        tracker = Tracker(self.db, client)
        result = tracker.scan_latest()
        self.assertEqual(result.filings, 2)
        self.assertEqual([b.owner_name for b in result.buys], ["Ceo Carl"])
        self.assertTrue(self.db.seen("0000000001-26-000002"))

        # second scan: page 0 is all known, so nothing is re-downloaded
        client.requests.clear()
        result = tracker.scan_latest()
        self.assertEqual((result.filings, result.buys), (0, []))
        self.assertEqual(client.requests, [latest_feed_url(0, 100)])

    def test_latest_refs_pages_until_known(self):
        page0 = atom_feed([("4", "0000000001-26-000009", "1", "Issuer"), ("4", "0000000001-26-000008", "1", "Issuer")])
        page1 = atom_feed([("4", "0000000001-26-000008", "2", "Reporting"), ("4", "0000000001-26-000007", "1", "Issuer")])
        page2 = atom_feed([("4", "0000000001-26-000006", "1", "Issuer")])
        self.db.record_filing("0000000001-26-000006", "4", "1", None)
        client = FakeClient({latest_feed_url(0, 2): page0, latest_feed_url(2, 2): page1, latest_feed_url(4, 2): page2})
        refs = Tracker(self.db, client).latest_refs(page_size=2)
        self.assertEqual([r.accession for r in refs], ["0000000001-26-000009", "0000000001-26-000008", "0000000001-26-000007"])

    def test_unparseable_filing_is_recorded_not_retried(self):
        client = FakeClient({sub_url("1", "0000000001-26-000001"): "<SEC-DOCUMENT>garbage</SEC-DOCUMENT>"})
        tracker = Tracker(self.db, client)
        from stocktrack.feeds import FilingRef

        ref = FilingRef("0000000001-26-000001", "1", "4")
        r = tracker.ingest([ref])
        self.assertEqual((r.filings, r.errors), (1, 1))
        self.assertEqual(self.db.stats()["errors"], 1)
        self.assertEqual(tracker.ingest([ref]).filings, 0)

    def test_backfill_skips_weekends_and_missing_days(self):
        index = (
            "4                ACME CORP                       320193      20261005    "
            "edgar/data/320193/0000000001-26-000001.txt\n"
        )
        client = FakeClient(
            {
                daily_index_url(dt.date(2026, 10, 5)): index,
                sub_url("320193", "0000000001-26-000001"): buy_filing("0000000001-26-000001", "11", "Ceo Carl", "CEO"),
            }
        )
        days = []
        result = Tracker(self.db, client).backfill(
            days=4, end=dt.date(2026, 10, 6), on_day=lambda d, refs: days.append((d, refs is not None))
        )
        # Oct 3-4 is a weekend; Oct 6 has no index in the fake
        self.assertEqual(days, [(dt.date(2026, 10, 5), True), (dt.date(2026, 10, 6), False)])
        self.assertEqual(len(result.buys), 1)

    def _load(self, filings):
        pages = {sub_url("320193", acc): text for acc, text in filings}
        tracker = Tracker(self.db, FakeClient(pages))
        from stocktrack.feeds import FilingRef

        tracker.ingest([FilingRef(acc, "320193", "4") for acc, _ in filings])
        return tracker

    def test_ranked_and_clusters(self):
        tracker = self._load(
            [
                ("0000000001-26-000001", buy_filing("0000000001-26-000001", "11", "Ceo Carl", "CEO", date="2026-10-01")),
                ("0000000001-26-000002", buy_filing("0000000001-26-000002", "12", "Dir Dana", date="2026-10-03", shares=2000)),
                ("0000000001-26-000003", buy_filing("0000000001-26-000003", "13", "Dir Dave", date="2026-10-05", shares=3000)),
                ("0000000001-26-000004", buy_filing("0000000001-26-000004", "14", "Solo Sam", date="2026-10-05",
                                                    issuer_cik="0000000555", ticker="SOLO", shares=4000)),
            ]
        )
        ranked = tracker.ranked(since="2026-09-01")
        self.assertEqual(len(ranked), 4)
        self.assertEqual(ranked[0].buy.owner_name, "Ceo Carl")
        self.assertEqual(ranked[0].score.cluster_size, 3)
        solo = next(s for s in ranked if s.buy.ticker == "SOLO")
        self.assertEqual(solo.score.cluster_size, 1)

        self.assertEqual([s.buy.owner_name for s in tracker.ranked(since="2026-09-01", ticker="solo")], ["Solo Sam"])
        self.assertEqual(len(tracker.ranked(since="2026-10-04")), 2)
        self.assertTrue(all(s.score.total >= 50 for s in tracker.ranked(since="2026-09-01", min_score=50)))

        clusters = tracker.clusters(since="2026-09-01")
        self.assertEqual(len(clusters), 1)
        c = clusters[0]
        self.assertEqual((c.ticker, len(c.insiders), c.first_date, c.last_date), ("ACME", 3, "2026-10-01", "2026-10-05"))
        self.assertAlmostEqual(c.total_value, (10_000 + 2_000 + 3_000) * 20.0)

        # alerts use the same cluster-aware score
        self.assertEqual(tracker.score(ranked[0].buy).score.total, ranked[0].score.total)

    def test_alert_bookkeeping(self):
        tracker = self._load([("0000000001-26-000001", buy_filing("0000000001-26-000001", "11", "Ceo Carl", "CEO"))])
        self.assertFalse(self.db.was_alerted("0000000001-26-000001"))
        self.db.mark_alerted("0000000001-26-000001")
        self.assertTrue(self.db.was_alerted("0000000001-26-000001"))
        self.assertEqual(len(tracker.ranked(since="2026-01-01")), 1)


if __name__ == "__main__":
    unittest.main()
