import datetime as dt
import unittest

from stocktrack.feeds import (
    FORM4_TYPES_WITH_AMENDMENTS,
    daily_index_url,
    filing_index_url,
    parse_atom,
    parse_daily_index,
)
from tests.helpers import atom_feed

DAILY_INDEX = """Description:           Daily Index of EDGAR Dissemination Feed by Form Type
Last Data Received:    Oct 6, 2026

Form Type   Company Name                                                  CIK         Date Filed  File Name
---------------------------------------------------------------------------------------------------------------------------------------------
3                SOMEONE NEW                                                   2000001     20261006    edgar/data/2000001/0001000000-26-000001.txt
4                ACME  CORP  (DOUBLE  SPACED)                                  320193      20261006    edgar/data/320193/0001104659-26-113911.txt
4                SMITH JOHN                                                    1234567     20261006    edgar/data/1234567/0001104659-26-113911.txt
4/A              ACME CORP                                                     320193      20261006    edgar/data/320193/0001104659-26-113999.txt
424B3            SOME FUND                                                     999         20261006    edgar/data/999/0000999-26-000001.txt
"""


class DailyIndexTest(unittest.TestCase):
    def test_parses_form4_lines_once_per_accession(self):
        refs = parse_daily_index(DAILY_INDEX)
        self.assertEqual(len(refs), 1)
        r = refs[0]
        self.assertEqual((r.accession, r.cik, r.form_type, r.filed), ("0001104659-26-113911", "320193", "4", "2026-10-06"))
        self.assertEqual(r.submission_url, "https://www.sec.gov/Archives/edgar/data/320193/0001104659-26-113911.txt")

    def test_amendments_optional(self):
        refs = parse_daily_index(DAILY_INDEX, FORM4_TYPES_WITH_AMENDMENTS)
        self.assertEqual([r.form_type for r in refs], ["4", "4/A"])

    def test_url_quarter(self):
        self.assertTrue(daily_index_url(dt.date(2026, 10, 6)).endswith("/2026/QTR4/form.20261006.idx"))
        self.assertTrue(daily_index_url(dt.date(2026, 3, 31)).endswith("/2026/QTR1/form.20260331.idx"))


class AtomTest(unittest.TestCase):
    def test_filters_form_types_and_dedupes(self):
        feed = atom_feed(
            [
                ("424B3", "0002028541-26-000011", "2028541", "Filer"),
                ("4", "0001062993-26-005214", "2098041", "Reporting"),
                ("4", "0001062993-26-005214", "1006045", "Issuer"),
                ("4/A", "0001062993-26-005215", "1006045", "Issuer"),
                ("4", "0001062993-26-005216", "1006045", "Issuer"),
            ]
        )
        refs = parse_atom(feed.encode("latin-1"))
        self.assertEqual([r.accession for r in refs], ["0001062993-26-005214", "0001062993-26-005216"])
        self.assertEqual(refs[0].cik, "2098041")
        self.assertEqual(refs[0].filed, "2026-10-07T06:10:14-04:00")

    def test_index_url(self):
        self.assertEqual(
            filing_index_url("0001006045", "0001062993-26-005214"),
            "https://www.sec.gov/Archives/edgar/data/1006045/000106299326005214/0001062993-26-005214-index.htm",
        )


if __name__ == "__main__":
    unittest.main()
