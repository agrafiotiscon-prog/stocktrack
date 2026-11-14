---
type: "home"
updated: "2026-11-14"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-11 Backtest]]: the latest full backtest
- [[2026-11-14]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,945 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.830).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[STWD]] | [[Pollack Jonathan Lee]] | Director | $2.0M | 67 | – |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | CEO, Chairman of the Board | $14.7M | 87 | – |
| 2026-11-13 | [[INDI]] | [[ALDRICH DAVID J]] | Director | $299K | 47 | – |
| 2026-11-13 | [[CTRI]] | [[Patton Charles R]] | Director | $250K | 55 | – |
| 2026-11-13 | [[IOND]] | [[Abbate Michael]] | Director | $1.3M | 53 | – |
| 2026-11-13 | [[FISN]] | [[Muller Elizabeth]] | CEO, President | $22K | 48 | – |
| 2026-11-13 | [[CRVS]] | [[Arcara Jeffrey]] | Chief Business Officer | $50K | 45 | – |
| 2026-11-13 | [[CTEV]] | [[Dalton Travis]] | Pres., CEO & Executive Chair | $150K | 58 | – |
| 2026-11-13 | [[UPST]] | [[Gu Paul]] | Chief Executive Officer | $1.0M | 63 | – |
| 2026-11-13 | [[FUN]] | [[JAFFER REHAN]] | Director | $9.2M | 72 | – |
| 2026-11-13 | [[NXRT]] | [[McGraner Matt]] | See Remarks | $100K | 40 | – |
| 2026-11-13 | [[BW]] | [[Moeller Philip D]] | Director | $14K | 42 | – |
| 2026-11-13 | [[BW]] | [[Tato Joseph A]] | Director | $53K | 45 | – |
| 2026-11-13 | [[AKAM]] | [[LEIGHTON F THOMSON]] | Chief Executive Officer | $2.6M | 52 | – |
| 2026-11-13 | [[CAT]] | [[MacLennan David]] | Director | $209K | 43 | – |


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
