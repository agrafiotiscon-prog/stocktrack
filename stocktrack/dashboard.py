"""A single-file HTML dashboard of the research: backtest, kinds of buy, portfolios and the live test.

The page is self-contained (data embedded as JSON, no external scripts), so it opens
from disk, renders in the Claude app and can be hosted anywhere. Everything is
computed here; the page's script only draws it.
"""

from __future__ import annotations

import datetime as dt
import json
import math
from pathlib import Path

from stocktrack import advisor as adv
from stocktrack.backtest import POST_HOC, PRIMARY, STRATEGIES, cost_per_side
from stocktrack.ledger import is_forward
from stocktrack.vault import FEATURE_TITLES, forward_by_strategy, forward_stats, unique_rows

TEMPLATE = Path(__file__).with_name("dashboard.html")
LIVE_DAYS = 120  # recent buys shown in the live table
DESK_DAYS = 10  # buys shown on the signal desk (calendar days back from the latest filing)
LEADS = ("cfo_exec_25k", "momentum_buy")  # post-hoc leads being judged on the live test
HYPOTHESIS_SAMPLE = 100  # matured 63-session outcomes before a hypothesis is judged


def _r(x, digits: int = 5):
    """Round for the page; NaN and infinities become null."""
    if x is None or isinstance(x, bool):
        return x
    if isinstance(x, float):
        if math.isnan(x) or math.isinf(x):
            return None
        return float(f"{x:.{digits}g}")
    return x


def _ctp(d: dict | None) -> dict:
    d = d or {}
    years = d.get("by_year") or {}
    return {"ann": _r(d.get("annualized")), "t": _r(d.get("t"), 3), "p": _r(d.get("p"), 3),
            "months": d.get("months"), "years_pos": sum(1 for v in years.values() if v > 0),
            "years_n": len(years)}


def _years(d: dict | None) -> dict:
    return {y: _r(v, 4) for y, v in sorted(((d or {}).get("by_year") or {}).items())}


def _kinds(res: dict) -> list[dict]:
    out = []
    for feat, buckets in res["slices"].items():
        for bucket, s in buckets.items():
            ev = s.get("events", {}).get(str(PRIMARY), {})
            vs_all = s.get("vs_all_buys") or {}
            out.append({
                "feature": feat, "bucket": bucket, "signals": s.get("signals", 0),
                "verdict": s.get("verdict", "not enough data"), "enough": bool(s.get("enough_data")),
                "vs_typical": s.get("vs_all_verdict"), "vs_typical_ann": _r(vs_all.get("annualized")),
                "vs_typical_holm": _r(s.get("p_holm_vs_all"), 3),
                "excess": _r(ev.get("mean")), "median": _r(ev.get("median")), "beat": _r(ev.get("hit"), 3),
                "surv": _ctp(s.get("ctp_vs_survivors")), "surv_disc": _ctp(s.get("discovery_vs_survivors")),
                "surv_hold": _ctp(s.get("holdout_vs_survivors")), "surv_years": _years(s.get("ctp_vs_survivors")),
                "spy": _ctp(s.get("ctp")), "spy_disc": _ctp(s.get("discovery")), "spy_hold": _ctp(s.get("holdout")),
                "spy_years": _years(s.get("ctp")),
            })
    return out


def _curve(curve: list) -> list:
    return [[m, _r(s, 5), _r(b, 5)] for m, s, b in curve]


def _strategies(res: dict) -> list[dict]:
    out = []
    for key, s in res["strategies"].items():
        holds = {}
        for hold, p in s.get("portfolio", {}).items():
            holds[hold] = {k: _r(p.get(k)) for k in (
                "trades", "avg_positions", "strategy_cagr", "strategy_vol", "strategy_sharpe", "strategy_max_drawdown",
                "spy_cagr", "spy_sharpe", "spy_max_drawdown", "hedged_cagr", "hedged_sharpe", "hedged_max_drawdown",
                "beta", "alpha_annual", "years_beating_spy", "costs_pct_nav_per_year", "final_nav")}
            holds[hold]["curve"] = _curve(p.get("curve", []))
        costs = s.get("portfolio_costs", {})
        out.append({
            "key": key, "title": s.get("description") or STRATEGIES[key][0], "post_hoc": key in POST_HOC,
            "signals": s.get("signals", 0), "surv": _ctp(s.get("ctp_vs_survivors")), "spy": _ctp(s.get("ctp")),
            "spy_disc": _ctp(s.get("discovery")), "spy_hold": _ctp(s.get("holdout")), "holds": holds,
            "cost_free_cagr": _r((costs.get("0x") or {}).get("strategy_cagr")),
            "double_cost_cagr": _r((costs.get("2x") or {}).get("strategy_cagr")),
        })
    return out


