"""Turn Form 4 purchases into scored "insider buy" signals.

A buy event is all open-market purchases (transaction code P) in one filing.
It is scored 0-100 on what tends to make insider buying meaningful:

  value       up to 30  dollars spent, on a log scale ($100K = 10, $1M = 20, $10M = 30)
  role        up to 25  CEOs and CFOs know the most; 10% holders and funds the least
  conviction  up to 20  how much the purchase grew the insider's stake (new position = max)
  cluster     up to 25  several different insiders buying the same stock around the same time

minus penalties for purchases under a pre-scheduled Rule 10b5-1 plan, for
automatic plan purchases (dividend reinvestment, employee/director stock
purchase plans), and for filings made long after the trade (Form 4 is due
within two business days).
"""

from __future__ import annotations

import datetime as dt
import math
import re
from dataclasses import dataclass, field

from stocktrack.feeds import filing_index_url
from stocktrack.form4 import Form4, Owner

ROLE_POINTS = {
    "CEO": 25,
    "CFO": 22,
    "President": 22,
    "Chair": 22,
    "C-Suite": 18,
    "Officer": 14,
    "Director": 12,
    "10% Owner": 8,
    "Other": 4,
}

STRONG = 60  # e.g. a CEO spending $1M to grow their stake by half
NOTABLE = 40

CLUSTER_WINDOW_DAYS = 14
CLUSTER_MIN_VALUE = 25_000  # smaller buys don't make a stock a cluster buy
LATE_FILING_DAYS = 10
PLAN_PENALTY = 15
PLAN_PURCHASE_PENALTY = 30
LATE_PENALTY = 10
MAX_TRANSACTION_VALUE = 5e9  # far beyond any real insider purchase

# Footnote language for purchases that happen automatically rather than by choice.
PLAN_PURCHASE_RE = re.compile(
    r"dividend reinvestment|reinvest\w* (?:of )?(?:the )?(?:cash )?dividends|\bdrip\b"
    r"|stock purchase plan|\bespp\b|401\(k\)|deferred compensation|dividend equivalent",
    re.I,
)

NON_COMMON_RE = re.compile(
    r"prefer|\bpfd\b|\bnotes?\b|debenture|\bbonds?\b|warrant|\brights?\b|capital securities|convertible",
    re.I,
)

# Nasdaq convention: 5-letter symbols ending in X are mutual funds.
_FUND_TICKER_RE = re.compile(r"^[A-Z]{4}X$")


def is_listed_stock(ticker: str) -> bool:
    """False for issuers you can't trade on an exchange: no ticker (private and
    non-traded funds, BDCs) or a mutual-fund ticker (interval funds)."""
    return bool(ticker) and not _FUND_TICKER_RE.match(ticker)


@dataclass
class BuyEvent:
    accession: str
    issuer_cik: str
    issuer_name: str
    ticker: str
    owner_cik: str
    owner_name: str
    owner_names: str  # every reporting owner on a joint filing, "; "-separated
    role: str
    officer_title: str
    first_date: str
    last_date: str
    filed_at: str
    shares: float
    value: float
    avg_price: float | None
    shares_before: float | None
    shares_after: float | None
    plan_10b5_1: bool
    plan_purchase: bool  # bought via DRIP, an employee/director stock purchase plan, etc.
    n_transactions: int
    url: str
    owner_ciks: str = ""  # every reporting owner's CIK, ";"-separated

    @property
    def counts_toward_cluster(self) -> bool:
        return self.value >= CLUSTER_MIN_VALUE and not self.plan_purchase

    @property
    def stake_increase(self) -> float | None:
        """Fractional growth of the holding (0.25 = +25%); inf for a new position."""
        if self.shares_before is None or self.shares_after is None:
            return None
        if self.shares_before <= 0:
            return math.inf if self.shares_after > 0 else None
        return (self.shares_after - self.shares_before) / self.shares_before

    @property
    def filing_delay_days(self) -> int | None:
        try:
            traded = dt.date.fromisoformat(self.last_date)
            filed = dt.date.fromisoformat(self.filed_at[:10])
        except ValueError:
            return None
        return (filed - traded).days


@dataclass
class Score:
    total: int
    value_pts: float
    role_pts: float
    conviction_pts: float
    cluster_pts: float
    penalty: float
    cluster_size: int
    tags: list[str] = field(default_factory=list)  # e.g. "Stake +40%", "Cluster: 3 insiders"

    @property
    def label(self) -> str:
        if self.total >= STRONG:
            return "Strong"
        if self.total >= NOTABLE:
            return "Notable"
        return "Minor"


