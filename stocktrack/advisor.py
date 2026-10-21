"""Signal report cards: how a new insider buy's profile has done before, what usually followed, and how big a
position the research would take.

What the evidence supports, and so what this does:

* Individual buys are mostly noise. A regression on every feature predicted nothing out of sample (2016+ rank
  correlation about 0), so there is no fine-grained score here.
* A few features beat or lagged the typical buy in the same direction in both 2006-2015 and 2016+. Those
  consistent features are the profile's "tilts" (each the smaller of its two periods' edges), added up into one
  of three tiers: above typical, typical, below typical.
* The method was tested honestly: tilts picked the same way from the two halves of 2006-2015 alone, then applied
  unchanged to 2016+, separated buys that beat comparable stocks from buys that didn't (reported in
  "validation"). The live tilts use both full periods, so the forward test is their real check.
* Risk (the spread of 3-month outcomes) depends strongly on share price and liquidity, so position size comes
  from risk, not from the tier: a loss budget the reader sets, over the 1-in-10 bad outcome for similar stocks,
  capped by the tested rules (5% of the account, 2% of a day's dollar volume).

Nothing here is personal advice.
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import math
from collections import defaultdict

from stocktrack import backtest as bt
from stocktrack.signals import BuyEvent

TILT_FEATURES = ("role", "cluster", "insider_type", "prior_3m_return", "price", "liquidity", "value", "stake_increase")
MIN_N = 150  # buys of a kind needed in each period
MIN_EFFECT = 0.01  # a tilt must be at least 1% a year, the same way, in both periods
TIER_EDGE = 0.02  # summed tilts of +-2% a year or more leave the typical tier
SPLIT_EARLY = "2010-12-31"  # validation: tilts chosen on 2006-2010 vs 2011-2015, tested on 2016+
MAX_POSITION = 0.05  # the tested portfolios hold up to 20 equal positions
ADV_CAP = 0.02  # and never more than 2% of a day's dollar volume
MIN_CELL = 200


def _q(vals: list[float], q: float) -> float | None:
    return bt.percentile(sorted(vals), q) if vals else None


def _exit_date(e: bt.Ev, cal: bt.Calendar) -> str:
    c = e.exit_cal.get(bt.PRIMARY)
    return cal.dates[c] if c is not None else "9999"


def live_sample(evs: list[bt.Ev]) -> list[bt.Ev]:
    """The buys the forward test logs: discretionary, listed, $2+, $1M+/day, one per company-day."""
    return bt.unique_signals([e for e in evs if e.liquid and e.in_study and not e.buy.plan_purchase
                              and bt.is_listed_stock(e.symbol or "") and bt.PRIMARY in e.abn])


# --- tilts ---------------------------------------------------------------------------------


def feature_effects(periods: list[list[bt.Ev]], cal: bt.Calendar, levels: dict[str, list[str]]) -> dict:
    """Each feature level's yearly edge over the typical buy in each period (calendar-time difference)."""
    base = [bt.calendar_time(p, cal) for p in periods]
    out: dict[str, dict[str, dict]] = {}
    for f in TILT_FEATURES:
        out[f] = {}
        for lv in levels[f]:
            effs, ts, ns = [], [], []
            for p, b in zip(periods, base):
                g = [e for e in p if bt.FEATURES[f](e) == lv]
                st = bt.ctp_stats(bt.difference_series(bt.calendar_time(g, cal), b, cal), boot=0) if len(g) >= MIN_N else {}
                effs.append(st.get("annualized"))
                ts.append(st.get("t"))
                ns.append(len(g))
            ok = all(x is not None for x in effs)
            consistent = ok and (all(x >= MIN_EFFECT for x in effs) or all(x <= -MIN_EFFECT for x in effs))
            # The tilt is the smaller of the two edges: what held at least that well in both periods.
            tilt = min(effs, key=abs) if consistent else 0.0
            out[f][lv] = {"effects": effs, "t": ts, "n": ns, "tilt": tilt}
    return out


def levels_of(evs: list[bt.Ev]) -> dict[str, list[str]]:
    return {f: sorted({bt.FEATURES[f](e) for e in evs}) for f in TILT_FEATURES}


def tilt_total(levels: dict[str, str], effects: dict) -> float:
    return sum(effects.get(f, {}).get(lv, {}).get("tilt", 0.0) for f, lv in levels.items())


def tier(total: float) -> str:
    return "above" if total >= TIER_EDGE else "below" if total <= -TIER_EDGE else "typical"


def _levels(e: bt.Ev) -> dict[str, str]:
    return {f: bt.FEATURES[f](e) for f in TILT_FEATURES}


# --- outcomes --------------------------------------------------------------------------------


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


