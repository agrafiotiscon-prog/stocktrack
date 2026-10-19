"""Event study and portfolio backtest of insider purchases.

Rules that keep it honest:

* Entry is the OPEN of the first trading day after the filing date, the first
  price anyone could have traded on once the purchase was public. The trade
  date is never used for entry.
* Horizons count market sessions (SPY's calendar). Exits use the stock's close on
  that session, or its last close within 5 sessions; staler than that (halted,
  delisted) means no return.
* Abnormal return = stock return minus SPY's over the same open-to-close window.
* Every feature is point-in-time: clusters and insider track records only use
  filings (and outcomes) that were public before entry.
* Statistics treat each calendar month as one observation (the average of that
  month's events), so a crash month with 500 correlated buys counts once.
  Returns are winsorized at the 1st/99th percentile per horizon.
* 2006-2015 is in-sample, 2016 onward out-of-sample; slice p-values get a Holm
  correction for testing many slices; a walk-forward test picks the score
  threshold each year using only earlier years.
* Prices come from currently listed symbols only (see history.py), so delisted
  companies are missing. Coverage is reported per year.
"""

from __future__ import annotations

import bisect
import datetime as dt
import heapq
import math
import random
import statistics
from array import array
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Iterable

from stocktrack.history import BENCHMARK, PriceHistory, PriceStore, TickerMap
from stocktrack.signals import BuyEvent, dedupe_purchases, is_listed_stock, score_buy

HORIZONS = (1, 5, 21, 63, 126, 252)
PRIMARY = 63
PATH_LEN = 126  # sessions of daily returns kept per event for portfolio simulation
IN_SAMPLE_END = "2015-12-31"
MAX_ENTRY_DELAY = 3  # sessions between filing and first stock bar before we call it stale
MAX_STALE = 5  # sessions an exit price may be stale
CLUSTER_DAYS = 14
TRACK_MIN = 3  # prior outcomes needed before an insider has a "track record"


@dataclass(slots=True)
class Ev:
    buy: BuyEvent
    filed: str
    symbol: str | None = None
    resolve: str = ""
    exchange: str = ""
    entry_date: str | None = None
    entry_cal: int = -1
    price: float | None = None  # raw price the day before entry
    adv: float | None = None  # 20-session average dollar volume before entry
    price_ratio: float | None = None  # insider's avg price / market price on trade date
    mkt_value: float | None = None
    prior_ret: float | None = None  # stock return over the 63 sessions before entry
    ret: dict = field(default_factory=dict)
    abn: dict = field(default_factory=dict)
    exit_date: dict = field(default_factory=dict)
    path: array | None = None  # daily returns aligned to the SPY calendar from entry
    # point-in-time features
    cluster: int = 1
    kind: str = "unknown"  # routine / opportunistic / unknown (Cohen-Malloy-Pomorski)
    track_n: int = 0
    track_mean: float | None = None
    first_in_year_insider: bool = True
    first_in_year_issuer: bool = True
    score: int = 0

    @property
    def year(self) -> int:
        return int(self.filed[:4])

    @property
    def month(self) -> str:
        return (self.entry_date or self.filed)[:7]

    @property
    def value(self) -> float:
        """Dollar value, from market prices when the filing's price looks wrong."""
        if self.price_ratio is not None and not 0.5 <= self.price_ratio <= 2.0 and self.mkt_value:
            return self.mkt_value
        return self.buy.value

    @property
    def liquid(self) -> bool:
        return (self.price or 0) >= 2.0 and (self.adv or 0) >= 1_000_000


# --- market data ---------------------------------------------------------


class Calendar:
    def __init__(self, spy: PriceHistory) -> None:
        self.spy = spy
        self.dates = spy.dates
        self.index = {d: i for i, d in enumerate(spy.dates)}
        self.daily = [0.0] + [spy.close[i] / spy.close[i - 1] - 1 for i in range(1, len(spy.dates))]

    def first_after(self, day: str) -> int:
        return bisect.bisect_right(self.dates, day)


