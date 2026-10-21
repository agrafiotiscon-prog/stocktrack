"""Signal report cards: how strong a new insider buy looks, what usually followed buys like it, and how big a
position the research would take.

The strength model is a ridge regression on the point-in-time features of each buy (role, cluster, prior move,
price, liquidity, size, stake change, routine/opportunistic, filing delay, novelty), predicting the 3-month
(63-session) return over comparable surviving stocks and over SPY. Honesty rules:

* The model that is *validated* is fit on 2006-2015 only (exits before 2016), with its shrinkage chosen by an
  earlier/later split inside that period. It is then scored once on 2016 onward, which it never saw.
* The model used on live signals is refit on everything with the same shrinkage, so its grades mean the same.
* Grades are history's quantiles of the prediction: A = top 10%, B = next 20%, C = middle 40%, D = bottom 30%.
* Outcomes shown for a grade are the 2016+ out-of-sample ones. Risk (the spread of outcomes) comes from all
  years for stocks of the same price and liquidity, because risk, not the edge, decides position size.

Nothing here is personal advice: sizing follows the tested portfolio rules plus a loss budget the reader sets.
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import math
from collections import defaultdict

from stocktrack import backtest as bt
from stocktrack.signals import BuyEvent

MODEL_FEATURES = ("role", "cluster", "prior_3m_return", "price", "liquidity", "value", "stake_increase",
                  "insider_type", "filing_delay", "insider_novelty")
LAMBDAS = (0.0, 300.0, 1000.0, 3000.0, 10000.0, 30000.0)
GRADES = (("A", 0.90), ("B", 0.70), ("C", 0.30))  # share of history below the grade's lower edge; D is the rest
CV_SPLIT = "2011-12-31"
MAX_POSITION = 0.05  # the tested portfolios hold up to 20 equal positions
ADV_CAP = 0.02  # and never more than 2% of a day's dollar volume
RISK_BUDGETS = (0.005, 0.01, 0.02)  # share of the account to lose in a 1-in-10 bad outcome
MIN_CELL = 200


# --- linear algebra (small, dense) ---------------------------------------------------


def _solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[piv][col]) < 1e-12:
            continue
        m[col], m[piv] = m[piv], m[col]
        for r in range(col + 1, n):
            f = m[r][col] / m[col][col]
            if f:
                for k in range(col, n + 1):
                    m[r][k] -= f * m[col][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        if abs(m[r][r]) < 1e-12:
            continue
        x[r] = (m[r][n] - sum(m[r][k] * x[k] for k in range(r + 1, n))) / m[r][r]
    return x


def _ridge(rows: list[tuple[list[int], float]], p: int, lam: float) -> list[float]:
    """Ridge on one-hot rows (column 0 is the unpenalized intercept)."""
    xtx = [[0.0] * p for _ in range(p)]
    xty = [0.0] * p
    for cols, y in rows:
        for i in cols:
            xty[i] += y
            row = xtx[i]
            for j in cols:
                row[j] += 1.0
    for i in range(1, p):
        xtx[i][i] += lam
    return _solve(xtx, xty)


def _ranks(xs: list[float]) -> list[float]:
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2
        i = j + 1
    return r


def spearman(x: list[float], y: list[float]) -> float:
    if len(x) < 3:
        return float("nan")
    rx, ry = _ranks(x), _ranks(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx)
    syy = sum((b - my) ** 2 for b in ry)
    return sxy / math.sqrt(sxx * syy) if sxx and syy else float("nan")


# --- features --------------------------------------------------------------------------


def levels_of(evs: list[bt.Ev]) -> dict[str, list[str]]:
    """Each feature's levels, most common first (the first is the baseline column, left out)."""
    out = {}
    for f in MODEL_FEATURES:
        counts: dict[str, int] = defaultdict(int)
        for e in evs:
            counts[bt.FEATURES[f](e)] += 1
        out[f] = sorted(counts, key=lambda k: (-counts[k], k))
    return out


def columns(levels: dict[str, list[str]]) -> list[tuple[str, str]]:
    return [("", "intercept")] + [(f, lv) for f in MODEL_FEATURES for lv in levels[f][1:]]


