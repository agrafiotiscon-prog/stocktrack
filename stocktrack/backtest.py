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
import math
import random
import statistics
from array import array
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Iterable

from stocktrack.history import BENCHMARK, PriceHistory, PriceStore, TickerMap
from stocktrack.signals import BuyEvent, count_insiders, dedupe_purchases, is_listed_stock, score_buy

HORIZONS = (1, 5, 21, 63, 126, 252)
PRIMARY = 63
PATH_LEN = 126  # sessions of daily returns kept per event for portfolios
DISCOVERY_END = "2015-12-31"
HOLDOUT_START = "2016-01-01"
MAX_ENTRY_DELAY = 5  # sessions after filing within which the stock must trade
MAX_STALE = 10  # sessions an exit price may be stale
PRICE_RATIO = (0.67, 1.5)  # insider price / market close on trade date
STUDY_MIN_PRICE, STUDY_MIN_ADV = 1.0, 100_000
EW_MIN_MEMBERS = 100  # sessions with a thinner survivor index don't count as a benchmark
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
    placebo: float | None = None  # same stock a year later, 63-session AR (no earlier signal overlapping)
    placebo_all: float | None = None  # same, without the overlap exclusion (a conservative bound)
    path: array | None = None
    cluster: int = 1
    kind: str = "unclassified"
    track_n: int = 0
    track: float | None = None  # shrunk mean of past 63-session ARs
    first_in_year_insider: bool | None = True  # None: within a year of the data start
    first_in_year_issuer: bool | None = True
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
        n = len(spy.dates)
        # Survivor index, filled by build_events: close-to-close returns of a
        # buy-and-hold portfolio rebalanced to equal weights monthly, plus the
        # equal-weight open-to-close return for entry days.
        self.ew_daily = [0.0] * n
        self.ew_intraday = [0.0] * n
        self.ew_level: list[float] = []
        self.ew_count = [0] * n  # stocks in the index each session
        self.ew_thin: list[int] = []  # running count of sessions under EW_MIN_MEMBERS
        self.ew_thin_months: set[str] = set()

    def first_after(self, day: str) -> int:
        return bisect.bisect_right(self.dates, day)

    def finish_ew(self, acc: "EWAccumulator", min_members: int = EW_MIN_MEMBERS) -> None:
        self.ew_daily = [a / b if b else 0.0 for a, b in zip(acc.num, acc.den)]
        self.ew_intraday = [a / b if b else 0.0 for a, b in zip(acc.intra, acc.count)]
        self.ew_count = list(acc.count)
        self.ew_thin_months = set()
        level, self.ew_level = 1.0, []
        for r in self.ew_daily:
            level *= 1 + r
            self.ew_level.append(level)
        # Sessions with too few stocks (the start of the data) aren't a benchmark.
        thin, self.ew_thin = 0, []
        for c, n in enumerate(self.ew_count):
            if n < min_members:
                thin += 1
                self.ew_thin_months.add(self.dates[c][:7])
            self.ew_thin.append(thin)

    def ew_usable(self, c_from: int, c_to: int) -> bool:
        """Is the survivor index populated on every session from c_from to c_to?"""
        return self.ew_thin[c_to] == (self.ew_thin[c_from - 1] if c_from else 0)

    def ew_return(self, c_from: int, c_to: int) -> float:
        """Survivor index from the open of session c_from to the close of c_to."""
        return (1 + self.ew_intraday[c_from]) * self.ew_level[c_to] / self.ew_level[c_from] - 1


class EWAccumulator:
    def __init__(self, n: int) -> None:
        self.num, self.den = [0.0] * n, [0.0] * n
        self.intra, self.count = [0.0] * n, [0] * n


def _quiet(hist: PriceHistory, clean: list[int], bars: list[int]) -> bool:
    """Did these bars trade under 3x the dollar volume of the 20 clean bars before them?"""
    window = [hist.dollar_volume_day[x] for x in clean[-20:]]
    avg = sum(window) / len(window) if window else 0.0
    return avg > 0 and all(hist.dollar_volume_day[x] < 3 * avg for x in bars)


def _split_like_drop(hist: PriceHistory, a: int, b: int) -> bool:
    """A fall to 1/R that looks like a missed R:1 split: R close to a whole number and
    the whole step in the opening gap with a flat session after it. Real crashes
    rarely land on a whole ratio and usually keep moving during the day."""
    jump = hist.close[b] / hist.close[a]
    ratio = 1 / jump
    gap = hist.open[b] / hist.close[a]
    return (abs(ratio - round(ratio)) <= 0.05 * ratio and abs(gap / jump - 1) <= 0.1
            and abs(hist.close[b] / hist.open[b] - 1) <= 0.1)