def align(hist: PriceHistory, cal: Calendar) -> PriceHistory:
    """Drop bars on days the benchmark didn't trade, so calendar indexes stay sorted."""
    keep = [k for k, d in enumerate(hist.dates) if d in cal.index]
    if len(keep) == len(hist.dates):
        return hist
    return PriceHistory(hist.symbol, [hist.dates[k] for k in keep], [hist.open[k] for k in keep],
                        [hist.close[k] for k in keep], [hist.dollar_volume_day[k] for k in keep],
                        [hist.raw_close[k] for k in keep])


def attach_market_data(ev: Ev, hist: PriceHistory, cal: Calendar) -> None:
    """Entry, forward returns, price checks and the simulation path for one event.

    `hist` must be aligned to the calendar (see align()).
    """
    b = ev.buy
    bar_cal = [cal.index[d] for d in hist.dates]

    # Did the insider pay something close to the market price? (catches typos)
    ti = hist.index_on_or_before(b.last_date) if b.last_date else None
    if ti is not None and b.last_date:
        gap = (dt.date.fromisoformat(b.last_date) - dt.date.fromisoformat(hist.dates[ti])).days
        if gap <= 7:
            raw = hist.raw_close[ti]
            ev.mkt_value = b.shares * raw
            if b.avg_price:
                ev.price_ratio = b.avg_price / raw

    i = hist.index_after(ev.filed)
    if i is None:
        return
    c_entry = bar_cal[i]
    if c_entry - cal.first_after(ev.filed) > MAX_ENTRY_DELAY:
        return
    ev.entry_date, ev.entry_cal = hist.dates[i], c_entry
    entry_px = hist.open[i]
    if i >= 1:
        ev.price = hist.raw_close[i - 1]
        ev.adv = hist.dollar_volume(i, 20)
    if i >= 64:
        ev.prior_ret = hist.close[i - 1] / hist.close[i - 64] - 1

    # Stock bars by calendar index, for exits and the path.
    cals = bar_cal
    for h in HORIZONS:
        c_exit = c_entry + h - 1
        if c_exit >= len(cal.dates):
            break  # not mature yet
        j = bisect.bisect_right(cals, c_exit, lo=i) - 1
        if j < i or c_exit - cals[j] > MAX_STALE:
            break  # stopped trading
        r = hist.close[j] / entry_px - 1
        spy_r = cal.spy.close[c_exit] / cal.spy.open[c_entry] - 1
        ev.ret[h], ev.abn[h], ev.exit_date[h] = r, r - spy_r, cal.dates[c_exit]

    path = array("f")
    prev_close, last_bar_cal, j = entry_px, c_entry, i
    for k in range(PATH_LEN):
        c = c_entry + k
        if c >= len(cal.dates):
            break
        if j < len(cals) and cals[j] == c:
            path.append(hist.close[j] / prev_close - 1)
            prev_close, last_bar_cal = hist.close[j], c
            j += 1
        else:
            if c - last_bar_cal > MAX_STALE:
                break
            path.append(0.0)
    ev.path = path


def build_events(buys: Iterable[BuyEvent], store: PriceStore, tickers: TickerMap,
                 progress: Callable[[int, int], None] | None = None) -> tuple[list[Ev], Calendar]:
    spy = store.load(BENCHMARK)
    if spy is None:
        raise RuntimeError("no SPY history; fetch prices first")
    cal = Calendar(spy)
    ordered = sorted(buys, key=lambda b: (b.filed_at[:10], b.accession))
    evs = [Ev(buy=b, filed=b.filed_at[:10]) for b in dedupe_purchases(ordered) if b.filed_at]
    by_symbol: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        ev.symbol, ev.resolve = tickers.resolve(ev.buy.issuer_cik, ev.buy.ticker)
        ev.exchange = tickers.exchange(ev.buy.issuer_cik)
        if ev.symbol:
            by_symbol[ev.symbol].append(ev)
    for n, (sym, group) in enumerate(sorted(by_symbol.items()), 1):
        hist = store.load(sym)
        if hist is not None:
            hist = align(hist, cal)
            for ev in group:
                attach_market_data(ev, hist, cal)
        if progress:
            progress(n, len(by_symbol))
    return evs, cal


