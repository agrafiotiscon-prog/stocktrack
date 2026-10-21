"""Research pipeline: load history, fetch prices, backtest, forward-test ledger, vault.

Local state (not committed): ~/.stocktrack/research.db and ~/.stocktrack/cache/.
Committed state: data/ (backtest summaries, the forward-test ledger) and vault/.
"""

from __future__ import annotations

import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import logging
import os
import subprocess
from pathlib import Path

from stocktrack import backtest as bt
from stocktrack.bulk import download_datasets, quarter_events
from stocktrack.history import BENCHMARK, PriceStore, TickerMap
from stocktrack.researchdb import ResearchDB
from stocktrack.sec import HttpClient

log = logging.getLogger(__name__)

HOME = Path(os.environ.get("STOCKTRACK_HOME", Path.home() / ".stocktrack"))
CACHE = HOME / "cache"


def research_db() -> ResearchDB:
    return ResearchDB(os.environ.get("STOCKTRACK_RESEARCH_DB", HOME / "research.db"))


def price_store(max_age_days: float = 7.0) -> PriceStore:
    return PriceStore(CACHE / "prices", max_age_days=max_age_days)


def load_history(http: HttpClient, db: ResearchDB, refresh_latest: bool = True, echo=print,
                 min_year: int | None = None) -> int:
    """Download any missing quarterly datasets and load their purchases into the research DB.

    The newest quarter is re-downloaded and re-loaded (SEC revises it), older ones only once.
    `min_year` skips older quarters (the daily run only needs a few years of history).
    """
    paths = download_datasets(http, CACHE / "sec-bulk", refresh_latest=refresh_latest, min_year=min_year)
    added = 0
    for i, path in enumerate(paths):
        latest = i == len(paths) - 1
        if db.is_loaded(path.name) and not (latest and refresh_latest):
            continue
        events = quarter_events(path)
        db.add_events(events, source="bulk", loaded_name=path.name)
        added += len(events)
        echo(f"{path.name}: {len(events)} purchase filings")
    return added


def fetch_prices(http: HttpClient, db: ResearchDB, store: PriceStore, echo=print) -> dict:
    """Prefetch price histories for every company in the research DB that is still listed."""
    tickers = TickerMap.load(http, CACHE)
    symbols = {BENCHMARK, HEDGE, "^IRX"}
    how_counts: dict[str, int] = {}
    for e in db.events():
        sym, how = tickers.resolve(e.issuer_cik, e.ticker)
        how_counts[how] = how_counts.get(how, 0) + 1
        if sym:
            symbols.add(sym)
    echo(f"{len(symbols)} symbols to price; event ticker resolution: {how_counts}")

    def progress(i: int, n: int) -> None:
        if i % 250 == 0 or i == n:
            echo(f"  prices {i}/{n}")

    stats = store.prefetch(symbols, progress=progress)
    echo(f"prices: {stats}")
    return stats


