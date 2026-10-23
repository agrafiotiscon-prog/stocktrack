"""Forward-test ledger: every qualifying live buy, logged when filed, with outcomes as they mature.

This is the out-of-sample test that can't be overfit: rows are written before
their outcome exists and are never re-scored. Each run records the latest price
too, so a stock that is later delisted keeps its last known outcome instead of
silently vanishing (which is what makes historical backtests on free data
optimistic).
"""

from __future__ import annotations

import csv
import dataclasses
import datetime as dt
import logging
from pathlib import Path

from stocktrack.backtest import (HORIZONS, SIM_MIN_ADV, SIM_MIN_PRICE, STRATEGIES, Calendar, Ev, align,
                                 attach_market_data)
from stocktrack.history import PriceStore
from stocktrack.signals import BuyEvent, is_listed_stock

log = logging.getLogger(__name__)

LEDGER_HORIZONS = (5, 21, 63, 126, 252)
_BUY_FIELDS = [f.name for f in dataclasses.fields(BuyEvent)]
FEATURE_FIELDS = ["symbol", "score", "cluster", "kind", "track_n", "track", "first_in_year_insider",
                  "first_in_year_issuer", "prior_ret", "price", "adv", "strategies",
                  "tier", "tilt"]  # signal-desk profile when logged (from 2026-10-23)
OUTCOME_FIELDS = (["entry_date", "entry_price", "last_seen", "last_price", "status", "ret_now", "abn_now"]
                  + [f"ret_{h}" for h in LEDGER_HORIZONS] + [f"abn_{h}" for h in LEDGER_HORIZONS])
COLUMNS = ["logged"] + _BUY_FIELDS + FEATURE_FIELDS + OUTCOME_FIELDS

_FLOAT = {"shares", "value", "avg_price", "shares_before", "shares_after", "track", "prior_ret", "price", "tilt",
          "adv", "entry_price", "last_price", "ret_now", "abn_now"} | {f"ret_{h}" for h in LEDGER_HORIZONS} | {
              f"abn_{h}" for h in LEDGER_HORIZONS}
_INT = {"n_transactions", "score", "cluster", "track_n"}
_BOOL = {"plan_10b5_1", "plan_purchase", "first_in_year_insider", "first_in_year_issuer"}


def _parse(row: dict[str, str]) -> dict:
    out: dict = {}
    for k in COLUMNS:
        v = row.get(k, "")
        if k in _FLOAT:
            out[k] = float(v) if v not in ("", None) else None
        elif k in _INT:
            out[k] = int(float(v)) if v not in ("", None) else 0
        elif k in _BOOL:
            out[k] = v in ("1", "True", "true")
        else:
            out[k] = v or ""
    return out


