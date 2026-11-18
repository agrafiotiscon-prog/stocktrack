---
type: "home"
updated: "2026-11-18"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-18 Backtest]]: the latest full backtest
- [[2026-11-18]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,092 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.815).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.6% a year after costs with a 40% max drawdown, against SPY's +10.8% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.7%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[TSM]] | [[BURNS URSULA M]] | Director | $500K | 60 | – |
| 2026-11-17 | [[MP]] | [[Corbett Ryan]] | Chief Financial Officer | $92K | 56 | – |
| 2026-11-17 | [[STEW]] | [[Quinlan Shane Kevin]] | Director | $100K | 42 | – |
| 2026-11-17 | [[RMIX]] | [[Fleming Ned N III]] | Director | $238K | 46 | – |
| 2026-11-17 | [[RMIX]] | [[Wentroth Thomas G]] | Chief Financial Officer | $995 | 54 | – |
| 2026-11-17 | [[ECC]] | [[Onorio Kenneth P]] | CFO / COO | $104K | 45 | – |
| 2026-11-17 | [[STUB]] | [[Bhargava Sameer]] | Director | $1.5M | 66 | – |
| 2026-11-17 | [[STUB]] | [[Raab Andrew John]] | Director | $2.0M | 67 | – |
| 2026-11-17 | [[FISN]] | [[JANOVER BLAKE]] | Director | $11K | 44 | – |
| 2026-11-17 | [[FISN]] | [[Muller Richard]] | Chief Technology Officer | $32K | 43 | – |
| 2026-11-17 | [[ATEC]] | [[Koning John Todd]] | CHIEF FINANCIAL OFFICER | $99K | 48 | – |
| 2026-11-17 | [[PRAA]] | [[FREDRICKSON STEVEN D]] | Chair | $295K | 57 | – |
| 2026-11-17 | [[NPCE]] | [[Williams Patrick F]] | Chief Financial Officer | $99K | 56 | – |
| 2026-11-17 | [[NPCE]] | [[Becker Joel]] | CHIEF EXECUTIVE OFFICER | $99K | 55 | – |
| 2026-11-17 | [[UPST]] | [[Gu Paul]] | Chief Executive Officer | $950K | 60 | – |


## Live queries (Dataview plugin)

```dataview
TABLE ticker, insider, role, score, value, abn_now AS "vs SPY so far", status
FROM "Signals"
SORT filed DESC
LIMIT 30
```

```dataview
TABLE verdict, signals, holdout_excess AS "2016+ excess/yr"
FROM "Slices"
SORT holdout_excess DESC
```