def _live_rows(ledger: list[dict], today: str) -> list[dict]:
    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=LIVE_DAYS)).isoformat()
    rows = [r for r in ledger if r["filed_at"][:10] >= cutoff]
    rows.sort(key=lambda r: (r["filed_at"], r["accession"]), reverse=True)
    return [{
        "filed": r["filed_at"][:10], "symbol": r["symbol"] or r["ticker"], "company": r["issuer_name"],
        "insider": r["owner_name"], "role": r["officer_title"] or r["role"], "value": _r(r["value"], 6),
        "score": r["score"], "cluster": r["cluster"], "kind": r["kind"], "prior": _r(r["prior_ret"], 3),
        "strategies": [k for k in (r["strategies"] or "").split("|") if k in STRATEGIES],
        "entry": r["entry_date"], "status": r["status"], "now": _r(r.get("abn_now"), 4),
        "forward": is_forward(r), "url": r["url"],
    } for r in rows]


def _hypotheses(hyp: dict, ledger: list[dict]) -> list[dict]:
    """Progress of each registered hypothesis on the forward-test rows that count for it.

    Rows count once their entry shows they were logged before the open; rows logged before an
    upcoming open (still pending) are included in "logged" but can't have outcomes yet.
    """
    if not hyp or not hyp.get("registered"):
        return []
    start = (dt.date.fromisoformat(hyp["registered"]) + dt.timedelta(days=1)).isoformat()
    recent = [r for r in ledger if r["logged"][:10] >= start]
    counted = [r for r in recent if is_forward(r)]
    logged = [r for r in recent if is_forward(r) or r["status"] == "pending"]
    everyone = unique_rows(counted)

    def avoid(r: dict) -> bool:
        return r["role"] == "Other" or r["kind"] == "routine"

    out = []
    for h in hyp.get("hypotheses", []):
        key = h.get("strategy") or ""
        if key in STRATEGIES:
            match, title = (lambda r, k=key: k in (r["strategies"] or "").split("|")), STRATEGIES[key][0]
        elif key.startswith("avoid:"):
            match, title = avoid, "Owners filing as \"Other\" and routine insiders"
        else:
            continue  # an unknown group can't be scored
        s = forward_stats(unique_rows([r for r in counted if match(r)]), PRIMARY)
        base = forward_stats(everyone, PRIMARY)
        out.append({"key": key, "title": title, "claim": h.get("claim", ""), "expected": h.get("expected", ""),
                    "logged": len(unique_rows([r for r in logged if match(r)])), "since": start,
                    "matured": s.get("n", 0), "needed": HYPOTHESIS_SAMPLE,
                    "mean": _r(s.get("mean")), "all_mean": _r(base.get("mean"))})
    return out


def _desk(ledger: list[dict], model: dict | None) -> dict | None:
    """Report cards for the latest buys: one per company and filing day."""
    if not model or not ledger:
        return None
    latest = max(r["filed_at"][:10] for r in ledger)
    cutoff = (dt.date.fromisoformat(latest) - dt.timedelta(days=DESK_DAYS)).isoformat()
    groups: dict[tuple, list[dict]] = {}
    for r in ledger:
        if r["filed_at"][:10] >= cutoff:
            groups.setdefault((r["issuer_cik"], r["filed_at"][:10]), []).append(r)
    cards = []
    for (_, filed), rows in groups.items():
        scored = [(adv.score(r, model), r) for r in rows]
        sc, lead = max(scored, key=lambda x: (x[0]["tilt"], x[1]["value"] or 0))
        entry = lead["entry_date"] or adv.next_market_day(filed)
        price = lead["entry_price"] or lead["price"]
        cards.append({
            "symbol": lead["symbol"] or lead["ticker"], "company": lead["issuer_name"], "filed": filed,
            "url": lead["url"], "status": lead["status"], "entered": bool(lead["entry_date"]),
            "entry": entry, "exit": adv.add_market_days(entry, PRIMARY - 1),
            "entry_price": _r(lead["entry_price"], 5), "last_close": _r(lead["price"], 5), "price": _r(price, 5),
            "insider_price": _r(lead["avg_price"], 5), "adv": _r(lead["adv"], 4), "prior": _r(lead["prior_ret"], 3),
            "now": _r(lead.get("abn_now"), 4), "ret_now": _r(lead.get("ret_now"), 4), "forward": is_forward(lead),
            "cost_side": _r(cost_per_side(lead["price"], lead["adv"]), 3), "cluster": lead["cluster"],
            "insiders": [{"name": r["owner_name"], "role": r["officer_title"] or r["role"], "value": _r(r["value"], 6)}
                         for r in sorted(rows, key=lambda r: -(r["value"] or 0))],
            "value": _r(sum(r["value"] or 0 for r in rows), 6),
            "leads": sorted({k for r in rows for k in (r["strategies"] or "").split("|") if k in LEADS}),
            "tier": sc["tier"], "tilt": _r(sc["tilt"], 4),
            "tilts": [{"feature": t["feature"], "level": t["level"], "tilt": _r(t["tilt"], 4),
                       "effects": [_r(x, 4) for x in t["effects"]]} for t in sc["tilts"]],
            "risk": {k: _r(v, 4) for k, v in sc["risk"].items()},
        })
    order = {"above": 0, "typical": 1, "below": 2}
    cards.sort(key=lambda c: (order[c["tier"]], -(c["tilt"] or 0), -(c["value"] or 0)))
    v = model.get("validation", {})
    return {
        "cards": cards, "since": cutoff, "latest": latest,
        "base": {k: (_r(x) if not isinstance(x, dict) else {kk: _r(vv) for kk, vv in x.items()})
                 for k, x in model.get("base", {}).items()},
        "validation": {"tiers": {k: {"ann": _r(t.get("ctp", {}).get("annualized")), "t": _r(t.get("ctp", {}).get("t"), 3),
                                     "n": t.get("n"), "beat_spy": _r(t.get("beat_spy"), 3)}
                                 for k, t in v.get("tiers", {}).items()},
                       "spread": {k: _r(x) for k, x in v.get("above_minus_below", {}).items()},
                       "portfolios": {k: {kk: _r(vv) for kk, vv in x.items()} for k, x in v.get("portfolios", {}).items()},
                       "chosen_on": v.get("chosen_on"), "tested_on": v.get("tested_on")},
        "tier_share": {k: _r(x, 3) for k, x in model.get("tier_share", {}).items()},
        "rules": model.get("rules", {}), "tier_edge": model.get("tier_edge"), "fitted": model.get("fitted"),
    }