# --- point-in-time features ----------------------------------------------


def add_pit_features(evs: list[Ev]) -> None:
    """Cluster size, routine/opportunistic, track record and novelty, using only earlier filings."""
    by_day: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        by_day[ev.filed].append(ev)

    issuer_recent: dict[str, list[Ev]] = defaultdict(list)  # discretionary buys, for clusters
    months: dict[str, dict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    last_owner: dict[str, str] = {}
    last_issuer: dict[str, str] = {}
    pending: list[tuple[str, int, str, float]] = []  # (known_date, seq, owner, abn63) heap
    track: dict[str, list[float]] = defaultdict(lambda: [0, 0.0])
    seq = 0

    for day in sorted(by_day):
        todays = by_day[day]
        # Outcomes known before this day's entries become part of track records.
        while pending and pending[0][0] < (todays[0].entry_date or day):
            _, _, owner, abn = heapq.heappop(pending)
            track[owner][0] += 1
            track[owner][1] += abn
        # Same-day filings are public before the next open, so they count for clusters.
        for ev in todays:
            if ev.buy.counts_toward_cluster:
                issuer_recent[ev.buy.issuer_cik].append(ev)
        for ev in todays:
            b = ev.buy
            peers = issuer_recent[b.issuer_cik]
            cutoff = (dt.date.fromisoformat(day) - dt.timedelta(days=60)).isoformat()
            while peers and peers[0].filed < cutoff:
                peers.pop(0)
            near = [p for p in peers if p is not ev and _days_apart(p.buy.last_date, b.last_date) <= CLUSTER_DAYS]
            ev.cluster = len({x.owner_cik for x in dedupe_purchases([b, *(p.buy for p in near)])})

            owner = b.owner_cik
            n, total = track[owner]
            ev.track_n = int(n)
            ev.track_mean = total / n if n else None

            year = int((b.first_date or day)[:4])
            month = int((b.first_date or day)[5:7])
            hist = months[owner]
            prior = [hist.get(year - k, set()) for k in (1, 2, 3)]
            if all(prior):
                ev.kind = "routine" if all(month in p for p in prior) else "opportunistic"
            ev.first_in_year_insider = _days_apart(last_owner.get(owner, ""), day) > 365
            ev.first_in_year_issuer = _days_apart(last_issuer.get(b.issuer_cik, ""), day) > 365
            ev.score = score_buy(b, ev.cluster).total
        for ev in todays:
            b = ev.buy
            year = int((b.first_date or day)[:4])
            months[b.owner_cik][year].add(int((b.first_date or day)[5:7]))
            last_owner[b.owner_cik] = day
            last_issuer[b.issuer_cik] = day
            if PRIMARY in ev.abn:
                seq += 1
                heapq.heappush(pending, (ev.exit_date[PRIMARY], seq, b.owner_cik, ev.abn[PRIMARY]))


def _days_apart(a: str, b: str) -> int:
    try:
        return abs((dt.date.fromisoformat(a) - dt.date.fromisoformat(b)).days)
    except ValueError:
        return 10**6


# --- statistics ------------------------------------------------------------


def percentile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return float("nan")
    k = (len(sorted_vals) - 1) * q
    lo, hi = math.floor(k), math.ceil(k)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (k - lo)


def winsor_bounds(evs: list[Ev], h: int, q: float = 0.01) -> tuple[float, float]:
    vals = sorted(ev.abn[h] for ev in evs if h in ev.abn)
    return percentile(vals, q), percentile(vals, 1 - q)


def p_value(t: float) -> float:
    """Two-sided p-value from a t statistic (normal approximation)."""
    return math.erfc(abs(t) / math.sqrt(2))


def summarize(evs: list[Ev], h: int, bounds: tuple[float, float], boot: int = 0, seed: int = 7) -> dict:
    lo, hi = bounds
    pts = [(ev.month, min(max(ev.abn[h], lo), hi), ev.ret[h]) for ev in evs if h in ev.abn]
    if not pts:
        return {"n": 0}
    abns = sorted(a for _, a, _ in pts)
    by_month: dict[str, list[float]] = defaultdict(list)
    for m, a, _ in pts:
        by_month[m].append(a)
    monthly = [sum(v) / len(v) for v in by_month.values()]
    out = {
        "n": len(pts),
        "months": len(monthly),
        "mean": sum(abns) / len(abns),
        "median": percentile(abns, 0.5),
        "hit": sum(1 for a in abns if a > 0) / len(abns),
        "raw_mean": sum(r for _, _, r in pts) / len(pts),
        "monthly_mean": sum(monthly) / len(monthly),
    }
    if len(monthly) >= 3:
        sd = statistics.stdev(monthly)
        out["t"] = out["monthly_mean"] / (sd / math.sqrt(len(monthly))) if sd > 0 else 0.0
        out["p"] = p_value(out["t"])
    if boot and len(monthly) >= 12:
        rng = random.Random(seed)
        means = sorted(sum(rng.choices(monthly, k=len(monthly))) / len(monthly) for _ in range(boot))
        out["ci"] = [percentile(means, 0.025), percentile(means, 0.975)]
    return out


def holm(pvals: dict[str, float]) -> dict[str, float]:
    """Holm-Bonferroni adjusted p-values."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, running, out = len(items), 0.0, {}
    for k, (key, p) in enumerate(items):
        running = max(running, min(1.0, (m - k) * p))
        out[key] = running
    return out


# --- features to slice by ------------------------------------------------------


def _bucket(x: float | None, edges: list[tuple[float, str]], missing: str = "unknown") -> str:
    if x is None:
        return missing
    for edge, label in edges:
        if x < edge:
            return label
    return edges[-1][1]


def _stake(ev: Ev) -> str:
    inc = ev.buy.stake_increase
    if inc is None:
        return "unknown"
    if math.isinf(inc):
        return "new position"
    return _bucket(inc, [(0.05, "<5%"), (0.2, "5-20%"), (0.5, "20-50%"), (math.inf, "50%+")])


ROLE_GROUP = {"CEO": "CEO", "CFO": "CFO", "President": "President/Chair", "Chair": "President/Chair",
              "C-Suite": "Other exec", "Officer": "Other exec", "Director": "Director",
              "10% Owner": "10% owner", "Other": "Other"}

FEATURES: dict[str, Callable[[Ev], str]] = {
    "role": lambda e: ROLE_GROUP.get(e.buy.role, "Other"),
    "value": lambda e: _bucket(e.value, [(25e3, "<$25K"), (100e3, "$25-100K"), (500e3, "$100-500K"),
                                        (2e6, "$500K-2M"), (math.inf, "$2M+")]),
    "stake_increase": _stake,
    "cluster": lambda e: {1: "1 insider", 2: "2 insiders"}.get(e.cluster, "3+ insiders"),
    "insider_type": lambda e: e.kind,
    "track_record": lambda e: "no history" if e.track_n < TRACK_MIN or e.track_mean is None else _bucket(
        e.track_mean, [(-0.05, "past buys lagged (<-5%)"), (0.05, "past buys flat"),
                       (math.inf, "past buys won (>+5%)")]),
    "prior_3m_return": lambda e: _bucket(e.prior_ret, [(-0.3, "down 30%+"), (-0.1, "down 10-30%"),
                                                       (0.1, "flat"), (0.3, "up 10-30%"), (math.inf, "up 30%+")]),
    "price": lambda e: _bucket(e.price, [(1, "<$1"), (5, "$1-5"), (20, "$5-20"), (math.inf, "$20+")]),
    "liquidity": lambda e: _bucket(e.adv, [(1e5, "<$100K/day"), (1e6, "$100K-1M/day"),
                                           (1e7, "$1-10M/day"), (math.inf, "$10M+/day")]),
    "current_exchange": lambda e: e.exchange or "unknown",  # today's listing, not at the time
    "score": lambda e: _bucket(e.score, [(20, "0-19"), (40, "20-39"), (60, "40-59"), (80, "60-79"), (101, "80+")]),
    "plan_purchase": lambda e: "DRIP/plan" if e.buy.plan_purchase else "discretionary",
    "filing_delay": lambda e: _bucket(e.buy.filing_delay_days, [(3, "0-2 days"), (11, "3-10 days"),
                                                                (math.inf, "11+ days")]),
    "insider_novelty": lambda e: "first buy in 12m" if e.first_in_year_insider else "repeat buyer",
    "issuer_novelty": lambda e: "first insider buy at company in 12m" if e.first_in_year_issuer
    else "company had insider buys in last 12m",
    "period": lambda e: "2006-2015" if e.filed <= IN_SAMPLE_END else "2016+",
}


# --- strategies ------------------------------------------------------------------

STRATEGIES: dict[str, tuple[str, Callable[[Ev], bool]]] = {
    "all_liquid": ("Every discretionary insider buy in a liquid stock",
                   lambda e: not e.buy.plan_purchase),
    "score_40": ("Live score 40+ (notable)", lambda e: e.score >= 40 and not e.buy.plan_purchase),
    "score_60": ("Live score 60+ (strong)", lambda e: e.score >= 60 and not e.buy.plan_purchase),
    "ceo_cfo_100k": ("CEO or CFO buying $100K+", lambda e: e.buy.role in ("CEO", "CFO") and e.value >= 1e5),
    "cluster_3": ("3+ insiders buying within 14 days", lambda e: e.cluster >= 3),
    "opportunistic": ("Opportunistic insiders (Cohen-Malloy-Pomorski)", lambda e: e.kind == "opportunistic"
                      and not e.buy.plan_purchase),
    "contrarian": ("Insider buying after a 30%+ drop", lambda e: (e.prior_ret or 0) <= -0.3
                   and not e.buy.plan_purchase),
    "proven_insider": ("Insiders whose past buys beat SPY by 5%+", lambda e: e.track_n >= TRACK_MIN
                       and (e.track_mean or 0) > 0.05),
    "big_stake_up": ("Exec/director growing stake 20%+ with $100K+", lambda e: e.buy.role not in ("10% Owner", "Other")
                     and (e.buy.stake_increase or 0) >= 0.2 and e.value >= 1e5),
    "first_buy_exec": ("Exec's first buy in a year, $50K+", lambda e: e.first_in_year_insider
                       and e.buy.role in ("CEO", "CFO", "President", "Chair", "C-Suite") and e.value >= 5e4),
}


def cost_per_side(price: float | None) -> float:
    """Spread + slippage + commission per trade side, by share price."""
    p = price or 0
    if p >= 10:
        return 0.001
    if p >= 5:
        return 0.0025
    if p >= 2:
        return 0.005
    if p >= 1:
        return 0.01
    return 0.02


def simulate(evs: list[Ev], cal: Calendar, hold: int, slots: int = 20, costs: bool = True) -> dict:
    """Daily equal-weight portfolio: each signal is bought at the next open and held `hold` sessions.

    Up to `slots` positions get 1/slots of capital each (the rest sits in cash);
    beyond that every position gets an equal share.
    """
    n = len(cal.dates)
    total = [0.0] * n
    count = [0] * n
    cost = [0.0] * n
    first = n
    for ev in evs:
        if ev.path is None or not len(ev.path):
            continue
        c0 = ev.entry_cal
        steps = min(hold, len(ev.path))
        first = min(first, c0)
        for k in range(steps):
            total[c0 + k] += ev.path[k]
            count[c0 + k] += 1
        if costs:
            side = cost_per_side(ev.price)
            cost[c0] += side
            cost[c0 + steps - 1] += side
    if first >= n:
        return {"trades": 0}
    port, mn, spy = [], [], []
    for c in range(first, n):
        k = max(slots, count[c])
        r = (total[c] - cost[c]) / k
        port.append(r)
        mn.append(r - (min(count[c], k) / k) * cal.daily[c])
        spy.append(cal.daily[c])
    out = {"trades": sum(1 for ev in evs if ev.path is not None and len(ev.path)),
           "start": cal.dates[first], "end": cal.dates[-1],
           "exposure": sum(min(count[c], slots) / slots for c in range(first, n)) / (n - first)}
    out.update({f"strategy_{k}": v for k, v in perf(port).items()})
    out.update({f"spy_{k}": v for k, v in perf(spy).items()})
    out.update({f"neutral_{k}": v for k, v in perf(mn).items()})
    years: dict[str, list[list[float]]] = defaultdict(lambda: [[], []])
    for c, r, s in zip(range(first, n), port, spy):
        years[cal.dates[c][:4]][0].append(r)
        years[cal.dates[c][:4]][1].append(s)
    out["by_year"] = {y: {"strategy": _compound(a), "spy": _compound(b)} for y, (a, b) in sorted(years.items())}
    return out


def _compound(rets: list[float]) -> float:
    v = 1.0
    for r in rets:
        v *= 1 + r
    return v - 1


def perf(daily: list[float]) -> dict:
    if len(daily) < 2:
        return {}
    equity, peak, mdd = 1.0, 1.0, 0.0
    for r in daily:
        equity *= 1 + r
        peak = max(peak, equity)
        mdd = min(mdd, equity / peak - 1)
    years = len(daily) / 252
    sd = statistics.pstdev(daily)
    mean = sum(daily) / len(daily)
    return {
        "total": equity - 1,
        "cagr": equity ** (1 / years) - 1 if equity > 0 else -1.0,
        "vol": sd * math.sqrt(252),
        "sharpe": mean / sd * math.sqrt(252) if sd > 0 else 0.0,
        "max_drawdown": mdd,
    }


# --- the full run -------------------------------------------------------------------


def coverage(evs: list[Ev]) -> dict:
    years: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for ev in evs:
        y = years[ev.filed[:4]]
        y["events"] += 1
        y["listed_ticker"] += ev.symbol is not None
        y["priced"] += ev.entry_date is not None
        y[f"has_{PRIMARY}d"] += PRIMARY in ev.abn
    how: dict[str, int] = defaultdict(int)
    for ev in evs:
        how[ev.resolve] += 1
    return {"by_year": {k: dict(v) for k, v in sorted(years.items())}, "ticker_resolution": dict(how)}


def walk_forward(evs: list[Ev], bounds, thresholds=(0, 20, 30, 40, 50, 60, 70), start_year: int = 2010) -> dict:
    """Each year, pick the score threshold with the best mean 63d abnormal return on outcomes
    already known by Jan 1 of that year, then apply it to that year's buys."""
    pool = [e for e in evs if PRIMARY in e.abn and e.liquid and not e.buy.plan_purchase]
    chosen, picked = {}, []
    lo, hi = bounds
    last_year = max((e.year for e in pool), default=start_year)
    for year in range(start_year, last_year + 1):
        cutoff = f"{year}-01-01"
        known = [e for e in pool if e.exit_date[PRIMARY] < cutoff]
        best, best_mean = 0, -math.inf
        for t in thresholds:
            vals = [min(max(e.abn[PRIMARY], lo), hi) for e in known if e.score >= t]
            if len(vals) >= 200:
                m = sum(vals) / len(vals)
                if m > best_mean:
                    best, best_mean = t, m
        chosen[str(year)] = best
        picked.extend(e for e in pool if e.year == year and e.score >= best)
    return {"thresholds": chosen, "stats": summarize(picked, PRIMARY, bounds, boot=500)}


def run_backtest(evs: list[Ev], cal: Calendar, echo=print) -> dict:
    add_pit_features(evs)
    priced = [e for e in evs if e.entry_date is not None and is_listed_stock(e.symbol or "")]
    bounds = {h: winsor_bounds(priced, h) for h in HORIZONS}
    echo(f"{len(evs)} events, {len(priced)} with prices")

    result: dict = {"coverage": coverage(evs), "horizons": list(HORIZONS), "primary": PRIMARY,
                    "in_sample_end": IN_SAMPLE_END, "winsor": {str(h): bounds[h] for h in HORIZONS}}
    result["overall"] = {str(h): summarize(priced, h, bounds[h], boot=500) for h in HORIZONS}

    slices, pvals = {}, {}
    for name, fn in FEATURES.items():
        groups: dict[str, list[Ev]] = defaultdict(list)
        for e in priced:
            groups[fn(e)].append(e)
        slices[name] = {}
        for label, g in sorted(groups.items()):
            row = {str(h): summarize(g, h, bounds[h], boot=300 if h == PRIMARY else 0) for h in (5, 21, 63, 126, 252)}
            row["is"] = summarize([e for e in g if e.filed <= IN_SAMPLE_END], PRIMARY, bounds[PRIMARY])
            row["oos"] = summarize([e for e in g if e.filed > IN_SAMPLE_END], PRIMARY, bounds[PRIMARY])
            slices[name][label] = row
            if "p" in row[str(PRIMARY)] and row[str(PRIMARY)]["n"] >= 100:
                pvals[f"{name}|{label}"] = row[str(PRIMARY)]["p"]
        echo(f"  sliced by {name}")
    adjusted = holm(pvals)
    for key, p in adjusted.items():
        name, label = key.split("|", 1)
        slices[name][label][str(PRIMARY)]["p_holm"] = p
    result["slices"] = slices

    liquid = [e for e in priced if e.liquid]
    strategies = {}
    for key, (desc, pred) in STRATEGIES.items():
        sel = [e for e in liquid if pred(e)]
        strategies[key] = {
            "description": desc,
            "events": {str(h): summarize(sel, h, bounds[h], boot=500 if h == PRIMARY else 0) for h in (5, 21, 63, 126, 252)},
            "is": summarize([e for e in sel if e.filed <= IN_SAMPLE_END], PRIMARY, bounds[PRIMARY], boot=300),
            "oos": summarize([e for e in sel if e.filed > IN_SAMPLE_END], PRIMARY, bounds[PRIMARY], boot=300),
            "portfolio": {str(h): simulate(sel, cal, h) for h in (21, 63)},
        }
        echo(f"  strategy {key}: {len(sel)} buys")
    result["strategies"] = strategies
    result["walk_forward"] = walk_forward(priced, bounds[PRIMARY])
    result["best_insiders"] = best_insiders(priced, bounds[PRIMARY])
    return result


def best_insiders(evs: list[Ev], bounds, min_buys: int = 5, top: int = 50) -> list[dict]:
    """Insiders with the best record of buys beating SPY over the following quarter."""
    lo, hi = bounds
    by_owner: dict[str, list[Ev]] = defaultdict(list)
    for e in evs:
        if PRIMARY in e.abn and not e.buy.plan_purchase:
            by_owner[e.buy.owner_cik].append(e)
    rows = []
    for owner, g in by_owner.items():
        if len(g) < min_buys:
            continue
        a = [min(max(e.abn[PRIMARY], lo), hi) for e in g]
        mean = sum(a) / len(a)
        sd = statistics.stdev(a) if len(a) > 1 else 0.0
        last = max(g, key=lambda e: e.filed)
        rows.append({
            "owner_cik": owner, "name": last.buy.owner_name, "role": last.buy.officer_title or last.buy.role,
            "buys": len(g), "mean_abn": mean, "hit": sum(1 for x in a if x > 0) / len(a),
            "t": mean / (sd / math.sqrt(len(a))) if sd > 0 else 0.0,
            "tickers": sorted({e.symbol or e.buy.ticker for e in g})[:6], "last_buy": last.filed,
        })
    rows.sort(key=lambda r: (r["t"], r["mean_abn"]), reverse=True)
    return rows[:top]
