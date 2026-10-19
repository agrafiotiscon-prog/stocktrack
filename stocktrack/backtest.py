"""Event study and portfolio backtest of insider purchases, 2006 onward.

How it stays honest (see vault/Methodology.md for the full list):

* Entry is the OPEN of the first trading day after the filing date, the first
  price anyone could trade once the purchase was public. Variant "C" enters a
  full session later, at that day's close; a finding must survive both.
* Horizons count market sessions on SPY's calendar. Exits use the stock's last
  close within 10 sessions; staler (halted, delisted) means no return, and
  windows that run past the data are censored, never partial.
* Abnormal return = stock minus SPY over the same window. A second benchmark,
  the equal-weighted average of every surviving stock we can price, measures
  how much of any edge is just "survived to today" plus a small-cap tilt.
* Each filing is checked against the market: the insider's price must be within
  0.67-1.5x of the stock's close on the trade date, or the price series is
  presumed to be the wrong security (or the filing a typo) and dropped.
* Every feature is point-in-time: clusters, track records and the
  routine/opportunistic split only use filings and outcomes public before entry.
  Bucket edges are fixed numbers, never sample quantiles.
* Several filings by one company on one day are one signal.
* Significance comes from calendar-time portfolios (one return per month,
  Newey-West t-stats, block bootstrap), never from treating overlapping events
  as independent. 2006-2015 is discovery, 2016 onward is holdout, and p-values
  get a Holm correction for the number of slices tested.
* Prices exist only for companies still listed today, so roughly half of all
  insider buys can't be priced. Coverage, a survivorship bound and the survivor
  benchmark are reported next to the results.
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
PATH_LEN = 126  # sessions of daily returns kept per event for portfolios
DISCOVERY_END = "2015-12-31"
MAX_ENTRY_DELAY = 5  # sessions after filing within which the stock must trade
MAX_STALE = 10  # sessions an exit price may be stale
PRICE_RATIO = (0.67, 1.5)  # insider price / market close on trade date
STUDY_MIN_PRICE, STUDY_MIN_ADV = 1.0, 100_000
SIM_MIN_PRICE, SIM_MIN_ADV = 2.0, 1_000_000
CLUSTER_DAYS = 14
TRACK_MIN = 3
TRACK_CLIP = 1.0  # fixed clip for track-record returns (no sample quantiles)
MIN_SIGNALS, MIN_MONTHS = 200, 60  # minimum data in discovery before a slice is tested
CRISIS = (("2008-09", "2009-06"), ("2020-03", "2020-06"))
SEED = 20061


@dataclass(slots=True)
class Ev:
    buy: BuyEvent
    filed: str
    symbol: str | None = None
    resolve: str = ""
    status: str = "unpriced"  # priced / unlisted / reused / no_history / price_mismatch / no_entry_bar / unverified
    entry_date: str | None = None
    entry_cal: int = -1
    price: float | None = None  # raw close before entry
    adv: float | None = None  # 20-session average dollar volume before entry
    price_ratio: float | None = None
    prior_ret: float | None = None  # 63 sessions before entry
    pre_drift: float | None = None  # trade-date close to entry open (not tradable)
    ret: dict = field(default_factory=dict)
    abn: dict = field(default_factory=dict)  # vs SPY, entry at open
    abn_c: dict = field(default_factory=dict)  # vs SPY, entry at close (variant C)
    abn_ew: dict = field(default_factory=dict)  # vs survivor equal-weight index
    exit_cal: dict = field(default_factory=dict)
    placebo: float | None = None  # same stock, a year earlier, 63-session AR
    path: array | None = None
    cluster: int = 1
    kind: str = "unclassified"
    track_n: int = 0
    track: float | None = None  # shrunk mean of past 63-session ARs
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
        return self.buy.value

    @property
    def priced(self) -> bool:
        return self.status == "priced"

    @property
    def in_study(self) -> bool:
        return self.priced and (self.price or 0) >= STUDY_MIN_PRICE and (self.adv or 0) >= STUDY_MIN_ADV

    @property
    def liquid(self) -> bool:
        return self.priced and (self.price or 0) >= SIM_MIN_PRICE and (self.adv or 0) >= SIM_MIN_ADV

    @property
    def issuer_day(self) -> tuple[str, str]:
        return self.buy.issuer_cik, self.entry_date or self.filed


# --- market data ---------------------------------------------------------


class Calendar:
    def __init__(self, spy: PriceHistory) -> None:
        self.spy = spy
        self.dates = spy.dates
        self.index = {d: i for i, d in enumerate(spy.dates)}
        self.daily = [0.0] + [spy.close[i] / spy.close[i - 1] - 1 for i in range(1, len(spy.dates))]
        self.ew_daily = [0.0] * len(spy.dates)  # survivor equal-weight index, filled by build_events
        self.ew_level: list[float] = []

    def first_after(self, day: str) -> int:
        return bisect.bisect_right(self.dates, day)

    def finish_ew(self, sums: list[float], counts: list[int]) -> None:
        self.ew_daily = [s / n if n else 0.0 for s, n in zip(sums, counts)]
        level, self.ew_level = 1.0, []
        for r in self.ew_daily:
            level *= 1 + r
            self.ew_level.append(level)

    def ew_return(self, c_from: int, c_to: int) -> float:
        """Survivor index from the close before c_from to the close of c_to."""
        base = self.ew_level[c_from - 1] if c_from >= 1 else 1.0
        return self.ew_level[c_to] / base - 1


def align(hist: PriceHistory, cal: Calendar) -> tuple[PriceHistory, int]:
    """Keep bars on benchmark trading days and drop isolated bad ticks.

    A bad tick is a close that jumps more than +300% and reverses more than 75%
    on the next bar (or the mirror image), or a raw price under one cent.
    Returns the cleaned history and the number of bars repaired.
    """
    keep = [k for k, d in enumerate(hist.dates) if d in cal.index and hist.raw_close[k] >= 0.01]
    repaired = len([k for k, d in enumerate(hist.dates) if d in cal.index]) - len(keep)
    clean: list[int] = []
    for pos, k in enumerate(keep):
        if clean and pos + 1 < len(keep):
            prev, nxt = hist.close[clean[-1]], hist.close[keep[pos + 1]]
            up, down = hist.close[k] / prev - 1, nxt / hist.close[k] - 1
            if (up > 3.0 and down < -0.75) or (up < -0.75 and down > 3.0):
                repaired += 1
                continue
        clean.append(k)
    if len(clean) == len(hist.dates):
        return hist, 0
    return PriceHistory(hist.symbol, [hist.dates[k] for k in clean], [hist.open[k] for k in clean],
                        [hist.close[k] for k in clean], [hist.dollar_volume_day[k] for k in clean],
                        [hist.raw_close[k] for k in clean]), repaired


def _exit_bar(cals: list[int], c_exit: int, lo: int) -> int | None:
    j = bisect.bisect_right(cals, c_exit, lo=lo) - 1
    if j < lo or c_exit - cals[j] > MAX_STALE:
        return None
    return j


def attach_market_data(ev: Ev, hist: PriceHistory, cal: Calendar, verify: bool = True) -> None:
    """Price check, entry, forward returns and the portfolio path for one event.

    `hist` must come from align(). Sets ev.status to "priced" on success.
    """
    b = ev.buy
    cals = [cal.index[d] for d in hist.dates]

    # Does the insider's price match this stock's market price on the trade date?
    ti = hist.index_on_or_before(b.last_date) if b.last_date else None
    verified = False
    if ti is not None and b.avg_price:
        trade_cal = bisect.bisect_right(cal.dates, b.last_date) - 1
        if trade_cal - cals[ti] <= MAX_ENTRY_DELAY:
            ev.price_ratio = b.avg_price / hist.raw_close[ti]
            if verify and not PRICE_RATIO[0] <= ev.price_ratio <= PRICE_RATIO[1]:
                ev.status = "price_mismatch"
                return
            verified = True
    if verify and not verified:
        ev.status = "unverified"
        return

    first = cal.first_after(ev.filed)
    i = bisect.bisect_left(cals, first)
    if i >= len(cals) or cals[i] - first > MAX_ENTRY_DELAY:
        ev.status = "no_entry_bar"
        return
    c_entry = cals[i]
    ev.status, ev.entry_date, ev.entry_cal = "priced", hist.dates[i], c_entry
    entry_open, entry_close = hist.open[i], hist.close[i]
    if i >= 1:
        ev.price = hist.raw_close[i - 1]
        ev.adv = hist.dollar_volume(i, 20)
    if i >= 64:
        ev.prior_ret = hist.close[i - 1] / hist.close[i - 64] - 1
    if ti is not None and ti < i:
        ev.pre_drift = entry_open / hist.close[ti] - 1

    for h in HORIZONS:
        c_exit = c_entry + h - 1
        if c_exit >= len(cal.dates):
            break  # censored: not enough data yet
        j = _exit_bar(cals, c_exit, i)
        if j is None:
            break  # stopped trading
        r = hist.close[j] / entry_open - 1
        ev.ret[h], ev.exit_cal[h] = r, c_exit
        ev.abn[h] = r - (cal.spy.close[c_exit] / cal.spy.open[c_entry] - 1)
        if h > 1:
            ev.abn_c[h] = (hist.close[j] / entry_close - 1) - (cal.spy.close[c_exit] / cal.spy.close[c_entry] - 1)

    path = array("f")
    prev_close, last_bar_cal, j = entry_open, c_entry, i
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


def placebo_ar(hist: PriceHistory, cal: Calendar, c_entry: int) -> float | None:
    """63-session AR for the same stock entered at calendar index c_entry."""
    cals = [cal.index[d] for d in hist.dates]
    i = bisect.bisect_left(cals, c_entry)
    if i >= len(cals) or cals[i] - c_entry > MAX_ENTRY_DELAY:
        return None
    c0, c_exit = cals[i], cals[i] + PRIMARY - 1
    if c_exit >= len(cal.dates):
        return None
    j = _exit_bar(cals, c_exit, i)
    if j is None:
        return None
    return (hist.close[j] / hist.open[i] - 1) - (cal.spy.close[c_exit] / cal.spy.open[c0] - 1)


def _add_to_ew(hist: PriceHistory, cal: Calendar, sums: list[float], counts: list[int]) -> None:
    cals = [cal.index[d] for d in hist.dates]
    window, total = 20, 0.0
    for k in range(1, len(cals)):
        total += hist.dollar_volume_day[k - 1]
        if k > window:
            total -= hist.dollar_volume_day[k - 1 - window]
        if cals[k] != cals[k - 1] + 1 or hist.raw_close[k - 1] < STUDY_MIN_PRICE:
            continue
        if k >= window and total / window >= STUDY_MIN_ADV:
            sums[cals[k]] += hist.close[k] / hist.close[k - 1] - 1
            counts[cals[k]] += 1


def build_events(buys: Iterable[BuyEvent], store: PriceStore, tickers: TickerMap,
                 progress: Callable[[int, int], None] | None = None) -> tuple[list[Ev], Calendar, dict]:
    spy = store.load(BENCHMARK)
    if spy is None:
        raise RuntimeError("no SPY history; fetch prices first")
    cal = Calendar(spy)
    ordered = sorted((b for b in buys if b.filed_at), key=lambda b: (b.filed_at[:10], b.accession))
    deduped = dedupe_purchases(ordered)
    evs = [Ev(buy=b, filed=b.filed_at[:10]) for b in deduped]
    meta = {"filings": len(ordered), "duplicate_filings": len(ordered) - len(deduped), "bars_repaired": 0}
    by_symbol: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        ev.symbol, ev.resolve = tickers.resolve(ev.buy.issuer_cik, ev.buy.ticker)
        if ev.symbol:
            by_symbol[ev.symbol].append(ev)
        else:
            ev.status = ev.resolve  # unlisted / reused
    sums, counts = [0.0] * len(cal.dates), [0] * len(cal.dates)
    for n, (sym, group) in enumerate(sorted(by_symbol.items()), 1):
        raw = store.load(sym)
        if raw is None:
            for ev in group:
                ev.status = "no_history"
            continue
        hist, repaired = align(raw, cal)
        meta["bars_repaired"] += repaired
        if not hist.dates:
            continue
        _add_to_ew(hist, cal, sums, counts)
        for ev in group:
            attach_market_data(ev, hist, cal)
        entries = sorted(ev.entry_cal for ev in group if ev.priced)
        for ev in group:
            if ev.priced:
                p = ev.entry_cal - 252
                k = bisect.bisect_left(entries, p - 63)
                if p > 0 and not (k < len(entries) and entries[k] <= p + 63):
                    ev.placebo = placebo_ar(hist, cal, p)
        if progress:
            progress(n, len(by_symbol))
    cal.finish_ew(sums, counts)
    for ev in evs:
        for h, c_exit in ev.exit_cal.items():
            ev.abn_ew[h] = ev.ret[h] - cal.ew_return(ev.entry_cal, c_exit)
    return evs, cal, meta


# --- point-in-time features ----------------------------------------------


def add_pit_features(evs: list[Ev]) -> None:
    """Cluster size, routine/opportunistic, track record and novelty from earlier filings only."""
    by_day: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        by_day[ev.filed].append(ev)

    issuer_recent: dict[str, list[Ev]] = defaultdict(list)
    months: dict[str, dict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    last_owner: dict[str, str] = {}
    last_issuer: dict[str, str] = {}
    pending: list[tuple[int, int, str, float]] = []  # (exit calendar index, seq, owner, ar63)
    track: dict[str, list[float]] = defaultdict(lambda: [0, 0.0])
    seq = 0

    for day in sorted(by_day):
        todays = by_day[day]
        entry = min((e.entry_cal for e in todays if e.entry_cal >= 0), default=None)
        # Outcomes that closed before this day's entry are public and usable.
        while pending and entry is not None and pending[0][0] < entry:
            _, _, owner, ar = heapq.heappop(pending)
            track[owner][0] += 1
            track[owner][1] += ar
        for ev in todays:
            if ev.buy.counts_toward_cluster:
                issuer_recent[ev.buy.issuer_cik].append(ev)
        cutoff = (dt.date.fromisoformat(day) - dt.timedelta(days=60)).isoformat()
        for ev in todays:
            b = ev.buy
            peers = issuer_recent[b.issuer_cik]
            while peers and peers[0].filed < cutoff:
                peers.pop(0)
            near = [p.buy for p in peers if p is not ev and _days_apart(p.buy.last_date, b.last_date) <= CLUSTER_DAYS]
            ev.cluster = len({x.owner_cik for x in dedupe_purchases([b, *near])})

            n, total = track[b.owner_cik]
            ev.track_n = int(n)
            ev.track = (n / (n + 5)) * (total / n) if n else None

            year, month = int((b.first_date or day)[:4]), int((b.first_date or day)[5:7])
            hist = months[b.owner_cik]
            prior = [hist.get(year - k, set()) for k in (1, 2, 3)]
            if all(prior):
                ev.kind = "routine" if all(month in p for p in prior) else "opportunistic"
            ev.first_in_year_insider = _days_apart(last_owner.get(b.owner_cik, ""), day) > 365
            ev.first_in_year_issuer = _days_apart(last_issuer.get(b.issuer_cik, ""), day) > 365
            ev.score = score_buy(b, ev.cluster).total
        for ev in todays:
            b = ev.buy
            months[b.owner_cik][int((b.first_date or day)[:4])].add(int((b.first_date or day)[5:7]))
            last_owner[b.owner_cik] = day
            last_issuer[b.issuer_cik] = day
            if PRIMARY in ev.abn:
                seq += 1
                ar = max(-TRACK_CLIP, min(TRACK_CLIP, ev.abn[PRIMARY]))
                heapq.heappush(pending, (ev.exit_cal[PRIMARY], seq, b.owner_cik, ar))


def _days_apart(a: str, b: str) -> int:
    try:
        return abs((dt.date.fromisoformat(a) - dt.date.fromisoformat(b)).days)
    except ValueError:
        return 10**6


# --- statistics --------------------------------------------------------------


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
    return math.erfc(abs(t) / math.sqrt(2))


def unique_signals(evs: Iterable[Ev]) -> list[Ev]:
    """One event per company per entry day (several filings the same day share one return)."""
    seen, out = set(), []
    for ev in evs:
        if ev.issuer_day not in seen:
            seen.add(ev.issuer_day)
            out.append(ev)
    return out


def event_stats(evs: list[Ev], h: int, bounds: tuple[float, float], key: str = "abn",
                boot: int = 0, seed: int = SEED) -> dict:
    """Event-level averages; CIs from a bootstrap that resamples whole months."""
    lo, hi = bounds
    pts = [(ev.month, min(max(getattr(ev, key)[h], lo), hi), ev.ret.get(h), getattr(ev, key)[h])
           for ev in unique_signals(evs) if h in getattr(ev, key)]
    if not pts:
        return {"n": 0}
    vals = sorted(a for _, a, _, _ in pts)
    out = {"n": len(pts), "mean": sum(vals) / len(vals), "median": percentile(vals, 0.5),
           "hit": sum(1 for a in vals if a > 0) / len(vals), "raw_mean": sum(r for *_, r in pts) / len(pts)}
    if boot:
        by_month: dict[str, list[float]] = defaultdict(lambda: [0.0, 0])
        for m, a, _, _ in pts:
            by_month[m][0] += a
            by_month[m][1] += 1
        groups = list(by_month.values())
        if len(groups) >= 12:
            rng = random.Random(seed)
            means = []
            for _ in range(boot):
                draw = rng.choices(groups, k=len(groups))
                means.append(sum(g[0] for g in draw) / sum(g[1] for g in draw))
            means.sort()
            out["ci"] = [percentile(means, 0.025), percentile(means, 0.975)]
    return out


def newey_west_t(x: list[float], lags: int = 3) -> tuple[float, float]:
    """(mean, t-stat) with Newey-West standard errors."""
    t_len = len(x)
    if t_len < lags + 2:
        return (sum(x) / t_len if t_len else 0.0), 0.0
    mean = sum(x) / t_len
    d = [v - mean for v in x]
    g = [sum(d[t] * d[t - lag] for t in range(lag, t_len)) / t_len for lag in range(lags + 1)]
    var = g[0] + 2 * sum((1 - lag / (lags + 1)) * g[lag] for lag in range(1, lags + 1))
    se = math.sqrt(max(var, 1e-18) / t_len)
    return mean, mean / se


def block_bootstrap(x: list[float], draws: int = 2000, block: int = 6, seed: int = SEED) -> dict:
    t_len = len(x)
    if t_len < 2 * block:
        return {}
    rng = random.Random(seed)
    nblocks = math.ceil(t_len / block)
    means = []
    for _ in range(draws):
        sample: list[float] = []
        for _ in range(nblocks):
            s = rng.randrange(0, t_len - block + 1)
            sample.extend(x[s:s + block])
        sample = sample[:t_len]
        means.append(sum(sample) / t_len)
    means.sort()
    share_le = sum(1 for m in means if m <= 0) / draws
    return {"ci": [percentile(means, 0.025), percentile(means, 0.975)],
            "p_boot": min(1.0, 2 * min(share_le, 1 - share_le))}


def ols(y: list[float], x: list[float]) -> tuple[float, float]:
    """(alpha, beta) of y on x."""
    n = len(y)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    beta = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx if sxx else 0.0
    return my - beta * mx, beta


def holm(pvals: dict[str, float]) -> dict[str, float]:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, running, out = len(items), 0.0, {}
    for k, (key, p) in enumerate(items):
        running = max(running, min(1.0, (m - k) * p))
        out[key] = running
    return out


# --- calendar-time portfolios -------------------------------------------------


def calendar_time(evs: list[Ev], cal: Calendar, hold: int = PRIMARY, min_positions: float = 5) -> dict:
    """Monthly returns of a portfolio holding every signal for `hold` sessions.

    Buy-and-hold weights (each position starts at 1 and drifts with its price),
    each company held once at a time. Months averaging fewer than
    `min_positions` positions are dropped.
    """
    n = len(cal.dates)
    num, den, cnt = [0.0] * n, [0.0] * n, [0] * n
    held_until: dict[str, int] = {}
    for ev in sorted((e for e in evs if e.path is not None and len(e.path)), key=lambda e: e.entry_cal):
        c0 = ev.entry_cal
        if held_until.get(ev.buy.issuer_cik, -1) >= c0:
            continue
        steps = min(hold, len(ev.path))
        held_until[ev.buy.issuer_cik] = c0 + steps - 1
        v = 1.0
        for k in range(steps):
            r = ev.path[k]
            num[c0 + k] += v * r
            den[c0 + k] += v
            cnt[c0 + k] += 1
            v *= 1 + r
    months: dict[str, list] = {}
    for c in range(n):
        if den[c] <= 0:
            continue
        m = cal.dates[c][:7]
        acc = months.setdefault(m, [1.0, 1.0, 0, 0])
        acc[0] *= 1 + num[c] / den[c]
        acc[1] *= 1 + cal.daily[c]
        acc[2] += 1
        acc[3] += cnt[c]
    series = []
    dropped = 0
    for m in sorted(months):
        pr, sr, days, pos = months[m]
        if pos / days < min_positions:
            dropped += 1
            continue
        series.append((m, pr - 1, sr - 1))
    if cal.dates and series and series[-1][0] == cal.dates[-1][:7]:
        series.pop()  # incomplete final month
    return {"series": series, "dropped_months": dropped}


def ctp_stats(series: list[tuple[str, float, float]], boot: int = 2000) -> dict:
    if len(series) < 6:
        return {"months": len(series)}
    excess = [p - s for _, p, s in series]
    mean, t = newey_west_t(excess)
    alpha, beta = ols([p for _, p, _ in series], [s for _, _, s in series])
    years: dict[str, list[float]] = defaultdict(list)
    for (m, p, s), x in zip(series, excess):
        years[m[:4]].append(x)
    by_year = {y: sum(v) for y, v in years.items()}
    out = {"months": len(series), "excess_mean": mean, "t": t, "p": p_value(t),
           "alpha": alpha, "beta": beta, "annualized": (1 + mean) ** 12 - 1,
           "years_positive": sum(1 for v in by_year.values() if v > 0) / len(by_year), "by_year": by_year}
    out.update(block_bootstrap(excess, draws=boot))
    crisis = [x for (m, _, _), x in zip(series, excess) if any(a <= m <= b for a, b in CRISIS)]
    total = sum(excess)
    out["crisis_share"] = sum(crisis) / total if total else 0.0
    return out


def split_series(series, end: str = DISCOVERY_END[:7]):
    return [r for r in series if r[0] <= end], [r for r in series if r[0] > end]


def difference_series(a, b):
    """Monthly (A - B) over months both portfolios cover, as a series ctp_stats can test."""
    bm = {m: p for m, p, _ in b}
    return [(m, p - bm[m], 0.0) for m, p, _ in a if m in bm]


# --- features --------------------------------------------------------------------


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
    return _bucket(inc, [(0.05, "<5%"), (0.25, "5-25%"), (1.0, "25-100%"), (math.inf, "100%+")])


ROLE_GROUP = {"CEO": "CEO", "CFO": "CFO", "President": "President/Chair", "Chair": "President/Chair",
              "C-Suite": "Other exec", "Officer": "Other exec", "Director": "Director",
              "10% Owner": "10% owner", "Other": "Other"}

# Pre-registered slices: fixed bucket edges, written down before the first run.
FEATURES: dict[str, Callable[[Ev], str]] = {
    "role": lambda e: ROLE_GROUP.get(e.buy.role, "Other"),
    "value": lambda e: _bucket(e.value, [(25e3, "<$25K"), (100e3, "$25-100K"), (250e3, "$100-250K"),
                                        (1e6, "$250K-1M"), (math.inf, "$1M+")]),
    "stake_increase": _stake,
    "cluster": lambda e: {1: "1 insider", 2: "2 insiders"}.get(e.cluster, "3+ insiders"),
    "insider_type": lambda e: e.kind,
    "track_record": lambda e: "none" if e.track_n < TRACK_MIN or e.track is None
    else ("good" if e.track >= 0 else "poor"),
    "prior_3m_return": lambda e: _bucket(e.prior_ret, [(-0.3, "down 30%+"), (-0.1, "down 10-30%"),
                                                       (0.1, "flat"), (0.3, "up 10-30%"), (math.inf, "up 30%+")]),
    "price": lambda e: _bucket(e.price, [(5, "$1-5"), (20, "$5-20"), (math.inf, "$20+")]),
    "liquidity": lambda e: _bucket(e.adv, [(1e6, "$100K-1M/day"), (1e7, "$1-10M/day"),
                                           (1e8, "$10-100M/day"), (math.inf, "$100M+/day")]),
    "score": lambda e: _bucket(e.score, [(20, "0-19"), (40, "20-39"), (60, "40-59"), (80, "60-79"),
                                         (101, "80+")]),
    "plan_purchase": lambda e: "DRIP/plan" if e.buy.plan_purchase else "discretionary",
    "filing_delay": lambda e: _bucket(e.buy.filing_delay_days, [(3, "0-2 days"), (11, "3-10 days"),
                                                                (math.inf, "11+ days")]),
    "insider_novelty": lambda e: "first buy in 12m" if e.first_in_year_insider else "repeat buyer",
    "company_novelty": lambda e: "first insider buy in 12m" if e.first_in_year_issuer else "recent insider buys",
}

FEATURE_NOTES = {
    "insider_type": "Cohen-Malloy-Pomorski classification computed from purchases only (sales aren't loaded); "
                    "classifiable from 2009.",
    "track_record": f"Shrunk mean of the insider's earlier 63-session abnormal returns known before entry, "
                    f"n/(n+5) x mean; needs {TRACK_MIN}+ earlier outcomes.",
    "price": "Raw share price the day before entry; sub-$1 stocks are outside the study sample.",
    "liquidity": "Average daily dollar volume over the 20 sessions before entry.",
}

STRATEGIES: dict[str, tuple[str, Callable[[Ev], bool]]] = {
    "all_liquid": ("Every discretionary insider buy", lambda e: not e.buy.plan_purchase),
    "score_40": ("Live score 40+ (notable)", lambda e: e.score >= 40 and not e.buy.plan_purchase),
    "score_60": ("Live score 60+ (strong)", lambda e: e.score >= 60 and not e.buy.plan_purchase),
    "ceo_cfo_100k": ("CEO or CFO buying $100K+", lambda e: e.buy.role in ("CEO", "CFO") and e.value >= 1e5
                     and not e.buy.plan_purchase),
    "cluster_3": ("3+ insiders buying within 14 days", lambda e: e.cluster >= 3),
    "opportunistic": ("Opportunistic insiders (Cohen-Malloy-Pomorski)", lambda e: e.kind == "opportunistic"
                      and not e.buy.plan_purchase),
    "contrarian": ("Insider buying after a 30%+ drop", lambda e: (e.prior_ret or 0) <= -0.3
                   and not e.buy.plan_purchase),
    "proven_insider": ("Insiders whose earlier buys beat SPY", lambda e: e.track_n >= TRACK_MIN
                       and (e.track or 0) > 0 and not e.buy.plan_purchase),
    "big_stake_up": ("Exec/director growing stake 25%+ with $100K+", lambda e: e.buy.role not in ("10% Owner", "Other")
                     and (e.buy.stake_increase or 0) >= 0.25 and e.value >= 1e5 and not e.buy.plan_purchase),
    "first_buy_exec": ("Exec's first buy in a year, $50K+", lambda e: e.first_in_year_insider
                       and e.buy.role in ("CEO", "CFO", "President", "Chair", "C-Suite") and e.value >= 5e4
                       and not e.buy.plan_purchase),
}


# --- portfolio simulation ------------------------------------------------------------


def cost_per_side(price: float | None, adv: float | None, size: float = 0.0) -> float:
    p = price or 0
    c = 0.01 if p < 5 else 0.005 if p < 10 else 0.0025 if p < 25 else 0.001
    if (adv or 0) < 5e6:
        c += 0.0025
    if adv and size > 0.01 * adv:
        c += 0.0025
    return c


def simulate(evs: list[Ev], cal: Calendar, hold: int = PRIMARY, slots: int = 20, nav0: float = 100_000.0,
             cost_mult: float = 1.0, rf_daily: list[float] | None = None) -> dict:
    """$100K, `slots` positions, each signal bought at the next open and held `hold` sessions.

    When more signals arrive than free slots, the highest scores win. Size is
    NAV/slots, capped by cash and 2% of the stock's daily dollar volume.
    """
    n = len(cal.dates)
    todo: dict[int, list[Ev]] = defaultdict(list)
    for e in evs:
        if e.path is not None and len(e.path) and e.liquid:
            todo[e.entry_cal].append(e)
    if not todo:
        return {"trades": 0}
    start = min(todo)
    cash, nav = nav0, nav0
    open_pos: list[list] = []  # [ev, value, step, steps]
    held: set[str] = set()
    navs, trades, skipped, costs_paid, positions_sum = [], 0, 0, 0.0, 0
    for c in range(start, n):
        # entries at the open
        cands = sorted(todo.get(c, []), key=lambda e: (-e.score, -e.value, e.buy.accession))
        for e in cands:
            if len(open_pos) >= slots:
                skipped += 1
                continue
            if e.buy.issuer_cik in held:
                continue
            size = min(nav / slots, cash, 0.02 * (e.adv or 0))
            if size <= 1:
                skipped += 1
                continue
            fee = size * cost_per_side(e.price, e.adv, size) * cost_mult
            cash -= size
            costs_paid += fee
            open_pos.append([e, size - fee, 0, min(hold, len(e.path))])
            held.add(e.buy.issuer_cik)
            trades += 1
        # mark to market, exits at the close
        still = []
        for pos in open_pos:
            e, value, step, steps = pos
            value *= 1 + e.path[step]
            step += 1
            if step >= steps:
                fee = value * cost_per_side(e.price, e.adv, value) * cost_mult
                cash += value - fee
                costs_paid += fee
                held.discard(e.buy.issuer_cik)
            else:
                still.append([e, value, step, steps])
        open_pos = still
        if rf_daily:
            cash *= 1 + rf_daily[c]
        nav = cash + sum(p[1] for p in open_pos)
        navs.append(nav)
        positions_sum += len(open_pos)
    daily = [navs[0] / nav0 - 1] + [navs[k] / navs[k - 1] - 1 for k in range(1, len(navs))]
    spy = cal.daily[start:n]
    out = {"trades": trades, "skipped": skipped, "start": cal.dates[start], "end": cal.dates[-1],
           "avg_positions": positions_sum / len(navs), "final_nav": navs[-1],
           "costs_pct_nav_per_year": costs_paid / (sum(navs) / len(navs)) / (len(navs) / 252)}
    out.update({f"strategy_{k}": v for k, v in perf(daily, rf_daily[start:n] if rf_daily else None).items()})
    out.update({f"spy_{k}": v for k, v in perf(spy, rf_daily[start:n] if rf_daily else None).items()})
    alpha, beta = ols(daily, spy)
    out["beta"], out["alpha_annual"] = beta, alpha * 252
    active = [a - b for a, b in zip(daily, spy)]
    sd = statistics.pstdev(active)
    out["information_ratio"] = (sum(active) / len(active)) / sd * math.sqrt(252) if sd else 0.0
    years: dict[str, list[list[float]]] = defaultdict(lambda: [[], []])
    for c, r, s in zip(range(start, n), daily, spy):
        years[cal.dates[c][:4]][0].append(r)
        years[cal.dates[c][:4]][1].append(s)
    out["by_year"] = {y: {"strategy": _compound(a), "spy": _compound(b)} for y, (a, b) in sorted(years.items())}
    out["years_beating_spy"] = sum(1 for v in out["by_year"].values() if v["strategy"] > v["spy"]) / len(out["by_year"])
    # monthly NAV for equity-curve charts
    curve, spy_level = {}, 1.0
    for c, v, s in zip(range(start, n), navs, spy):
        spy_level *= 1 + s
        curve[cal.dates[c][:7]] = (v / nav0, spy_level)
    out["curve"] = [[m, round(a, 4), round(b, 4)] for m, (a, b) in curve.items()]
    return out


def _compound(rets: list[float]) -> float:
    v = 1.0
    for r in rets:
        v *= 1 + r
    return v - 1


def perf(daily: list[float], rf: list[float] | None = None) -> dict:
    if len(daily) < 2:
        return {}
    equity, peak, mdd = 1.0, 1.0, 0.0
    for r in daily:
        equity *= 1 + r
        peak = max(peak, equity)
        mdd = min(mdd, equity / peak - 1)
    days = len(daily) * 365.25 / 252
    sd = statistics.pstdev(daily)
    ex = [r - (rf[k] if rf else 0.0) for k, r in enumerate(daily)]
    return {"total": equity - 1, "cagr": equity ** (365.25 / days) - 1 if equity > 0 else -1.0,
            "vol": sd * math.sqrt(252), "sharpe": (sum(ex) / len(ex)) * 252 / (sd * math.sqrt(252)) if sd else 0.0,
            "max_drawdown": -mdd}


# --- the run ----------------------------------------------------------------------


def coverage(evs: list[Ev]) -> dict:
    years: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    reasons: dict[str, int] = defaultdict(int)
    for ev in evs:
        y = years[ev.filed[:4]]
        y["signals"] += 1
        y["priced"] += ev.priced
        y["in_study"] += ev.in_study
        y[f"has_{PRIMARY}d"] += PRIMARY in ev.abn and ev.in_study
        reasons[ev.status] += 1
    for y in years.values():
        y["coverage"] = y["priced"] / y["signals"] if y["signals"] else 0.0
    return {"by_year": {k: dict(v) for k, v in sorted(years.items())}, "status": dict(reasons)}


def survivorship_bound(evs: list[Ev], bounds) -> dict:
    """Headline mean AR63 if the unpriced signals had done like the median / 10th percentile priced one."""
    lo, hi = bounds
    pool = [e for e in evs if is_listed_stock(e.buy.ticker) and not e.buy.plan_purchase]
    priced = sorted(min(max(e.abn[PRIMARY], lo), hi) for e in unique_signals(pool) if e.in_study and PRIMARY in e.abn)
    unpriced = len(unique_signals([e for e in pool if not e.priced and e.filed < "2025-07-01"]))
    if not priced:
        return {}
    mean = sum(priced) / len(priced)
    med, p10 = percentile(priced, 0.5), percentile(priced, 0.1)
    total = len(priced) + unpriced
    return {"reported": mean, "neutral": (mean * len(priced) + med * unpriced) / total,
            "pessimistic": (mean * len(priced) + p10 * unpriced) / total,
            "priced": len(priced), "unpriced": unpriced}


def slice_report(groups: dict[str, list[Ev]], base_series, cal: Calendar, bounds: dict) -> dict:
    out = {}
    for label, g in sorted(groups.items()):
        sig = unique_signals(g)
        disc = [e for e in sig if e.filed <= DISCOVERY_END]
        ct = calendar_time(sig, cal)
        d_ser, h_ser = split_series(ct["series"])
        row = {
            "signals": len(sig),
            "events": {str(h): event_stats(sig, h, bounds[h], boot=1000 if h == PRIMARY else 0)
                       for h in (5, 21, 63, 126, 252)},
            "variant_c": event_stats(sig, PRIMARY, bounds[PRIMARY], key="abn_c"),
            "vs_survivors": event_stats(sig, PRIMARY, bounds[PRIMARY], key="abn_ew"),
            "ctp": ctp_stats(ct["series"]),
            "discovery": ctp_stats(d_ser, boot=1000),
            "holdout": ctp_stats(h_ser, boot=1000),
            "vs_all_buys": ctp_stats(difference_series(ct["series"], base_series), boot=1000),
            "enough_data": len(disc) >= MIN_SIGNALS and len(d_ser) >= MIN_MONTHS,
        }
        out[label] = row
    return out


def verdicts(slices: dict) -> None:
    """Label each slice with the pre-registered verdict rule (mutates `slices`)."""
    disc_p = {}
    for feat, rows in slices.items():
        for label, r in rows.items():
            if r["enough_data"] and "p" in r["discovery"]:
                disc_p[f"{feat}|{label}"] = r["discovery"]["p"]
    disc_adj = holm(disc_p)
    passed = {k for k, p in disc_adj.items()
              if p < 0.05 and slices[k.split("|")[0]][k.split("|", 1)[1]]["discovery"]["excess_mean"] > 0}
    hurt = {k for k, p in disc_adj.items()
            if p < 0.05 and slices[k.split("|")[0]][k.split("|", 1)[1]]["discovery"]["excess_mean"] < 0}
    hold_adj = holm({k: slices[k.split("|")[0]][k.split("|", 1)[1]]["holdout"].get("p", 1.0) for k in passed | hurt})
    diff_p = {}
    for feat, rows in slices.items():
        for label, r in rows.items():
            if r["enough_data"] and "p" in r["vs_all_buys"]:
                diff_p[f"{feat}|{label}"] = r["vs_all_buys"]["p"]
    diff_adj = holm(diff_p)
    for feat, rows in slices.items():
        for label, r in rows.items():
            key = f"{feat}|{label}"
            r["p_holm_discovery"] = disc_adj.get(key)
            r["p_holm_holdout"] = hold_adj.get(key)
            r["p_holm_vs_all"] = diff_adj.get(key)
            if not r["enough_data"]:
                r["verdict"] = "not enough data"
                continue
            h = r["holdout"]
            same_sign_hold = key in hold_adj and hold_adj[key] < 0.05 and (
                h.get("excess_mean", 0) > 0) == (key in passed)
            c_ok = r["variant_c"].get("mean", 0) > 0
            ew_ok = r["vs_survivors"].get("mean", 0) > 0
            years_ok = r["ctp"].get("years_positive", 0) >= 0.6
            if key in passed and same_sign_hold and c_ok and ew_ok and years_ok:
                r["verdict"] = "works"
            elif key in hurt and same_sign_hold:
                r["verdict"] = "hurts"
            elif key in passed or (h.get("p", 1) < 0.05 and h.get("excess_mean", 0) > 0):
                r["verdict"] = "promising"
            elif key in hurt or (h.get("p", 1) < 0.05 and h.get("excess_mean", 0) < 0):
                r["verdict"] = "looks negative"
            else:
                r["verdict"] = "no evidence"
            vs = r["vs_all_buys"]
            if diff_adj.get(key, 1) < 0.05:
                r["vs_all_verdict"] = "better than typical" if vs.get("excess_mean", 0) > 0 else "worse than typical"
            else:
                r["vs_all_verdict"] = "no different"


def walk_forward(evs: list[Ev], cal: Calendar, thresholds=(40, 50, 60, 70), start_year: int = 2011) -> dict:
    """Each year, pick the score threshold whose calendar-time Sharpe was best on outcomes
    known by Jan 1, apply it unchanged to that year's signals, and join the years."""
    pool = [e for e in unique_signals(evs) if e.liquid and not e.buy.plan_purchase]
    # A calendar-time month's return is realized at month end, and its holdings
    # only include signals filed by then, so on Jan 1 of year Y every month
    # through December of Y-1 is known.
    full = {t: calendar_time([e for e in pool if e.score >= t], cal)["series"] for t in thresholds}
    chosen, picked = {}, []
    last_year = max((e.year for e in pool), default=start_year)
    for year in range(start_year, last_year + 1):
        known_through = f"{year - 1}-12"
        best, best_sharpe = thresholds[0], -math.inf
        for t in thresholds:
            ex = [p - s for m, p, s in full[t] if m <= known_through]
            if len(ex) >= 24:
                sd = statistics.pstdev(ex)
                sharpe = (sum(ex) / len(ex)) / sd if sd else 0.0
                if sharpe > best_sharpe:
                    best, best_sharpe = t, sharpe
        chosen[str(year)] = best
        picked.extend(e for e in pool if e.year == year and e.score >= best)
    ct = calendar_time(picked, cal)
    return {"thresholds": chosen, "signals": len(picked), "ctp": ctp_stats(ct["series"]),
            "events": event_stats(picked, PRIMARY, (-1e9, 1e9))}