def _active(e: bt.Ev, index: dict[tuple[str, str], int]) -> list[int]:
    cols = [0]
    for f in MODEL_FEATURES:
        j = index.get((f, bt.FEATURES[f](e)))
        if j is not None:
            cols.append(j)
    return cols


def _predict(coef: list[float], cols: list[int]) -> float:
    return sum(coef[i] for i in cols)


def _clip(x: float, bounds: tuple[float, float]) -> float:
    return min(max(x, bounds[0]), bounds[1])


# --- outcomes ----------------------------------------------------------------------------


def max_drawdown(path, steps: int = bt.PRIMARY) -> float | None:
    """Worst fall from a running high during the hold, starting at the entry price."""
    if path is None or not len(path):
        return None
    level, peak, worst = 1.0, 1.0, 0.0
    for r in path[:steps]:
        level *= 1 + r
        peak = max(peak, level)
        worst = min(worst, level / peak - 1)
    return worst


def _q(vals: list[float], q: float) -> float | None:
    return bt.percentile(sorted(vals), q) if vals else None


def _summary(evs: list[bt.Ev], bounds_ew, bounds_spy) -> dict:
    ew = [_clip(e.abn_ew[bt.PRIMARY], bounds_ew) for e in evs if bt.PRIMARY in e.abn_ew]
    spy = [_clip(e.abn[bt.PRIMARY], bounds_spy) for e in evs if bt.PRIMARY in e.abn]
    if not spy:
        return {"n": 0}
    return {"n": len(spy), "mean_ew": sum(ew) / len(ew) if ew else None, "mean_spy": sum(spy) / len(spy),
            "beat_spy": sum(1 for v in spy if v > 0) / len(spy),
            "beat_ew": sum(1 for v in ew if v > 0) / len(ew) if ew else None,
            "p10_spy": _q(spy, 0.1), "p50_spy": _q(spy, 0.5), "p90_spy": _q(spy, 0.9)}


def risk_table(evs: list[bt.Ev]) -> dict[str, dict]:
    """Spread of 3-month raw returns and drawdowns by price and liquidity bucket, all years."""
    cells: dict[str, list[bt.Ev]] = defaultdict(list)
    for e in evs:
        if bt.PRIMARY in e.ret:
            cells[risk_key(bt.FEATURES["price"](e), bt.FEATURES["liquidity"](e))].append(e)
            cells["all"].append(e)
    out = {}
    for key, group in cells.items():
        rets = [e.ret[bt.PRIMARY] for e in group]
        dds = [d for d in (max_drawdown(e.path) for e in group) if d is not None]
        out[key] = {"n": len(rets), "p10": _q(rets, 0.1), "p25": _q(rets, 0.25), "p50": _q(rets, 0.5),
                    "p75": _q(rets, 0.75), "p90": _q(rets, 0.9),
                    "lose30": sum(1 for r in rets if r <= -0.3) / len(rets),
                    "dd50": _q(dds, 0.5), "dd90": _q(dds, 0.1)}
    return out


def risk_key(price_bucket: str, liquidity_bucket: str) -> str:
    return f"{price_bucket}|{liquidity_bucket}"


# --- fitting -----------------------------------------------------------------------------


def _exit_date(e: bt.Ev, cal: bt.Calendar) -> str | None:
    c = e.exit_cal.get(bt.PRIMARY)
    return cal.dates[c] if c is not None else None


def _grade(pred: float, cuts: dict[str, float]) -> str:
    for g, _ in GRADES:
        if pred >= cuts[g]:
            return g
    return "D"


def _cuts(preds: list[float]) -> dict[str, float]:
    s = sorted(preds)
    return {g: bt.percentile(s, q) for g, q in GRADES}


def _rows(evs, index, key, bounds):
    return [(_active(e, index), _clip(getattr(e, key)[bt.PRIMARY], bounds)) for e in evs if bt.PRIMARY in getattr(e, key)]


