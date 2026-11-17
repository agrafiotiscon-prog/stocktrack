---
type: "home"
updated: "2026-11-17"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-11 Backtest]]: the latest full backtest
- [[2026-11-17]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,945 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.830).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[BW]] | [[BRC Group Holdings, Inc]] | 10% Owner | $212K | 66 | – |
| 2026-11-16 | [[MX]] | [[LEE CHAE]] | Chief Executive Officer | $218K | 63 | – |
| 2026-11-16 | [[EQPT]] | [[Schlacks Jabbok]] | Founder & CEO | $63K | 50 | – |
| 2026-11-16 | [[SKYD]] | [[Cardinale Gerald J]] | Director | $1.0M | 52 | – |
| 2026-11-16 | [[KTOS]] | [[King David Arnold]] | Director | $201K | 45 | – |
| 2026-11-16 | [[BRSP]] | [[Mazzei Michael]] | CEO | $1.0M | 58 | – |
| 2026-11-16 | [[MP]] | [[Corbett Ryan]] | Chief Financial Officer | $129K | 58 | – |
| 2026-11-16 | [[KURA]] | [[WILSON TROY EDWARD]] | President and CEO | $1.5M | 66 | – |
| 2026-11-16 | [[ADIG]] | [[Carlet Michael]] | Executive VP, CFO | $100K | 71 | – |
| 2026-11-16 | [[ADIG]] | [[Cardazzi Marco]] | Executive VP and CMO | $25K | 61 | – |
| 2026-11-16 | [[ADIG]] | [[Lane Jeannine J]] | Exec. VP, GC, Corp. Sec. & CCO | $50K | 57 | – |
| 2026-11-16 | [[ADIG]] | [[Aarnes Robert B]] | President and CEO | $100K | 68 | – |
| 2026-11-16 | [[HL]] | [[Andres Dale]] | Director | $125K | 43 | – |
| 2026-11-16 | [[ADIG]] | [[Copeland Alicia Crispin]] | Executive VP and COO | $51K | 70 | – |
| 2026-11-16 | [[FPS]] | [[Hottinger Tyson]] | Chief Legal Officer | $245K | 77 | – |


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