def best_insiders(evs: list[Ev], bounds, min_buys: int = 5, top: int = 50) -> list[dict]:
    lo, hi = bounds
    by_owner: dict[str, list[Ev]] = defaultdict(list)
    for e in unique_signals(evs):
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
        rows.append({"owner_cik": owner, "name": last.buy.owner_name, "role": last.buy.officer_title or last.buy.role,
                     "buys": len(g), "mean_abn": mean, "hit": sum(1 for x in a if x > 0) / len(a),
                     "t": mean / (sd / math.sqrt(len(a))) if sd > 0 else 0.0,
                     "tickers": sorted({e.symbol or e.buy.ticker for e in g})[:6], "last_buy": last.filed})
    rows.sort(key=lambda r: (r["t"], r["mean_abn"]), reverse=True)
    return rows[:top]


def insider_records(evs: list[Ev], bounds) -> dict[str, tuple[int, float]]:
    """Every insider's (count, mean clipped 63-session AR) over buys with known outcomes."""
    acc: dict[str, list[float]] = defaultdict(lambda: [0, 0.0])
    for e in unique_signals(evs):
        if PRIMARY in e.abn and not e.buy.plan_purchase:
            a = acc[e.buy.owner_cik]
            a[0] += 1
            a[1] += max(-TRACK_CLIP, min(TRACK_CLIP, e.abn[PRIMARY]))
    return {k: (int(n), s / n) for k, (n, s) in acc.items() if n}


