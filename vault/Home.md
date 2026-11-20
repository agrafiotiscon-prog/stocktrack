---
type: "home"
updated: "2026-11-20"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-18 Backtest]]: the latest full backtest
- [[2026-11-20]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,092 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.815).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.6% a year after costs with a 40% max drawdown, against SPY's +10.8% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.7%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | Director | $183K | 70 | – |
| 2026-11-19 | [[SCM]] | [[Ladd Robert T]] | President and CEO | $197K | 44 | – |
| 2026-11-19 | [[PAL]] | [[Schraudenbach John]] | Director | $78K | 66 | – |
| 2026-11-19 | [[PAL]] | [[COL DOUGLAS L]] | Director | $84K | 66 | – |
| 2026-11-19 | [[CCB]] | [[HOVDE STEVEN D]] | Director | $550K | 49 | – |
| 2026-11-19 | [[BSM]] | [[Carter Thomas L Jr]] | Executive Chairman | $338K | 40 | – |
| 2026-11-19 | [[IRTC]] | [[TALWALKAR ABHIJIT Y]] | Director | $764K | 51 | – |
| 2026-11-19 | [[BGS]] | [[Mills Robert D]] | President & CEO | $250K | 54 | – |
| 2026-11-19 | [[PLD]] | [[KELLY ALFRED F JR]] | Director | $587K | 50 | – |
| 2026-11-19 | [[APC]] | [[HEYER ANDREW R]] | Director | $279K | 46 | – |
| 2026-11-19 | [[BCML]] | [[PERDUE MICHAEL J]] | Director | $151K | 44 | – |
| 2026-11-19 | [[ITT]] | [[Berryman Kevin C]] | Director | $502K | 49 | – |
| 2026-11-19 | [[SKYD]] | [[Cardinale Gerald J]] | Director | $495K | 48 | – |
| 2026-11-19 | [[HPP]] | [[COLEMAN VICTOR J]] | Chief Executive Officer | $81K | 62 | – |
| 2026-11-19 | [[AVK]] | [[MAITLAND TRACY V]] | CHAIRMAN, PRESIDENT & CEO | $203K | 55 | – |


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
