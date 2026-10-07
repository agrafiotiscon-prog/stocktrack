"""Command-line interface: python -m stocktrack <command>."""

from __future__ import annotations

import argparse
import datetime as dt
import logging
import os
import sys
import time
import urllib.error
from pathlib import Path

from stocktrack import __version__
from stocktrack.alerts import Notifier, format_alert
from stocktrack.db import Database
from stocktrack.prices import PriceService
from stocktrack.report import render_report
from stocktrack.sec import HttpClient, MissingUserAgent
from stocktrack.signals import money, stake_text
from stocktrack.tracker import IngestResult, Signal, Tracker

DEFAULT_DB = os.environ.get("STOCKTRACK_DB", str(Path.home() / ".stocktrack" / "stocktrack.db"))

log = logging.getLogger("stocktrack")


def _client(args) -> HttpClient:
    return HttpClient(args.user_agent or os.environ.get("STOCKTRACK_USER_AGENT", ""))


def _tracker(args, online: bool) -> Tracker:
    return Tracker(
        Database(args.db),
        client=_client(args) if online else None,
        include_amendments=getattr(args, "amendments", False),
    )


def _since(days: int) -> str:
    return (dt.date.today() - dt.timedelta(days=days)).isoformat()


def _progress(i: int, n: int) -> None:
    if sys.stderr.isatty():
        print(f"\r  fetching filings {i}/{n}", end="" if i < n else "\n", file=sys.stderr, flush=True)


def _cut(s: str, n: int) -> str:
    return s if len(s) <= n else s[: n - 1] + "…"


def print_table(signals: list[Signal], with_prices: bool = False) -> None:
    if not signals:
        print("No insider buys match. Run `scan` or `backfill` to collect filings.")
        return
    head = f"{'SCORE':>5}  {'TICKER':<6}  {'INSIDER':<24}  {'ROLE':<18}  {'TRADED':<10}  {'VALUE':>8}  {'STAKE':>6}"
    if with_prices:
        head += f"  {'NOW':>9}  {'VS PAID':>7}"
    print(head + "  SIGNALS")
    for s in signals:
        b = s.buy
        stake = stake_text(b.stake_increase)
        line = (
            f"{s.score.total:>5}  {_cut(b.ticker or '-', 6):<6}  {_cut(b.owner_name, 24):<24}  "
            f"{_cut(b.officer_title or b.role, 18):<18}  {b.last_date:<10}  "
            f"{money(b.value) if b.value else '-':>8}  {stake:>6}"
        )
        if with_prices:
            q = s.quote
            chg = q.change_from(b.avg_price) if q else None
            line += f"  {f'${q.price:,.2f}' if q else '-':>9}  {f'{chg:+.1%}' if chg is not None else '-':>7}"
        tags = [t for t in s.score.tags if not (t.startswith("Stake ") or t == "New position")]
        print(line + "  " + ", ".join(tags))


def _add_prices(signals: list[Signal]) -> None:
    prices = PriceService()
    for s in signals:
        s.quote = prices.quote(s.buy.ticker)


def _alert_new(tracker: Tracker, result: IngestResult, args, notifier: Notifier) -> int:
    sent = 0
    prices = PriceService() if args.prices else None
    for buy in result.buys:
        sig = tracker.score(buy)
        if sig.score.total < args.min_score or buy.value < args.min_value:
            continue
        if tracker.db.was_alerted(buy.accession):
            continue
        if prices:
            sig.quote = prices.quote(buy.ticker)
        text = format_alert(sig)
        print("\n" + text, flush=True)
        notifier.send(text)
        tracker.db.mark_alerted(buy.accession)
        sent += 1
    return sent


def cmd_scan(args) -> int:
    tracker = _tracker(args, online=True)
    notifier = Notifier.from_env()
    result = tracker.scan_latest(max_pages=args.pages, progress=_progress)
    sent = _alert_new(tracker, result, args, notifier)
    print(
        f"Processed {result.filings} new Form 4 filings: {len(result.buys)} insider buys, "
        f"{sent} alerts" + (f", {result.errors} errors" if result.errors else "")
    )
    return 0


