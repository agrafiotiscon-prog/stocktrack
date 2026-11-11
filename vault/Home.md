---
type: "home"
updated: "2026-11-11"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-11 Backtest]]: the latest full backtest
- [[2026-11-11]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,945 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.830).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +10.9% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[MX]] | [[Amoruso Cristiano]] | Director | $1.4M | 58 | – |
| 2026-11-10 | [[ATEC]] | [[Valentine Keith]] | Director | $243K | 48 | – |
| 2026-11-10 | [[WW]] | [[BYE STEPHEN J]] | President and CEO | $138K | 68 | – |
| 2026-11-10 | [[WW]] | [[Gavales Lisa A]] | Director | $55K | 51 | – |
| 2026-11-10 | [[FUN]] | [[JAFFER REHAN]] | Director | $14.9M | 77 | – |
| 2026-11-10 | [[GLXY]] | [[DEASON DOUGLAS R]] | Director | $70K | 40 | – |
| 2026-11-10 | [[BSM]] | [[Carter Thomas L Jr]] | Executive Chairman | $686K | 44 | – |
| 2026-11-10 | [[EGBN]] | [[Newell Eric R]] | Senior EVP, CFO | $50K | 41 | – |
| 2026-11-10 | [[TXO]] | [[SIMPSON BOB R]] | Director | $3.1M | 41 | – |
| 2026-11-10 | [[FUN]] | [[HADDRILL RICHARD M]] | Executive Chair | $91K | 57 | – |
| 2026-11-10 | [[WD]] | [[Pinkus Gary S]] | Director | $201K | 45 | – |
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | EVP, Chief Operating Officer | $150K | 75 | – |
| 2026-11-10 | [[MCY]] | [[Braunegg George Gwyer]] | Director | $50K | 43 | – |
| 2026-11-10 | [[STVN]] | [[MOREL DONALD E JR]] | Director | $327K | 47 | – |
| 2026-11-10 | [[SUNC]] | [[Skidmore David K]] | Director | $94K | 42 | – |


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