PREREGISTRATION = {
    "written": "2026-10-19, before the first full run",
    "question": "Do stocks beat the market after insider open-market purchases, and which kinds of purchase work best?",
    "sample": "SEC Form 4 open-market purchases (code P), 2006 onward, one signal per company per filing day; "
              "study sample needs a verified price, raw price >= $1 and 20-day dollar volume >= $100K.",
    "primary_horizon_sessions": bt.PRIMARY,
    "other_horizons": [h for h in bt.HORIZONS if h != bt.PRIMARY],
    "benchmark": "SPY (buy-and-hold, same entry and exit days); secondary: equal-weighted survivor index",
    "entry": "open of the first session after the filing date; variant C enters at that session's close",
    "discovery_period": f"2006-01-01 to {bt.DISCOVERY_END}",
    "holdout_period": f"{bt.DISCOVERY_END} onward",
    "significance": "calendar-time portfolios held 63 sessions, monthly excess over SPY, Newey-West t (3 lags), "
                    "Holm correction within each family",
    "minimum_data": f"{bt.MIN_SIGNALS}+ signals and {bt.MIN_MONTHS}+ usable months in discovery",
    "slices": {
        "role": ["CEO", "CFO", "President/Chair", "Other exec", "Director", "10% owner", "Other"],
        "value": ["<$25K", "$25-100K", "$100-250K", "$250K-1M", "$1M+"],
        "stake_increase": ["<5%", "5-25%", "25-100%", "100%+", "new position", "unknown"],
        "cluster": ["1 insider", "2 insiders", "3+ insiders"],
        "insider_type": ["routine", "opportunistic", "unclassified"],
        "track_record": ["none", "good", "poor"],
        "prior_3m_return": ["down 30%+", "down 10-30%", "flat", "up 10-30%", "up 30%+"],
        "price": ["$1-5", "$5-20", "$20+"],
        "liquidity": ["$100K-1M/day", "$1-10M/day", "$10-100M/day", "$100M+/day"],
        "score": ["0-19", "20-39", "40-59", "60-79", "80+"],
        "plan_purchase": ["discretionary", "DRIP/plan"],
        "filing_delay": ["0-2 days", "3-10 days", "11+ days"],
        "insider_novelty": ["first buy in 12m", "repeat buyer"],
        "company_novelty": ["first insider buy in 12m", "recent insider buys"],
    },
    "strategies": {k: v[0] for k, v in bt.STRATEGIES.items()},
    "walk_forward": "score threshold in {40, 50, 60, 70}, chosen each year from 2011 by calendar-time Sharpe "
                    "on months already realized",
    "verdict_rule": {
        "works": "positive with Holm p < 0.05 in discovery AND same sign with Holm p < 0.05 in holdout AND "
                 "positive under entry variant C AND positive against the survivor index AND positive in 60%+ of years",
        "promising": "passes in only one period",
        "hurts": "significantly negative in both periods",
        "no evidence": "otherwise",
        "not enough data": "fails the minimum-data rule (decided on counts only)",
    },
}


def config_hash() -> str:
    h = hashlib.sha256()
    for mod in ("backtest.py", "signals.py", "bulk.py", "history.py"):
        h.update((Path(__file__).parent / mod).read_bytes())
    return h.hexdigest()[:16]


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                              cwd=Path(__file__).parent, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


HEDGE = "IWM"  # Russell 2000 ETF: a tradable small-cap hedge


def daily_returns(store: PriceStore, symbol: str, cal: bt.Calendar) -> list[float] | None:
    """Close-to-close returns of `symbol` on the benchmark calendar (0 on missing days)."""
    try:
        h = store.get(symbol)
    except Exception:  # best effort
        h = None
    if h is None:
        return None
    closes = dict(zip(h.dates, h.close))
    out, prev = [], None
    for d in cal.dates:
        c = closes.get(d)
        out.append(c / prev - 1 if c and prev else 0.0)
        prev = c or prev
    return out


def risk_free(store: PriceStore, cal: bt.Calendar) -> tuple[list[float] | None, str]:
    """Daily T-bill return from Yahoo's ^IRX (13-week yield, %), carried forward; None if unavailable."""
    try:
        irx = store.get("^IRX")
    except Exception:  # best effort
        irx = None
    if irx is None:
        return None, "0 (^IRX unavailable)"
    by_day = dict(zip(irx.dates, irx.close))
    out, last = [], 0.0
    for d in cal.dates:
        if d in by_day and 0 <= by_day[d] < 25:
            last = by_day[d] / 100 / 252
        out.append(last)
    return out, "^IRX 13-week T-bill"


def run_full_backtest(http: HttpClient, db: ResearchDB, store: PriceStore, out_dir: str | Path,
                      echo=print) -> dict:
    """Run the backtest on everything in the research DB and write results to out_dir."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    tickers = TickerMap.load(http, CACHE)
    buys = db.events()
    echo(f"{len(buys)} filings in the research DB")

    def progress(i: int, n: int) -> None:
        if i % 1000 == 0 or i == n:
            echo(f"  priced {i}/{n} symbols")

    evs, cal, meta = bt.build_events(buys, store, tickers, progress)
    rf, rf_note = risk_free(store, cal)
    hedge = daily_returns(store, HEDGE, cal)
    result = bt.run_backtest(evs, cal, echo=echo, rf_daily=rf, hedge_daily=hedge)
    zips = sorted(p.name for p in (CACHE / "sec-bulk").glob("*.zip"))
    snapshot = max((p.stat().st_mtime for p in (CACHE / "prices").glob("*.json.gz")), default=0)
    result["meta"] = {
        "run_date": dt.date.today().isoformat(), "git_commit": git_commit(), "config_hash": config_hash(),
        "datasets": f"{zips[0]} .. {zips[-1]} ({len(zips)} files)" if zips else "",
        "price_snapshot": dt.datetime.fromtimestamp(snapshot, dt.timezone.utc).date().isoformat() if snapshot else "",
        "last_price_date": cal.dates[-1], "seed": bt.SEED, "risk_free": rf_note, **meta,
    }
    (out / "latest.json").write_text(json.dumps(result, indent=1, default=_json_default))
    (out / f"{result['meta']['run_date']}.json.gz").write_bytes(
        gzip.compress(json.dumps(result, default=_json_default).encode()))
    _write_insider_records(out / "insider_track.csv.gz", bt.insider_records(evs, result_bounds(result)))
    _append_tests_log(out / "tests_log.csv", result)
    _write_signals(HOME / "research" / "signals.csv.gz", evs)
    write_advisor(evs, cal, out, echo)
    echo(f"wrote {out / 'latest.json'}")
    return result


def write_advisor(evs: list[bt.Ev], cal: bt.Calendar, out_dir: str | Path, echo=print) -> Path:
    """Fit and validate the signal-strength model behind the dashboard's report cards."""
    from stocktrack import advisor

    path = Path(out_dir) / "advisor.json"
    path.write_text(json.dumps(advisor.fit(evs, cal, echo=echo), indent=1, allow_nan=False))
    return path


