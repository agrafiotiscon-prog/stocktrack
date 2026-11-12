---
type: "home"
updated: "2026-11-12"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-11 Backtest]]: the latest full backtest
- [[2026-11-12]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,945 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.830).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[MP]] | [[Rosenthal Michael Stuart]] | Chief Operating Officer | $1.2M | 63 | – |
| 2026-11-12 | [[TH]] | [[Archer James Bradley]] | Director and CEO and President | $313K | 43 | – |
| 2026-11-12 | [[MP]] | [[WEISENBURGER RANDALL J]] | Director | $2.0M | 72 | – |
| 2026-11-12 | [[MP]] | [[Corbett Ryan]] | Chief Financial Officer | $199K | 61 | – |
| 2026-11-12 | [[GSM]] | [[Girardeau David Marie, Gabriel]] | SEE REMARKS | $41K | 55 | – |
| 2026-11-12 | [[GSM]] | [[CROCKETT BRUCE LARMOUR]] | Director | $21K | 52 | – |
| 2026-11-12 | [[GSM]] | [[Lopez Madrid Javier]] | EXECUTIVE CHAIRMAN | $75K | 66 | – |
| 2026-11-12 | [[COHR]] | [[ANDERSON JAMES ROBERT]] | CEO | $997K | 62 | – |
| 2026-11-12 | [[GSM]] | [[Levi Marco]] | CHIEF EXECUTIVE OFFICER | $51K | 56 | – |
| 2026-11-12 | [[CSQR]] | [[MULLEE SPENCER EDWARD]] | Chief Executive Officer | $247K | 41 | – |
| 2026-11-12 | [[COHR]] | [[Digirolomo Enrico]] | Director | $223K | 46 | – |
| 2026-11-10 | [[MX]] | [[Amoruso Cristiano]] | Director | $1.4M | 58 | +7.6% |
| 2026-11-10 | [[ATEC]] | [[Valentine Keith]] | Director | $243K | 48 | +1.7% |
| 2026-11-10 | [[WW]] | [[BYE STEPHEN J]] | President and CEO | $138K | 68 | -2.5% |
| 2026-11-10 | [[WW]] | [[Gavales Lisa A]] | Director | $55K | 51 | -2.5% |


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