def align(hist: PriceHistory, cal: Calendar) -> tuple[PriceHistory, int]:
    """Keep bars on benchmark trading days, drop bad ticks and flag data breaks.

    * Bad ticks: a close that jumps 4x up (or to under a quarter) on ordinary
      volume and comes back to within 2x of where it was within 3 bars. The bars
      in between are dropped. Heavily traded spikes are real and kept.
    * Data breaks: a step Yahoo didn't adjust for, i.e. a missed split. A 3x rise
      on dollar volume under 3x its 20-day average (a missed reverse split), or a
      fall to 1/3 or less that also looks like a split: a whole-number ratio, all
      in the opening gap, on ordinary dollar volume. Other big falls are real
      crashes and are kept. Returns that span a break are censored (hist.breaks).
    Sub-penny bars are kept, so a near-total loss is recorded rather than lost.
    Returns the cleaned history and the number of bars dropped.
    """
    keep = [k for k, d in enumerate(hist.dates) if d in cal.index]
    close = hist.close
    clean: list[int] = []
    dropped = 0
    pos = 0
    while pos < len(keep):
        k = keep[pos]
        if clean:
            prev = close[clean[-1]]
            jump = close[k] / prev
            if jump > 4 or jump < 0.25:
                back = next((q for q in range(pos + 1, min(pos + 4, len(keep)))
                             if 0.5 <= close[keep[q]] / prev <= 2), None)
                if back is not None and _quiet(hist, clean, keep[pos:back]):
                    dropped += back - pos
                    pos = back
                    continue
        clean.append(k)
        pos += 1
    breaks = []
    for q in range(1, len(clean)):
        a, b = clean[q - 1], clean[q]
        jump = close[b] / close[a]
        if ((jump > 3 or jump < 1 / 3) and _quiet(hist, clean[:q], [b])
                and (jump > 3 or _split_like_drop(hist, a, b))):
            breaks.append(hist.dates[b])
    if len(clean) == len(hist.dates) and not breaks:
        return hist, 0
    out = PriceHistory(hist.symbol, [hist.dates[k] for k in clean], [hist.open[k] for k in clean],
                       [close[k] for k in clean], [hist.dollar_volume_day[k] for k in clean],
                       [hist.raw_close[k] for k in clean])
    out.breaks = breaks
    return out, dropped


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
    if verify and b.last_date and b.last_date > ev.filed:
        ev.status = "bad_trade_date"  # a trade dated after its own filing is a typo
        return

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
    # Decision-time facts come from bars before the entry session.
    if i >= 1:
        ev.price = hist.raw_close[i - 1]
        ev.adv = hist.dollar_volume(i, 20)
    if i >= 64:
        ev.prior_ret = hist.close[i - 1] / hist.close[i - 64] - 1
    if first >= len(cal.dates):
        ev.status = "awaiting_entry"  # filed after the last session in the data
        return
    if i >= len(cals) or cals[i] - first > MAX_ENTRY_DELAY:
        ev.status = "no_entry_bar"
        return
    c_entry = cals[i]
    ev.status, ev.entry_date, ev.entry_cal = "priced", hist.dates[i], c_entry
    entry_open, entry_close = hist.open[i], hist.close[i]
    if ti is not None and ti < i:
        ev.pre_drift = entry_open / hist.close[ti] - 1
    # A data break (an unadjusted split, say) after entry censors everything past it.
    stop = min((cal.index[d] for d in hist.breaks if d > ev.entry_date and d in cal.index), default=len(cal.dates))

    for h in HORIZONS:
        c_exit = c_entry + h - 1
        if c_exit >= len(cal.dates) or c_exit >= stop:
            break  # censored: not enough data yet, or a data break
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
        if c >= len(cal.dates) or c >= stop:
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


def _unprice(ev: Ev, status: str) -> None:
    ev.status, ev.entry_date, ev.entry_cal, ev.path = status, None, -1, None
    ev.ret, ev.abn, ev.abn_c, ev.abn_ew, ev.exit_cal = {}, {}, {}, {}, {}


def placebo_ar(hist: PriceHistory, cal: Calendar, c_entry: int, cals: list[int] | None = None) -> float | None:
    """63-session AR for the same stock entered at calendar index c_entry (censored at a data break, as events are)."""
    if cals is None:
        cals = [cal.index[d] for d in hist.dates]
    i = bisect.bisect_left(cals, c_entry)
    if i >= len(cals) or cals[i] - c_entry > MAX_ENTRY_DELAY:
        return None
    c0, c_exit = cals[i], cals[i] + PRIMARY - 1
    if c_exit >= len(cal.dates):
        return None
    if any(c0 < cal.index[d] <= c_exit for d in hist.breaks if d in cal.index):
        return None
    j = _exit_bar(cals, c_exit, i)
    if j is None:
        return None
    return (hist.close[j] / hist.open[i] - 1) - (cal.spy.close[c_exit] / cal.spy.open[c0] - 1)


