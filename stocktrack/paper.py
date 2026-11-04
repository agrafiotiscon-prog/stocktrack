"""An interim research paper on the live forward test, built from the committed results.

`paper_data` measures what the ledger (data/picks.csv) has collected so far and sets it against the
backtest's expectations; `render` lays it out as a self-contained, print-ready HTML paper; and
`build_paper` writes it, plus a PDF when a local Chromium is available to print it.
"""

from __future__ import annotations

import datetime as dt
import html
import math
import random
import shutil
import subprocess
from pathlib import Path

from stocktrack import advisor as adv
from stocktrack.backtest import POST_HOC, PRIMARY, STRATEGIES, cost_per_side
from stocktrack.dashboard import HYPOTHESIS_SAMPLE, _hypotheses, _largest_per_company_day
from stocktrack.ledger import is_forward
from stocktrack.vault import forward_rows, unique_rows

WEEK = 5  # sessions: the first horizon with matured live outcomes
BOOT = 10_000  # bootstrap draws for the entry-day confidence interval
EXTREMES = 6  # best and worst one-week outcomes listed in the appendix
OFF_MARKET = 0.15  # insider price this far from the prior close suggests an offering or another share class
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
CHROMIUM = ("/opt/pw-browsers/chromium", "chromium", "chromium-browser", "google-chrome")


# --- statistics ------------------------------------------------------------------------