def cmd_watch(args) -> int:
    tracker = _tracker(args, online=True)
    notifier = Notifier.from_env()
    channels = ", ".join(notifier.names) or "console only"
    print(
        f"Watching EDGAR every {args.interval}s for insider buys scoring {args.min_score}+ "
        f"and worth {money(args.min_value)}+ (alerts: {channels}). Ctrl+C to stop.",
        flush=True,
    )
    while True:
        try:
            result = tracker.scan_latest(max_pages=args.pages)
            sent = _alert_new(tracker, result, args, notifier)
            stamp = dt.datetime.now().strftime("%H:%M:%S")
            print(f"[{stamp}] {result.filings} new filings, {len(result.buys)} buys, {sent} alerts", flush=True)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            log.warning("scan failed, will retry: %s", e)
        except Exception:  # e.g. EDGAR serving a malformed feed page; keep the bot alive
            log.exception("scan failed, will retry")
        try:
            time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nStopped.")
            return 0


def cmd_backfill(args) -> int:
    tracker = _tracker(args, online=True)

    def on_day(day: dt.date, refs) -> None:
        if refs is None:
            print(f"{day}: no index yet (holiday, or today's index is published in the evening)")
        else:
            todo = sum(1 for r in refs if not tracker.db.seen(r.accession))
            print(f"{day}: {len(refs)} Form 4 filings ({todo} new)", flush=True)

    result = tracker.backfill(args.days, progress=_progress, on_day=on_day)
    print(
        f"Processed {result.filings} filings: {len(result.buys)} insider buys"
        + (f", {result.errors} errors" if result.errors else "")
    )
    if args.alert:
        _alert_new(tracker, result, args, Notifier.from_env())
    print()
    found = sorted((tracker.score(b) for b in result.buys), key=lambda s: s.score.total, reverse=True)
    print_table(found[:20])
    return 0


def cmd_top(args) -> int:
    tracker = _tracker(args, online=False)
    signals = tracker.ranked(
        since=_since(args.days), ticker=args.ticker, min_score=args.min_score, min_value=args.min_value
    )[: args.limit]
    if args.prices:
        _add_prices(signals)
    print_table(signals, with_prices=args.prices)
    return 0


def cmd_clusters(args) -> int:
    tracker = _tracker(args, online=False)
    clusters = tracker.clusters(since=_since(args.days), min_insiders=args.min_insiders)
    if not clusters:
        print(f"No stocks with {args.min_insiders}+ insiders buying in the last {args.days} days.")
        return 0
    for c in clusters[: args.limit]:
        print(
            f"{c.ticker or '-':<6} {c.issuer_name}: {len(c.insiders)} insiders, "
            f"{money(c.total_value)} from {c.first_date} to {c.last_date}"
        )
        for b in c.insiders:
            print(f"         {_cut(b.owner_name, 30):<30} {_cut(b.officer_title or b.role, 24):<24} {money(b.value):>8}")
    return 0


def cmd_report(args) -> int:
    tracker = _tracker(args, online=False)
    since = _since(args.days)
    signals = tracker.ranked(since=since, min_score=args.min_score, min_value=args.min_value)[: args.limit]
    if args.prices:
        _add_prices(signals)
    clusters = tracker.clusters(since=since)
    html = render_report(signals, clusters, since, dt.date.today().isoformat(), with_prices=args.prices)
    out = Path(args.output)
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({len(signals)} buys, {len(clusters)} clusters)")
    return 0


def cmd_stats(args) -> int:
    for k, v in _tracker(args, online=False).db.stats().items():
        print(f"{k:>12}: {v}")
    return 0