def _add_to_ew(hist: PriceHistory, cal: Calendar, acc: EWAccumulator, start_cal: int,
               own_entries: list[int]) -> None:
    """Add a stock to the survivor index: other insider-bought stocks, held buy-and-hold.

    * It joins only once its first insider filing is public: before that, being in
      this sample depends on a future buy (which tends to follow declines).
    * Days inside its own post-signal windows (entry to entry + 63 sessions) are left
      out, so the index measures *other* stocks; those signals are already public.
      Membership is point in time: a member is held to the open of its own entry
      session (the overnight reaction to an after-hours filing counts) and sold there.
    * Weights drift with returns and reset to equal at each month start, matching
      the buy-and-hold returns it is compared with (a daily-rebalanced average of
      returns would be inflated by bid-ask bounce).
    """
    cals = [cal.index[d] for d in hist.dates]
    breaks = {cal.index[d] for d in hist.breaks if d in cal.index}
    window, total = 20, 0.0
    weight, month = None, ""
    for k in range(1, len(cals)):
        total += hist.dollar_volume_day[k - 1]
        if k > window:
            total -= hist.dollar_volume_day[k - 1 - window]
        c = cals[k]
        j = bisect.bisect_right(own_entries, c) - 1
        own = j >= 0 and c < own_entries[j] + PRIMARY
        member = (c >= start_cal and cals[k] == cals[k - 1] + 1 and hist.raw_close[k - 1] >= STUDY_MIN_PRICE
                  and k >= window and total / window >= STUDY_MIN_ADV and c not in breaks)
        m = cal.dates[c][:7]
        if member and own and weight is not None:  # held overnight into its own entry session
            w = weight if m == month else 1.0
            acc.num[c] += w * (hist.open[k] / hist.close[k - 1] - 1)
            acc.den[c] += w
        if not member or own:
            weight = None
            continue
        if weight is None or m != month:
            weight, month = 1.0, m
        r = hist.close[k] / hist.close[k - 1] - 1
        acc.num[c] += weight * r
        acc.den[c] += weight
        acc.intra[c] += hist.close[k] / hist.open[k] - 1
        acc.count[c] += 1
        weight *= 1 + r


def build_events(buys: Iterable[BuyEvent], store: PriceStore, tickers: TickerMap,
                 progress: Callable[[int, int], None] | None = None,
                 min_members: int = EW_MIN_MEMBERS) -> tuple[list[Ev], Calendar, dict]:
    spy = store.load(BENCHMARK)
    if spy is None:
        raise RuntimeError("no SPY history; fetch prices first")
    cal = Calendar(spy)
    ordered = sorted((b for b in buys if b.filed_at), key=lambda b: (b.filed_at[:10], b.accession))
    deduped = dedupe_purchases(ordered)
    evs = [Ev(buy=b, filed=b.filed_at[:10]) for b in deduped]
    # bars_dropped: sub-penny days plus isolated bad ticks removed by align()
    meta = {"filings": len(ordered), "duplicate_filings": len(ordered) - len(deduped), "bars_dropped": 0}
    by_symbol: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        ev.symbol, ev.resolve = tickers.resolve(ev.buy.issuer_cik, ev.buy.ticker)
        if ev.symbol:
            by_symbol[ev.symbol].append(ev)
        else:
            ev.status = ev.resolve  # unlisted / class_gone
    meta["ticker_resolution"] = {}
    for ev in evs:
        meta["ticker_resolution"][ev.resolve] = meta["ticker_resolution"].get(ev.resolve, 0) + 1
    acc = EWAccumulator(len(cal.dates))
    for n, (sym, group) in enumerate(sorted(by_symbol.items()), 1):
        raw = store.load(sym)
        if raw is None:
            for ev in group:
                ev.status = "no_history"
            continue
        hist, repaired = align(raw, cal)
        meta["bars_dropped"] += repaired
        meta["data_breaks"] = meta.get("data_breaks", 0) + len(hist.breaks)
        if not hist.dates:
            continue
        for ev in group:
            attach_market_data(ev, hist, cal)
        # A reused ticker belongs to another company now; trust its history for this
        # issuer only if the issuer's filings match it consistently, not by chance.
        for issuer in {ev.buy.issuer_cik for ev in group if ev.resolve == "reused"}:
            pair = [ev for ev in group if ev.buy.issuer_cik == issuer]
            ratios = sorted(ev.price_ratio for ev in pair if ev.price_ratio is not None)
            passed = sum(1 for ev in pair if ev.priced or ev.status == "awaiting_entry")
            if not ratios or passed < 0.8 * len(ratios) or not 0.9 <= percentile(ratios, 0.5) <= 1.1:
                for ev in pair:
                    if ev.status in ("priced", "awaiting_entry", "no_entry_bar"):
                        _unprice(ev, "price_mismatch")
        entries = sorted(ev.entry_cal for ev in group if ev.priced)
        if entries:
            # The stock joins the index at its own company's first filing, not at a
            # filing by a former holder of the ticker.
            own = {ev.buy.issuer_cik for ev in group if ev.priced}
            start = min(cal.first_after(ev.filed) for ev in group if ev.buy.issuer_cik in own)
            _add_to_ew(hist, cal, acc, start, entries)
        # Placebo: the same stock over a 63-session window a year after the buy.
        # ev.placebo leaves out windows overlapping an earlier signal's post-entry
        # window. Which events keep one depends on later buys, so the event side of
        # the comparison uses every event with a placebo_all (see _placebo).
        cals = [cal.index[d] for d in hist.dates]
        for ev in group:
            if ev.priced:
                p = ev.entry_cal + 252
                ev.placebo_all = placebo_ar(hist, cal, p, cals)
                k = bisect.bisect_left(entries, p - 62)
                if not (k < len(entries) and entries[k] < p):
                    ev.placebo = ev.placebo_all
        if progress:
            progress(n, len(by_symbol))
    cal.finish_ew(acc, min_members)
    for ev in evs:
        for h, c_exit in ev.exit_cal.items():
            if cal.ew_usable(ev.entry_cal, c_exit):
                ev.abn_ew[h] = ev.ret[h] - cal.ew_return(ev.entry_cal, c_exit)
    return evs, cal, meta