def _stats(vals: list[float]) -> dict:
    """Mean, median, share positive and a normal-approximation 95% CI (shown from 20 values up)."""
    n = len(vals)
    if not n:
        return {"n": 0}
    s = sorted(vals)
    mean = sum(s) / n
    out = {"n": n, "mean": mean, "median": (s[(n - 1) // 2] + s[n // 2]) / 2, "hit": sum(v > 0 for v in s) / n,
           "min": s[0], "max": s[-1]}
    if n >= 20:
        sd = math.sqrt(sum((v - mean) ** 2 for v in s) / (n - 1))
        out["ci"] = (mean - 1.96 * sd / math.sqrt(n), mean + 1.96 * sd / math.sqrt(n))
    return out


def day_bootstrap(rows: list[dict], key: str, reps: int = BOOT, seed: int = 0) -> tuple[float, float] | None:
    """95% CI for the mean, resampling whole entry days.

    Buys entered on the same day share that week's market moves, so they are not independent;
    resampling days keeps that dependence. Needs at least 5 entry days.
    """
    days: dict[str, list[float]] = {}
    for r in rows:
        if r.get(key) is not None:
            days.setdefault(r["entry_date"], []).append(r[key])
    keys = sorted(days)
    if len(keys) < 5:
        return None
    rng = random.Random(seed)
    means = []
    for _ in range(reps):
        pick = [days[rng.choice(keys)] for _ in keys]
        means.append(sum(sum(v) for v in pick) / sum(len(v) for v in pick))
    means.sort()
    return means[int(0.025 * reps)], means[int(0.975 * reps) - 1]


def _market_days(start: str, end: str) -> int:
    """Market sessions after `start` up to and including `end`."""
    d, last, n = dt.date.fromisoformat(start), dt.date.fromisoformat(end), 0
    while d < last:
        d += dt.timedelta(days=1)
        n += adv.is_market_day(d)
    return n


def _role(r: dict) -> str:
    return adv.bt.FEATURES["role"](adv.ev_from_row(r))


def _score_band(r: dict) -> str:
    s = r.get("score") or 0
    return "60+" if s >= 60 else "40-59" if s >= 40 else "0-39"


def paper_data(ledger: list[dict], res: dict, hyp: dict | None, today: str, commit: str | None = None) -> dict:
    """Every number the paper reports, from the ledger and the backtest results."""
    fwd_all = forward_rows(ledger)
    fwd = unique_rows(fwd_all)
    week = [r for r in fwd if r.get(f"abn_{WEEK}") is not None]
    key = f"abn_{WEEK}"
    vals = [r[key] for r in week]

    cohorts = []
    for day in sorted({r["entry_date"] for r in fwd}):
        rs = [r for r in fwd if r["entry_date"] == day]
        done = [r for r in rs if r.get(key) is not None]
        spy = done[0][f"ret_{WEEK}"] - done[0][key] if done else None
        cohorts.append({"entry": day, "n": len(rs), "matured": len(done),
                        "mean": _stats([r[key] for r in done]).get("mean"), "spy": spy})

    events = res["strategies"]["all_liquid"]["events"]
    groups = []
    for k, (title, _) in STRATEGIES.items():
        rs = unique_rows([r for r in fwd_all if k in (r["strategies"] or "").split("|")])
        ev = res["strategies"].get(k, {}).get("events", {})
        groups.append({"key": k, "title": title, "post_hoc": k in POST_HOC, "n": len(rs),
                       "week": _stats([r[key] for r in rs if r.get(key) is not None]),
                       "open": _stats([r["abn_now"] for r in rs if r.get("abn_now") is not None]),
                       "bt_week": ev.get(str(WEEK), {}).get("mean"), "bt_hit": ev.get(str(WEEK), {}).get("hit"),
                       "bt_hold": ev.get(str(PRIMARY), {}).get("mean")})

    def split(label_of, rows: list[dict], order: list[str]) -> list[dict]:
        out = []
        for lab in order:
            rs = [r for r in rows if label_of(r) == lab]
            out.append({"label": lab, "n": len(rs), "week": _stats([r[key] for r in rs if r.get(key) is not None]),
                        "open": _stats([r["abn_now"] for r in rs if r.get("abn_now") is not None])})
        return out

    tiered = _largest_per_company_day([r for r in fwd_all if r.get("tier")])
    open_rows = [r for r in fwd if r["status"] in ("open", "dead") and r.get("abn_now") is not None]
    held = [_market_days(r["entry_date"], r["last_seen"]) + 1 for r in open_rows if r.get("last_seen")]

    late = unique_rows([r for r in ledger if r["entry_date"] and not is_forward(r)])
    first_logged = min((r["logged"][:10] for r in fwd), default=today)

    def extreme(r: dict) -> dict:
        gap = r["avg_price"] / r["price"] - 1 if r.get("avg_price") and r.get("price") else None
        return {"symbol": r["symbol"] or r["ticker"], "company": r["issuer_name"],
                "role": r["officer_title"] or r["role"], "value": r["value"], "entry": r["entry_date"],
                "week": r[key], "off_market": gap is not None and abs(gap) > OFF_MARKET, "gap": gap}

    ranked = sorted(week, key=lambda r: r[key])
    hyps = []
    for h in _hypotheses(hyp or {}, ledger):
        elapsed = max(_market_days(h["since"], today), 1)
        rate = h["logged"] / elapsed
        reach = adv.add_market_days(today, math.ceil((h["needed"] - h["logged"]) / rate)) if rate > 0 and h["logged"] < h["needed"] else None
        hyps.append(dict(h, rate=rate, reach=reach, judged=adv.add_market_days(reach, PRIMARY) if reach else None))

    o = res["overall"]
    costs = sorted(2 * cost_per_side(r["price"], r["adv"]) for r in fwd if r.get("price") and r.get("adv"))
    first_entry = min((r["entry_date"] for r in fwd), default=None)
    all_sig = res["strategies"]["all_liquid"].get("signals") or 0
    return {
        "today": today, "commit": commit, "first_logged": first_logged,
        "first_entry": first_entry,
        "first_month": adv.add_market_days(first_entry, 20) if first_entry else None,
        "first_hold": adv.add_market_days(first_entry, PRIMARY - 1) if first_entry else None,
        "costs": (costs[len(costs) // 10], costs[len(costs) * 9 // 10]) if len(costs) >= 10 else None,
        "bt_share_60": (res["strategies"].get("score_60", {}).get("signals") or 0) / all_sig if all_sig else None,
        "last_entry": max((r["entry_date"] for r in fwd), default=None),
        "ledger_rows": len(ledger), "forward_rows": len(fwd_all), "company_days": len(fwd),
        "companies": len({r["issuer_cik"] for r in fwd}), "insiders": len({r["owner_cik"] for r in fwd_all}),
        "pending": sum(r["status"] == "pending" for r in ledger),
        "week": _stats(vals), "week_boot": day_bootstrap(week, key),
        "hold_matured": sum(r.get(f"abn_{PRIMARY}") is not None for r in fwd),
        "week_raw": _stats([r[f"ret_{WEEK}"] for r in week]),
        "week_days": len({r["entry_date"] for r in week}),
        "values": vals, "cohorts": cohorts, "groups": groups,
        "scores": split(_score_band, fwd, ["0-39", "40-59", "60+"]),
        "roles": split(_role, fwd, ["CEO", "CFO", "Other exec", "President/Chair", "Director", "10% owner", "Other"]),
        "tiers": split(lambda r: r["tier"], tiered, ["above", "typical", "below"]),
        "open": _stats([r["abn_now"] for r in open_rows]), "held": sum(held) / len(held) if held else None,
        "late": {"n": len(late), "week": _stats([r[key] for r in late if r.get(key) is not None]),
                 "month": _stats([r["abn_21"] for r in late if r.get("abn_21") is not None])},
        "best": [extreme(r) for r in ranked[::-1][:EXTREMES]], "worst": [extreme(r) for r in ranked[:EXTREMES]],
        "hypotheses": hyps, "needed": HYPOTHESIS_SAMPLE,
        "backtest": {"run_date": res["meta"].get("run_date"), "prices_to": res["meta"].get("last_price_date"),
                     "filings": res["meta"].get("filings"), "signals": res["strategies"]["all_liquid"].get("signals"),
                     "surv": (o.get("ctp_vs_survivors") or {}).get("annualized"),
                     "surv_t": (o.get("ctp_vs_survivors") or {}).get("t"),
                     "spy_hold": (o.get("holdout") or {}).get("annualized"),
                     "spy_hold_p": (o.get("holdout") or {}).get("p"),
                     "week": events[str(WEEK)], "hold": events[str(PRIMARY)]},
    }


# --- rendering ---------------------------------------------------------------------------


def _e(x) -> str:
    return html.escape(str(x), quote=True)


def pct(x, digits: int = 1, signed: bool = True) -> str:
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return "–"
    v = f"{x * 100:.{digits}f}"
    if float(v) == 0:
        return f"{0:.{digits}f}%"
    return ("+" if signed and x > 0 else "") + v.replace("-", "−") + "%"


def num(x, digits: int = 2) -> str:
    return "–" if x is None else f"{x:.{digits}f}"


def money(x) -> str:
    if x is None:
        return "–"
    a = abs(x)
    if a >= 999.5e6:
        return f"${x / 1e9:.1f}B"
    if a >= 9.95e6:
        return f"${x / 1e6:.0f}M"
    if a >= 999.5e3:
        return f"${x / 1e6:.1f}M"
    if a >= 999.5:
        return f"${x / 1e3:.0f}K"
    return f"${x:.0f}"


def day(s: str | None, year: bool = True) -> str:
    if not s:
        return "–"
    d = dt.date.fromisoformat(s)
    return f"{d:%B} {d.day}, {d.year}" if year else f"{d:%b} {d.day}"


def ci(c) -> str:
    return f"[{pct(c[0])}, {pct(c[1])}]" if c else "–"


def _table(cap: str, num: int, head: list[str], rows: list[list], right: set[int], note: str = "", cls: str = "") -> str:
    th = "".join(f'<th class="{"r" if i in right else ""}">{_e(h)}</th>' for i, h in enumerate(head))
    body = "".join("<tr>" + "".join(f'<td class="{"r" if i in right else ""}">{c}</td>' for i, c in enumerate(r))
                   + "</tr>" for r in rows)
    foot = f'<p class="tnote">{note}</p>' if note else ""
    return (f'<figure class="tab {cls}"><figcaption><b>Table {num}.</b> {cap}</figcaption>'
            f"<table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>{foot}</figure>")


def _fig(num: int, svg: str, cap: str) -> str:
    return f'<figure class="fig">{svg}<figcaption><b>Figure {num}.</b> {cap}</figcaption></figure>'


def _cohort_chart(cohorts: list[dict]) -> str:
    """Bars of buys logged per entry day, the matured part filled, with that cohort's one-week mean above."""
    W, H, L, B, T = 640, 196, 36, 34, 30
    n = len(cohorts) or 1
    top = max([c["n"] for c in cohorts] + [5])
    top = math.ceil(top / 5) * 5
    bw = (W - L - 10) / n
    y = lambda v: T + (H - T - B) * (1 - v / top)  # noqa: E731
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Buys logged per entry day">']
    for t in range(0, top + 1, 5 if top <= 30 else 10):
        out.append(f'<line x1="{L}" x2="{W - 6}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="grid"/>'
                   f'<text x="{L - 6}" y="{y(t) + 3.5:.1f}" class="ax" text-anchor="end">{t}</text>')
    for i, c in enumerate(cohorts):
        x = L + i * bw + bw * 0.18
        w = bw * 0.64
        out.append(f'<rect x="{x:.1f}" y="{y(c["n"]):.1f}" width="{w:.1f}" height="{y(0) - y(c["n"]):.1f}" class="bar-open"/>')
        if c["matured"]:
            out.append(f'<rect x="{x:.1f}" y="{y(c["matured"]):.1f}" width="{w:.1f}" height="{y(0) - y(c["matured"]):.1f}" class="bar"/>')
        if c["mean"] is not None:
            cls = "pos" if c["mean"] >= 0 else "neg"
            out.append(f'<text x="{x + w / 2:.1f}" y="{y(c["n"]) - 6:.1f}" class="lab {cls}" text-anchor="middle">{_e(pct(c["mean"], 1))}</text>')
        out.append(f'<text x="{x + w / 2:.1f}" y="{H - B + 16:.1f}" class="ax" text-anchor="middle">{_e(day(c["entry"], False))}</text>')
    out.append(f'<text x="{L}" y="14" class="ax">Buys per entry day (company-days)</text>')
    out.append(f'<rect x="{W - 250}" y="5" width="10" height="10" class="bar"/><text x="{W - 235}" y="14" class="ax">one-week outcome in</text>'
               f'<rect x="{W - 120}" y="5" width="10" height="10" class="bar-open"/><text x="{W - 105}" y="14" class="ax">still open</text>')
    out.append("</svg>")
    return "".join(out)


def _hist_chart(vals: list[float], mean: float | None, bt_mean: float | None) -> str:
    """Histogram of one-week excess returns in 2-point bins, tails gathered at the ends."""
    W, H, L, B, T = 640, 186, 36, 32, 26
    lo, hi, step = -0.20, 0.20, 0.02
    nb = round((hi - lo) / step)
    counts = [0] * (nb + 2)  # first and last bins hold the tails
    for v in vals:
        i = 0 if v < lo else nb + 1 if v >= hi else 1 + int((v - lo) // step)
        counts[min(i, nb + 1)] += 1
    top = max(counts + [1])
    top = math.ceil(top / 5) * 5
    bw = (W - L - 10) / (nb + 2)
    x = lambda v: L + bw * (1 + (min(max(v, lo), hi) - lo) / step)  # noqa: E731
    y = lambda c: T + (H - T - B) * (1 - c / top)  # noqa: E731
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Distribution of one-week excess returns">']
    for t in range(0, top + 1, 5):
        out.append(f'<line x1="{L}" x2="{W - 6}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="grid"/>'
                   f'<text x="{L - 6}" y="{y(t) + 3.5:.1f}" class="ax" text-anchor="end">{t}</text>')
    for i, c in enumerate(counts):
        if c:
            left = L + i * bw
            mid = lo + (i - 0.5) * step
            cls = "bar-neg" if (i == 0 or (0 < i <= nb and mid < 0)) else "bar"
            out.append(f'<rect x="{left + 1:.1f}" y="{y(c):.1f}" width="{bw - 2:.1f}" height="{y(0) - y(c):.1f}" class="{cls}"/>')
    for v, lab in ((lo, f"<{pct(lo, 0)}"), (-0.1, pct(-0.1, 0)), (0, "0%"), (0.1, pct(0.1, 0)), (hi, f"≥{pct(hi, 0)}")):
        xx = L + bw * 0.5 if v == lo else L + bw * (nb + 1.5) if v == hi else x(v)
        out.append(f'<text x="{xx:.1f}" y="{H - B + 16:.1f}" class="ax" text-anchor="middle">{_e(lab)}</text>')
    if mean is not None:
        out.append(f'<line x1="{x(mean):.1f}" x2="{x(mean):.1f}" y1="{T - 4}" y2="{y(0)}" class="mark"/>'
                   f'<text x="{x(mean) + 4:.1f}" y="{T + 2}" class="lab">live mean {_e(pct(mean))}</text>')
    if bt_mean is not None:
        out.append(f'<line x1="{x(bt_mean):.1f}" x2="{x(bt_mean):.1f}" y1="{T + 10}" y2="{y(0)}" class="mark2"/>'
                   f'<text x="{x(bt_mean) - 4:.1f}" y="{T + 16}" class="lab muted" text-anchor="end">backtest {_e(pct(bt_mean))}</text>')
    out.append(f'<text x="{L}" y="12" class="ax">Number of buys</text></svg>')
    return "".join(out)


SHORT = {"all_liquid": "All buys", "score_40": "Live score 40+", "score_60": "Live score 60+",
         "ceo_cfo_100k": "CEO or CFO, $100K+", "cluster_3": "3+ insiders in 14 days",
         "opportunistic": "Opportunistic insiders", "contrarian": "After a 30%+ drop",
         "proven_insider": "Earlier buys beat SPY", "big_stake_up": "Stake up 25%+, $100K+",
         "first_buy_exec": "Exec's first buy in a year", "cfo_exec_25k": "CFO or other exec, $25K+",
         "momentum_buy": "After a 30%+ run-up"}


def _group_chart(groups: list[dict], min_n: int = 3) -> str:
    """Live one-week mean (dot) against the backtest's one-week mean (ring) for each group."""
    gs = [g for g in groups if g["week"].get("n", 0) >= min_n and g["bt_week"] is not None]
    W, row, L, T = 640, 22, 190, 30
    H = T + row * len(gs) + 30
    vals = [g["week"]["mean"] for g in gs] + [g["bt_week"] for g in gs] + [0.0]
    lo, hi = min(vals + [-0.02]), max(vals + [0.02])
    pad = (hi - lo) * 0.1
    lo, hi = lo - pad, hi + pad
    x = lambda v: L + (W - L - 20) * (v - lo) / (hi - lo)  # noqa: E731
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Live and backtest one-week means by group">']
    out.append(f'<line x1="{x(0):.1f}" x2="{x(0):.1f}" y1="{T - 8}" y2="{H - 24}" class="zero"/>')
    raw = (hi - lo) / 4
    mag = 10 ** math.floor(math.log10(raw))
    step = next(k * mag for k in (1, 2, 5, 10) if raw / mag <= k * 1.5)
    t = math.ceil(lo / step) * step
    while t <= hi + 1e-12:
        out.append(f'<text x="{x(t):.1f}" y="{H - 8}" class="ax" text-anchor="middle">{_e(pct(t, 0 if step >= 0.01 else 1))}</text>')
        t += step
    for i, g in enumerate(gs):
        yy = T + i * row + row / 2
        a, b = g["week"]["mean"], g["bt_week"]
        out.append(f'<line x1="{L - 6}" x2="{W - 14}" y1="{yy:.1f}" y2="{yy:.1f}" class="grid"/>'
                   f'<text x="{L - 10}" y="{yy + 3.5:.1f}" class="ax" text-anchor="end">{_e(SHORT.get(g["key"], g["title"]))} (n={g["week"]["n"]})</text>'
                   f'<line x1="{x(b):.1f}" x2="{x(a):.1f}" y1="{yy:.1f}" y2="{yy:.1f}" class="link"/>'
                   f'<circle cx="{x(b):.1f}" cy="{yy:.1f}" r="4" class="ring"/>'
                   f'<circle cx="{x(a):.1f}" cy="{yy:.1f}" r="4" class="{"dot" if a >= 0 else "dot-neg"}"/>')
    out.append(f'<circle cx="{L}" cy="12" r="4" class="dot"/><text x="{L + 8}" y="15.5" class="ax">live, one week</text>'
               f'<circle cx="{L + 110}" cy="12" r="4" class="ring"/><text x="{L + 118}" y="15.5" class="ax">backtest, one week (2006–2026)</text>')
    out.append("</svg>")
    return "".join(out)


CSS = """
@page { size: Letter; margin: 20mm 19mm 20mm; @bottom-center { content: counter(page); font: 9pt 'Inter', sans-serif; color: #666; } }
:root { --ink: #1a1a1a; --muted: #5f6368; --rule: #c9ccd1; --blue: #1f5fa8; --red: #b8322c; --grey: #8a9099; }
* { box-sizing: border-box; }
html { background: #fff; }
body { margin: 0 auto; max-width: 7.2in; color: var(--ink); font: 10.5pt/1.48 'Charter', 'Iowan Old Style', 'Caladea', 'Cambria', Georgia, serif;
       text-rendering: optimizeLegibility; font-variant-numeric: oldstyle-nums proportional-nums; hyphens: auto; }
@media screen { body { padding: 32px 20px 64px; } }
header { text-align: center; margin: 4mm 0 6mm; }
.kicker { font: 600 8.5pt 'Inter', sans-serif; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }
h1 { font-size: 19pt; line-height: 1.22; margin: 8px 0 8px; font-weight: 700; letter-spacing: -.005em; }
.byline { font-size: 10pt; color: var(--muted); }
.abstract { margin: 6mm 7mm 5mm; font-size: 9.8pt; }
.abstract h2 { font: 700 8.5pt 'Inter', sans-serif; letter-spacing: .12em; text-transform: uppercase; text-align: center; margin: 0 0 4px; }
.keywords { margin: 4px 7mm 6mm; font-size: 9pt; color: var(--muted); }
h2 { font-size: 12.5pt; margin: 7mm 0 2mm; break-after: avoid; }
h3 { font-size: 10.8pt; font-style: italic; font-weight: 600; margin: 4mm 0 1mm; break-after: avoid; }
p { margin: 0 0 2.4mm; text-align: justify; }
.num, td, .ax, .lab, .tnote { font-variant-numeric: lining-nums tabular-nums; }
figure { margin: 4mm 0 5mm; break-inside: avoid; }
figure.long { break-inside: auto; }
thead { display: table-header-group; } tr { break-inside: avoid; }
figcaption { font-size: 9pt; color: #333; margin-bottom: 2mm; text-align: left; }
.fig figcaption { margin: 1.5mm 0 0; }
.fig svg { width: 100%; height: auto; display: block; }
table { width: 100%; border-collapse: collapse; font: 8.6pt/1.35 'Inter', sans-serif; }
thead th { border-top: 1.2px solid var(--ink); border-bottom: .8px solid var(--ink); font-weight: 600; text-align: left; padding: 3px 5px; vertical-align: bottom; }
tbody td { padding: 2.4px 5px; border-bottom: .4px solid #e3e5e8; vertical-align: top; }
tbody tr:last-child td { border-bottom: 1.2px solid var(--ink); }
.r { text-align: right; white-space: nowrap; }
.tab.long td:first-child { width: 36%; }
.tnote { font: 8pt/1.35 'Inter', sans-serif; color: var(--muted); margin: 1.5mm 0 0; text-align: left; }
.pos { fill: var(--blue); color: var(--blue); } .neg { fill: var(--red); color: var(--red); }
td .neg { color: var(--red); }
svg .grid { stroke: #e6e8eb; stroke-width: 1; } svg .zero { stroke: #9aa0a6; stroke-width: 1; }
svg .ax { font: 9px 'Inter', sans-serif; fill: #5f6368; } svg .lab { font: 600 9px 'Inter', sans-serif; fill: var(--ink); }
svg .lab.muted { fill: var(--muted); font-weight: 500; }
svg .bar { fill: var(--blue); } svg .bar-open { fill: #c7d7ec; } svg .bar-neg { fill: var(--red); }
svg .mark { stroke: var(--ink); stroke-width: 1.4; } svg .mark2 { stroke: var(--grey); stroke-width: 1.4; stroke-dasharray: 3 3; }
svg .dot { fill: var(--blue); } svg .dot-neg { fill: var(--red); } svg .ring { fill: #fff; stroke: var(--grey); stroke-width: 1.6; }
svg .link { stroke: #c9ccd1; stroke-width: 2; }
.box { border: .8px solid var(--rule); padding: 3mm 4mm; margin: 4mm 0; break-inside: avoid; font-size: 9.8pt; }
.box b:first-child { font: 700 8.5pt 'Inter', sans-serif; letter-spacing: .08em; text-transform: uppercase; display: block; margin-bottom: 1mm; }
ol.refs { font-size: 9pt; padding-left: 5mm; margin: 0; } ol.refs li { margin-bottom: 1mm; }
td.gap { width: 6%; border-bottom: 0; }
.small { font-size: 9pt; color: var(--muted); }
"""


def render(d: dict) -> str:
    w, b, bt = d["week"], d["week_boot"], d["backtest"]
    bw = bt["week"]
    has_week = w.get("n", 0) > 0
    inside = b and b[0] <= bw["mean"] <= b[1]
    spans_zero = b and b[0] < 0 < b[1]
    spy_week = (d["week_raw"]["mean"] - w["mean"]) if has_week else None
    bands = {x["label"]: x["week"] for x in d["scores"]}
    hi_band, lo_band = bands.get("60+", {}), bands.get("0-39", {})
    if hi_band.get("n", 0) >= 3 and lo_band.get("n", 0) >= 3:
        score_led = hi_band["mean"] > lo_band["mean"]
        score_line = (f"Buys scoring 60 or more {'have' if score_led else 'have not'} led so far "
                      f"({pct(hi_band['mean'])} against {pct(lo_band['mean'])} for scores below 40, one week).")
    else:
        score_led, score_line = None, "Too few high-scored buys have matured to compare score bands."
    ranked_groups = sorted((g for g in d["groups"] if g["week"].get("n", 0) >= 5), key=lambda g: -g["week"]["mean"])
    roles_ranked = sorted((x for x in d["roles"] if x["n"]), key=lambda x: -x["n"])
    role_name = {"CEO": "chief executives", "CFO": "chief financial officers", "Other exec": "other executives",
                 "President/Chair": "presidents and chairs", "Director": "directors", "10% owner": "10% owners",
                 "Other": "other filers"}
    late_month, first_hold = day(d.get("first_month")), day(d.get("first_hold"))
    if d["backtest"]["spy_hold_p"] is not None and d["backtest"]["spy_hold_p"] >= 0.05:
        spy_phrase = f"but have not reliably beaten the S&amp;P 500 since 2016 ({pct(bt['spy_hold'])} a year, not significant)"
    else:
        spy_phrase = f"and beat the S&amp;P 500 by {pct(bt['spy_hold'])} a year since 2016"

    title = "Do insider purchases predict returns in real time? An interim report from a pre-registered forward test"
    if has_week:
        result = (f"The {w['n']} buys with a completed first week beat the S&amp;P 500 by {pct(w['mean'])} on average "
                  f"(median {pct(w['median'])}; {pct(w['hit'], 0, False)} ahead). Resampling whole entry days, the 95% "
                  f"interval is {ci(b)}, which {'includes' if spans_zero else 'excludes'} zero"
                  + (f" and contains the backtest's one-week average of {pct(bw['mean'])}." if inside else
                     f"; the backtest's one-week average was {pct(bw['mean'])}."))
    else:
        result = "No logged buy has completed its first week yet."
    abstract = (
        f"Twenty years of SEC Form 4 filings suggest that stocks bought by their own insiders beat comparable stocks "
        f"by about {pct(bt['surv'])} a year, {spy_phrase}. Because those findings "
        f"were shaped by looking at the same data, we test them forward: from {day(d['first_logged'])}, a daily job "
        f"has logged every qualifying open-market insider purchase before the market opens, then tracked its return "
        f"against the S&amp;P 500. By {day(d['today'])} it had logged {d['company_days']} company-days across "
        f"{d['companies']} companies. {result} No buy has yet reached the one-month or three-month horizons the "
        f"hypotheses are judged on, so this report describes data collection and early noise, not evidence. "
        f"{score_line}")

    sec = []
    sec.append(f"""
<h2>1. Introduction</h2>
<p>Corporate insiders must report their trades in their own company's stock to the SEC within two business days,
on Form 4. Purchases on the open market are the interesting ones: insiders sell for many reasons, but they buy
mainly when they expect the price to rise. A long literature finds that insider purchases are followed by abnormal
returns [1–3], and that the information is concentrated in non-routine, “opportunistic” trades [4].</p>
<p>This project began with a 20-year backtest of {bt['filings']:,} purchase filings from 2006 to {day(bt['prices_to'])}.
Its current run ({day(bt['run_date'])}) finds that, over the three months after a filing, the stock beat an index of
comparable surviving stocks by {pct(bt['surv'])} a year (t {num(bt['surv_t'], 1)}), but beat the S&amp;P 500 by only
{pct(bt['spy_hold'])} a year since 2016 (p {num(bt['spy_hold_p'], 2)}). Several kinds of buy looked stronger than average,
such as purchases by chief financial officers, but they were found by looking at that data, so the data cannot also
confirm them. Section 5 lists the hypotheses that were written down for a fresh test.</p>
<p>This paper reports that fresh test as it stands: what has been collected, how the first outcomes compare with
the backtest, and when the registered hypotheses can be judged. It is an interim report; nothing in it is
investment advice.</p>
""")
    sec.append(f"""
<h2>2. Design</h2>
<p><i>Data.</i> Every weekday morning (Tuesday to Saturday, 06:53 New York time) the job reads the previous
business day's Form 4 filings from EDGAR and keeps open-market purchases (transaction code P) of exchange-listed
shares priced at $2 or more that trade at least $1 million a day, excluding dividend-reinvestment and plan purchases.</p>
<p><i>Timing rule.</i> A buy counts only if it was written to the ledger before 13:30 UTC on its entry day, the
first session after the filing (the 09:30 open in summer, an hour before it in winter); the ledger records the
timestamp. Buys logged later, for example ones filed
before Monday's open, are kept but excluded (Section 4.5).</p>
<p><i>Outcome.</i> The excess return is the stock's return from the entry-day open to the close {WEEK}, 21, 63, 126
and 252 sessions later, minus the S&amp;P 500 ETF's (SPY) return over the same window. No trading costs are deducted
and nothing is winsorized. Insiders buying the same company on the same day share one entry, so each company-day
counts once, as in the backtest.</p>
<p><i>Groups.</i> Each buy is tagged with the pre-registered backtest strategies it matches and with a live score
(0–100). From October 24 each buy's signal-desk profile (above typical, typical or below typical) is also
recorded at logging, so later refits cannot change what is judged.</p>
<p><i>Inference.</i> Buys entered on the same day share that week's market moves, so they are not independent.
Confidence intervals therefore resample whole entry days ({BOOT:,} draws); a naive interval that treats every buy as
independent is shown for comparison and is too narrow.</p>
""")

    roles = [[_e(x["label"]), str(x["n"]), pct(x["n"] / d["company_days"], 0, False) if d["company_days"] else "–"]
             for x in d["roles"] if x["n"]]
    scores = [[_e(x["label"]), str(x["n"]), pct(x["n"] / d["company_days"], 0, False) if d["company_days"] else "–"]
              for x in d["scores"]]
    sec.append(f"""
<h2>3. The sample so far</h2>
<p>Between {day(d['first_logged'])} and {day(d['today'])} the ledger received {d['ledger_rows']} rows. Of these,
{d['forward_rows']} were logged in time to count, forming {d['company_days']} company-days in {d['companies']}
companies, bought by {d['insiders']} different insiders, with entries from {day(d['first_entry'], False)} to
{day(d['last_entry'], False)}. A further {d['pending']} rows await their first session. Figure 1 shows the daily flow,
about {d['company_days'] / max(len(d['cohorts']), 1):.0f} company-days per session.</p>
<p>{_e(role_name.get(roles_ranked[0]['label'], roles_ranked[0]['label']).capitalize()) if roles_ranked else 'No role'} make up the largest group of buyers{', followed by ' + ' and '.join(role_name.get(x['label'], x['label']) for x in roles_ranked[1:3]) if len(roles_ranked) > 2 else ''} (Table 1).
{pct(d['scores'][2]['n'] / d['company_days'], 0, False) if d['company_days'] else '–'} of the buys scored 60 or more on the live
score, against {pct(d.get('bt_share_60'), 0, False)} in the backtest's universe.</p>
{_table("Who bought, and how the live score graded the buys (company-days that count).", 1,
        ["Buyer's role", "Buys", "Share", "", "Live score", "Buys", "Share"],
        [(roles[i] if i < len(roles) else ["", "", ""]) + ['<span class="gap"></span>']
         + (scores[i] if i < len(scores) else ["", "", ""]) for i in range(max(len(roles), len(scores)))],
        {1, 2, 5, 6})}
{_fig(1, _cohort_chart(d['cohorts']), "Company-days entered per session. The darker part has completed its first week; the label is that entry day's average one-week excess return over SPY. Buys entered on the same day share that week's market moves, which is why Table 2's interval resamples whole days.")}
""")

    rows2 = [["All buys, one week", str(w.get("n", 0)), pct(w.get("mean")), pct(w.get("median")),
              pct(w.get("hit"), 0, False), ci(b), ci(w.get("ci"))],
             ["Backtest, same universe, one week", f"{bw['n']:,}", pct(bw["mean"]), pct(bw["median"]),
              pct(bw["hit"], 0, False), "–", "–"]]
    t2_note = (f"Live returns are not winsorized; the backtest's are winsorized at 1% and 99%. The raw stock return "
               f"over the same weeks averaged {pct(d['week_raw'].get('mean'))}, so SPY returned about "
               f"{pct(spy_week)} in those windows. Day-resampled interval from {d['week_days']} entry days.")
    sec.append(f"""
<h2>4. Results</h2>
<h3>4.1 The first week</h3>
<p>{d['week'].get('n', 0)} company-days, entered on {d['week_days']} different days, have completed their first five
sessions. Table 2 compares them with the backtest's one-week result for the same universe of liquid,
discretionary buys. The live average is {'above' if has_week and w['mean'] > bw['mean'] else 'below'} the backtest's,
and {'more' if has_week and w['hit'] > bw['hit'] else 'fewer'} buys finished ahead than in the backtest
({pct(w.get('hit'), 0, False)} against {pct(bw['hit'], 0, False)}). But the interval that respects the shared market moves is wide:
{'it includes zero' if spans_zero else 'it excludes zero'}{' and the backtest value' if inside else ''}.
With {d['week_days']} entry days, the data cannot yet tell a true one-week edge of zero from one of a few percent.</p>
{_table("One-week excess return over SPY: live forward test against the 20-year backtest.", 2,
        ["Sample", "Buys", "Mean", "Median", "Ahead", "95% CI (by day)", "95% CI (naive)"], rows2, {1, 2, 3, 4, 5, 6}, t2_note)}
{_fig(2, _hist_chart(d['values'], w.get('mean'), bw['mean']), "Distribution of one-week excess returns over SPY for every matured company-day, in 2-point bins; the outer bars gather everything beyond ±20%. The solid line is the live mean, the dashed line the backtest's.")}
""")

    grows = []
    for g in d["groups"]:
        gw, go = g["week"], g["open"]
        label = _e(g["title"].replace(" (post-hoc)", "")) + (" <i>(post-hoc)</i>" if g["post_hoc"] else "")
        grows.append([label, str(g["n"]), str(gw.get("n", 0)),
                      pct(gw.get("mean")) if gw.get("n", 0) >= 3 else "–", pct(gw.get("hit"), 0, False) if gw.get("n", 0) >= 3 else "–",
                      pct(go.get("mean")), pct(g["bt_week"]), pct(g["bt_hold"])])
    sec.append(f"""
<h3>4.2 The pre-registered strategies</h3>
<p>Table 3 breaks the sample down by the strategies registered before the first backtest run. Most groups have only
a handful of matured buys, so their one-week averages are dominated by single stocks. Figure 3 sets each group's live
week against its backtest week.{
    (' Among groups with at least five matured buys, the highest live averages so far belong to '
     + ' and '.join('“' + _e(SHORT.get(g['key'], g['title'])) + f"” ({pct(g['week']['mean'])})" for g in ranked_groups[:2])
     + ', and the lowest to ' + ' and '.join('“' + _e(SHORT.get(g['key'], g['title'])) + f"” ({pct(g['week']['mean'])})" for g in ranked_groups[-2:][::-1])
     + '.') if len(ranked_groups) >= 4 else ''} One week of a three-month hypothesis is not evidence either way.</p>
{_table("Live results by pre-registered strategy. “Open” is the average excess return of all its buys from entry to the latest close.", 3,
        ["Strategy", "Logged", "1-week n", "1-week mean", "Ahead", "Open now", "Backtest 1 week", "Backtest 63 sessions"],
        grows, {1, 2, 3, 4, 5, 6, 7}, "Means are shown from 3 matured buys. Post-hoc strategies were added after the first backtest run and are judged only on live data.", "long")}
{_fig(3, _group_chart(d['groups']), "Live one-week mean (filled) against the backtest's one-week mean (ring) for groups with at least three matured buys.")}
""")

    def band_rows(xs: list[dict], fmt) -> list[list]:
        return [[fmt(x["label"]), str(x["n"]), str(x["week"].get("n", 0)), pct(x["week"].get("mean")) if x["week"].get("n", 0) >= 3 else "–",
                 pct(x["week"].get("hit"), 0, False) if x["week"].get("n", 0) >= 3 else "–", pct(x["open"].get("mean"))] for x in xs]

    tier_name = {"above": "Above typical", "typical": "Typical", "below": "Below typical"}
    sec.append(f"""
<h3>4.3 Live score and signal-desk profile</h3>
<p>If the score or the profile carried information, higher bands would lead. {score_line} The bands hold few matured
buys, and the profiles have only been recorded since October 24 (Table 4).</p>
{_table("One-week and open excess returns by live score band and by the signal-desk profile recorded at logging.", 4,
        ["Band", "Logged", "1-week n", "1-week mean", "Ahead", "Open now"],
        band_rows(d["scores"], lambda s: f"Score {s}") + band_rows(d["tiers"], lambda t: tier_name.get(t, t)), {1, 2, 3, 4, 5},
        "Profiles count each company-day once, with its largest buy, as the registered tier hypothesis does.")}
<h3>4.4 Open positions</h3>
<p>All {d['open'].get('n', 0)} company-days that have entered are marked to their latest close. After an average of
{d['held'] or 0:.0f} sessions they are {pct(d['open'].get('mean'))} ahead of SPY on average (median
{pct(d['open'].get('median'))}; {pct(d['open'].get('hit'), 0, False)} ahead). These overlapping, unequal holding periods
are not a test of anything, but they show where the first one-month outcomes, due from {late_month}, are heading.</p>
<h3>4.5 Buys logged too late to count</h3>
<p>{d['late']['n']} company-days were logged after their entry session had opened, most of them on the first day,
when the job back-filled filings from late September and early October. They are excluded from every result above.
For completeness: {d['late']['week'].get('n', 0)} have one-week outcomes averaging {pct(d['late']['week'].get('mean'))}, and
{d['late']['month'].get('n', 0)} have one-month outcomes averaging {pct(d['late']['month'].get('mean'))}
({pct(d['late']['month'].get('hit'), 0, False)} ahead).</p>
""")

    hrows = []
    for h in d["hypotheses"]:
        hrows.append([_e(h["title"]), _e(h["expected"]), day(h["since"], False), str(h["logged"]), f"{h['rate']:.2f}",
                      day(h["reach"]) if h["reach"] else "–", day(h["judged"]) if h["judged"] else "–"])
    sec.append(f"""
<h2>5. The registered hypotheses</h2>
<p>{WORDS.get(len(d['hypotheses']), str(len(d['hypotheses']))).capitalize()} hypothes{'is is' if len(d['hypotheses']) == 1 else 'es are'} on record in <span class="small">data/backtest/hypotheses.json</span>. Each is judged once
{d['needed']} of its buys have completed 63 sessions: it is supported if the mean excess return over SPY is positive
and its 95% interval excludes zero. {"No buy has completed 63 sessions yet." if not d["hold_matured"] else f"{d['hold_matured']} buys have completed 63 sessions so far."} Table 5 projects, from the rate at which
each group has been logging buys, when it will reach {d['needed']} buys and when the last of them will mature.</p>
{_table("Registered hypotheses, their expected effect, and when they can be judged at the current logging rate.", 5,
        ["Hypothesis", "Expected", "Since", "Logged", "Per session", "100 logged by", "Judged after"], hrows, {2, 3, 4, 5, 6},
        "Projections assume the logging rate stays as it has been; they will move. The tier hypothesis is gated by its smaller group.")}
""")

    def ext_rows(xs):
        return [[f"<b>{_e(x['symbol'])}</b>", _e(x["company"][:34]), _e((x["role"] or "")[:26]), money(x["value"]),
                 day(x["entry"], False), pct(x["week"]) + (" ‡" if x["off_market"] else "")] for x in xs]

    sec.append(f"""
<h2>6. Discussion</h2>
<p><i>Too early to judge.</i> One week is the shortest horizon the ledger tracks, and the hypotheses are about three
months. Over a single week, company news and market swings dwarf any plausible edge: the backtest's one-week average
is {pct(bw['mean'])}, while live buys range from {pct(w.get('min'))} to {pct(w.get('max'))}.</p>
<p><i>One market, one month.</i> Every outcome so far comes from a few weeks in October and November 2026. Small
companies, which most insider buys are, can lead or lag the S&amp;P 500 for months at a time, and that alone can push
every group the same way. The entry-day interval in Table 2 is the honest measure of how little is known.</p>
<p><i>Costs.</i> Returns are before trading costs. Under the backtest's cost model a round trip costs
{f"{pct(d['costs'][0], 1, False)} to {pct(d['costs'][1], 1, False)} for the middle 80% of these buys" if d.get('costs') else 'up to a few percent'},
depending on price and trading volume, which matters next to one-week edges of a percent or two.</p>
<p><i>Data quirks.</i> Some filings coded as open-market purchases are not ordinary trades. Several large buys were at
prices far from the market's (marked ‡ in the appendix), which suggests an offering, a private placement or another
share class; some buyers are institutions adding to closed-end funds; and some officer titles read only “See Remarks”.
These rows follow the pre-registered rules and stay in the sample.</p>
<h2>7. Conclusion</h2>
<p>The forward test is working as designed: it logs {d['company_days'] / max(len(d['cohorts']), 1):.0f} qualifying
company-days a session, before the open, and tracks them against SPY. The first week's results are consistent with the
backtest and with no edge at all. The first one-month outcomes arrive on {late_month} and the first three-month ones
on {first_hold}. At the current pace, the last of the registered hypotheses can be judged around
{day(max((h['judged'] for h in d['hypotheses'] if h['judged']), default=None))}.</p>
<h2>References</h2>
<ol class="refs">
<li>Seyhun, H. N. (1986). Insiders' profits, costs of trading, and market efficiency. <i>Journal of Financial Economics</i>, 16(2), 189–212.</li>
<li>Lakonishok, J., &amp; Lee, I. (2001). Are insider trades informative? <i>Review of Financial Studies</i>, 14(1), 79–111.</li>
<li>Jeng, L. A., Metrick, A., &amp; Zeckhauser, R. (2003). Estimating the returns to insider trading: A performance-evaluation perspective. <i>Review of Economics and Statistics</i>, 85(2), 453–471.</li>
<li>Cohen, L., Malloy, C., &amp; Pomorski, L. (2012). Decoding inside information. <i>Journal of Finance</i>, 67(3), 1009–1043.</li>
</ol>
<h2>Appendix: the largest one-week moves</h2>
{_table("The best and worst one-week excess returns among matured company-days.", 6,
        ["Ticker", "Company", "Buyer", "Bought", "Entry", "1 week vs SPY"],
        ext_rows(d["best"]) + [["", "", "", "", "", ""]] + ext_rows(d["worst"]), {3, 4, 5},
        f"‡ The insider's price was more than {OFF_MARKET:.0%} from the prior close: likely an offering, private placement or another share class.")}
<div class="box"><b>Reproducing this paper</b>
Every number comes from the repository's committed files: <span class="small">data/picks.csv</span> (the ledger),
<span class="small">data/backtest/latest.json</span> and <span class="small">data/backtest/hypotheses.json</span>.
Regenerate with <span class="small">python3 -m stocktrack research paper</span>{f' (this copy: commit {_e(d["commit"])})' if d.get('commit') else ''}.
This is research, not investment advice.</div>
""")

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Insider buying forward test: interim report</title><style>{CSS}</style></head>
<body>
<header><div class="kicker">Interim report · live statistics to {_e(day(d['today']))}</div>
<h1>{title}</h1>
<div class="byline">stocktrack research · forward-test ledger started {_e(day(d['first_logged']))}</div></header>
<section class="abstract"><h2>Abstract</h2><p>{abstract}</p></section>
<p class="keywords"><i>Keywords:</i> insider trading, Form 4, forward test, pre-registration, event study</p>
{''.join(sec)}
</body></html>
"""


# --- output ------------------------------------------------------------------------------


def find_chromium() -> str | None:
    for c in CHROMIUM:
        p = shutil.which(c) or (c if Path(c).exists() else None)
        if p:
            return p
    return None


def print_pdf(html_path: Path, pdf_path: Path, chromium: str | None = None) -> Path | None:
    """Print the HTML paper to PDF with headless Chromium; None when no browser is available."""
    exe = chromium or find_chromium()
    if not exe:
        return None
    subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()],
                   check=True, capture_output=True, timeout=120)
    return pdf_path


def build_paper(out_dir: str | Path, ledger: list[dict], res: dict, hyp: dict | None, today: str | None = None,
                commit: str | None = None, pdf: bool = True) -> list[Path]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    today = today or dt.date.today().isoformat()
    path = out / "forward-test.html"
    path.write_text(render(paper_data(ledger, res, hyp, today, commit)), encoding="utf-8")
    written = [path]
    if pdf:
        made = print_pdf(path, out / "forward-test.pdf")
        if made:
            written.append(made)
    return written