_VICE = re.compile(r"\b(vice|vp|svp|evp)\b")


def owner_role(o: Owner) -> str:
    title = o.officer_title.lower()
    if title or o.is_officer:
        if re.search(r"\bchief executive\b|\bceo\b", title):
            return "CEO"
        if re.search(r"\bchief financial\b|\bcfo\b", title):
            return "CFO"
        if re.search(r"\bpresident\b", title) and not _VICE.search(title):
            return "President"
        if re.search(r"\bchair", title):
            return "Chair"
        if re.search(r"\bchief\b|\bc[a-z]o\b", title):
            return "C-Suite"
        if o.is_officer:
            return "Officer"
    if o.is_director:
        if re.search(r"\bchair", f"{title} {o.other_text.lower()}"):
            return "Chair"
        return "Director"
    if o.is_ten_percent:
        return "10% Owner"
    return "Other"


def build_buy(form: Form4) -> BuyEvent | None:
    """Aggregate a filing's open-market purchases into one event, or None if it has none.

    Purchases of preferred stock, notes, warrants and the like are left out:
    they aren't a bet on the common stock this tool prices.
    """
    buys = [t for t in form.purchases if not NON_COMMON_RE.search(t.security or "")]
    if not buys:
        return None

    shares = sum(t.shares or 0 for t in buys)
    # A filer sometimes types the total cost into the per-share price field;
    # treat implausibly large transactions as unpriced rather than trust them.
    priced = [t for t in buys if t.shares and t.price and t.shares * t.price <= MAX_TRANSACTION_VALUE]
    value = sum(t.shares * t.price for t in priced)
    priced_shares = sum(t.shares for t in priced)
    avg_price = value / priced_shares if priced_shares else None

    # Holding before/after, per ownership line (direct, or each indirect vehicle).
    # The last purchase's post-transaction balance minus everything bought in the
    # filing gives the balance before the first purchase.
    groups: dict[tuple[str, str], list] = {}
    for t in buys:
        g = groups.setdefault((t.direct_indirect, t.nature.lower()), [0.0, None])
        g[0] += t.shares or 0
        if t.shares_after is not None:
            g[1] = t.shares_after
    known = [(bought, after) for bought, after in groups.values() if after is not None]
    shares_after = sum(after for _, after in known) if known else None
    shares_before = sum(max(after - bought, 0.0) for bought, after in known) if known else None

    ranked = sorted(form.owners, key=lambda o: ROLE_POINTS[owner_role(o)], reverse=True)
    primary = ranked[0] if ranked else Owner(cik="", name="")
    dates = sorted(t.date for t in buys if t.date)
    # Remarks cover the whole filing, so a DRIP mention there flags it too.
    plan_text = " ".join([form.remarks, *(n for t in buys for n in form.notes(t))])

    return BuyEvent(
        accession=form.accession,
        issuer_cik=form.issuer_cik.lstrip("0"),
        issuer_name=form.issuer_name,
        ticker=form.ticker,
        owner_cik=primary.cik.lstrip("0"),
        owner_name=primary.name,
        owner_names="; ".join(o.name for o in form.owners),
        role=owner_role(primary),
        officer_title=primary.officer_title,
        first_date=dates[0] if dates else "",
        last_date=dates[-1] if dates else "",
        filed_at=form.filed_at,
        shares=shares,
        value=value,
        avg_price=avg_price,
        shares_before=shares_before,
        shares_after=shares_after,
        plan_10b5_1=bool(form.plan_10b5_1),
        plan_purchase=bool(PLAN_PURCHASE_RE.search(plan_text)),
        n_transactions=len(buys),
        url=filing_index_url(form.issuer_cik or primary.cik, form.accession) if form.accession else "",
        owner_ciks=";".join(o.cik.lstrip("0") for o in form.owners),
    )


ENTITY_ROLES = ("10% Owner", "Other")


def owner_set(b: BuyEvent) -> set[str]:
    """Reporting-owner CIKs of a filing (falling back to the primary owner)."""
    ciks = {c for c in (b.owner_ciks or "").split(";") if c}
    return ciks or {b.owner_cik}


def same_purchase(a: BuyEvent, b: BuyEvent) -> bool:
    """Do two filings report one purchase (e.g. a fund and its manager, or a trust and its trustee)?

    They must match on company, trade date, share count and price, and also be
    linked: a shared reporting owner, the same post-trade balance, or a fund/entity
    filer. Two directors who each bought 1,000 shares that day stay separate.
    """
    if a.issuer_cik != b.issuer_cik or a.last_date != b.last_date:
        return False
    if round(a.shares) == 0 or round(a.shares) != round(b.shares):
        return False
    if a.avg_price and b.avg_price and abs(a.avg_price / b.avg_price - 1) > 0.01:
        return False
    if owner_set(a) & owner_set(b):
        return True
    if a.shares_after is not None and a.shares_after == b.shares_after:
        return True
    return a.role in ENTITY_ROLES or b.role in ENTITY_ROLES


