---
type: "methodology"
backtest: "2026-10-20"
---

# Methodology

**Data.** SEC Insider Transactions Data Sets (2006q1_form345.zip .. 2026q3_form345.zip (83 files)) plus daily EDGAR filings for the latest weeks.
Only Form 4 open-market purchases (transaction code P) count. Prices are daily, split- and dividend-adjusted, from Yahoo
Finance (snapshot 2026-10-20, last price date 2026-10-19).

**One signal per company per day.** Several insiders filing on the same day share one return, so they count once.
Repeat reports of the same purchase by related filers (a fund and its manager) count once.

**No look-ahead.**
- Entry is the **open of the first trading session after the filing date**, the first price anyone could act on.
  Variant C enters at that session's close.
- Clusters, insider track records and the routine/opportunistic split use only filings and outcomes public
  before entry. A test deletes all later filings and checks the features don't change.
- Bucket edges are fixed numbers, written down in `data/backtest/preregistration.json` before the first run.

**Returns.** Horizons count market sessions (1, 5, 21, 63, 126, 252; 63, about 3 months, is primary). Excess return =
stock minus SPY over the same window. Returns are winsorized at the 1st/99th percentile. Windows that run past the
data are left out, never partial. A stock that stops trading for 10+ sessions has no return for later horizons.

**Survivor index.** Equal-weighted daily returns of every priced stock, each joining only after its first insider
filing is public (joining earlier would select on future insider buys, which tend to follow declines).

**Price checks.** The insider's reported price must be within 0.67-1.5x of the stock's market price on the trade
date. Otherwise the price series is presumed to be a different security (a reused ticker, another share class, an
ADR) or the filing a typo, and the signal is dropped. Tickers resolve through SEC's company ID, never the symbol
alone. Isolated bad ticks and sub-penny days are removed.

**Significance.** Each kind of buy becomes a calendar-time portfolio: every signal held 63 sessions, buy-and-hold
weights, one position per company. Its monthly return minus SPY's is tested with Newey-West t-statistics (3 lags) and a
block bootstrap. 2006-2015 is the discovery period and 2016 onward the holdout. p-values get a Holm correction for the
number of slices tested (52 tests per family). Every test ever run is appended to `data/backtest/tests_log.csv`.

**Verdicts.** ✅ works = significant (after Holm) and positive in both periods, positive when entering a session later,
positive against the survivor index in both periods, and positive in 60%+ of years. 🟡 promising = significant in one
period only. 🔁 reversed = significant in opposite directions in the two periods. ❌ hurts / 🟠 looks negative =
significantly negative. ⚪ no evidence = can't tell from zero. ❔ not enough data = fewer than 200 signals or 60 months
in discovery. Holdout-only findings are Holm-corrected across all slices.

**Portfolio simulation.** $100,000, 20 slots, each signal bought at the next open and held 21/63/126 sessions. When
signals outnumber free slots, the highest scores win. Position size is the smaller of NAV/20, cash and 2% of daily
dollar volume. Only stocks at $2+ trading $1M+/day qualify. Costs per side: under $5: 1%, $5-10: 0.5%, $10-25: 0.25%,
$25+: 0.1%, plus 0.25% if dollar volume is under $5M and 0.25% if the position exceeds 1% of daily volume. Idle cash earns
^IRX 13-week T-bill.

**Known limits.** Prices exist only for companies still listed today (see coverage in the backtest note). That flatters
results, and the survivor index and survivorship bound show by how much. The adjustment is for market beta only (no
size/value factors). The routine/opportunistic split uses purchases only, because sales aren't loaded.

**Changes after the pre-registration** are bug fixes only, each listed in `data/backtest/CHANGES.md`
(found by an independent adversarial review of the code).

**Reproducibility.** Git commit `7ad7d7d`, config hash `7a43c9e85fe88959`, seed 20061.