# --- point-in-time features ----------------------------------------------


def add_pit_features(evs: list[Ev], history_start: str | None = None) -> None:
    """Cluster size, routine/opportunistic, track record and novelty from earlier filings only.

    `history_start` is the first filing date loaded; within a year of it the
    "first buy in 12 months" flags are unknown (earlier buys weren't loaded).
    """
    by_day: dict[str, list[Ev]] = defaultdict(list)
    for ev in evs:
        by_day[ev.filed].append(ev)
    if not by_day:
        return
    start = history_start or min(by_day)
    novelty_known_from = (dt.date.fromisoformat(start) + dt.timedelta(days=365)).isoformat()

    issuer_recent: dict[str, list[Ev]] = defaultdict(list)
    months: dict[str, dict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    last_owner: dict[str, str] = {}
    last_issuer: dict[str, str] = {}
    outcomes: dict[str, list[tuple[int, float]]] = defaultdict(list)  # owner -> sorted (exit index, AR63)
    counted: set[tuple[str, tuple[str, str]]] = set()

    for day in sorted(by_day):
        todays = by_day[day]
        # Same-day filings are public before the next open, so they count for clusters.
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
            ev.cluster = count_insiders(dedupe_purchases([b, *near]))

            # Track record: earlier buys whose 63-session outcome closed before this entry.
            past = outcomes[b.owner_cik]
            if ev.entry_cal >= 0 and past:
                known = past[:bisect.bisect_left(past, (ev.entry_cal, -math.inf))]
                n = len(known)
                ev.track_n = n
                ev.track = (n / (n + 5)) * (sum(a for _, a in known) / n) if n else None

            year, month = int((b.first_date or day)[:4]), int((b.first_date or day)[5:7])
            hist = months[b.owner_cik]
            prior = [hist.get(year - k, set()) for k in (1, 2, 3)]
            if all(prior):
                ev.kind = "routine" if all(month in p for p in prior) else "opportunistic"
            if day >= novelty_known_from:
                ev.first_in_year_insider = _days_apart(last_owner.get(b.owner_cik, ""), day) > 365
                ev.first_in_year_issuer = _days_apart(last_issuer.get(b.issuer_cik, ""), day) > 365
            else:
                ev.first_in_year_insider = ev.first_in_year_issuer = None
            ev.score = score_buy(b, ev.cluster).total
        for ev in todays:
            b = ev.buy
            months[b.owner_cik][int((b.first_date or day)[:4])].add(int((b.first_date or day)[5:7]))
            last_owner[b.owner_cik] = day
            last_issuer[b.issuer_cik] = day
            # Same rule as insider_records: discretionary buys, one per company-day.
            if PRIMARY in ev.abn and not b.plan_purchase and (b.owner_cik, ev.issuer_day) not in counted:
                counted.add((b.owner_cik, ev.issuer_day))
                ar = max(-TRACK_CLIP, min(TRACK_CLIP, ev.abn[PRIMARY]))
                bisect.insort(outcomes[b.owner_cik], (ev.exit_cal[PRIMARY], ar))


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
    """Event-level averages of excess returns (winsorized).

    `stock_return` is the plain stock return and `unwinsorized` the excess
    before clipping. CIs come from a moving-block bootstrap over consecutive
    entry months: an h-session window spans about h/21 months, so neighbouring
    months' returns overlap and must be resampled together.
    """
    lo, hi = bounds
    pts = [(ev.month, min(max(getattr(ev, key)[h], lo), hi), ev.ret.get(h), getattr(ev, key)[h])
           for ev in unique_signals(evs) if h in getattr(ev, key)]
    if not pts:
        return {"n": 0}
    vals = sorted(a for _, a, _, _ in pts)
    rets = [r for _, _, r, _ in pts if r is not None]
    out = {"n": len(pts), "mean": sum(vals) / len(vals), "median": percentile(vals, 0.5),
           "hit": sum(1 for a in vals if a > 0) / len(vals),
           "stock_return": sum(rets) / len(rets) if rets else None,
           "unwinsorized": sum(u for *_, u in pts) / len(pts)}
    if boot:
        by_month: dict[str, list[float]] = defaultdict(lambda: [0.0, 0])
        for m, a, _, _ in pts:
            by_month[m][0] += a
            by_month[m][1] += 1
        groups = [by_month[m] for m in sorted(by_month)]
        block = max(1, math.ceil(h / 21))
        if len(groups) >= 4 * block:
            rng = random.Random(seed)
            nblocks = math.ceil(len(groups) / block)
            means = []
            for _ in range(boot):
                tot = cnt = 0.0
                for _ in range(nblocks):
                    s = rng.randrange(0, len(groups) - block + 1)
                    for g in groups[s:s + block]:
                        tot += g[0]
                        cnt += g[1]
                means.append(tot / cnt)
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
    if draws <= 0 or t_len < 2 * block:
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
    below = sum(1 for m in means if m < 0) + 0.5 * sum(1 for m in means if m == 0)  # mid-p
    share = below / draws
    return {"ci": [percentile(means, 0.025), percentile(means, 0.975)],
            "p_boot": min(1.0, 2 * min(share, 1 - share))}


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


def calendar_time(evs: list[Ev], cal: Calendar, hold: int = PRIMARY, min_positions: float = 5,
                  bench: str = "spy") -> dict:
    """Monthly returns of a portfolio holding every signal for `hold` sessions, and its benchmark.

    Buy-and-hold weights (each position starts at 1 and drifts with its price),
    each company held once at a time. The benchmark gets the same weights: SPY
    from the open on a position's entry day (when the position starts), close to
    close after; or the survivor index (`bench="ew"`, close to close). Months
    averaging fewer than `min_positions` positions are dropped, and so are months
    when the survivor index is too thin to be a benchmark.
    """
    n = len(cal.dates)
    num, den, cnt, bnum = [0.0] * n, [0.0] * n, [0] * n, [0.0] * n
    held_until: dict[str, int] = {}
    daily_bench = cal.ew_daily if bench == "ew" else cal.daily
    for ev in sorted((e for e in evs if e.path is not None and len(e.path)), key=lambda e: e.entry_cal):
        c0 = ev.entry_cal
        if held_until.get(ev.buy.issuer_cik, -1) >= c0:
            continue
        steps = min(hold, len(ev.path))
        held_until[ev.buy.issuer_cik] = c0 + steps - 1
        v = 1.0
        for k in range(steps):
            c = c0 + k
            r = ev.path[k]
            num[c] += v * r
            den[c] += v
            cnt[c] += 1
            if k == 0:  # the position starts at the open
                day0 = cal.spy.close[c] / cal.spy.open[c] - 1 if bench == "spy" else cal.ew_intraday[c]
                bnum[c] += v * day0
            else:
                bnum[c] += v * daily_bench[c]
            v *= 1 + r
    months: dict[str, list] = {}
    daily: dict[int, tuple[float, float]] = {}
    for c in range(n):
        if den[c] <= 0:
            continue
        rp, rb = num[c] / den[c], bnum[c] / den[c]
        daily[c] = (rp, rb)
        m = cal.dates[c][:7]
        acc = months.setdefault(m, [1.0, 1.0, 0, 0])
        acc[0] *= 1 + rp
        acc[1] *= 1 + rb
        acc[2] += 1
        acc[3] += cnt[c]
    series = []
    dropped = 0
    last_month = cal.dates[-1][:7] if cal.dates else ""
    for m in sorted(months):
        pr, sr, days, pos = months[m]
        if pos / days < min_positions or (bench == "ew" and m in cal.ew_thin_months):
            dropped += 1
            continue
        if m == last_month:
            continue  # incomplete final month
        series.append((m, pr - 1, sr - 1))
    return {"series": series, "dropped_months": dropped, "daily": daily}


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


def difference_series(a: dict, b: dict, cal: Calendar) -> list[tuple[str, float, float]]:
    """Monthly return of portfolio A minus portfolio B (calendar_time outputs), compounded
    over the days both hold positions, in months both series keep; ctp_stats can test it."""
    keep = {m for m, _, _ in a["series"]} & {m for m, _, _ in b["series"]}
    acc: dict[str, list[float]] = {}
    for c, (ra, _) in a["daily"].items():
        rb = b["daily"].get(c)
        m = cal.dates[c][:7]
        if rb is None or m not in keep:
            continue
        x = acc.setdefault(m, [1.0, 1.0])
        x[0] *= 1 + ra
        x[1] *= 1 + rb[0]
    return [(m, x[0] - x[1], 0.0) for m, x in sorted(acc.items())]


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
    "insider_novelty": lambda e: "unknown" if e.first_in_year_insider is None
    else ("first buy in 12m" if e.first_in_year_insider else "repeat buyer"),
    "company_novelty": lambda e: "unknown" if e.first_in_year_issuer is None
    else ("first insider buy in 12m" if e.first_in_year_issuer else "recent insider buys"),
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
    "first_buy_exec": ("Exec's first buy in a year, $50K+", lambda e: e.first_in_year_insider is True
                       and e.buy.role in ("CEO", "CFO", "President", "Chair", "C-Suite") and e.value >= 5e4
                       and not e.buy.plan_purchase),
    # Post-hoc ideas, added 2026-10-20 after seeing the run-2 results (see data/backtest/hypotheses.json).
    # Their backtest numbers are in-sample by construction; only the live forward test can confirm them.
    "cfo_exec_25k": ("CFO or other non-CEO executive buying $25K+ (post-hoc)",
                     lambda e: e.buy.role in ("CFO", "C-Suite", "Officer") and e.value >= 25e3
                     and not e.buy.plan_purchase),
    "momentum_buy": ("Insider buying after a 30%+ run-up (post-hoc)",
                     lambda e: (e.prior_ret or 0) >= 0.3 and not e.buy.plan_purchase and e.kind != "routine"),
}

