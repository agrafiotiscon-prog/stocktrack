import math
import unittest
from dataclasses import replace

from stocktrack.form4 import Owner, parse_form4_xml
from stocktrack.signals import (
    BuyEvent,
    build_buy,
    cluster_size,
    dedupe_purchases,
    money,
    owner_role,
    score_buy,
    stake_text,
)
from tests.helpers import form4_xml, owner_xml, tx_xml


def make_buy(**kw) -> BuyEvent:
    base = dict(
        accession="acc-1",
        issuer_cik="320193",
        issuer_name="Acme Corp",
        ticker="ACME",
        owner_cik="111",
        owner_name="Doe Jane",
        owner_names="Doe Jane",
        role="Director",
        officer_title="",
        first_date="2026-10-01",
        last_date="2026-10-01",
        filed_at="2026-10-02T16:00:00",
        shares=10_000,
        value=100_000,
        avg_price=10.0,
        shares_before=40_000,
        shares_after=50_000,
        plan_10b5_1=False,
        n_transactions=1,
        url="https://www.sec.gov/x",
    )
    base.update(kw)
    return BuyEvent(**base)


class RoleTest(unittest.TestCase):
    def role(self, **kw):
        return owner_role(Owner(cik="1", name="x", **kw))

    def test_titles(self):
        self.assertEqual(self.role(is_officer=True, officer_title="President and Chief Executive Officer"), "CEO")
        self.assertEqual(self.role(is_officer=True, officer_title="Executive Chairman & CEO"), "CEO")
        self.assertEqual(self.role(is_officer=True, officer_title="EVP & CFO"), "CFO")
        self.assertEqual(self.role(is_officer=True, officer_title="President"), "President")
        self.assertEqual(self.role(is_officer=True, officer_title="Senior Vice President, Sales"), "Officer")
        self.assertEqual(self.role(is_officer=True, officer_title="Chief Operating Officer"), "C-Suite")
        self.assertEqual(self.role(is_officer=True, officer_title="CTO"), "C-Suite")
        self.assertEqual(self.role(is_officer=True, officer_title="Executive Chairman"), "Chair")

    def test_relationships_without_title(self):
        self.assertEqual(self.role(is_director=True), "Director")
        self.assertEqual(self.role(is_director=True, other_text="Chairman of the Board"), "Chair")
        self.assertEqual(self.role(is_ten_percent=True), "10% Owner")
        self.assertEqual(self.role(), "Other")


class BuildBuyTest(unittest.TestCase):
    def test_no_purchases(self):
        f = parse_form4_xml(form4_xml(txs=[tx_xml(code="S", ad="D"), tx_xml(code="A")]))
        self.assertIsNone(build_buy(f))

    def test_aggregates_purchases_across_holdings(self):
        xml = form4_xml(
            txs=[
                tx_xml(date="2026-09-30", shares=1000, price=10.0, after=11_000),
                tx_xml(date="2026-10-01", shares=1000, price=12.0, after=12_000),
                tx_xml(date="2026-10-01", shares=500, price=11.0, after=2_500, di="I", nature="By Trust"),
                tx_xml(date="2026-10-01", code="S", ad="D", shares=100, price=12.0, after=11_900),
            ]
        )
        b = build_buy(parse_form4_xml(xml, accession="0000000000-26-000001", filed_at="2026-10-02T16:00:00"))
        self.assertEqual(b.shares, 2500)
        self.assertAlmostEqual(b.value, 10_000 + 12_000 + 5_500)
        self.assertAlmostEqual(b.avg_price, 27_500 / 2500)
        self.assertEqual((b.first_date, b.last_date), ("2026-09-30", "2026-10-01"))
        # direct: 12,000 after, 10,000 before; trust: 2,500 after, 2,000 before
        self.assertEqual((b.shares_before, b.shares_after), (12_000, 14_500))
        self.assertAlmostEqual(b.stake_increase, 0.2083, places=3)
        self.assertEqual((b.role, b.issuer_cik, b.n_transactions), ("CEO", "320193", 3))
        self.assertIn("/edgar/data/320193/000000000026000001/", b.url)

    def test_unpriced_purchase_counts_shares_but_not_value(self):
        b = build_buy(parse_form4_xml(form4_xml(txs=[tx_xml(shares=100, price=None), tx_xml(shares=100, price=5)])))
        self.assertEqual((b.shares, b.value, b.avg_price), (200, 500, 5.0))

    def test_new_position(self):
        b = build_buy(parse_form4_xml(form4_xml(txs=[tx_xml(shares=1000, after=1000)])))
        self.assertEqual(b.shares_before, 0)
        self.assertTrue(math.isinf(b.stake_increase))

    def test_joint_filing_uses_most_senior_owner(self):
        xml = form4_xml(
            owners=[
                owner_xml(cik="0000000001", name="Big Fund LP", ten_percent=True),
                owner_xml(cik="0000000002", name="Founder Fred", officer=True, director=True, title="CEO"),
            ]
        )
        b = build_buy(parse_form4_xml(xml))
        self.assertEqual((b.owner_name, b.owner_cik, b.role), ("Founder Fred", "2", "CEO"))
        self.assertEqual(b.owner_names, "Big Fund LP; Founder Fred")


