---
type: "home"
updated: "2026-10-21"
---

# Insider Buying Research

A research log on one question: **do stocks go up after insiders buy them, and which buys are worth following?** Every SEC Form 4 open-market purchase since 2006 is backtested, and every new buy is logged and tracked forward.

- [[Findings]]: what the evidence says, in plain English
- [[What Works]]: the scoreboard
- [[2026-10-21 Backtest]]: the latest full backtest
- [[2026-10-21]]: today's research log
- [[Best Insiders]] · [[Methodology]]

## Headline

- On average a stock beat the S&P 500 by **+0.9%** over the 3 months after an insider purchase was filed (95% CI -0.1% to +2.0%, 100,993 signals since 2006). That is roughly +3.5% a year, but the median stock *lagged* by 0.9%.
- The edge was real in **2006-2015** (+7.9% a year, p 0.006) and has **faded since 2016** (+1.1% a year, p 0.767).
- The best simulated portfolio (*Insider buying after a 30%+ run-up (post-hoc)*) returned +20.0% a year after costs with a 40% max drawdown, against SPY's +11.1% and 55%.
- Survivorship: about half of all insider buys are in companies that no longer trade and can't be priced. If those did like a typical priced buy, the average falls from +0.9% to -0.1%; if they did badly, to -12.6%.

## Latest notable buys

| Filed | Ticker | Insider | Role | Value | Score | vs SPY so far |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | Director | $11.5M | 60 | -2.3% |
| 2026-10-19 | [[CTY]] | [[NELSEN ROBERT]] | Director | $3.1M | 40 | -3.3% |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | Director | $2.4M | 64 | +0.8% |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | CEO; Chairman | $1.0M | 60 | +3.5% |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | President | $5.7M | 71 | +3.5% |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | Director | $23.7M | 62 | +2.2% |
| 2026-10-16 | [[BYRN]] | [[Roth Adam L]] | Director | $70K | 40 | -2.4% |
| 2026-10-16 | [[PAM]] | [[Mindlin Marcos Marcelo]] | Director | $35.1M | 49 | -4.9% |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | Chief Operating Officer | $1.5M | 72 | -3.7% |
| 2026-10-16 | [[BORR]] | [[Troim Tor Olav]] | Director | $2.3M | 51 | -3.7% |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | President | $44K | 63 | -0.7% |
| 2026-10-15 | [[IMSR]] | [[Pardee Charles G]] | Director | $22K | 55 | -13.0% |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | Chief Executive Officer | $3.0M | 70 | -2.4% |
| 2026-10-15 | [[TRXB]] | [[Alexandria Venture Investments, LLC]] | 10% Owner | $2.5M | 55 | +2.4% |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | Director | $850K | 51 | +5.6% |


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