def fit(evs: list[bt.Ev], cal: bt.Calendar, echo=print) -> dict:
    """Fit, validate and summarize the strength model. Returns the advisor.json content."""
    # The live universe: discretionary buys of listed stocks at $2+ trading $1M+/day, one per company-day.
    sample = bt.unique_signals([e for e in evs if e.liquid and e.in_study and not e.buy.plan_purchase
                                and bt.is_listed_stock(e.symbol or "") and bt.PRIMARY in e.abn])
    disc = [e for e in sample if (_exit_date(e, cal) or "9999") <= bt.DISCOVERY_END]
    hold = [e for e in sample if e.filed >= bt.HOLDOUT_START]
    disc_ew = sorted(e.abn_ew[bt.PRIMARY] for e in disc if bt.PRIMARY in e.abn_ew)
    b_ew = (bt.percentile(disc_ew, 0.01), bt.percentile(disc_ew, 0.99)) if disc_ew else (-1.0, 1.0)
    b_spy = bt.winsor_bounds(disc, bt.PRIMARY)
    levels = levels_of(sample)
    cols = columns(levels)
    index = {c: i for i, c in enumerate(cols)}
    p = len(cols)

    # Shrinkage: earlier part of discovery predicts the later part.
    early = [e for e in disc if (_exit_date(e, cal) or "9999") <= CV_SPLIT]
    late = [e for e in disc if e.filed > CV_SPLIT and bt.PRIMARY in e.abn_ew]
    cv = {}
    for lam in LAMBDAS:
        coef = _ridge(_rows(early, index, "abn_ew", b_ew), p, lam)
        cv[lam] = spearman([_predict(coef, _active(e, index)) for e in late], [e.abn_ew[bt.PRIMARY] for e in late])
    lam = max(LAMBDAS, key=lambda k: (cv[k] if not math.isnan(cv[k]) else -9, k))
    echo(f"  advisor: shrinkage {lam:g} (validation rank correlation {cv[lam]:.3f})")

    # The validated model: discovery only, scored once on 2016+.
    coef_disc = _ridge(_rows(disc, index, "abn_ew", b_ew), p, lam)
    pred_disc = {id(e): _predict(coef_disc, _active(e, index)) for e in sample}
    cuts_disc = _cuts([pred_disc[id(e)] for e in disc])
    hold_ew = [e for e in hold if bt.PRIMARY in e.abn_ew]
    ic_hold = spearman([pred_disc[id(e)] for e in hold_ew], [e.abn_ew[bt.PRIMARY] for e in hold_ew])
    ic_years = {}
    for year in sorted({e.filed[:4] for e in hold_ew}):
        ys = [e for e in hold_ew if e.filed[:4] == year]
        if len(ys) >= 50:
            ic_years[year] = spearman([pred_disc[id(e)] for e in ys], [e.abn_ew[bt.PRIMARY] for e in ys])
    by_grade: dict[str, list[bt.Ev]] = defaultdict(list)
    for e in hold:
        by_grade[_grade(pred_disc[id(e)], cuts_disc)].append(e)
    grades_hold = {}
    for g in ("A", "B", "C", "D"):
        group = by_grade.get(g, [])
        s = _summary(group, b_ew, b_spy)
        ct = bt.ctp_stats(bt.calendar_time(group, cal, bench="ew")["series"], boot=0) if group else {}
        s.update({"ann_ew": ct.get("annualized"), "t_ew": ct.get("t"), "months": ct.get("months")})
        grades_hold[g] = s
    spread = bt.ctp_stats(bt.difference_series(bt.calendar_time(by_grade.get("A", []) + by_grade.get("B", []), cal),
                                               bt.calendar_time(by_grade.get("C", []) + by_grade.get("D", []), cal),
                                               cal), boot=0)

    def sim(group):
        r = bt.simulate([dataclasses.replace(e, score=int(1e4 * pred_disc[id(e)])) for e in group], cal)
        return {k: r.get(k) for k in ("strategy_cagr", "spy_cagr", "strategy_max_drawdown", "strategy_sharpe", "trades")}

    portfolios = {"graded_ab": sim(by_grade.get("A", []) + by_grade.get("B", [])), "all": sim(hold)}
    echo(f"  advisor: 2016+ rank correlation {ic_hold:.3f}; A {grades_hold['A'].get('ann_ew')} "
         f"D {grades_hold['D'].get('ann_ew')} a year vs comparable stocks")

    # The live model: everything, same shrinkage. Effects are centered on the average buy for display.
    coef = _ridge(_rows(sample, index, "abn_ew", b_ew), p, lam)
    coef_spy = _ridge(_rows(sample, index, "abn", b_spy), p, lam)
    preds = [_predict(coef, _active(e, index)) for e in sample]
    effects: dict[str, dict[str, float]] = {}
    for f in MODEL_FEATURES:
        counts: dict[str, int] = defaultdict(int)
        for e in sample:
            counts[bt.FEATURES[f](e)] += 1
        raw = {lv: (coef[index[(f, lv)]] if (f, lv) in index else 0.0) for lv in levels[f]}
        mean = sum(raw[lv] * counts[lv] for lv in raw) / max(1, sum(counts.values()))
        effects[f] = {lv: raw[lv] - mean for lv in raw}
    return _clean({
        "fitted": dt.date.today().isoformat(), "sample": len(sample), "discovery": len(disc), "holdout": len(hold),
        "features": list(MODEL_FEATURES), "levels": levels, "columns": [list(c) for c in cols],
        "coef_ew": coef, "coef_spy": coef_spy, "lambda": lam, "cv": {f"{k:g}": v for k, v in cv.items()},
        "cuts": _cuts(preds), "effects": effects, "average_pred": sum(preds) / len(preds),
        "validation": {"rank_corr": ic_hold, "rank_corr_years": ic_years, "grades": grades_hold,
                       "top_vs_bottom": {k: spread.get(k) for k in ("annualized", "t", "p", "months", "years_positive")},
                       "portfolios": portfolios, "cuts": cuts_disc, "bounds_ew": list(b_ew), "bounds_spy": list(b_spy)},
        "risk": risk_table(sample),
    })