class ScoreTest(unittest.TestCase):
    def test_components(self):
        b = make_buy(role="CEO", officer_title="CEO", value=1_000_000, shares_before=100_000, shares_after=150_000)
        s = score_buy(b)
        self.assertAlmostEqual(s.value_pts, 20)
        self.assertEqual(s.role_pts, 25)
        self.assertAlmostEqual(s.conviction_pts, 20 * math.sqrt(0.5 / 0.5))
        self.assertEqual(s.cluster_pts, 0)
        self.assertEqual(s.total, 65)
        self.assertEqual(s.label, "Strong")
        self.assertEqual(s.tags, ["Stake +50%"])

    def test_value_scale_is_capped(self):
        self.assertEqual(score_buy(make_buy(value=5_000)).value_pts, 0)
        self.assertAlmostEqual(score_buy(make_buy(value=100_000)).value_pts, 10)
        self.assertEqual(score_buy(make_buy(value=1e9)).value_pts, 30)

    def test_cluster_points(self):
        b = make_buy()
        self.assertEqual([score_buy(b, n).cluster_pts for n in (1, 2, 3, 4, 7)], [0, 12, 20, 25, 25])
        self.assertIn("Cluster: 3 insiders", score_buy(b, 3).tags)

    def test_penalties(self):
        base = score_buy(make_buy()).total
        planned = score_buy(make_buy(plan_10b5_1=True))
        self.assertEqual(planned.total, base - 15)
        self.assertIn("10b5-1 plan", planned.tags)
        late = score_buy(make_buy(last_date="2026-08-01", filed_at="2026-10-02T09:00:00"))
        self.assertEqual(late.total, base - 10)
        self.assertIn("Filed 62d late", late.tags)

    def test_score_never_negative(self):
        b = make_buy(role="Other", value=0, shares_before=None, shares_after=None, plan_10b5_1=True)
        self.assertEqual(score_buy(b).total, 0)


class ClusterTest(unittest.TestCase):
    def test_counts_distinct_insiders_in_window(self):
        me = make_buy(accession="a", owner_cik="1", last_date="2026-10-10", shares=100)
        peers = [
            me,
            make_buy(accession="b", owner_cik="2", last_date="2026-10-01", shares=200),
            make_buy(accession="c", owner_cik="2", last_date="2026-10-02", shares=300),  # same insider again
            make_buy(accession="d", owner_cik="3", last_date="2026-10-24", shares=400),
            make_buy(accession="e", owner_cik="4", last_date="2026-10-25", shares=500),  # outside 14 days
            make_buy(accession="f", owner_cik="5", last_date="2026-10-10", shares=600, issuer_cik="999"),
        ]
        self.assertEqual(cluster_size(me, peers), 3)
        self.assertEqual(cluster_size(me, peers, window_days=3), 1)

    def test_same_purchase_reported_by_related_filers_counts_once(self):
        fund = make_buy(accession="a", owner_cik="1", shares=5000)
        manager = make_buy(accession="b", owner_cik="2", shares=5000)
        self.assertEqual(cluster_size(fund, [fund, manager]), 1)
        self.assertEqual(dedupe_purchases([fund, manager]), [fund])


class FormatTest(unittest.TestCase):
    def test_money_and_stake(self):
        self.assertEqual([money(v) for v in (950, 25_000, 1_250_000, 3e9)], ["$950", "$25K", "$1.2M", "$3.0B"])
        self.assertEqual(
            [stake_text(v) for v in (None, math.inf, 0.004, 0.25, 0.0)], ["", "New", "+<1%", "+25%", "+0%"]
        )

    def test_filing_delay(self):
        self.assertEqual(make_buy(last_date="2026-10-01", filed_at="2026-10-03T08:00:00").filing_delay_days, 2)
        self.assertIsNone(make_buy(filed_at="").filing_delay_days)
        self.assertIsNone(replace(make_buy(), shares_before=None).stake_increase)


if __name__ == "__main__":
    unittest.main()