def outcomes(evs: list[bt.Ev], bounds: tuple[float, float]) -> dict:
    """What happened over 63 sessions: vs SPY per buy, and vs comparable stocks."""
    spy = [min(max(e.abn[bt.PRIMARY], bounds[0]), bounds[1]) for e in evs if bt.PRIMARY in e.abn]
    ew = [min(max(e.abn_ew[bt.PRIMARY], bounds[0]), bounds[1]) for e in evs if bt.PRIMARY in e.abn_ew]
    if not spy:
        return {"n": 0}
    return {"n": len(spy), "mean_spy": sum(spy) / len(spy), "beat_spy": sum(1 for v in spy if v > 0) / len(spy),
            "p10_spy": _q(spy, 0.1), "p50_spy": _q(spy, 0.5), "p90_spy": _q(spy, 0.9),
            "mean_ew": sum(ew) / len(ew) if ew else None,
            "beat_ew": sum(1 for v in ew if v > 0) / len(ew) if ew else None}


def risk_key(price_bucket: str, liquidity_bucket: str) -> str:
    return f"{price_bucket}|{liquidity_bucket}"


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
                    "lose20": sum(1 for r in rets if r <= -0.2) / len(rets),
                    "gain20": sum(1 for r in rets if r >= 0.2) / len(rets),
                    "dd_median": _q(dds, 0.5), "dd_bad": _q(dds, 0.1)}
    return out


def _ctp(group: list[bt.Ev], cal: bt.Calendar) -> dict:
    st = bt.ctp_stats(bt.calendar_time(group, cal, bench="ew")["series"], boot=0) if group else {}
    return {k: st.get(k) for k in ("annualized", "t", "p", "months", "years_positive")}


# --- fitting ------------------------------------------------------------------------------------


