import datetime as dt
import json
import re
import unittest

from stocktrack import advisor as adv
from stocktrack import dashboard as dash
from stocktrack import ledger as led
from tests.test_research import PipelineTest


class MarketCalendarTest(unittest.TestCase):
    def test_nyse_holidays(self):
        self.assertEqual(sorted(d.isoformat() for d in adv.market_holidays(2026)), [
            "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03",
            "2026-09-07", "2026-11-26", "2026-12-25"])
        self.assertIn(dt.date(2027, 3, 26), adv.market_holidays(2027))  # Good Friday
        self.assertIn(dt.date(2027, 12, 24), adv.market_holidays(2027))  # Christmas on a Saturday
        self.assertNotIn(dt.date(2027, 12, 31), adv.market_holidays(2027))  # New Year 2028 on a Saturday isn't moved

    def test_market_days(self):
        self.assertEqual(adv.next_market_day("2026-11-25"), "2026-11-27")  # skips Thanksgiving
        self.assertEqual(adv.next_market_day("2026-10-23"), "2026-10-26")  # Friday -> Monday
        self.assertEqual(adv.add_market_days("2026-10-21", 0), "2026-10-21")
        self.assertEqual(adv.add_market_days("2026-10-21", 5), "2026-10-28")


class SizingTest(unittest.TestCase):
    def test_loss_budget_sets_the_size(self):
        p = adv.position({"p10": -0.25}, 0.01)
        self.assertAlmostEqual(p["share"], 0.04)
        self.assertEqual(p["limited_by"], "loss budget")

    def test_sizes_to_the_one_in_twenty_case_when_known(self):
        p = adv.position({"p05": -0.4, "p10": -0.25}, 0.01)
        self.assertAlmostEqual(p["share"], 0.025)
        self.assertAlmostEqual(p["bad_case"], -0.4)

    def test_caps(self):
        self.assertEqual(adv.position({"p10": -0.1}, 0.02)["limited_by"], "5% cap")  # 0.02/0.1 = 20% > 5%
        self.assertAlmostEqual(adv.position({"p10": -0.1}, 0.02)["share"], adv.MAX_POSITION)
        thin = adv.position({"p10": -0.25}, 0.01, adv=1e6, account=1e6)  # 4% = $40K > 2% of $1M a day
        self.assertEqual(thin["limited_by"], "liquidity")
        self.assertAlmostEqual(thin["share"], 0.02)
        self.assertAlmostEqual(adv.position({"p10": 0.02}, 0.01)["bad_case"], -0.05)  # a floor on the bad case

    def test_tiers(self):
        self.assertEqual(adv.tier(0.03), "above")
        self.assertEqual(adv.tier(0.0), "typical")
        self.assertEqual(adv.tier(-0.02), "below")


class AdvisorFitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PipelineTest.setUpClass()
        cls.model = adv.fit(PipelineTest.evs, PipelineTest.cal, echo=lambda *a: None)

    def test_fit_is_strict_json_with_its_parts(self):
        json.dumps(self.model, allow_nan=False)
        for k in ("effects", "validation", "risk", "base", "rules", "tier_share"):
            self.assertIn(k, self.model)
        self.assertIn("all", self.model["risk"])
        self.assertEqual(set(self.model["effects"]), set(adv.TILT_FEATURES))

    def test_tilts_need_the_same_direction_in_both_periods(self):
        cal = PipelineTest.cal
        sample = adv.live_sample(PipelineTest.evs)
        early = sample[: len(sample) // 2]
        late = sample[len(sample) // 2:]
        effects = adv.feature_effects([early, late], cal, adv.levels_of(sample))
        for lvs in effects.values():
            for d in lvs.values():
                if d["tilt"]:
                    self.assertTrue(all(x * d["tilt"] > 0 for x in d["effects"]))
                    self.assertEqual(abs(d["tilt"]), min(abs(x) for x in d["effects"]))

    def test_score_and_desk_cards(self):
        ev = next(e for e in PipelineTest.evs if e.liquid)
        row = led.new_row(ev, logged=ev.filed)
        model = dict(self.model)
        model["effects"] = {f: {} for f in adv.TILT_FEATURES}
        role = adv.bt.FEATURES["role"](ev)
        model["effects"]["role"] = {role: {"effects": [0.03, 0.05], "tilt": 0.03}}
        sc = adv.score(row, model)
        self.assertEqual(sc["tier"], "above")
        self.assertEqual(sc["tilts"][0]["level"], role)
        desk = dash.dashboard_data(PipelineTest.res, [row], None, today=ev.filed, advisor=model)["desk"]
        self.assertEqual(len(desk["cards"]), 1)
        card = desk["cards"][0]
        self.assertEqual(card["tier"], "above")
        self.assertEqual(card["exit"], adv.add_market_days(card["entry"], 62))
        json.dumps(desk, allow_nan=False)

    def test_one_card_per_company_from_one_row(self):
        ev = next(e for e in PipelineTest.evs if e.liquid)
        base = led.new_row(ev, logged=ev.filed)
        day = base["filed_at"][:10]
        before = (dt.date.fromisoformat(day) - dt.timedelta(days=3)).isoformat() + base["filed_at"][10:]
        small = dict(base, accession="a1", owner_cik="1", owner_name="Small", value=1_000.0, avg_price=5.0, cluster=3)
        big = dict(base, accession="a2", owner_cik="2", owner_name="Big", value=500_000.0, avg_price=9.5, cluster=1)
        old = dict(base, accession="a3", owner_cik="3", owner_name="Old", filed_at=before)
        desk = dash.dashboard_data(PipelineTest.res, [small, big, old], None, today=day, advisor=self.model)["desk"]
        self.assertEqual(len(desk["cards"]), 1)
        card = desk["cards"][0]
        self.assertEqual(card["buyer"]["name"], "Big")  # the largest buy that day, not the best-scoring one
        self.assertEqual(card["insider_price"], 9.5)
        self.assertEqual(card["cluster"], 3)  # rows logged early can miss same-day filings
        self.assertEqual(card["others"], 1)
        self.assertEqual(card["value"], 501_000.0)
        self.assertEqual(card["earlier"], [before[:10]])

    def test_entered_cards_show_the_latest_close(self):
        ev = next(e for e in PipelineTest.evs if e.liquid)
        row = led.new_row(ev, logged=ev.filed)
        pending = dash.dashboard_data(PipelineTest.res, [row], None, today=ev.filed, advisor=self.model)["desk"]["cards"][0]
        self.assertEqual((pending["close"], pending["close_date"]), (dash._r(row["price"], 5), None))
        entered = dict(row, entry_date=adv.next_market_day(row["filed_at"][:10]), entry_price=row["price"],
                       last_price=row["price"] * 0.7, last_seen="2030-01-02", status="open")
        card = dash.dashboard_data(PipelineTest.res, [entered], None, today=ev.filed, advisor=self.model)["desk"]["cards"][0]
        self.assertEqual(card["close"], dash._r(row["price"] * 0.7, 5))
        self.assertEqual(card["close_date"], "2030-01-02")
        self.assertEqual(card["pre_close"], dash._r(row["price"], 5))

    def test_template_reads_only_fields_the_cards_have(self):
        html = dash.TEMPLATE.read_text(encoding="utf-8")
        block = html[html.index("// ---------- signal desk"):html.index("// ---------- what works")]
        ev = next(e for e in PipelineTest.evs if e.liquid)
        card = dash.dashboard_data(PipelineTest.res, [led.new_row(ev, logged=ev.filed)], None, today=ev.filed,
                                   advisor=self.model)["desk"]["cards"][0]
        self.assertLessEqual(set(re.findall(r"\bc\.(\w+)", block)), set(card))

    def test_the_ledger_keeps_the_profile_recorded_at_logging(self):
        import tempfile
        from pathlib import Path
        ev = next(e for e in PipelineTest.evs if e.liquid)
        row = led.new_row(ev, logged=ev.filed)
        sc = adv.score(row, self.model)
        row["tier"], row["tilt"] = sc["tier"], sc["tilt"]
        with tempfile.TemporaryDirectory() as d:
            led.save(Path(d) / "picks.csv", [row, dict(led.new_row(ev, logged=ev.filed), accession="untiered")])
            back = {r["accession"]: r for r in led.load(Path(d) / "picks.csv")}
        self.assertEqual(back[row["accession"]]["tier"], sc["tier"])
        self.assertAlmostEqual(back[row["accession"]]["tilt"], sc["tilt"], places=6)
        self.assertFalse(back["untiered"]["tier"])  # rows logged before 2026-10-23 have no profile
        self.assertIsNone(back["untiered"]["tilt"])

    def test_no_model_means_no_desk(self):
        ev = next(e for e in PipelineTest.evs if e.liquid)
        self.assertIsNone(dash.dashboard_data(PipelineTest.res, [led.new_row(ev, logged=ev.filed)], None)["desk"])


class HypothesesTest(unittest.TestCase):
    def test_bad_entries_are_skipped_not_misattributed(self):
        PipelineTest.setUpClass()
        ev = next(e for e in PipelineTest.evs if e.priced)
        row = led.new_row(ev, logged=ev.filed)
        hyp = {"registered": "2000-01-01", "hypotheses": [{"strategy": "retired_key", "claim": "x"}, {"claim": "no key"},
                                                          {"strategy": "avoid: role Other", "claim": "lags"}]}
        out = dash.dashboard_data(PipelineTest.res, [row], hyp)["live"]["hypotheses"]
        self.assertEqual([h["key"] for h in out], ["avoid: role Other"])
        self.assertEqual(dash.dashboard_data(PipelineTest.res, [row], {"hypotheses": []})["live"]["hypotheses"], [])

    def test_tier_groups_count_a_company_day_once(self):
        PipelineTest.setUpClass()
        ev = next(e for e in PipelineTest.evs if e.priced)
        row = led.new_row(ev, logged=ev.filed)
        small, big = dict(row, accession="s", value=1.0, tier="above"), dict(row, accession="b", value=9.0, tier="below")
        hyp = {"registered": "2000-01-01", "hypotheses": [{"strategy": "tier: above vs below", "claim": "x"}]}
        h = dash.dashboard_data(PipelineTest.res, [small, big], hyp)["live"]["hypotheses"][0]
        self.assertEqual(h["logged"], 0)  # the largest buy is below typical, so no above-typical company-day yet


if __name__ == "__main__":
    unittest.main()