def run_backtest(evs: list[Ev], cal: Calendar, echo=print, rf_daily: list[float] | None = None) -> dict:
    add_pit_features(evs)
    study = [e for e in evs if e.in_study and is_listed_stock(e.symbol or "")]
    bounds = {h: winsor_bounds(study, h) for h in HORIZONS}
    echo(f"{len(evs)} signals, {sum(e.priced for e in evs)} priced, {len(study)} in the study sample")
    res: dict = {"horizons": list(HORIZONS), "primary": PRIMARY, "discovery_end": DISCOVERY_END,
                 "coverage": coverage(evs), "winsor": {str(h): bounds[h] for h in HORIZONS}}

    base = unique_signals(study)
    base_ct = calendar_time(base, cal)
    res["overall"] = {
        "signals": len(base),
        "events": {str(h): event_stats(base, h, bounds[h], boot=2000 if h == PRIMARY else 0) for h in HORIZONS},
        "variant_c": event_stats(base, PRIMARY, bounds[PRIMARY], key="abn_c", boot=1000),
        "vs_survivors": event_stats(base, PRIMARY, bounds[PRIMARY], key="abn_ew", boot=1000),
        "ctp": ctp_stats(base_ct["series"], boot=5000),
        "discovery": ctp_stats(split_series(base_ct["series"])[0]),
        "holdout": ctp_stats(split_series(base_ct["series"])[1]),
        "placebo": _placebo(base, bounds[PRIMARY]),
        "pre_drift_mean": _mean([e.pre_drift for e in base if e.pre_drift is not None and abs(e.pre_drift) < 1]),
        "survivorship": survivorship_bound(evs, bounds[PRIMARY]),
        "excluded_tail": event_stats([e for e in evs if e.priced and not e.in_study], PRIMARY, bounds[PRIMARY]),
    }
    echo("  overall done")

    slices = {}
    for name, fn in FEATURES.items():
        groups: dict[str, list[Ev]] = defaultdict(list)
        for e in study:
            groups[fn(e)].append(e)
        slices[name] = slice_report(groups, base_ct["series"], cal, bounds)
        echo(f"  sliced by {name}")
    verdicts(slices)
    res["slices"] = slices
    res["feature_notes"] = FEATURE_NOTES

    liquid = [e for e in study if e.liquid]
    strategies = {}
    for key, (desc, pred) in STRATEGIES.items():
        sel = unique_signals([e for e in liquid if pred(e)])
        ct = calendar_time(sel, cal)
        d_ser, h_ser = split_series(ct["series"])
        strategies[key] = {
            "description": desc, "signals": len(sel),
            "events": {str(h): event_stats(sel, h, bounds[h], boot=1000 if h == PRIMARY else 0) for h in (5, 21, 63, 126)},
            "variant_c": event_stats(sel, PRIMARY, bounds[PRIMARY], key="abn_c"),
            "vs_survivors": event_stats(sel, PRIMARY, bounds[PRIMARY], key="abn_ew"),
            "ctp": ctp_stats(ct["series"]), "discovery": ctp_stats(d_ser), "holdout": ctp_stats(h_ser),
            "portfolio": {f"{h}d": simulate(sel, cal, hold=h, rf_daily=rf_daily) for h in (21, 63, 126)},
            "portfolio_costs": {f"{m}x": _sim_brief(simulate(sel, cal, cost_mult=m, rf_daily=rf_daily))
                                for m in (0, 2)},
        }
        echo(f"  strategy {key}: {len(sel)} signals")
    res["strategies"] = strategies
    res["walk_forward"] = walk_forward(study, cal)
    echo("  walk-forward done")
    res["best_insiders"] = best_insiders(study, bounds[PRIMARY])
    return res


def _sim_brief(s: dict) -> dict:
    return {k: s.get(k) for k in ("strategy_cagr", "strategy_sharpe", "strategy_max_drawdown", "spy_cagr")}


def _mean(xs: list[float]) -> float | None:
    return sum(xs) / len(xs) if xs else None


def _placebo(evs: list[Ev], bounds) -> dict:
    lo, hi = bounds
    pairs = [(min(max(e.abn[PRIMARY], lo), hi), min(max(e.placebo, lo), hi))
             for e in evs if PRIMARY in e.abn and e.placebo is not None]
    if not pairs:
        return {"n": 0}
    return {"n": len(pairs), "event_mean": _mean([a for a, _ in pairs]), "placebo_mean": _mean([b for _, b in pairs]),
            "difference": _mean([a - b for a, b in pairs])}
