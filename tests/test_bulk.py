import tempfile
import unittest
import zipfile
from pathlib import Path

from stocktrack.bulk import quarter_end, quarter_events, sec_date

SUB = ["ACCESSION_NUMBER", "FILING_DATE", "PERIOD_OF_REPORT", "DOCUMENT_TYPE", "ISSUERCIK", "ISSUERNAME",
       "ISSUERTRADINGSYMBOL", "REMARKS", "AFF10B5ONE"]
OWN = ["ACCESSION_NUMBER", "RPTOWNERCIK", "RPTOWNERNAME", "RPTOWNER_RELATIONSHIP", "RPTOWNER_TITLE", "RPTOWNER_TXT"]
TX = ["ACCESSION_NUMBER", "NONDERIV_TRANS_SK", "SECURITY_TITLE", "TRANS_DATE", "TRANS_CODE", "TRANS_SHARES",
      "TRANS_PRICEPERSHARE", "TRANS_ACQUIRED_DISP_CD", "SHRS_OWND_FOLWNG_TRANS", "DIRECT_INDIRECT_OWNERSHIP",
      "NATURE_OF_OWNERSHIP", "TRANS_SHARES_FN", "SHRS_OWND_FOLWNG_TRANS_FN"]
FN = ["ACCESSION_NUMBER", "FOOTNOTE_ID", "FOOTNOTE_TXT"]


def tsv(cols, rows):
    return "\t".join(cols) + "\n" + "".join("\t".join(str(r.get(c, "")) for c in cols) + "\n" for r in rows)


def make_zip(path: Path) -> None:
    subs = [
        {"ACCESSION_NUMBER": "A1", "FILING_DATE": "03-JUN-2010", "DOCUMENT_TYPE": "4", "ISSUERCIK": "0000000777",
         "ISSUERNAME": "Acme", "ISSUERTRADINGSYMBOL": "ACME"},
        {"ACCESSION_NUMBER": "A2", "FILING_DATE": "04-JUN-2010", "DOCUMENT_TYPE": "4/A", "ISSUERCIK": "777",
         "ISSUERNAME": "Acme", "ISSUERTRADINGSYMBOL": "ACME"},
    ]
    owners = [
        {"ACCESSION_NUMBER": "A1", "RPTOWNERCIK": "0000001001", "RPTOWNERNAME": "Big Fund LP",
         "RPTOWNER_RELATIONSHIP": "TenPercentOwnerOther"},
        {"ACCESSION_NUMBER": "A1", "RPTOWNERCIK": "0000001002", "RPTOWNERNAME": "Fund GP",
         "RPTOWNER_RELATIONSHIP": "DirectorOther"},
        {"ACCESSION_NUMBER": "A2", "RPTOWNERCIK": "1003", "RPTOWNERNAME": "Amender", "RPTOWNER_RELATIONSHIP": "Officer"},
    ]
    txs = [  # stored out of filing order; the surrogate key gives the order
        {"ACCESSION_NUMBER": "A1", "NONDERIV_TRANS_SK": "12", "SECURITY_TITLE": "Common Stock", "TRANS_DATE": "02-JUN-2010",
         "TRANS_CODE": "P", "TRANS_SHARES": "100", "TRANS_PRICEPERSHARE": "10", "TRANS_ACQUIRED_DISP_CD": "A",
         "SHRS_OWND_FOLWNG_TRANS": "1200", "DIRECT_INDIRECT_OWNERSHIP": "D", "TRANS_SHARES_FN": "F1"},
        {"ACCESSION_NUMBER": "A1", "NONDERIV_TRANS_SK": "11", "SECURITY_TITLE": "Common Stock", "TRANS_DATE": "01-JUN-2010",
         "TRANS_CODE": "P", "TRANS_SHARES": "100", "TRANS_PRICEPERSHARE": "10", "TRANS_ACQUIRED_DISP_CD": "A",
         "SHRS_OWND_FOLWNG_TRANS": "1100", "DIRECT_INDIRECT_OWNERSHIP": "D", "SHRS_OWND_FOLWNG_TRANS_FN": "F2"},
        {"ACCESSION_NUMBER": "A1", "NONDERIV_TRANS_SK": "13", "SECURITY_TITLE": "Series A Preferred Stock",
         "TRANS_DATE": "02-JUN-2010", "TRANS_CODE": "P", "TRANS_SHARES": "5000", "TRANS_PRICEPERSHARE": "25",
         "TRANS_ACQUIRED_DISP_CD": "A", "SHRS_OWND_FOLWNG_TRANS": "5000", "DIRECT_INDIRECT_OWNERSHIP": "D"},
        {"ACCESSION_NUMBER": "A2", "NONDERIV_TRANS_SK": "21", "SECURITY_TITLE": "Common Stock", "TRANS_DATE": "02-JUN-2010",
         "TRANS_CODE": "P", "TRANS_SHARES": "5", "TRANS_PRICEPERSHARE": "10", "TRANS_ACQUIRED_DISP_CD": "A"},
    ]
    notes = [{"ACCESSION_NUMBER": "A1", "FOOTNOTE_ID": "F1", "FOOTNOTE_TXT": "Weighted average price."},
             {"ACCESSION_NUMBER": "A1", "FOOTNOTE_ID": "F2", "FOOTNOTE_TXT": "Includes dividend reinvestment shares."}]
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("SUBMISSION.tsv", tsv(SUB, subs))
        z.writestr("REPORTINGOWNER.tsv", tsv(OWN, owners))
        z.writestr("NONDERIV_TRANS.tsv", tsv(TX, txs))
        z.writestr("FOOTNOTES.tsv", tsv(FN, notes))


class BulkTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "2010q2_form345.zip"
        make_zip(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def test_quarter_events(self):
        events = quarter_events(self.path)
        self.assertEqual([e.accession for e in events], ["A1"])  # 4/A amendments are skipped
        e = events[0]
        # "TenPercentOwnerOther" / "DirectorOther" are concatenated flags, not "Other"
        self.assertEqual(e.role, "Director")
        self.assertEqual(e.owner_ciks, "1001;1002")
        # Preferred stock is left out; the two common purchases remain
        self.assertEqual((e.shares, e.value), (200, 2000))
        # Holdings follow filing order (SK 11 then 12): 1,000 before, 1,200 after
        self.assertEqual((e.shares_before, e.shares_after), (1000, 1200))
        self.assertEqual((e.first_date, e.last_date, e.filed_at), ("2010-06-01", "2010-06-02", "2010-06-03"))
        # A note on the post-trade balance doesn't make it a plan purchase
        self.assertFalse(e.plan_purchase)

    def test_dates(self):
        self.assertEqual(sec_date("29-DEC-2025"), "2025-12-29")
        self.assertEqual(sec_date("bad"), "")
        self.assertEqual(quarter_end("2026q3_form345.zip"), "2026-09-30")
        self.assertEqual(quarter_end("2025q4_form345.zip"), "2025-12-31")


if __name__ == "__main__":
    unittest.main()
