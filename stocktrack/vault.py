"""Generate the Obsidian research vault from backtest results and the forward-test ledger.

Every note is plain Markdown with YAML frontmatter, so it reads fine on its own
and the Dataview plugin can query it like a database. Generated notes are
rewritten on each run; anything under a "## Notes" heading in a Research Log
note is preserved, so commentary isn't lost.
"""

from __future__ import annotations

import datetime as dt
import math
import re
from collections import defaultdict
from pathlib import Path

from stocktrack.backtest import PRIMARY, STRATEGIES
from stocktrack.ledger import LEDGER_HORIZONS
from stocktrack.signals import money

VERDICT_ICON = {"works": "✅", "promising": "🟡", "no evidence": "⚪", "looks negative": "🟠", "hurts": "❌",
                "reversed": "🔁", "not enough data": "❔"}
FEATURE_TITLES = {
    "role": "Role", "value": "Purchase size", "stake_increase": "Stake increase", "cluster": "Cluster buying",
    "insider_type": "Routine vs opportunistic", "track_record": "Insider track record",
    "prior_3m_return": "Prior 3-month move", "price": "Share price", "liquidity": "Liquidity",
    "score": "Live score", "plan_purchase": "Plan purchases", "filing_delay": "Filing delay",
    "insider_novelty": "Insider's first buy in a year", "company_novelty": "Company's first insider buy in a year",
}
SIGNAL_NOTE_MIN_SCORE = 40
SIGNAL_NOTE_DAYS = 400


# --- formatting helpers ----------------------------------------------------------


def pct(x, digits: int = 1, signed: bool = True) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    return f"{x * 100:+.{digits}f}%" if signed else f"{x * 100:.{digits}f}%"


def num(x, digits: int = 2) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    return f"{x:.{digits}f}"