def cmd_test_alert(args) -> int:
    notifier = Notifier.from_env()
    if not notifier.channels:
        print("No alert channels configured. Set STOCKTRACK_DISCORD_WEBHOOK, STOCKTRACK_SLACK_WEBHOOK, "
              "or STOCKTRACK_TELEGRAM_BOT_TOKEN + STOCKTRACK_TELEGRAM_CHAT_ID.")
        return 1
    results = notifier.send("stocktrack test alert: insider buy alerts will appear here.")
    for name, err in results.items():
        print(f"{name}: {'ok' if err is None else 'FAILED - ' + err}")
    return 0 if all(e is None for e in results.values()) else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="stocktrack",
        description="Track significant insider buying from SEC Form 4 filings.",
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument("--db", default=DEFAULT_DB, help="SQLite database path (env STOCKTRACK_DB)")
    p.add_argument("--user-agent", help="SEC contact User-Agent, e.g. 'Jane Doe jane@example.com' "
                   "(env STOCKTRACK_USER_AGENT)")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="command", required=True)

    def alert_opts(sp, min_score=50, min_value=50_000):
        sp.add_argument("--min-score", type=int, default=min_score, help="alert threshold (default %(default)s)")
        sp.add_argument("--min-value", type=float, default=min_value,
                        help="minimum purchase value in dollars (default %(default)s)")
        sp.add_argument("--prices", action="store_true", help="include the current price (Yahoo Finance)")
        sp.add_argument("--amendments", action="store_true", help="also process Form 4/A amendments")

    sp = sub.add_parser("scan", help="process new filings from the live EDGAR feed once")
    sp.add_argument("--pages", type=int, default=10, help="max feed pages of 100 entries (default %(default)s)")
    alert_opts(sp)
    sp.set_defaults(func=cmd_scan)

    sp = sub.add_parser("watch", help="keep scanning and alert on significant buys")
    sp.add_argument("--interval", type=int, default=120, help="seconds between scans (default %(default)s)")
    sp.add_argument("--pages", type=int, default=10, help="max feed pages per scan (default %(default)s)")
    alert_opts(sp)
    sp.set_defaults(func=cmd_watch)

    sp = sub.add_parser("backfill", help="process the past N days of filings from EDGAR's daily indexes")
    sp.add_argument("--days", type=int, default=7, help="calendar days to cover (default %(default)s)")
    sp.add_argument("--alert", action="store_true", help="send alerts for qualifying buys found")
    alert_opts(sp)
    sp.set_defaults(func=cmd_backfill)

    sp = sub.add_parser("top", help="rank stored insider buys")
    sp.add_argument("--days", type=int, default=30, help="look back this many days (default %(default)s)")
    sp.add_argument("--ticker", help="only this ticker")
    sp.add_argument("--min-score", type=int, default=0)
    sp.add_argument("--min-value", type=float, default=0)
    sp.add_argument("--limit", type=int, default=25)
    sp.add_argument("--prices", action="store_true", help="include the current price (Yahoo Finance)")
    sp.set_defaults(func=cmd_top)

    sp = sub.add_parser("clusters", help="stocks where several insiders are buying")
    sp.add_argument("--days", type=int, default=14, help="look back this many days (default %(default)s)")
    sp.add_argument("--min-insiders", type=int, default=2)
    sp.add_argument("--limit", type=int, default=20)
    sp.set_defaults(func=cmd_clusters)

    sp = sub.add_parser("report", help="write an HTML dashboard")
    sp.add_argument("-o", "--output", default="insider_buys.html")
    sp.add_argument("--days", type=int, default=30, help="look back this many days (default %(default)s)")
    sp.add_argument("--min-score", type=int, default=0)
    sp.add_argument("--min-value", type=float, default=0)
    sp.add_argument("--limit", type=int, default=300)
    sp.add_argument("--prices", action="store_true", help="include the current price (Yahoo Finance)")
    sp.set_defaults(func=cmd_report)

    sp = sub.add_parser("stats", help="database summary")
    sp.set_defaults(func=cmd_stats)

    sp = sub.add_parser("test-alert", help="send a test message to configured alert channels")
    sp.set_defaults(func=cmd_test_alert)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )
    try:
        return args.func(args)
    except MissingUserAgent as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 130
