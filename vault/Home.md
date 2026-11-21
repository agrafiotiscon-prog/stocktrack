---
type: "home"
updated: "2026-11-21"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-11-18 Backtest]]: the latest full backtest
- [[2026-11-21]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.8%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 101,092 signals since 2006). That is roughly +3.3% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.8% a year, p 0.007) and has **faded since 2016** (+0.8% a year, p 0.815).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +19.6% a year after costs with a 40% max drawdown, against SPY's +10.8% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.8% to -0.1%; if they did badly, to -12.7%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[UPST]] | [[Gu Paul]] | Chief Executive Officer | $860K | 76 | – |
| 2026-11-20 | [[UPST]] | [[Girouard Dave]] | Director | $951K | 46 | – |
| 2026-11-20 | [[HBCP]] | [[Hill Darren M]] | Chief Risk Officer | $315K | 53 | – |
| 2026-11-20 | [[CRMD]] | [[Blum Susan]] | Chief Financial Officer | $23K | 56 | – |
| 2026-11-20 | [[EQPT]] | [[Schlacks Jabbok]] | Founder & CEO | $180K | 65 | – |
| 2026-11-20 | [[ARR]] | [[Harper Gordon]] | CFO | $27K | 46 | – |
| 2026-11-20 | [[TJX]] | [[PINTOFF CRAIG ADAM]] | Director | $200K | 45 | – |
| 2026-11-20 | [[UPBD]] | [[LEWIS HAROLD G]] | Director | $399K | 73 | – |
| 2026-11-20 | [[HPP]] | [[COLEMAN VICTOR J]] | Chief Executive Officer | $75K | 62 | – |
| 2026-11-20 | [[OFRM]] | [[Garner Jennifer Anne]] | Director | $118K | 50 | – |
| 2026-11-20 | [[AVEX]] | [[Morrison Christine M]] | Chief Legal Officer | $102K | 43 | – |
| 2026-11-20 | [[OFRM]] | [[Morris Scott James]] | Director | $142K | 69 | – |
| 2026-11-20 | [[INOD]] | [[Massey Stewart R]] | Director | $321K | 47 | – |
| 2026-11-20 | [[GLXY]] | [[DEASON DOUGLAS R]] | Director | $99K | 42 | – |
| 2026-11-20 | [[GLXY]] | [[Novogratz Michael]] | Chief Executive Officer | $4.9M | 84 | – |


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