def pval(p) -> str:
    if p is None:
        return "–"
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def safe(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|#^\[\]]', "-", name).strip(" .")
    return re.sub(r"\s+", " ", name)[:120] or "untitled"


def yaml_value(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return "" if isinstance(v, float) and (math.isnan(v) or math.isinf(v)) else f"{v:.6g}" if isinstance(v, float) else str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(yaml_value(x) for x in v) + "]"
    s = str(v)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def frontmatter(d: dict) -> str:
    return "---\n" + "".join(f"{k}: {yaml_value(v)}\n" for k, v in d.items()) + "---\n"


def table(headers: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def strategy_title(key: str) -> str:
    return safe(STRATEGIES[key][0]) if key in STRATEGIES else key


# --- forward test -----------------------------------------------------------------


def forward_rows(ledger: list[dict]) -> list[dict]:
    """Ledger rows logged no later than their entry day: a true out-of-sample test."""
    return [r for r in ledger if r["entry_date"] and r["logged"] <= r["entry_date"]]


def forward_stats(rows: list[dict], h: int) -> dict:
    vals = [r[f"abn_{h}"] for r in rows if r.get(f"abn_{h}") is not None]
    if not vals:
        return {"n": 0}
    vals.sort()
    return {"n": len(vals), "mean": sum(vals) / len(vals), "median": vals[len(vals) // 2],
            "hit": sum(1 for v in vals if v > 0) / len(vals)}


def forward_by_strategy(ledger: list[dict]) -> dict[str, dict]:
    rows = forward_rows(ledger)
    out = {"all": rows}
    for key in STRATEGIES:
        out[key] = [r for r in rows if key in (r["strategies"] or "").split("|")]
    return {k: {"rows": len(v), **{str(h): forward_stats(v, h) for h in (5, 21, 63, 126, 252)},
                "open_now": forward_stats([dict(r, abn_0=r.get("abn_now")) for r in v if r["status"] in ("open", "dead")], 0)}
            for k, v in out.items()}


# --- notes ---------------------------------------------------------------------------


def headline(res: dict) -> list[str]:
    o = res["overall"]
    e = o["events"][str(PRIMARY)]
    ci = e.get("ci") or [None, None]
    sb = o.get("survivorship", {})
    best = max(res["strategies"].items(), key=lambda kv: kv[1]["portfolio"]["63d"].get("strategy_cagr") or -9)
    p = best[1]["portfolio"]["63d"]
    return [
        f"On average a stock beat the S&P 500 by **{pct(e['mean'])}** over the 3 months after an insider purchase was "
        f"filed (95% CI {pct(ci[0])} to {pct(ci[1])}, {e['n']:,} signals since 2006). That is roughly "
        f"{pct((1 + e['mean']) ** 4 - 1)} a year, but the median stock *lagged* by {pct(-e['median'], signed=False)}.",
        f"The edge was real in **2006-2015** ({pct(o['discovery'].get('annualized'))} a year, p {pval(o['discovery'].get('p'))}) "
        f"and has **faded since 2016** ({pct(o['holdout'].get('annualized'))} a year, p {pval(o['holdout'].get('p'))}).",
        f"The best simulated portfolio (*{STRATEGIES[best[0]][0]}*) returned {pct(p.get('strategy_cagr'))} a year "
        f"after costs with a {pct(p.get('strategy_max_drawdown'), 0, False)} max drawdown, against SPY's "
        f"{pct(p.get('spy_cagr'))} and {pct(p.get('spy_max_drawdown'), 0, False)}.",
        f"Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did "
        f"like a typical priced buy, the average falls from {pct(sb.get('reported'))} to {pct(sb.get('neutral'))}; if they did "
        f"badly, to {pct(sb.get('pessimistic'))}.",
    ]


def what_works(res: dict, fwd: dict, today: str) -> str:
    lines = [frontmatter({"type": "scoreboard", "updated": today, "backtest": res["meta"]["run_date"]}),
             "# What Works\n",
             "The scoreboard for every idea tested. A ✅ needs the pre-registered bar: significant after correcting for "
             "the number of tests in **both** 2006-2015 and 2016+, positive when entering a session later, positive against "
             "surviving stocks, and positive in most years. See [[Methodology]].\n",
             "## Bottom line\n"]
    lines += [f"- {s}" for s in headline(res)]
    lines.append("\n## Kinds of insider buy\n")
    lines.append("*Excess return* is the 3-month return after the filing, minus SPY's. *vs typical buy* compares the "
                 "kind against all insider buys.\n")
    rows = []
    order = {"works": 0, "promising": 1, "reversed": 2, "looks negative": 3, "hurts": 4, "no evidence": 5,
             "not enough data": 6}
    for feat, buckets in res["slices"].items():
        for label, s in buckets.items():
            e = s["events"][str(PRIMARY)]
            rows.append((order.get(s.get("verdict"), 9), -(s["holdout"].get("excess_mean") or 0), [
                f"{VERDICT_ICON.get(s.get('verdict'), '')} {s.get('verdict', '')}",
                f"[[{FEATURE_TITLES.get(feat, feat)}]]: {label}", f"{s['signals']:,}",
                pct(e.get("mean")), pct(e.get("hit"), 0, False),
                pct(s["discovery"].get("annualized")), pct(s["holdout"].get("annualized")),
                s.get("vs_all_verdict", "–"), pct(s["ctp"].get("years_positive"), 0, False)]))
    rows.sort(key=lambda r: (r[0], r[1]))
    lines.append(table(["Verdict", "Kind of buy", "Signals", "3-mo excess", "Beat SPY", "2006-15 /yr", "2016+ /yr",
                        "vs typical buy", "Years +"], [r[2] for r in rows]))
    lines.append("\n## Strategies\n")
    lines.append("Simulated $100K account, up to 20 positions, each held 3 months, after trading costs. "
                 "*Live* is the forward test: buys logged before their outcome existed.\n")
    srows = []
    for key, s in res["strategies"].items():
        p = s["portfolio"]["63d"]
        f = fwd.get(key, {})
        f21 = f.get("21", {})
        srows.append([f"[[{strategy_title(key)}]]", f"{s['signals']:,}", pct(p.get("strategy_cagr")),
                      pct(p.get("spy_cagr")), num(p.get("strategy_sharpe")), pct(p.get("strategy_max_drawdown"), 0, False),
                      pct(s["holdout"].get("annualized")), f"{f21.get('n', 0)}",
                      pct(f21.get("mean")) if f21.get("n") else "–"])
    lines.append(table(["Strategy", "Signals", "CAGR", "SPY CAGR", "Sharpe", "Max DD", "2016+ excess /yr",
                        "Live matured (1 mo)", "Live 1-mo excess"], srows))
    lines.append("\n## What could make this wrong\n")
    o = res["overall"]
    lines += [
        f"- **Survivorship (flatters results).** Only companies still listed today can be priced: coverage is "
        f"{_coverage_range(res)}. Against an index of other surviving stocks the edge is "
        f"{pct(o['discovery_vs_survivors'].get('annualized'))}/yr in 2006-2015 and "
        f"{pct(o['holdout_vs_survivors'].get('annualized'))}/yr since 2016 (vs SPY: "
        f"{pct(o['discovery'].get('annualized'))} and {pct(o['holdout'].get('annualized'))}).",
        f"- **The move before you can act.** Between the insider's trade and the first possible entry the stock already "
        f"moved {pct(o.get('pre_drift_mean'))} on average. Entering one session later (variant C): "
        f"{pct(o['variant_c'].get('mean'))}.",
        f"- **Crisis rebounds.** {pct(o['ctp'].get('crisis_share'), 0, False)} of all excess return came from Sep 2008-Jun 2009 and "
        "Mar-Jun 2020.",
        "- **Costs are assumed**, not measured (0.1-1% per side by price, more for illiquid names). See the 0x/2x cost "
        "runs in each strategy note.",
        "- **Market beta only.** No size or value adjustment; small caps may explain part of any edge.",
        f"- **Placebo.** The same stocks a year after the buy returned {pct(o['placebo'].get('placebo_mean'))} over 3 "
        f"months, vs {pct(o['placebo'].get('event_mean'))} right after it.",
    ]
    lines.append("\n## Live forward test\n")
    lines.append(_forward_table(fwd))
    return "\n".join(lines) + "\n"


def _coverage_range(res: dict) -> str:
    by = res["coverage"]["by_year"]
    years = sorted(by)
    return f"{pct(by[years[0]]['coverage'], 0, False)} of buys in {years[0]} up to {pct(by[years[-1]]['coverage'], 0, False)} in {years[-1]}"


def _forward_table(fwd: dict) -> str:
    rows = []
    for key in ["all", *STRATEGIES]:
        f = fwd.get(key)
        if not f:
            continue
        name = "All logged buys" if key == "all" else f"[[{strategy_title(key)}]]"
        cells = [name, f"{f['rows']:,}"]
        for h in ("5", "21", "63"):
            s = f[h]
            cells.append(f"{pct(s['mean'])} (n={s['n']}, {pct(s['hit'], 0, False)} won)" if s.get("n") else "–")
        o = f["open_now"]
        cells.append(f"{pct(o['mean'])} (n={o['n']})" if o.get("n") else "–")
        rows.append(cells)
    note = ("The ledger started on 2026-10-19. Results need months to mature; until then this table is mostly empty "
            "and that is expected.\n\n")
    return note + table(["Group", "Logged", "1 week vs SPY", "1 month vs SPY", "3 months vs SPY", "Open now vs SPY"], rows)


def home(res: dict, fwd: dict, ledger: list[dict], today: str) -> str:
    recent = sorted((r for r in ledger if r["score"] >= SIGNAL_NOTE_MIN_SCORE), key=lambda r: r["filed_at"], reverse=True)[:15]
    lines = [frontmatter({"type": "home", "updated": today}),
             "# Insider Buying Research\n",
             "A research log on one question: **do stocks go up after insiders buy them, and which buys are worth "
             "following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged "
             "and tracked forward.\n",
             "- [[What Works]]: the scoreboard",
             f"- [[{res['meta']['run_date']} Backtest]]: the latest full backtest",
             f"- [[{today}]]: today's research log",
             "- [[Best Insiders]] · [[Methodology]]",
             "\n## Headline\n"]
    lines += [f"- {s}" for s in headline(res)]
    lines.append("\n## Latest notable buys\n")
    if recent:
        lines.append(table(["Filed", "Ticker", "Insider", "Role", "Value", "Score", "vs SPY so far"],
                           [[r["filed_at"][:10], f"[[{safe(r['ticker'] or r['symbol'])}]]", f"[[{insider_note(r)}]]",
                             r["officer_title"] or r["role"], money(r["value"]), r["score"], pct(r.get("abn_now"))]
                            for r in recent]))
    else:
        lines.append("No notable buys logged yet.\n")
    lines += ["\n## Live queries (Dataview plugin)\n",
              "```dataview\nTABLE ticker, insider, role, score, value, abn_now AS \"vs SPY so far\", status\n"
              "FROM \"Signals\"\nSORT filed DESC\nLIMIT 30\n```\n",
              "```dataview\nTABLE verdict, signals, holdout_excess AS \"2016+ excess/yr\"\nFROM \"Slices\"\n"
              "SORT holdout_excess DESC\n```\n"]
    return "\n".join(lines)


def methodology(res: dict) -> str:
    m = res["meta"]
    return f"""{frontmatter({"type": "methodology", "backtest": m["run_date"]})}
# Methodology

**Data.** SEC Insider Transactions Data Sets ({m.get("datasets", "")}) plus daily EDGAR filings for the latest weeks.
Only Form 4 open-market purchases (transaction code P) count. Prices are daily, split- and dividend-adjusted, from Yahoo
Finance (snapshot {m.get("price_snapshot", "")}, last price date {m.get("last_price_date", "")}).

**One signal per company per day.** Several insiders filing on the same day share one return, so they count once.
Repeat reports of the same purchase by related filers (a fund and its manager) count once.

**No look-ahead.**
- Entry is the **open of the first trading session after the filing date**, the first price anyone could act on.
  Variant C enters at that session's close.
- Clusters, insider track records and the routine/opportunistic split use only filings and outcomes public
  before entry. A test deletes all later filings and checks the features don't change.
- Bucket edges are fixed numbers, written down in `data/backtest/preregistration.json` before the first run.

**Returns.** Horizons count market sessions (1, 5, 21, 63, 126, 252; 63, about 3 months, is primary). Excess return =
stock minus SPY over the same window. Returns are winsorized at the 1st/99th percentile. Windows that run past the
data are left out, never partial. A stock that stops trading for 10+ sessions has no return for later horizons.

**Survivor index.** Equal-weighted daily returns of every priced stock, each joining only after its first insider
filing is public (joining earlier would select on future insider buys, which tend to follow declines).

**Price checks.** The insider's reported price must be within 0.67-1.5x of the stock's market price on the trade
date. Otherwise the price series is presumed to be a different security (a reused ticker, another share class, an
ADR) or the filing a typo, and the signal is dropped. Tickers resolve through SEC's company ID, never the symbol
alone. Isolated bad ticks and sub-penny days are removed.

**Significance.** Each kind of buy becomes a calendar-time portfolio: every signal held 63 sessions, buy-and-hold
weights, one position per company. Its monthly return minus SPY's is tested with Newey-West t-statistics (3 lags) and a
block bootstrap. 2006-2015 is the discovery period and 2016 onward the holdout. p-values get a Holm correction for the
number of slices tested ({_k(res)} tests per family). Every test ever run is appended to `data/backtest/tests_log.csv`.

**Verdicts.** ✅ works = significant (after Holm) and positive in both periods, positive when entering a session later,
positive against the survivor index in both periods, and positive in 60%+ of years. 🟡 promising = significant in one
period only. 🔁 reversed = significant in opposite directions in the two periods. ❌ hurts / 🟠 looks negative =
significantly negative. ⚪ no evidence = can't tell from zero. ❔ not enough data = fewer than 200 signals or 60 months
in discovery. Holdout-only findings are Holm-corrected across all slices.

**Portfolio simulation.** $100,000, 20 slots, each signal bought at the next open and held 21/63/126 sessions. When
signals outnumber free slots, the highest scores win. Position size is the smaller of NAV/20, cash and 2% of daily
dollar volume. Only stocks at $2+ trading $1M+/day qualify. Costs per side: under $5: 1%, $5-10: 0.5%, $10-25: 0.25%,
$25+: 0.1%, plus 0.25% if dollar volume is under $5M and 0.25% if the position exceeds 1% of daily volume. Idle cash earns
{m.get("risk_free", "0")}.

**Known limits.** Prices exist only for companies still listed today (see coverage in the backtest note). That flatters
results, and the survivor index and survivorship bound show by how much. The adjustment is for market beta only (no
size/value factors). The routine/opportunistic split uses purchases only, because sales aren't loaded.

**Reproducibility.** Git commit `{m.get("git_commit", "")}`, config hash `{m.get("config_hash", "")}`, seed {m.get("seed", "")}.
"""


def _k(res: dict) -> int:
    return sum(1 for rows in res["slices"].values() for r in rows.values() if r.get("enough_data"))


def backtest_report(res: dict) -> str:
    m, o = res["meta"], res["overall"]
    lines = [frontmatter({"type": "backtest", "date": m["run_date"], "signals": o["signals"],
                          "excess_63d": o["events"][str(PRIMARY)].get("mean"),
                          "discovery_excess_yr": o["discovery"].get("annualized"),
                          "holdout_excess_yr": o["holdout"].get("annualized")}),
             f"# {m['run_date']} Backtest\n"]
    lines += [f"- {s}" for s in headline(res)]
    lines.append("\n## Returns after the filing, by horizon\n")
    lines.append(table(["Horizon", "Signals", "Mean vs SPY", "Median", "Beat SPY", "Stock return (mean)"],
                       [[f"{h} sessions", f"{s['n']:,}", pct(s.get("mean"), 2), pct(s.get("median"), 2),
                         pct(s.get("hit"), 0, False), pct(s.get("stock_return"), 2)]
                        for h, s in o["events"].items() if s.get("n")]))
    lines.append("\n## Robustness\n")
    c = o["ctp"]
    lines.append(table(["Check", "Result"], [
        ["Calendar-time portfolio, monthly excess", f"{pct(c.get('excess_mean'), 2)} (t {num(c.get('t'))}, p {pval(c.get('p'))}, "
                                                    f"{c.get('months')} months)"],
        ["2006-2015 (discovery)", f"{pct(o['discovery'].get('annualized'))}/yr, p {pval(o['discovery'].get('p'))}"],
        ["2016+ (holdout)", f"{pct(o['holdout'].get('annualized'))}/yr, p {pval(o['holdout'].get('p'))}"],
        ["Beta to SPY", num(c.get("beta"))],
        ["Entering one session later (variant C)", pct(o["variant_c"].get("mean"), 2)],
        ["Against surviving stocks instead of SPY (event mean)", pct(o["vs_survivors"].get("mean"), 2)],
        ["Against surviving stocks: 2006-2015 / 2016+ (per year)",
         f"{pct(o['discovery_vs_survivors'].get('annualized'))} / {pct(o['holdout_vs_survivors'].get('annualized'))}"],
        ["Same stocks a year later (placebo)", f"{pct(o['placebo'].get('placebo_mean'), 2)}; event minus placebo "
                                               f"{pct(o['placebo'].get('difference'), 2)}"],
        ["Move between trade and first possible entry", pct(o.get("pre_drift_mean"), 2)],
        ["Survivorship bound (reported / neutral / pessimistic)",
         " / ".join(pct(o["survivorship"].get(k), 2) for k in ("reported", "neutral", "pessimistic"))],
        ["Share of excess from 2008-09 and 2020 crises", pct(c.get("crisis_share"), 0, False)],
        ["Sub-$1 or illiquid tail (left out)", f"{pct(o['excluded_tail'].get('mean'), 2)} mean, "
                                               f"{pct(o['excluded_tail'].get('median'), 2)} median, n={o['excluded_tail'].get('n', 0):,}"],
    ]))
    lines.append("\n## Excess return by year (calendar-time, all buys)\n")
    by = c.get("by_year", {})
    lines.append(table(["Year", "Excess vs SPY"], [[y, pct(v)] for y, v in sorted(by.items())]))
    lines.append("\n## Coverage\n")
    lines.append(table(["Year", "Signals", "Priced", "Coverage", "In study"],
                       [[y, f"{v['signals']:,}", f"{v['priced']:,}", pct(v["coverage"], 0, False), f"{v['in_study']:,}"]
                        for y, v in res["coverage"]["by_year"].items()]))
    st = res["coverage"]["status"]
    lines.append("\nWhy signals weren't priced: " + ", ".join(f"{k} {v:,}" for k, v in sorted(st.items(), key=lambda kv: -kv[1])) + ".\n")
    lines.append("\n## Walk-forward score threshold\n")
    wf = res["walk_forward"]
    lines.append(f"Each year from 2011 the score threshold is picked using only earlier months, then applied unchanged. "
                 f"Joined result: {pct(wf['ctp'].get('annualized'))}/yr over SPY (p {pval(wf['ctp'].get('p'))}, "
                 f"{wf['signals']:,} signals). Thresholds chosen: "
                 + ", ".join(f"{y}: {t}" for y, t in wf["thresholds"].items()) + ".\n")
    lines.append("\n## Slices\n")
    for feat in res["slices"]:
        lines.append(f"- [[{FEATURE_TITLES.get(feat, feat)}]]")
    lines.append("\n## Strategies\n")
    for key in res["strategies"]:
        lines.append(f"- [[{strategy_title(key)}]]")
    lines.append(f"\n## Run\n\n" + "".join(f"- {k}: `{v}`\n" for k, v in m.items()))
    return "\n".join(lines)


def slice_note(feat: str, buckets: dict, res: dict) -> str:
    title = FEATURE_TITLES.get(feat, feat)
    best = max(buckets.values(), key=lambda s: s["holdout"].get("annualized") or -9)
    lines = [frontmatter({"type": "slice", "feature": feat, "verdict": best.get("verdict"),
                          "signals": sum(s["signals"] for s in buckets.values()),
                          "holdout_excess": best["holdout"].get("annualized")}),
             f"# {title}\n"]
    note = res.get("feature_notes", {}).get(feat)
    if note:
        lines.append(note + "\n")
    rows = []
    for label, s in buckets.items():
        e = s["events"][str(PRIMARY)]
        rows.append([f"{VERDICT_ICON.get(s.get('verdict'), '')} {label}", f"{s['signals']:,}", pct(e.get("mean")),
                     pct(e.get("median")), pct(e.get("hit"), 0, False),
                     pct(s["discovery"].get("annualized")) + f" (p {pval(s.get('p_holm_discovery') or s['discovery'].get('p'))})",
                     pct(s["holdout"].get("annualized")) + f" (p {pval(s['holdout'].get('p'))})",
                     pct(s["variant_c"].get("mean")),
                     f"{pct(s['discovery_vs_survivors'].get('annualized'))} / {pct(s['holdout_vs_survivors'].get('annualized'))}",
                     s.get("vs_all_verdict", "–")])
    lines.append(table(["Bucket", "Signals", "3-mo vs SPY", "Median", "Beat SPY", "2006-15 /yr", "2016+ /yr",
                        "Enter later", "vs survivors (06-15 / 16+)", "vs typical buy"], rows))
    lines.append("\nHorizon detail (mean excess vs SPY):\n")
    lines.append(table(["Bucket", "1 week", "1 month", "3 months", "6 months", "1 year"],
                       [[label] + [pct(s["events"][h].get("mean")) for h in ("5", "21", "63", "126", "252")]
                        for label, s in buckets.items()]))
    lines.append("\nBack to [[What Works]].\n")
    return "\n".join(lines)


def strategy_note(key: str, s: dict, fwd: dict, ledger: list[dict]) -> str:
    desc = STRATEGIES[key][0]
    p = s["portfolio"]["63d"]
    lines = [frontmatter({"type": "strategy", "key": key, "signals": s["signals"], "cagr": p.get("strategy_cagr"),
                          "spy_cagr": p.get("spy_cagr"), "sharpe": p.get("strategy_sharpe"),
                          "max_drawdown": p.get("strategy_max_drawdown"), "holdout_excess": s["holdout"].get("annualized")}),
             f"# {desc}\n", f"Rule key: `{key}`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.\n",
             "## Backtest\n"]
    e = s["events"]
    lines.append(table(["Measure", "Value"], [
        ["Signals", f"{s['signals']:,}"],
        ["3-month excess vs SPY (mean / median)", f"{pct(e['63'].get('mean'))} / {pct(e['63'].get('median'))}"],
        ["Beat SPY over 3 months", pct(e["63"].get("hit"), 0, False)],
        ["Entering one session later", pct(s["variant_c"].get("mean"))],
        ["vs surviving stocks", pct(s["vs_survivors"].get("mean"))],
        ["2006-2015 excess /yr", f"{pct(s['discovery'].get('annualized'))} (p {pval(s['discovery'].get('p'))})"],
        ["2016+ excess /yr", f"{pct(s['holdout'].get('annualized'))} (p {pval(s['holdout'].get('p'))})"],
    ]))
    lines.append("\n## Simulated portfolio ($100K, 20 slots, after costs)\n")
    rows = []
    for hold, sim in s["portfolio"].items():
        rows.append([hold, pct(sim.get("strategy_cagr")), pct(sim.get("spy_cagr")), num(sim.get("strategy_sharpe")),
                     num(sim.get("spy_sharpe")), pct(sim.get("strategy_max_drawdown"), 0, False), num(sim.get("beta")),
                     pct(sim.get("years_beating_spy"), 0, False), f"{sim.get('trades', 0):,}",
                     pct(sim.get("costs_pct_nav_per_year"), 1, False)])
    lines.append(table(["Hold", "CAGR", "SPY", "Sharpe", "SPY Sharpe", "Max DD", "Beta", "Years beating SPY",
                        "Trades", "Costs/yr"], rows))
    c0, c2 = s["portfolio_costs"]["0x"], s["portfolio_costs"]["2x"]
    lines.append(f"\nCost sensitivity (63-session hold): no costs {pct(c0.get('strategy_cagr'))}/yr, double costs "
                 f"{pct(c2.get('strategy_cagr'))}/yr.\n")
    by = p.get("by_year", {})
    lines.append("\n### Year by year (63-session hold)\n")
    lines.append(table(["Year", "Strategy", "SPY", "Difference"],
                       [[y, pct(v["strategy"]), pct(v["spy"]), pct(v["strategy"] - v["spy"])] for y, v in by.items()]))
    f = fwd.get(key, {})
    lines.append("\n## Live forward test\n")
    if f and any(f[h].get("n") for h in ("5", "21", "63")):
        lines.append(table(["Horizon", "Matured", "Mean vs SPY", "Median", "Beat SPY"],
                           [[f"{h} sessions", f[h]["n"], pct(f[h].get("mean")), pct(f[h].get("median")),
                             pct(f[h].get("hit"), 0, False)] for h in ("5", "21", "63", "126", "252") if f[h].get("n")]))
    else:
        lines.append(f"{f.get('rows', 0)} buys logged so far; none have matured yet.\n")
    live = sorted((r for r in ledger if key in (r["strategies"] or "").split("|")), key=lambda r: r["filed_at"],
                  reverse=True)[:20]
    if live:
        lines.append("\n### Latest live signals\n")
        lines.append(table(["Filed", "Ticker", "Insider", "Value", "Score", "vs SPY so far", "Status"],
                           [[r["filed_at"][:10], f"[[{safe(r['ticker'] or r['symbol'])}]]", f"[[{insider_note(r)}]]",
                             money(r["value"]), r["score"], pct(r.get("abn_now")), r["status"]] for r in live]))
    lines.append(f"\n```dataview\nTABLE ticker, insider, score, abn_now AS \"vs SPY so far\", status\nFROM \"Signals\"\n"
                 f"WHERE contains(strategies, \"{key}\")\nSORT filed DESC\n```\n")
    lines.append("Back to [[What Works]].\n")
    return "\n".join(lines)


def insider_note(r: dict) -> str:
    return safe(r["owner_name"] or r["owner_cik"])


def signal_title(r: dict) -> str:
    return safe(f"{r['filed_at'][:10]} {r['ticker'] or r['symbol']} {r['owner_name']}")


def signal_note(r: dict) -> str:
    strategies = [k for k in (r["strategies"] or "").split("|") if k]
    fm = {"type": "signal", "ticker": r["ticker"] or r["symbol"], "company": r["issuer_name"], "insider": r["owner_name"],
          "role": r["officer_title"] or r["role"], "filed": r["filed_at"][:10], "traded": r["last_date"],
          "score": r["score"], "value": round(r["value"]), "cluster": r["cluster"], "insider_type": r["kind"],
          "price": r["price"], "strategies": strategies, "entry_date": r["entry_date"], "entry_price": r["entry_price"],
          "status": r["status"], "abn_now": r.get("abn_now"), "ret_now": r.get("ret_now")}
    for h in LEDGER_HORIZONS:
        fm[f"abn_{h}"] = r.get(f"abn_{h}")
    fm["forward_test"] = bool(r["entry_date"]) and r["logged"] <= r["entry_date"]
    fm["tags"] = ["signal"] + [f"strategy/{k}" for k in strategies]
    lines = [frontmatter(fm),
             f"# {r['ticker'] or r['symbol']}: {r['owner_name']} bought {money(r['value'])}\n",
             f"[[{safe(r['ticker'] or r['symbol'])}]] · [[{insider_note(r)}]] · "
             + " · ".join(f"[[{strategy_title(k)}]]" for k in strategies) + "\n",
             table(["", ""], [
                 ["Company", r["issuer_name"]], ["Insider", f"{r['owner_name']} ({r['officer_title'] or r['role']})"],
                 ["Traded / filed", f"{r['first_date']} to {r['last_date']} / {r['filed_at'][:10]}"],
                 ["Shares @ price", f"{r['shares']:,.0f} @ ${r['avg_price']:,.2f}" if r["avg_price"] else f"{r['shares']:,.0f}"],
                 ["Score / cluster", f"{r['score']} / {r['cluster']} insider(s)"],
                 ["Insider type / track record", f"{r['kind']} / " + (f"{r['track_n']} earlier buys, {pct(r['track'])}"
                                                                      if r["track_n"] else "no record")],
                 ["Prior 3 months", pct(r["prior_ret"])],
                 ["Entry", f"{r['entry_date']} @ ${r['entry_price']:,.2f}" if r["entry_date"] and r["entry_price"] else "awaiting next open"],
                 ["Status", r["status"]],
             ]),
             "\n## Outcome vs SPY\n",
             table(["1 week", "1 month", "3 months", "6 months", "1 year", "So far"],
                   [[pct(r.get(f"abn_{h}")) for h in LEDGER_HORIZONS] + [pct(r.get("abn_now"))]]),
             f"\n[SEC filing]({r['url']})\n"]
    return "\n".join(lines)


def ticker_note(ticker: str, rows: list[dict]) -> str:
    rows = sorted(rows, key=lambda r: r["filed_at"], reverse=True)
    lines = [frontmatter({"type": "ticker", "ticker": ticker, "company": rows[0]["issuer_name"], "signals": len(rows)}),
             f"# {ticker}: {rows[0]['issuer_name']}\n",
             table(["Filed", "Insider", "Role", "Value", "Score", "vs SPY so far", "Status"],
                   [[f"[[{signal_title(r)}|{r['filed_at'][:10]}]]" if r["score"] >= SIGNAL_NOTE_MIN_SCORE else r["filed_at"][:10],
                     f"[[{insider_note(r)}]]", r["officer_title"] or r["role"], money(r["value"]), r["score"],
                     pct(r.get("abn_now")), r["status"]] for r in rows])]
    return "\n".join(lines)


def insider_page(name: str, rows: list[dict], record: tuple[int, float] | None) -> str:
    rows = sorted(rows, key=lambda r: r["filed_at"], reverse=True)
    fm = {"type": "insider", "name": name, "cik": rows[0]["owner_cik"] if rows else "",
          "past_buys": record[0] if record else 0, "past_mean_abn_63": record[1] if record else None}
    lines = [frontmatter(fm), f"# {name}\n"]
    if record:
        lines.append(f"Backtest record: {record[0]} earlier buys, average 3-month excess vs SPY {pct(record[1])}. "
                     "(Past winners haven't reliably kept winning; see [[Insider track record]].)\n")
    if rows:
        lines.append(table(["Filed", "Ticker", "Role", "Value", "Score", "vs SPY so far"],
                           [[r["filed_at"][:10], f"[[{safe(r['ticker'] or r['symbol'])}]]", r["officer_title"] or r["role"],
                             money(r["value"]), r["score"], pct(r.get("abn_now"))] for r in rows]))
    return "\n".join(lines)


def best_insiders_note(res: dict, today: str) -> str:
    rows = res.get("best_insiders", [])
    lines = [frontmatter({"type": "leaderboard", "updated": today}), "# Best Insiders\n",
             "Insiders whose purchases most consistently beat SPY over the next 3 months (5+ buys, ranked by t-statistic). "
             "**Caution:** in the backtest, a good past record did *not* reliably predict future buys "
             "(see [[Insider track record]]). Treat this as a watchlist, not a signal.\n",
             table(["Insider", "Role", "Buys", "Avg 3-mo excess", "Won", "t", "Tickers", "Last buy"],
                   [[r["name"], r["role"], r["buys"], pct(r["mean_abn"]), pct(r["hit"], 0, False), num(r["t"], 1),
                     ", ".join(r["tickers"]), r["last_buy"]] for r in rows])]
    return "\n".join(lines)


def research_log(day: str, summary: dict, ledger: list[dict], fwd: dict, existing: str | None,
                 matured: list[tuple[int, dict]]) -> str:
    new = sorted((r for r in ledger if r["logged"] == day), key=lambda r: -r["score"])
    lines = [frontmatter({"type": "log", "date": day, "new_signals": len(new),
                          "notable": sum(1 for r in new if r["score"] >= SIGNAL_NOTE_MIN_SCORE)}),
             f"# {day}\n", "## Run\n"]
    lines += [f"- {k}: {v}" for k, v in summary.items()]
    lines.append("\n## New buys logged\n")
    if new:
        lines.append(table(["Ticker", "Insider", "Role", "Value", "Score", "Cluster", "Strategies"],
                           [[f"[[{safe(r['ticker'] or r['symbol'])}]]", f"[[{insider_note(r)}]]", r["officer_title"] or r["role"],
                             money(r["value"]), r["score"], r["cluster"],
                             ", ".join(f"[[{strategy_title(k)}]]" for k in (r["strategies"] or "").split("|") if k)]
                            for r in new[:40]]))
        if len(new) > 40:
            lines.append(f"\n…and {len(new) - 40} more in `data/picks.csv`.\n")
    else:
        lines.append("None.\n")
    lines.append("\n## Outcomes that matured today\n")
    if matured:
        lines.append(table(["Horizon", "Ticker", "Insider", "Filed", "vs SPY"],
                           [[f"{h} sessions", r["ticker"] or r["symbol"], r["owner_name"], r["filed_at"][:10],
                             pct(r[f"abn_{h}"])] for h, r in sorted(matured, key=lambda x: (x[0], x[1]["filed_at"]))]))
    else:
        lines.append("None yet.\n")
    lines.append("\n## Forward test so far\n")
    lines.append(_forward_table(fwd))
    notes = "\n## Notes\n\n"
    if existing and "\n## Notes\n" in existing:
        notes = existing[existing.index("\n## Notes\n"):]
        if not notes.endswith("\n"):
            notes += "\n"
    return "\n".join(lines) + notes


# --- driver --------------------------------------------------------------------------


def build_vault(vault: str | Path, res: dict, ledger: list[dict], records: dict[str, tuple[int, float]],
                today: str | None = None, run_summary: dict | None = None,
                matured: list[tuple[int, dict]] | None = None) -> int:
    root = Path(vault)
    today = today or dt.date.today().isoformat()
    fwd = forward_by_strategy(ledger)
    n = 0

    def put(rel: str, text: str) -> None:
        nonlocal n
        write(root / rel, text)
        n += 1

    put("Home.md", home(res, fwd, ledger, today))
    put("What Works.md", what_works(res, fwd, today))
    put("Methodology.md", methodology(res))
    put(f"Backtests/{res['meta']['run_date']} Backtest.md", backtest_report(res))
    put("Insiders/Best Insiders.md", best_insiders_note(res, today))
    for feat, buckets in res["slices"].items():
        put(f"Slices/{safe(FEATURE_TITLES.get(feat, feat))}.md", slice_note(feat, buckets, res))
    for key, s in res["strategies"].items():
        put(f"Strategies/{strategy_title(key)}.md", strategy_note(key, s, fwd, ledger))

    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=SIGNAL_NOTE_DAYS)).isoformat()
    recent = [r for r in ledger if r["filed_at"][:10] >= cutoff]
    by_ticker: dict[str, list[dict]] = defaultdict(list)
    by_insider: dict[str, list[dict]] = defaultdict(list)
    for r in recent:
        by_ticker[safe(r["ticker"] or r["symbol"])].append(r)
        by_insider[insider_note(r)].append(r)
        if r["score"] >= SIGNAL_NOTE_MIN_SCORE or r["strategies"]:
            put(f"Signals/{signal_title(r)}.md", signal_note(r))
    for t, rows in by_ticker.items():
        put(f"Tickers/{t}.md", ticker_note(t, rows))
    for name, rows in by_insider.items():
        put(f"Insiders/{name}.md", insider_page(name, rows, records.get(rows[0]["owner_cik"].lstrip("0"))))

    log_path = root / "Research Log" / f"{today}.md"
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else None
    put(f"Research Log/{today}.md", research_log(today, run_summary or {}, ledger, fwd, existing, matured or []))
    return n