def _clean(x):
    """NaN and infinities become None, so the file is strict JSON."""
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    return x


# --- scoring a live signal ------------------------------------------------------------


def _ev_from_row(row: dict) -> bt.Ev:
    buy = BuyEvent(**{f.name: row.get(f.name) for f in dataclasses.fields(BuyEvent)})
    ev = bt.Ev(buy=buy, filed=row["filed_at"][:10], symbol=row.get("symbol"))
    ev.price, ev.adv, ev.prior_ret = row.get("price"), row.get("adv"), row.get("prior_ret")
    ev.cluster, ev.kind = row.get("cluster") or 1, row.get("kind") or "unclassified"
    ev.track_n, ev.track = row.get("track_n") or 0, row.get("track")
    ev.first_in_year_insider = row.get("first_in_year_insider")
    ev.first_in_year_issuer = row.get("first_in_year_issuer")
    return ev


def score(row: dict, model: dict) -> dict:
    """Grade, expected edge, feature effects and risk for one ledger row."""
    ev = _ev_from_row(row)
    index = {tuple(c): i for i, c in enumerate(model["columns"])}
    cols = _active(ev, index)
    pred = _predict(model["coef_ew"], cols)
    pred_spy = _predict(model["coef_spy"], cols)
    levels = {f: bt.FEATURES[f](ev) for f in model["features"]}
    effects = [(f, lv, model["effects"].get(f, {}).get(lv, 0.0)) for f, lv in levels.items()]
    risk = model["risk"].get(risk_key(levels["price"], levels["liquidity"]))
    if not risk or risk["n"] < MIN_CELL:
        risk = model["risk"]["all"]
    return {"grade": _grade(pred, model["cuts"]), "pred_ew": pred, "pred_spy": pred_spy,
            "levels": levels, "effects": effects, "risk": risk}


def position(risk: dict, budget: float, adv: float | None, account: float | None = None) -> dict:
    """Research sizing: the loss budget over the 1-in-10 bad 3-month outcome, capped by the tested rules."""
    bad = abs(min(risk.get("p10") or -0.3, -0.05))
    share = min(budget / bad, MAX_POSITION)
    out = {"share": share, "bad_case": -bad, "limited_by": "risk" if budget / bad < MAX_POSITION else "max position"}
    if account and adv:
        cap = ADV_CAP * adv
        if share * account > cap:
            out.update(share=cap / account, limited_by="liquidity")
    return out