def dedupe_purchases(buys: list[BuyEvent]) -> list[BuyEvent]:
    """Drop repeat reports of the same purchase (see same_purchase), keeping the first."""
    kept: dict[tuple[str, str, int], list[BuyEvent]] = {}
    out = []
    for b in buys:
        group = kept.setdefault((b.issuer_cik, b.last_date, round(b.shares)), [])
        if any(same_purchase(k, b) for k in group):
            continue
        group.append(b)
        out.append(b)
    return out


def count_insiders(buys: list[BuyEvent]) -> int:
    """Distinct insiders among filings, treating filings that share any reporting owner
    (one fund family filing jointly, say) as one insider."""
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    roots = []
    for b in buys:
        ciks = sorted(owner_set(b))
        for c in ciks[1:]:
            parent[find(c)] = find(ciks[0])
        roots.append(ciks[0])
    return len({find(r) for r in roots})


def _within(a: str, b: str, days: int) -> bool:
    try:
        return abs((dt.date.fromisoformat(a) - dt.date.fromisoformat(b)).days) <= days
    except ValueError:
        return False


def cluster_size(buy: BuyEvent, peers: list[BuyEvent], window_days: int = CLUSTER_WINDOW_DAYS) -> int:
    """Distinct insiders buying the same issuer within window_days of this buy (itself included).

    Only discretionary buys of at least CLUSTER_MIN_VALUE count as other insiders.
    """
    nearby = [
        p
        for p in peers
        if p.issuer_cik == buy.issuer_cik
        and p.accession != buy.accession
        and p.counts_toward_cluster
        and _within(p.last_date, buy.last_date, window_days)
    ]
    return count_insiders(dedupe_purchases([buy, *nearby]))


def score_buy(buy: BuyEvent, cluster: int = 1) -> Score:
    tags: list[str] = []

    value_pts = 0.0
    if buy.value > 0:
        value_pts = min(30.0, max(0.0, 10 * math.log10(buy.value / 10_000)))

    role_pts = float(ROLE_POINTS.get(buy.role, 4))

    conviction_pts = 0.0
    inc = buy.stake_increase
    if inc is not None:
        if math.isinf(inc):
            conviction_pts = 20.0
            tags.append("New position")
        elif inc > 0:
            conviction_pts = 20.0 * min(1.0, math.sqrt(inc / 0.5))
            tags.append(f"Stake {stake_text(inc)}")

    cluster_pts = {1: 0.0, 2: 12.0, 3: 20.0}.get(cluster, 25.0)
    if cluster > 1:
        tags.append(f"Cluster: {cluster} insiders")

    penalty = 0.0
    if buy.plan_10b5_1:
        penalty += PLAN_PENALTY
        tags.append("10b5-1 plan")
    if buy.plan_purchase:
        penalty += PLAN_PURCHASE_PENALTY
        tags.append("DRIP/purchase plan")
    delay = buy.filing_delay_days
    if delay is not None and delay > LATE_FILING_DAYS:
        penalty += LATE_PENALTY
        tags.append(f"Filed {delay}d late")

    raw = value_pts + role_pts + conviction_pts + cluster_pts - penalty
    return Score(
        total=int(round(min(100.0, max(0.0, raw)))),
        value_pts=value_pts,
        role_pts=role_pts,
        conviction_pts=conviction_pts,
        cluster_pts=cluster_pts,
        penalty=penalty,
        cluster_size=cluster,
        tags=tags,
    )


def stake_text(inc: float | None) -> str:
    if inc is None:
        return ""
    if math.isinf(inc):
        return "New"
    if 0 < inc < 0.01:
        return "+<1%"
    return f"{inc:+.0%}"


def money(v: float) -> str:
    if v >= 1e9:
        return f"${v / 1e9:.1f}B"
    if v >= 1e6:
        return f"${v / 1e6:.1f}M"
    if v >= 1e3:
        return f"${v / 1e3:.0f}K"
    return f"${v:,.0f}"


def qty(v: float) -> str:
    if v >= 1e6:
        return f"{v / 1e6:.2f}M"
    if v >= 1e4:
        return f"{v / 1e3:.0f}K"
    return f"{v:,.0f}"