POST_HOC = {"cfo_exec_25k", "momentum_buy"}


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
             cost_mult: float = 1.0, rf_daily: list[float] | None = None,
             hedge_daily: list[float] | None = None) -> dict:
    """$100K, `slots` positions, each signal bought at the next open and held `hold` sessions.

    When more signals arrive than free slots, the highest scores win. Size is
    NAV/slots, capped by cash and 2% of the stock's daily dollar volume.
    With `hedge_daily` (e.g. IWM), also reports a hedged version that shorts the
    hedge against the invested fraction each day (exploratory; borrow costs ignored).
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
    exposure: list[float] = []  # invested fraction at the start of each day, after entries
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
        invested = sum(p[1] for p in open_pos)
        exposure.append(invested / (cash + invested) if cash + invested > 0 else 0.0)
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
    rf = rf_daily[start:n] if rf_daily else [0.0] * len(daily)
    out.update({f"strategy_{k}": v for k, v in perf(daily, rf).items()})
    out.update({f"spy_{k}": v for k, v in perf(spy, rf).items()})
    if hedge_daily:
        hedged = [r - e * hedge_daily[c] for c, r, e in zip(range(start, n), daily, exposure)]
        out.update({f"hedged_{k}": v for k, v in perf(hedged, rf).items()})
        out["hedge_cagr"] = perf(hedge_daily[start:n]).get("cagr")
    # Beta and alpha from monthly excess returns: small, thinly traded stocks react
    # to the market with a lag, which biases daily betas down (and alphas up).
    months: dict[str, list[float]] = {}
    for c, r, s, f in zip(range(start, n), daily, spy, rf):
        m = months.setdefault(cal.dates[c][:7], [1.0, 1.0, 1.0])
        m[0] *= 1 + r
        m[1] *= 1 + s
        m[2] *= 1 + f
    ys = [a - f for a, _, f in months.values()]
    xs = [b - f for _, b, f in months.values()]
    if len(ys) >= 12:
        alpha, beta = ols(ys, xs)
        out["beta"], out["alpha_annual"] = beta, (1 + alpha) ** 12 - 1
        active = [(a - b) for a, b, _ in months.values()]
        sd = statistics.pstdev(active)
        out["information_ratio"] = (sum(active) / len(active)) / sd * math.sqrt(12) if sd else 0.0
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


UNVERIFIABLE = ("unverified", "price_mismatch", "bad_trade_date")


def survivorship_bound(evs: list[Ev], bounds, period: tuple[str, str] = ("", "9999")) -> dict:
    """Mean AR63 if the unpriceable signals had done like the median / 10th-percentile priced one.

    Signals rejected by data checks (unverified prices, typos) aren't dead companies,
    so they aren't counted as unpriced.
    """
    lo, hi = bounds
    pool = [e for e in evs if is_listed_stock(e.buy.ticker) and not e.buy.plan_purchase
            and period[0] <= e.filed <= period[1]]
    priced = sorted(min(max(e.abn[PRIMARY], lo), hi) for e in unique_signals(pool) if e.in_study and PRIMARY in e.abn)
    unpriced = len(unique_signals([e for e in pool if not e.priced and e.status not in UNVERIFIABLE
                                   and e.status != "awaiting_entry" and e.filed < "2025-07-01"]))
    if not priced:
        return {}
    mean = sum(priced) / len(priced)
    med, p10 = percentile(priced, 0.5), percentile(priced, 0.1)
    total = len(priced) + unpriced
    return {"reported": mean, "neutral": (mean * len(priced) + med * unpriced) / total,
            "pessimistic": (mean * len(priced) + p10 * unpriced) / total,
            "priced": len(priced), "unpriced": unpriced}


def _periods(ct: dict, cal: Calendar, sig: list[Ev], boot: int) -> dict:
    """Discovery/holdout calendar-time stats against SPY and against the survivor index."""
    d_ser, h_ser = split_series(ct["series"])
    ew = calendar_time(sig, cal, bench="ew")
    d_ew, h_ew = split_series(ew["series"])
    return {"ctp": ctp_stats(ct["series"]), "discovery": ctp_stats(d_ser, boot=boot),
            "holdout": ctp_stats(h_ser, boot=boot), "ctp_vs_survivors": ctp_stats(ew["series"], boot=0),
            "discovery_vs_survivors": ctp_stats(d_ew, boot=0), "holdout_vs_survivors": ctp_stats(h_ew, boot=0)}


def slice_report(groups: dict[str, list[Ev]], base_ct: dict, cal: Calendar, bounds: dict) -> dict:
    out = {}
    for label, g in sorted(groups.items()):
        sig = unique_signals(g)
        disc = [e for e in sig if e.filed <= DISCOVERY_END]
        ct = calendar_time(sig, cal)
        row = {
            "signals": len(sig),
            "events": {str(h): event_stats(sig, h, bounds[h], boot=1000 if h == PRIMARY else 0)
                       for h in (5, 21, 63, 126, 252)},
            "variant_c": event_stats(sig, PRIMARY, bounds[PRIMARY], key="abn_c"),
            "vs_survivors": event_stats(sig, PRIMARY, bounds[PRIMARY], key="abn_ew"),
            **_periods(ct, cal, sig, boot=1000),
            "vs_all_buys": ctp_stats(difference_series(ct, base_ct, cal), boot=1000),
            "enough_data": len(disc) >= MIN_SIGNALS and len(split_series(ct["series"])[0]) >= MIN_MONTHS,
        }
        out[label] = row
    return out


def verdicts(slices: dict) -> None:
    """Label each slice with the pre-registered verdict rule (mutates `slices`).

    Holm families: (1) discovery p of every slice with enough data; (2) holdout p of
    the slices that passed (1), to confirm them; (3) holdout p of every slice, for
    holdout-only findings; (4) each slice minus all insider buys.
    """
    def row(key):
        feat, label = key.split("|", 1)
        return slices[feat][label]

    keys = [f"{f}|{lb}" for f, rows in slices.items() for lb, r in rows.items() if r["enough_data"]]
    disc_adj = holm({k: row(k)["discovery"]["p"] for k in keys if "p" in row(k)["discovery"]})
    passed = {k for k, p in disc_adj.items() if p < 0.05 and row(k)["discovery"]["excess_mean"] > 0}
    hurt = {k for k, p in disc_adj.items() if p < 0.05 and row(k)["discovery"]["excess_mean"] < 0}
    confirm_adj = holm({k: row(k)["holdout"].get("p", 1.0) for k in passed | hurt})
    hold_adj = holm({k: row(k)["holdout"]["p"] for k in keys if "p" in row(k)["holdout"]})
    diff_adj = holm({k: row(k)["vs_all_buys"]["p"] for k in keys if "p" in row(k)["vs_all_buys"]})
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
            hold_pos = h.get("excess_mean", 0) > 0
            confirmed = key in confirm_adj and confirm_adj[key] < 0.05
            hold_sig = hold_adj.get(key, 1) < 0.05
            survivors_ok = all(r[p].get("excess_mean", -1) > 0 for p in ("discovery_vs_survivors",
                                                                         "holdout_vs_survivors"))
            c_ok = r["variant_c"].get("mean", 0) > 0
            years_ok = r["ctp"].get("years_positive", 0) >= 0.6
            if key in passed and confirmed and hold_pos and c_ok and survivors_ok and years_ok:
                r["verdict"] = "works"
            elif key in hurt and confirmed and not hold_pos:
                r["verdict"] = "hurts"
            elif (key in passed and hold_sig and not hold_pos) or (key in hurt and hold_sig and hold_pos):
                r["verdict"] = "reversed"
            elif key in passed or (hold_sig and hold_pos):
                r["verdict"] = "promising"
            elif key in hurt or (hold_sig and not hold_pos):
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
    pool = [e for e in evs if e.liquid and not e.buy.plan_purchase]
    # A calendar-time month's return is realized at month end, and its holdings
    # only include signals filed by then, so on Jan 1 of year Y every month
    # through December of Y-1 is known. Filter by score before keeping one
    # signal per company-day, so a high-score filing isn't lost to a low-score one.
    full = {t: calendar_time(unique_signals(e for e in pool if e.score >= t), cal)["series"] for t in thresholds}
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
        picked.extend(unique_signals(e for e in pool if e.year == year and e.score >= best))
    ct = calendar_time(picked, cal)
    return {"thresholds": chosen, "signals": len(picked), "ctp": ctp_stats(ct["series"]),
            "events": event_stats(picked, PRIMARY, (-1e9, 1e9))}


def _by_owner(evs: list[Ev]) -> dict[str, list[Ev]]:
    """Each insider's discretionary buys with a known 63-session outcome, one per company-day."""
    by_owner: dict[str, dict[tuple, Ev]] = defaultdict(dict)
    for e in evs:
        if PRIMARY in e.abn and not e.buy.plan_purchase:
            by_owner[e.buy.owner_cik].setdefault(e.issuer_day, e)
    return {k: list(v.values()) for k, v in by_owner.items()}