def dashboard_data(res: dict, ledger: list[dict], hypotheses: dict | None = None, today: str | None = None,
                   generated: str | None = None, advisor: dict | None = None) -> dict:
    today = today or dt.date.today().isoformat()
    o, m = res["overall"], res["meta"]
    ev = o["events"][str(PRIMARY)]
    all_liquid = res["strategies"].get("all_liquid", {}).get("portfolio", {}).get(f"{PRIMARY}d", {})
    fwd = forward_by_strategy(ledger)
    statuses: dict[str, int] = {}
    for r in ledger:
        statuses[r["status"]] = statuses.get(r["status"], 0) + 1
    return {
        "meta": {"run_date": m.get("run_date"), "last_price_date": m.get("last_price_date"),
                 "datasets": m.get("datasets"), "filings": m.get("filings"), "signals": o.get("signals"),
                 "git_commit": m.get("git_commit"), "config_hash": m.get("config_hash"), "today": today,
                 "generated": generated or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")},
        "overall": {
            "surv": _ctp(o.get("ctp_vs_survivors")), "surv_disc": _ctp(o.get("discovery_vs_survivors")),
            "surv_hold": _ctp(o.get("holdout_vs_survivors")), "spy": _ctp(o.get("ctp")),
            "spy_disc": _ctp(o.get("discovery")), "spy_hold": _ctp(o.get("holdout")),
            "event": {"mean": _r(ev.get("mean")), "median": _r(ev.get("median")), "beat": _r(ev.get("hit"), 3),
                      "ci": [_r(x) for x in ev.get("ci", [])], "n": ev.get("n")},
            "pre_drift": _r(o.get("pre_drift_mean")),
            "placebo": {k: _r(v) for k, v in o.get("placebo", {}).items()},
            "survivorship": {k: _r(v) for k, v in o.get("survivorship", {}).items()},
            "copy_all": {"cagr": _r(all_liquid.get("strategy_cagr")), "spy_cagr": _r(all_liquid.get("spy_cagr")),
                         "mdd": _r(all_liquid.get("strategy_max_drawdown")),
                         "hedged": _r(all_liquid.get("hedged_cagr")), "trades": all_liquid.get("trades"),
                         "signals": res["strategies"].get("all_liquid", {}).get("signals")},
        },
        "years": [{"year": y, "surv": _r(v, 4), "spy": _r((o.get("ctp") or {}).get("by_year", {}).get(y), 4)}
                  for y, v in sorted(((o.get("ctp_vs_survivors") or {}).get("by_year") or {}).items())],
        "features": [{"key": k, "title": t} for k, t in FEATURE_TITLES.items() if k in res["slices"]],
        "kinds": _kinds(res),
        "strategies": _strategies(res),
        "live": {
            "rows": _live_rows(ledger, today),
            "logged": len(ledger), "statuses": statuses,
            "forward": {"signals": fwd["all"]["rows"], "open": fwd["all"]["open_now"].get("n", 0),
                        "open_mean": _r(fwd["all"]["open_now"].get("mean")),
                        "matured": {str(h): fwd["all"][str(h)].get("n", 0) for h in (5, 21, 63)},
                        "means": {str(h): _r(fwd["all"][str(h)].get("mean")) for h in (5, 21, 63)}},
            "hypotheses": _hypotheses(hypotheses or {}, ledger),
        },
        "desk": _desk(ledger, advisor),
    }


def _json_for_script(data: dict) -> str:
    """JSON that is safe inside a <script> element: no "</script>" or "<!--" can appear."""
    text = json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return text.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def render(data: dict) -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    marker = "/*__DASHBOARD_DATA__*/null"
    assert template.count(marker) == 1, "dashboard template is missing its data marker"
    return template.replace(marker, _json_for_script(data))


def build_dashboard(out_dir: str | Path, res: dict, ledger: list[dict], hypotheses: dict | None = None,
                    today: str | None = None, advisor: dict | None = None) -> Path:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "index.html"
    path.write_text(render(dashboard_data(res, ledger, hypotheses, today, advisor=advisor)), encoding="utf-8")
    return path
