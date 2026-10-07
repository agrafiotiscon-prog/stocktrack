# stocktrack

An insider-buying tracker. It watches SEC EDGAR for Form 4 filings, pulls out the
open-market purchases that company insiders make with their own money, scores how
significant each one is, spots clusters of insiders buying the same stock, and
alerts you on Discord, Slack or Telegram.

Insider trades are public: officers, directors and 10% holders must report them
on a Form 4 within two business days. Most of that flow is noise (option
exercises, grants, tax sales, pre-scheduled plans). The signal people look for is
**open-market buying** (transaction code `P`), and especially big buys by the CEO
or CFO that meaningfully grow their stake, or several insiders buying at once.

```
$ stocktrack top --days 10 --prices
SCORE  TICKER  INSIDER                   ROLE                TRADED         VALUE   STAKE        NOW  VS PAID  SIGNALS
   68  PSUS    ISRAEL RYAN               Chief Investment …  2026-10-06     $9.6M    +51%     $37.74    +0.7%
   65  NXH     LEMONIS MARCUS            EXECUTIVE CHAIRMA…  2026-10-06     $1.0M    +51%      $1.83   -33.7%
   48  AXIA3   Batista de Lima Filho P…  Director            2026-10-02     $5.3M    +10%          -        -
   46  BORR    Troim Tor Olav            Director            2026-10-05     $6.2M     +5%      $4.21    +1.9%
   46  HRL     Newlands William A        Chair               2026-10-05     $201K    +15%     $19.88    -1.1%
   25  UXIN    Dai Kun                   Chief Executive O…  2026-10-05      $11K    +28%      $1.25    -1.5%  10b5-1 plan
```

No API keys and no dependencies: just Python 3.10+ and the public EDGAR endpoints.

## Quick start

```bash
pip install -e .            # or run without installing: python -m stocktrack ...

# The SEC requires automated tools to identify themselves with a contact email.
export STOCKTRACK_USER_AGENT="Your Name you@example.com"

stocktrack backfill --days 14   # load the last two weeks (about a minute per trading day)
stocktrack top                  # best-scoring buys of the last 30 days
stocktrack clusters             # stocks where several insiders are buying
stocktrack report --prices      # write insider_buys.html, a sortable dashboard
stocktrack watch                # poll EDGAR every 2 minutes and alert on new significant buys
```

## Commands

| Command | What it does |
| --- | --- |
| `scan` | Process new filings from EDGAR's live feed once, alerting on qualifying buys. Good for cron. |
| `watch` | Run `scan` in a loop (`--interval` seconds, default 120). |
| `backfill --days N` | Process the last N calendar days from EDGAR's daily indexes (published each evening). |
| `top` | Rank stored buys. `--days`, `--ticker`, `--min-score`, `--min-value`, `--limit`, `--prices`. |
| `clusters` | Stocks with 2+ distinct insiders buying in the last `--days` (default 14). |
| `report` | Write an HTML dashboard (`-o`, `--days`, `--prices`). |
| `stats` | Database summary. |
| `test-alert` | Send a test message to the configured alert channels. |

`scan`, `watch` and `backfill --alert` send an alert when a new buy scores at least
`--min-score` (default 50) and is worth at least `--min-value` (default $50,000).
Add `--prices` to include the current price in alerts. Each buy is alerted once.

Filings are stored in SQLite at `~/.stocktrack/stocktrack.db` (override with
`--db` or `STOCKTRACK_DB`), so each filing is downloaded only once.

## How buys are scored (0-100)

Each Form 4 with open-market purchases becomes one buy event.

