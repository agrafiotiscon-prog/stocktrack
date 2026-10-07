import unittest

from stocktrack.alerts import Notifier, format_alert
from stocktrack.prices import Quote
from stocktrack.report import render_report
from stocktrack.signals import score_buy
from stocktrack.tracker import Cluster, Signal
from tests.test_signals import make_buy


class AlertTest(unittest.TestCase):
    def test_format(self):
        b = make_buy(
            role="CEO", officer_title="Chief Executive Officer", owner_name="Smith John",
            value=1_000_000, shares=50_000, avg_price=20.0, shares_before=100_000, shares_after=150_000,
        )
        sig = Signal(b, score_buy(b, cluster=2), Quote("ACME", 22.0, 30.0, 15.0))
        text = format_alert(sig)
        self.assertIn("Strong insider buy: ACME (score 77/100)", text)
        self.assertIn("Smith John (Chief Executive Officer) bought 50K sh @ $20.00 = $1.0M on 2026-10-01", text)
        self.assertIn("Stake +50% | Cluster: 2 insiders", text)
        self.assertIn("Now $22.00 (+10.0% vs insider price)", text)
        self.assertTrue(text.endswith(b.url))

    def test_channels_from_env(self):
        self.assertEqual(Notifier.from_env({}).names, [])
        n = Notifier.from_env(
            {
                "STOCKTRACK_DISCORD_WEBHOOK": "https://discord.example/hook",
                "STOCKTRACK_SLACK_WEBHOOK": "https://slack.example/hook",
                "STOCKTRACK_TELEGRAM_BOT_TOKEN": "123:abc",  # chat id missing: telegram stays off
            }
        )
        self.assertEqual(n.names, ["discord", "slack"])

    def test_failed_channel_is_reported(self):
        n = Notifier.from_env({"STOCKTRACK_SLACK_WEBHOOK": "http://127.0.0.1:9/nothing-listens"})
        self.assertIsNotNone(n.send("hi")["slack"])


class QuoteTest(unittest.TestCase):
    def test_math(self):
        q = Quote("ACME", 15.0, 20.0, 10.0)
        self.assertAlmostEqual(q.change_from(12.0), 0.25)
        self.assertIsNone(q.change_from(None))
        self.assertAlmostEqual(q.range_position, 0.5)


class ReportTest(unittest.TestCase):
    def test_renders_and_escapes(self):
        b = make_buy(issuer_name="<script>alert(1)</script> Inc", owner_name="O'Brien & Sons")
        other = make_buy(accession="acc-2", owner_cik="222", owner_name="Second Buyer", shares=777)
        html = render_report(
            [Signal(b, score_buy(b, 2), Quote("ACME", 11.0, None, None)), Signal(other, score_buy(other, 2))],
            [Cluster("320193", b.issuer_name, "ACME", [b, other])],
            "2026-09-01",
            "2026-10-07",
            with_prices=True,
        )
        self.assertIn("<title>Insider Buys</title>", html)
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt; Inc", html)
        self.assertIn("O&#x27;Brien &amp; Sons", html)
        self.assertIn("2 insiders", html)
        self.assertIn("+10.0%", html)

    def test_empty(self):
        html = render_report([], [], "2026-09-01", "2026-10-07")
        self.assertIn("No insider buys in this period yet", html)


if __name__ == "__main__":
    unittest.main()