def refit_advisor(http: HttpClient, db: ResearchDB, store: PriceStore, out_dir: str | Path, echo=print) -> Path:
    """Rebuild the events and refit only the advisor (no full backtest)."""
    evs, cal, _ = bt.build_events(db.events(), store, TickerMap.load(http, CACHE))
    bt.add_pit_features(evs)
    return write_advisor(evs, cal, out_dir, echo)


def result_bounds(result: dict) -> tuple[float, float]:
    lo, hi = result["winsor"][str(bt.PRIMARY)]
    return lo, hi


def _json_default(o):
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, (set, tuple)):
        return list(o)
    return str(o)


def _write_insider_records(path: Path, records: dict[str, tuple[int, float]]) -> None:
    rows = ["owner_cik,n,mean_abn63"] + [f"{k},{n},{m:.5f}" for k, (n, m) in sorted(records.items())]
    path.write_bytes(gzip.compress(("\n".join(rows) + "\n").encode()))


def load_insider_records(path: str | Path) -> dict[str, tuple[int, float]]:
    p = Path(path)
    if not p.exists():
        return {}
    out = {}
    for row in csv.DictReader(gzip.decompress(p.read_bytes()).decode().splitlines()):
        out[row["owner_cik"]] = (int(row["n"]), float(row["mean_abn63"]))
    return out


def _append_tests_log(path: Path, result: dict) -> None:
    """Every test ever run, so the number of tests behind each p-value is on record."""
    new = not path.exists()
    with path.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_date", "config_hash", "family", "test", "period", "months", "excess_mean", "t", "p",
                        "p_holm", "verdict"])
        run, cfg = result["meta"]["run_date"], result["meta"]["config_hash"]
        for feat, rows in result["slices"].items():
            for label, r in rows.items():
                for period, key in (("discovery", "p_holm_discovery"), ("holdout", "p_holm_holdout")):
                    s = r[period]
                    w.writerow([run, cfg, "slice_vs_spy", f"{feat}={label}", period, s.get("months", 0),
                                _f(s.get("excess_mean")), _f(s.get("t")), _f(s.get("p")), _f(r.get(key)),
                                r.get("verdict", "")])
                s = r["vs_all_buys"]
                w.writerow([run, cfg, "slice_vs_all_buys", f"{feat}={label}", "full", s.get("months", 0),
                            _f(s.get("excess_mean")), _f(s.get("t")), _f(s.get("p")), _f(r.get("p_holm_vs_all")),
                            r.get("vs_all_verdict", "")])


def _f(x) -> str:
    return "" if x is None else f"{x:.6g}"