| Component | Points | Why |
| --- | --- | --- |
| Value | up to 30 | Dollars spent, on a log scale: $100K = 10, $1M = 20, $10M = 30. |
| Role | up to 25 | CEO 25; CFO, President, Chair 22; other C-suite 18; officers 14; directors 12; 10% holders 8. |
| Conviction | up to 20 | How much the purchase grew the insider's holding. +50% or more, or a brand-new position, scores full. |
| Cluster | up to 25 | Distinct insiders each buying $25K+ of the same stock within 14 days: 2 = 12, 3 = 20, 4+ = 25. |
| Penalties | -30 / -15 / -10 | Automatic plan purchases (dividend reinvestment, employee or director stock purchase plans, deferred comp); purchases under a pre-scheduled Rule 10b5-1 plan; filings made more than 10 days after the trade. |

60+ is labelled **Strong** (for example, a CEO spending $1M to grow their stake by half),
40+ **Notable**. In the HTML report, hover a score to see its breakdown.

Some details:
- Only non-derivative `P` transactions count, so option exercises, grants, gifts and sales are ignored.
- Some plans also report their buys as code `P`: a board of directors buying through dividend reinvestment
  all on the same day, say. Footnotes on the trade and the filing's remarks are checked for that language.
  These buys get the -30 penalty and never count toward a cluster.
- Rankings and alerts skip issuers you can't trade on an exchange: no ticker (private funds, non-traded
  BDCs) or a mutual-fund ticker (interval funds). They are still stored; add `--include-funds` to see them.
- Joint filings (a fund and its manager, say) are attributed to the most senior reporting owner.
- When related entities file separate Form 4s for the same shares on the same day, they count as one purchase, so they don't inflate clusters or the rankings.
- Form 4/A amendments are skipped by default to avoid double counting (`--amendments` to include them).
- `top`, `clusters` and `report` filter on **trade date**, not filing date.

## Alerts

Set any of these environment variables, then run `stocktrack test-alert`:

| Channel | Variables |
| --- | --- |
| Discord | `STOCKTRACK_DISCORD_WEBHOOK` (channel settings, Integrations, Webhooks) |
| Slack | `STOCKTRACK_SLACK_WEBHOOK` (an incoming-webhook URL) |
| Telegram | `STOCKTRACK_TELEGRAM_BOT_TOKEN` (from @BotFather) and `STOCKTRACK_TELEGRAM_CHAT_ID` |

Alerts always print to the console too. A typical one:

```
🔥 Strong insider buy: NXH (score 65/100)
NEIGHBORHOOD INTELLIGENCE, INC.
LEMONIS MARCUS (EXECUTIVE CHAIRMAN & CEO) bought 362K sh @ $2.76 = $1.0M on 2026-10-06
Stake +51%
https://www.sec.gov/Archives/edgar/data/1130713/000113647826000010/0001136478-26-000010-index.htm
```

## Running it continuously

Either keep `stocktrack watch` running (tmux, screen, a systemd service), or call
`scan` from cron. EDGAR accepts filings on weekdays from 6am to 10pm Eastern:

```cron
*/5 6-22 * * 1-5  STOCKTRACK_USER_AGENT="Your Name you@example.com" STOCKTRACK_DISCORD_WEBHOOK="https://..." /path/to/stocktrack scan
```

## Data sources and limits

- **SEC EDGAR**: the [latest-filings feed](https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4)
  for live scanning and the [daily form indexes](https://www.sec.gov/Archives/edgar/daily-index/) for backfills.
  Requests are throttled to 8 per second, under the SEC's 10/s
  [fair-access limit](https://www.sec.gov/os/accessing-edgar-data), and retried with backoff on 429/5xx.
- **Prices** (`--prices`): Yahoo Finance's public chart endpoint. It is unofficial and can break; when it
  does, prices just show as `-`. Tickers are taken from the filing, so foreign issuers that report a
  home-market symbol (like `AXIA3`) may not resolve.

## Development

```bash
python -m unittest discover -s tests -t .
```

The tests run offline against synthetic filings.

## Disclaimer

This tool surfaces public regulatory filings. It is not investment advice, and
insider buying does not guarantee that a stock will go up.