def best_insiders(evs: list[Ev], bounds, min_buys: int = 5, top: int = 50) -> list[dict]:
    lo, hi = bounds
    rows = []
    for owner, g in _by_owner(evs).items():
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


def insider_records(evs: list[Ev], bounds=None) -> dict[str, tuple[int, float]]:
    """Every insider's (count, mean clipped 63-session AR) over buys with known outcomes."""
    out = {}
    for owner, g in _by_owner(evs).items():
        out[owner] = (len(g), sum(max(-TRACK_CLIP, min(TRACK_CLIP, e.abn[PRIMARY])) for e in g) / len(g))
    return out


def run_backtest(evs: list[Ev], cal: Calendar, echo=print, rf_daily: list[float] | None = None,
                 hedge_daily: list[float] | None = None) -> dict:
    add_pit_features(evs)
    study = [e for e in evs if e.in_study and is_listed_stock(e.symbol or "")]
    # Winsorizing bounds come from the discovery period only, so holdout returns
    # don't shape how discovery results are clipped.
    disc_study = [e for e in study if e.filed <= DISCOVERY_END] or study
    bounds = {h: winsor_bounds(disc_study, h) for h in HORIZONS}
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
        **_periods(base_ct, cal, base, boot=5000),
        "placebo": _placebo(base, bounds[PRIMARY]),
        "pre_drift_mean": _mean([e.pre_drift for e in base if e.pre_drift is not None and abs(e.pre_drift) < 1]),
        "survivorship": survivorship_bound(evs, bounds[PRIMARY]),
        "survivorship_discovery": survivorship_bound(evs, bounds[PRIMARY], ("", DISCOVERY_END)),
        "survivorship_holdout": survivorship_bound(evs, bounds[PRIMARY], (HOLDOUT_START, "9999")),
        "excluded_tail": event_stats([e for e in evs if e.priced and not e.in_study], PRIMARY, bounds[PRIMARY]),
    }
    echo("  overall done")

    slices = {}
    for name, fn in FEATURES.items():
        groups: dict[str, list[Ev]] = defaultdict(list)
        for e in study:
            groups[fn(e)].append(e)
        slices[name] = slice_report(groups, base_ct, cal, bounds)
        echo(f"  sliced by {name}")
    verdicts(slices)
    res["slices"] = slices
    res["feature_notes"] = FEATURE_NOTES

    liquid = [e for e in study if e.liquid]
    strategies = {}
    for key, (desc, pred) in STRATEGIES.items():
        sel = unique_signals([e for e in liquid if pred(e)])
        ct = calendar_time(sel, cal)
        strategies[key] = {
            "description": desc, "signals": len(sel),
            "events": {str(h): event_stats(sel, h, bounds[h], boot=1000 if h == PRIMARY else 0) for h in (5, 21, 63, 126)},
            "variant_c": event_stats(sel, PRIMARY, bounds[PRIMARY], key="abn_c"),
            "vs_survivors": event_stats(sel, PRIMARY, bounds[PRIMARY], key="abn_ew"),
            **_periods(ct, cal, sel, boot=1000),
            "portfolio": {f"{h}d": simulate(sel, cal, hold=h, rf_daily=rf_daily, hedge_daily=hedge_daily)
                          for h in (21, 63, 126)},
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
    """Events vs the same stocks a year later.

    The event side is every event whose placebo window exists. Which placebo windows
    are clean (no earlier signal overlapping) depends on buys after the event, so
    restricting events to those pairs would select on the future. The difference
    without any exclusion is reported as a conservative bound.
    """
    lo, hi = bounds

    def clip(x: float) -> float:
        return min(max(x, lo), hi)

    eligible = [e for e in evs if PRIMARY in e.abn and e.placebo_all is not None]
    clean = [clip(e.placebo) for e in eligible if e.placebo is not None]
    if not clean:
        return {"n": 0}
    event_mean, placebo_mean = _mean([clip(e.abn[PRIMARY]) for e in eligible]), _mean(clean)
    return {"n": len(eligible), "n_placebo": len(clean), "event_mean": event_mean, "placebo_mean": placebo_mean,
            "difference": event_mean - placebo_mean,
            "difference_no_exclusion": _mean([clip(e.abn[PRIMARY]) - clip(e.placebo_all) for e in eligible])}