def fit(evs: list[bt.Ev], cal: bt.Calendar, echo=print) -> dict:
    """Tilts, their out-of-sample check, base rates and the risk table. Returns the advisor.json content."""
    sample = live_sample(evs)
    disc = [e for e in sample if _exit_date(e, cal) <= bt.DISCOVERY_END]
    hold = [e for e in sample if e.filed >= bt.HOLDOUT_START]
    bounds = bt.winsor_bounds(disc, bt.PRIMARY) if disc else (-1.0, 1.0)
    levels = levels_of(sample)

    # The honest check: tilts chosen inside 2006-2015 only, applied unchanged to 2016+.
    early = [e for e in disc if _exit_date(e, cal) <= SPLIT_EARLY]
    late = [e for e in disc if e.filed > SPLIT_EARLY]
    v_effects = feature_effects([early, late], cal, levels)
    by_tier: dict[str, list[bt.Ev]] = defaultdict(list)
    for e in hold:
        by_tier[tier(tilt_total(_levels(e), v_effects))].append(e)
    spread = bt.ctp_stats(bt.difference_series(bt.calendar_time(by_tier["above"], cal),
                                               bt.calendar_time(by_tier["below"], cal), cal), boot=0)
    sims = {}
    for name, group in by_tier.items():
        r = bt.simulate(group, cal)
        sims[name] = {k: r.get(k) for k in ("strategy_cagr", "spy_cagr", "strategy_max_drawdown", "trades")}
    validation = {
        "chosen_on": "2006-2010 vs 2011-2015", "tested_on": "2016 onward",
        "tilts": {f"{f}:{lv}": d["tilt"] for f, lvs in v_effects.items() for lv, d in lvs.items() if d["tilt"]},
        "tiers": {name: {**outcomes(group, bounds), "ctp": _ctp(group, cal)} for name, group in by_tier.items()},
        "above_minus_below": {k: spread.get(k) for k in ("annualized", "t", "p", "months", "years_positive")},
        "portfolios": sims,
    }
    echo(f"  advisor: 2016+ above-typical minus below-typical {spread.get('annualized', float('nan')):+.3f}/yr "
         f"(t {spread.get('t', float('nan')):.2f})")

    # The live tilts: consistent across the two full periods.
    effects = feature_effects([disc, hold], cal, levels)
    live_tiers: dict[str, list[bt.Ev]] = defaultdict(list)
    for e in sample:
        live_tiers[tier(tilt_total(_levels(e), effects))].append(e)
    return _clean({
        "fitted": dt.date.today().isoformat(), "sample": len(sample), "discovery": len(disc), "holdout": len(hold),
        "features": list(TILT_FEATURES), "effects": effects, "tier_edge": TIER_EDGE, "min_effect": MIN_EFFECT,
        "tier_share": {k: len(v) / len(sample) for k, v in live_tiers.items()} if sample else {},
        "base": {**outcomes(sample, bounds), "ctp": _ctp(sample, cal), "ctp_disc": _ctp(disc, cal), "ctp_hold": _ctp(hold, cal)},
        "validation": validation,
        "risk": risk_table(sample),
        "rules": {"max_position": MAX_POSITION, "adv_cap": ADV_CAP, "hold_sessions": bt.PRIMARY},
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


# --- scoring a live signal ------------------------------------------------------------------


def ev_from_row(row: dict) -> bt.Ev:
    """A ledger row as an event with its decision-time facts, so the backtest's feature buckets apply."""
    buy = BuyEvent(**{f.name: row.get(f.name) for f in dataclasses.fields(BuyEvent)})
    ev = bt.Ev(buy=buy, filed=row["filed_at"][:10], symbol=row.get("symbol"))
    ev.price, ev.adv, ev.prior_ret = row.get("price"), row.get("adv"), row.get("prior_ret")
    ev.cluster, ev.kind = row.get("cluster") or 1, row.get("kind") or "unclassified"
    ev.track_n, ev.track = row.get("track_n") or 0, row.get("track")
    ev.first_in_year_insider = row.get("first_in_year_insider")
    ev.first_in_year_issuer = row.get("first_in_year_issuer")
    return ev


def score(row: dict, model: dict) -> dict:
    """Tier, tilts and risk for one ledger row."""
    levels = _levels(ev_from_row(row))
    effects = model["effects"]
    tilts = []
    for f, lv in levels.items():
        d = effects.get(f, {}).get(lv)
        if d and d.get("tilt"):
            tilts.append({"feature": f, "level": lv, "tilt": d["tilt"], "effects": d["effects"]})
    tilts.sort(key=lambda t: -abs(t["tilt"]))
    total = sum(t["tilt"] for t in tilts)
    risk = model["risk"].get(risk_key(levels["price"], levels["liquidity"]))
    if not risk or risk["n"] < MIN_CELL:
        risk = model["risk"]["all"]
    return {"tier": tier(total), "tilt": total, "tilts": tilts, "levels": levels, "risk": risk}


def position(risk: dict, budget: float, adv: float | None = None, account: float | None = None) -> dict:
    """Research sizing: the loss budget over the 1-in-10 bad 3-month outcome, capped by the tested rules."""
    bad = max(abs(min(risk.get("p10") or -0.3, 0.0)), 0.05)
    share, limit = budget / bad, "loss budget"
    if share > MAX_POSITION:
        share, limit = MAX_POSITION, "5% cap"
    if account and adv and share * account > ADV_CAP * adv:
        share, limit = ADV_CAP * adv / account, "liquidity"
    return {"share": share, "bad_case": -bad, "limited_by": limit}


# --- market calendar (for planned exit dates) ----------------------------------------------


def _easter(year: int) -> dt.date:
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    m = (32 + 2 * e + 2 * i - h - k) % 7
    n = (a + 11 * h + 22 * m) // 451
    month = (h + m - 7 * n + 114) // 31
    return dt.date(year, month, (h + m - 7 * n + 114) % 31 + 1)


def _nth_weekday(year: int, month: int, weekday: int, n: int) -> dt.date:
    """n-th weekday (Mon=0) of a month; n=-1 for the last."""
    if n > 0:
        first = dt.date(year, month, 1)
        return first + dt.timedelta(days=(weekday - first.weekday()) % 7 + 7 * (n - 1))
    last = (dt.date(year + (month == 12), month % 12 + 1, 1) - dt.timedelta(days=1))
    return last - dt.timedelta(days=(last.weekday() - weekday) % 7)


def _observed(d: dt.date) -> dt.date:
    return d - dt.timedelta(days=1) if d.weekday() == 5 else d + dt.timedelta(days=1) if d.weekday() == 6 else d


def market_holidays(year: int) -> set[dt.date]:
    """NYSE full-day holidays (rules in force since 2022)."""
    days = {_observed(dt.date(year, 1, 1)), _nth_weekday(year, 1, 0, 3), _nth_weekday(year, 2, 0, 3),
            _easter(year) - dt.timedelta(days=2), _nth_weekday(year, 5, 0, -1), _observed(dt.date(year, 6, 19)),
            _observed(dt.date(year, 7, 4)), _nth_weekday(year, 9, 0, 1), _nth_weekday(year, 11, 3, 4),
            _observed(dt.date(year, 12, 25))}
    if dt.date(year, 1, 1).weekday() == 5:  # New Year on a Saturday isn't observed on the Friday before
        days.discard(dt.date(year - 1, 12, 31))
    return days


def is_market_day(d: dt.date) -> bool:
    return d.weekday() < 5 and d not in market_holidays(d.year)


def next_market_day(day: str) -> str:
    d = dt.date.fromisoformat(day) + dt.timedelta(days=1)
    while not is_market_day(d):
        d += dt.timedelta(days=1)
    return d.isoformat()


def add_market_days(day: str, n: int) -> str:
    """The n-th market session after `day` (n=0 returns day itself)."""
    for _ in range(n):
        day = next_market_day(day)
    return day
