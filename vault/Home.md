---
type: "home"
updated: "2026-10-27"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-10-21 Backtest]]: the latest full backtest
- [[2026-10-27]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.9%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,993 signals since 2006). That is roughly +3.5% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.9% a year, p 0.006) and has **faded since 2016** (+1.1% a year, p 0.767).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-10-26 | [[GPI]] | [[Conifer Management, L.L.C]] | 10% Owner | $24.2M | 44 | – |
| 2026-10-26 | [[STC]] | [[Apel Thomas G]] | Director | $95K | 48 | – |
| 2026-10-26 | [[STC]] | [[Corey William S. Jr]] | Director | $94K | 54 | – |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | Director | $95K | 50 | – |
| 2026-10-26 | [[THRM]] | [[MASCARENAS PAUL ANTHONY]] | Director | $533K | 61 | – |
| 2026-10-26 | [[THRM]] | [[Presley William T]] | President & CEO | $130K | 53 | – |
| 2026-10-26 | [[PRTA]] | [[SCULLY WILLIAM P]] | 10% Owner | $1.2M | 40 | – |
| 2026-10-26 | [[BPRE]] | [[KAMFAR RAMIN]] | Director | $2.1M | 54 | – |
| 2026-10-23 | [[BPRE]] | [[Ruddy Jordan B]] | President | $25K | 48 | -0.1% |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | See Remarks | $439K | 64 | +1.0% |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | CFO & Treasurer | $40K | 68 | +1.0% |
| 2026-10-23 | [[RAPP]] | [[Sanchez Ramiro]] | Director | $98K | 67 | -3.1% |
| 2026-10-22 | [[DOLE]] | [[Pale Fire Capital SE]] | 10% Owner | $8.6M | 45 | -2.6% |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | Director | $100K | 67 | -8.7% |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | Director | $100K | 65 | -8.7% |


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
