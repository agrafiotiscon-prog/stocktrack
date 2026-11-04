---
type: "home"
updated: "2026-11-04"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-04 Backtest]]: the latest full backtest
- [[2026-11-04]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,883 signals since 2006). That is roughly +3.4% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.006) and has **faded since 2016** (+0.8% a year, p 0.827).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.9% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-03 | [[SIRI]] | [[BERKSHIRE HATHAWAY INC]] | 10% Owner | $26.9M | 40 | – |
| 2026-11-03 | [[LRN]] | [[Haggart Dylan G]] | Director | $17.6M | 52 | – |
| 2026-11-03 | [[BA]] | [[Buckley Mortimer J]] | Director | $998K | 64 | – |
| 2026-11-03 | [[BA]] | [[MOLLENKOPF STEVEN M]] | Director | $510K | 61 | – |
| 2026-11-03 | [[SITE]] | [[BLACK DOUG]] | CEO | $1.0M | 62 | – |
| 2026-11-03 | [[BBTX]] | [[RA CAPITAL MANAGEMENT, L.P]] | Director | $46.6M | 74 | – |
| 2026-11-03 | [[ENPH]] | [[Trivedi Shanker]] | Director | $31K | 49 | – |
| 2026-11-03 | [[RNST]] | [[LEVY JONATHAN A]] | Director | $82K | 41 | – |
| 2026-11-03 | [[MGM]] | [[Meister Keith A]] | Director | $51.7M | 58 | – |
| 2026-11-03 | [[STRZ]] | [[MACDONALD SCOTT D]] | CFO and Treasurer | $56K | 48 | – |
| 2026-11-03 | [[LKQ]] | [[Powell Michael Scott]] | Director | $192K | 57 | – |
| 2026-11-03 | [[LKQ]] | [[CLARKE ANDREW C]] | Director | $400K | 60 | – |
| 2026-11-03 | [[CAT]] | [[Fish James C Jr]] | Director | $620K | 45 | – |
| 2026-11-03 | [[TRTX]] | [[SILVERSTEIN WENDY]] | Director | $253K | 58 | – |
| 2026-11-03 | [[TRTX]] | [[Gillmore Michael]] | Director | $13K | 53 | – |


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