def _fmt(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "1" if v else "0"
    if isinstance(v, float):
        return f"{v:.6g}"
    return str(v)


def load(path: str | Path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return [_parse(r) for r in csv.DictReader(f)]


def save(path: str | Path, rows: list[dict]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: (r["filed_at"], r["accession"]))
    tmp = p.with_suffix(".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([_fmt(r.get(k)) for k in COLUMNS])
    tmp.replace(p)


def to_buy(row: dict) -> BuyEvent:
    return BuyEvent(**{f: row[f] for f in _BUY_FIELDS})


BUY_FIELDS = _BUY_FIELDS


def parse_buy(row: dict[str, str]) -> BuyEvent:
    """BuyEvent from a CSV row of its fields (as written by _fmt)."""
    return to_buy(_parse({k: row.get(k, "") for k in COLUMNS}))


def qualifies(ev: Ev) -> bool:
    """Ledger universe: discretionary buys of listed, liquid stocks whose price checks out."""
    return (ev.symbol is not None and is_listed_stock(ev.symbol) and not ev.buy.plan_purchase
            and ev.status in ("priced", "awaiting_entry")
            and (ev.price or 0) >= SIM_MIN_PRICE and (ev.adv or 0) >= SIM_MIN_ADV)


def new_row(ev: Ev, logged: str) -> dict:
    row = {k: None for k in OUTCOME_FIELDS}
    row.update({"logged": logged, "entry_date": "", "last_seen": "", **dataclasses.asdict(ev.buy)})
    row.update({
        "symbol": ev.symbol, "score": ev.score, "cluster": ev.cluster, "kind": ev.kind,
        "track_n": ev.track_n, "track": ev.track, "first_in_year_insider": ev.first_in_year_insider,
        "first_in_year_issuer": ev.first_in_year_issuer, "prior_ret": ev.prior_ret, "price": ev.price,
        "adv": ev.adv, "strategies": "|".join(k for k, (_, pred) in STRATEGIES.items() if pred(ev)),
        "status": "pending",
    })
    return row


def update_outcomes(rows: list[dict], store: PriceStore, cal: Calendar,
                    refresh: bool = True) -> tuple[int, list[tuple[int, dict]]]:
    """Fill entries and matured returns from fresh prices.

    Returns (rows changed, [(horizon, row)] for horizons that matured in this update).
    """
    changed, matured = 0, []
    for row in rows:
        if row["status"] in ("closed", "break"):
            continue
        try:
            hist = store.get(row["symbol"], refresh=refresh) if row["symbol"] else None
        except Exception as e:  # a failed download leaves the row as it was until the next run
            log.warning("price update failed for %s: %s", row["symbol"], e)
            continue
        if hist is None:
            if row["status"] == "open":
                row["status"] = "dead"  # symbol vanished: keep the last known price
                changed += 1
            continue
        hist, _ = align(hist, cal)
        ev = Ev(buy=to_buy(row), filed=row["filed_at"][:10])
        attach_market_data(ev, hist, cal, verify=False)
        if ev.entry_date is None:
            continue
        before = (row["entry_date"], row["last_seen"], row["status"])
        entry_px = hist.open[hist.dates.index(ev.entry_date)]
        # A data break after entry (a split Yahoo missed) ends the row: later prices are wrong.
        brk = next((d for d in hist.breaks if d > ev.entry_date), None)
        last = hist.dates.index(brk) - 1 if brk else len(hist.dates) - 1
        row["entry_date"], row["entry_price"] = ev.entry_date, entry_px
        row["last_seen"], row["last_price"] = hist.dates[last], hist.close[last]
        for h in LEDGER_HORIZONS:
            if h in ev.ret:
                if row[f"ret_{h}"] is None:
                    matured.append((h, row))
                row[f"ret_{h}"], row[f"abn_{h}"] = ev.ret[h], ev.abn[h]
        # Mark to market: entry to the latest close, against SPY over the same days.
        row["ret_now"] = hist.close[last] / entry_px - 1
        c_last = cal.index.get(hist.dates[last])
        if c_last is not None and c_last >= ev.entry_cal:
            spy_now = cal.spy.close[c_last] / cal.spy.open[ev.entry_cal] - 1
            row["abn_now"] = row["ret_now"] - spy_now
        if row[f"ret_{LEDGER_HORIZONS[-1]}"] is not None:
            row["status"] = "closed"
        elif brk:
            row["status"] = "break"  # final; reported in the daily summary for a manual check
        elif c_last is None or c_last < len(cal.dates) - 10:
            row["status"] = "dead"  # stopped trading; ret_now is its final outcome
        else:
            row["status"] = "open"
        changed += before != (row["entry_date"], row["last_seen"], row["status"])
    return changed, matured


def today_iso() -> str:
    return dt.date.today().isoformat()


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# 9:30 New York is 13:30 UTC in summer and 14:30 in winter; the earlier time is the safe cut-off.
OPEN_UTC = "T13:30:00Z"


def is_forward(row: dict) -> bool:
    """Was the row logged before its entry session opened? Only those count as a forward test.

    A date-only stamp (older rows) is taken as the end of that day, the safe assumption.
    """
    logged = row["logged"] if "T" in row["logged"] else row["logged"] + "T23:59:59Z"
    return bool(row["entry_date"]) and logged < row["entry_date"] + OPEN_UTC


assert set(LEDGER_HORIZONS) <= set(HORIZONS)
