import unittest

from stocktrack.form4 import Form4ParseError, parse_form4_xml, parse_submission
from tests.helpers import form4_xml, owner_xml, submission, tx_xml


class ParseForm4Test(unittest.TestCase):
    def test_issuer_owner_and_transactions(self):
        xml = form4_xml(
            owners=[owner_xml(cik="0001234567", name="Smith John", officer=True, director=True, title="CEO")],
            txs=[tx_xml(shares=1000, price=10.5, after=5000), tx_xml(code="S", ad="D", shares=200, after=4800)],
            ticker="acme",
        )
        f = parse_form4_xml(xml, accession="acc-1", filed_at="2026-10-02T16:30:00")
        self.assertEqual((f.issuer_cik, f.issuer_name, f.ticker), ("0000320193", "Acme Corp", "ACME"))
        self.assertEqual(f.form_type, "4")
        self.assertEqual(len(f.owners), 1)
        o = f.owners[0]
        self.assertEqual((o.cik, o.name, o.officer_title), ("0001234567", "Smith John", "CEO"))
        self.assertTrue(o.is_officer and o.is_director)
        self.assertFalse(o.is_ten_percent)
        self.assertEqual(len(f.transactions), 2)
        t = f.transactions[0]
        self.assertEqual((t.code, t.shares, t.price, t.shares_after, t.direct_indirect), ("P", 1000, 10.5, 5000, "D"))
        self.assertEqual([t.code for t in f.purchases], ["P"])
        self.assertEqual(f.plan_10b5_1, False)
        self.assertEqual(f.footnotes, {"F1": "Weighted average price."})

    def test_trade_footnotes_exclude_holding_footnotes(self):
        xml = form4_xml(
            txs=[tx_xml(trade_note="F2", holding_note="F3")],
            footnotes={"F2": "Bought via plan.", "F3": "Balance includes DRIP shares."},
        )
        f = parse_form4_xml(xml)
        t = f.transactions[0]
        self.assertEqual(t.footnote_ids, ["F2"])
        self.assertEqual(f.notes(t), ["Bought via plan."])

    def test_price_given_only_by_footnote(self):
        f = parse_form4_xml(form4_xml(txs=[tx_xml(price=None)]))
        self.assertIsNone(f.transactions[0].price)

    def test_10b5_1_flag_variants(self):
        self.assertTrue(parse_form4_xml(form4_xml(aff10b5one="1")).plan_10b5_1)
        self.assertTrue(parse_form4_xml(form4_xml(aff10b5one="true")).plan_10b5_1)
        self.assertIsNone(parse_form4_xml(form4_xml(aff10b5one=None)).plan_10b5_1)

    def test_no_ticker(self):
        self.assertEqual(parse_form4_xml(form4_xml(ticker="NONE")).ticker, "")

    def test_numbers_with_commas(self):
        f = parse_form4_xml(form4_xml(txs=[tx_xml(shares="1,500", price="$2.50", after="10,000")]))
        t = f.transactions[0]
        self.assertEqual((t.shares, t.price, t.shares_after), (1500, 2.5, 10000))

    def test_rejects_other_documents(self):
        with self.assertRaises(Form4ParseError):
            parse_form4_xml("<edgarSubmission/>")
        with self.assertRaises(Form4ParseError):
            parse_form4_xml("not xml")


class ParseSubmissionTest(unittest.TestCase):
    def test_extracts_xml_and_acceptance_time(self):
        text = submission(form4_xml(), accession="0000000000-26-000042", accepted="20261002163005")
        f = parse_submission(text, accession="0000000000-26-000042")
        self.assertEqual(f.accession, "0000000000-26-000042")
        self.assertEqual(f.filed_at, "2026-10-02T16:30:05")
        self.assertEqual(f.issuer_name, "Acme Corp")

    def test_encoding_declaration_is_ignored(self):
        xml = form4_xml(issuer_name="Café Holdings").replace(
            '<?xml version="1.0"?>', '<?xml version="1.0" encoding="ISO-8859-1"?>'
        )
        self.assertEqual(parse_submission(submission(xml)).issuer_name, "Café Holdings")

    def test_missing_xml(self):
        with self.assertRaises(Form4ParseError):
            parse_submission("<SEC-DOCUMENT>no xml here</SEC-DOCUMENT>")


if __name__ == "__main__":
    unittest.main()