def _write_signals(path: Path, evs: list[bt.Ev]) -> None:
    """Every signal with its features, prices and outcomes (local only; too big for git)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = ["accession", "filed", "ticker", "symbol", "status", "issuer", "insider", "role", "value", "score",
            "cluster", "kind", "track_n", "track", "price", "adv", "prior_ret", "entry_date"] + [
        f"abn_{h}" for h in bt.HORIZONS]
    with gzip.open(path, "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for e in evs:
            b = e.buy
            w.writerow([b.accession, e.filed, b.ticker, e.symbol or "", e.status, b.issuer_name, b.owner_name, b.role,
                        f"{b.value:.0f}", e.score, e.cluster, e.kind, e.track_n, _f(e.track), _f(e.price), _f(e.adv),
                        _f(e.prior_ret), e.entry_date or ""] + [_f(e.abn.get(h)) for h in bt.HORIZONS])


# --- daily routine -------------------------------------------------------------

LIVE_DIR = "live"
DAILY_HISTORY_YEARS = 4  # enough for clusters, novelty and the 3-year routine/opportunistic test
BACKTEST_MAX_AGE_DAYS = 7


def _read_gz_lines(path: Path) -> list[str]:
    return gzip.decompress(path.read_bytes()).decode().splitlines() if path.exists() else []


def _write_gz_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(("\n".join(lines) + "\n").encode(), mtime=0))


def _live_buys_load(path: Path) -> list:
    from stocktrack.ledger import parse_buy

    return [parse_buy(r) for r in csv.DictReader(_read_gz_lines(path)) if r.get("accession")]


def _live_buys_save(path: Path, buys: list) -> None:
    from stocktrack.ledger import BUY_FIELDS, _fmt

    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(BUY_FIELDS)
    for b in sorted({b.accession: b for b in buys}.values(), key=lambda b: (b.filed_at, b.accession)):
        w.writerow([_fmt(getattr(b, f)) for f in BUY_FIELDS])
    _write_gz_lines(path, buf.getvalue().splitlines())


def write_dashboard(data_dir: str | Path = "data", out_dir: str | Path = "dashboard", today: str | None = None) -> Path:
    """Regenerate the HTML dashboard from the committed results."""
    from stocktrack import ledger as led
    from stocktrack.dashboard import build_dashboard

    data = Path(data_dir)
    res = json.loads((data / "backtest" / "latest.json").read_text())
    hyp_path = data / "backtest" / "hypotheses.json"
    hypotheses = json.loads(hyp_path.read_text()) if hyp_path.exists() else None
    return build_dashboard(out_dir, res, led.load(data / "picks.csv"), hypotheses, today)


def daily(http: HttpClient, data_dir: str | Path = "data", vault_dir: str | Path = "vault",
          today: str | None = None, force_backtest: bool = False, scan_days: int = 5, echo=print,
          dashboard_dir: str | Path | None = "dashboard") -> dict:
    """One research cycle: collect new buys, log qualifying ones, update outcomes, refresh the vault and dashboard.

    Runs a full backtest too when the last one is older than a week (or when forced).
    """
    from stocktrack import ledger as led
    from stocktrack import vault as vlt
    from stocktrack.bulk import quarter_end
    from stocktrack.db import Database
    from stocktrack.tracker import Tracker

    data = Path(data_dir)
    today = today or dt.date.today().isoformat()
    summary: dict = {}
    db = research_db()

    # 1. History: recent bulk quarters (all of them when a backtest is due).
    latest_path = data / "backtest" / "latest.json"
    last_bt = json.loads(latest_path.read_text())["meta"]["run_date"] if latest_path.exists() else "1900-01-01"
    backtest_due = force_backtest or (dt.date.fromisoformat(today) - dt.date.fromisoformat(last_bt)).days >= BACKTEST_MAX_AGE_DAYS
    min_year = None if backtest_due else dt.date.fromisoformat(today).year - DAILY_HISTORY_YEARS
    load_history(http, db, refresh_latest=True, echo=echo, min_year=min_year)
    zips = sorted((CACHE / "sec-bulk").glob("*q*_form345.zip"))
    bulk_through = quarter_end(zips[-1].name) if zips else "2000-01-01"
    summary["SEC datasets through"] = bulk_through

    # 2. Live filings since the bulk data ends.
    live_path, seen_path = data / LIVE_DIR / "buys.csv.gz", data / LIVE_DIR / "seen.txt.gz"
    live_buys = [b for b in _live_buys_load(live_path) if b.filed_at[:10] > bulk_through]
    seen = set(_read_gz_lines(seen_path))
    tdb = Database(":memory:")
    for acc in seen:
        tdb.conn.execute("INSERT OR IGNORE INTO filings (accession, processed_at) VALUES (?, ?)", (acc, today))
    for b in live_buys:
        tdb.record_filing(b.accession, "4", b.issuer_cik, b)
    tracker = Tracker(tdb, http)
    start = max(dt.date.fromisoformat(bulk_through) + dt.timedelta(days=1),
                dt.date.fromisoformat(today) - dt.timedelta(days=scan_days))
    gap = (dt.date.fromisoformat(today) - start).days + 1
    res_live = tracker.backfill(gap, end=dt.date.fromisoformat(today))
    res_feed = tracker.scan_latest(max_pages=20)
    new_buys = res_live.buys + res_feed.buys
    live_buys += new_buys
    summary["Form 4 filings processed"] = res_live.filings + res_feed.filings
    summary["new insider buys"] = len(new_buys)
    # Remember every filing processed since the bulk data ends, so later runs skip them.
    seen = {r[0] for r in tdb.conn.execute("SELECT accession FROM filings")}
    db.add_events(live_buys, source="live")
    _live_buys_save(live_path, live_buys)
    _write_gz_lines(seen_path, sorted(seen))

    # 3. Backtest if due (also refreshes every price history).
    store = price_store(max_age_days=0.5)
    if backtest_due:
        fetch_prices(http, db, store, echo=echo)
        run_full_backtest(http, db, price_store(max_age_days=365), data / "backtest", echo=echo)
        summary["backtest"] = "re-run"
    res = json.loads(latest_path.read_text())
    records = load_insider_records(data / "backtest" / "insider_track.csv.gz")

    # 4. Point-in-time features for recent buys, then log the qualifying new ones.
    tickers = TickerMap.load(http, CACHE)
    since = (dt.date.fromisoformat(today) - dt.timedelta(days=365 * DAILY_HISTORY_YEARS)).isoformat()
    evs = [bt.Ev(buy=b, filed=b.filed_at[:10]) for b in
           bt.dedupe_purchases(sorted(db.events(since=since), key=lambda b: (b.filed_at[:10], b.accession)))]
    bt.add_pit_features(evs)
    ledger_path = data / "picks.csv"
    ledger = led.load(ledger_path)
    logged = {r["accession"] for r in ledger}
    window = (dt.date.fromisoformat(today) - dt.timedelta(days=scan_days + 3)).isoformat()
    try:
        spy = store.get(BENCHMARK, refresh=True)
    except Exception as e:  # log today's buys anyway; outcomes catch up on the next run
        log.warning("SPY refresh failed, using the cached history: %s", e)
        spy = None
    spy = spy or store.load(BENCHMARK)
    if spy is None:
        raise RuntimeError("no SPY history")
    cal = bt.Calendar(spy)
    new_rows = []
    for ev in evs:
        if ev.filed < window or ev.buy.accession in logged:
            continue
        ev.symbol, ev.resolve = tickers.resolve(ev.buy.issuer_cik, ev.buy.ticker)
        if not ev.symbol:
            continue
        rec = records.get(ev.buy.owner_cik)
        if rec:
            n, mean = rec
            ev.track_n, ev.track = n, (n / (n + 5)) * mean
        try:
            hist = store.get(ev.symbol)
        except Exception as e:  # one failed download shouldn't stop the run
            log.warning("price download failed for %s: %s", ev.symbol, e)
            continue
        if hist is None:
            continue
        aligned, _ = bt.align(hist, cal)
        bt.attach_market_data(ev, aligned, cal)
        if led.qualifies(ev):
            new_rows.append(led.new_row(ev, ""))
            logged.add(ev.buy.accession)
    # Stamp the rows when they are written: is_forward() trusts this time.
    stamp = led.now_utc()
    for row in new_rows:
        row["logged"] = stamp
    ledger += new_rows
    summary["buys logged to the forward test"] = len(new_rows)
    led.save(ledger_path, ledger)  # keep today's rows even if a later step fails

    # 5. Outcomes.
    changed, matured = led.update_outcomes(ledger, store, cal)
    summary["ledger rows updated"] = changed
    summary["outcomes matured"] = len(matured)
    stopped = sum(1 for r in ledger if r["status"] == "break")
    if stopped:
        summary["rows stopped at a data break (check by hand)"] = stopped
    led.save(ledger_path, ledger)

    # 6. Vault.
    n = vlt.build_vault(vault_dir, res, ledger, records, today=today, run_summary=summary, matured=matured)
    summary["vault notes written"] = n
    if dashboard_dir:
        write_dashboard(data, dashboard_dir, today)
    for k, v in summary.items():
        echo(f"{k}: {v}")
    return summary
