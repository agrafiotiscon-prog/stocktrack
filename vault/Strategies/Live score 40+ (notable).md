---
type: "strategy"
key: "score_40"
signals: 32348
cagr: 0.0579029
spy_cagr: 0.110825
sharpe: 0.280894
max_drawdown: 0.574297
holdout_excess: 0.0150415
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,348 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.6% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.2% |
| 2006-2015 excess /yr | +7.9% (p 0.011) |
| 2016+ excess /yr | +1.5% (p 0.720) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.5% | +11.1% | 0.31 | 0.56 | 59% | 1.26 | -4.7% | 33% | 4,866 | 8.6% | -0.8% / -0.11 / 62% |
| 63d | +5.8% | +11.1% | 0.28 | 0.56 | 57% | 1.24 | -5.4% | 38% | 1,660 | 2.6% | -2.0% / -0.19 / 57% |
| 126d | +5.3% | +11.1% | 0.26 | 0.56 | 68% | 1.16 | -5.3% | 29% | 840 | 1.3% | -2.6% / -0.26 / 49% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.5%/yr, double costs +3.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -11.1% | +5.1% | -16.2% |
| 2008 | -19.3% | -36.8% | +17.5% |
| 2009 | +36.1% | +26.4% | +9.7% |
| 2010 | +31.7% | +15.1% | +16.7% |
| 2011 | -13.7% | +1.9% | -15.6% |
| 2012 | +21.3% | +16.0% | +5.3% |
| 2013 | +34.7% | +32.3% | +2.4% |
| 2014 | +2.1% | +13.5% | -11.4% |
| 2015 | -7.8% | +1.2% | -9.0% |
| 2016 | +23.2% | +12.0% | +11.2% |
| 2017 | +19.4% | +21.7% | -2.3% |
| 2018 | -20.2% | -4.6% | -15.6% |
| 2019 | +42.2% | +31.2% | +10.9% |
| 2020 | +11.0% | +18.3% | -7.3% |
| 2021 | +6.0% | +28.7% | -22.7% |
| 2022 | -21.1% | -18.2% | -2.9% |
| 2023 | +29.6% | +26.2% | +3.4% |
| 2024 | -14.8% | +24.9% | -39.7% |
| 2025 | -5.7% | +17.7% | -23.4% |
| 2026 | +3.6% | +13.7% | -10.0% |


## Live forward test

9 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-22 | [[DOLE]] | [[Pale Fire Capital SE]] | $8.6M | 45 | – | pending |
| 2026-10-22 | [[RAPP]] | [[Silva Paul M]] | $100K | 67 | – | pending |
| 2026-10-22 | [[RAPP]] | [[Young Wendy B]] | $100K | 65 | – | pending |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | – | pending |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | – | pending |
| 2026-10-22 | [[NMCO]] | [[BANK OF AMERICA CORP -DE-]] | $974 | 40 | – | pending |
| 2026-10-22 | [[LEO]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | – | pending |
| 2026-10-22 | [[DSM]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | – | pending |
| 2026-10-22 | [[NMCO]] | [[Jones Nathaniel T]] | $4K | 40 | – | pending |
| 2026-10-22 | [[AGMB]] | [[Epstein David R]] | $89K | 41 | – | pending |
| 2026-10-21 | [[FBK]] | [[INGRAM ORRIN H II]] | $1.5M | 49 | +2.3% | open |
| 2026-10-21 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.3M | 59 | +0.5% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | +1.7% | open |
| 2026-10-21 | [[CRF]] | [[Bradshaw Joshua]] | $118K | 53 | +0.3% | open |
| 2026-10-21 | [[CLM]] | [[Bradshaw Joshua]] | $97K | 52 | -0.5% | open |
| 2026-10-21 | [[DX]] | [[BOSTON BYRON L]] | $100K | 50 | +1.4% | open |
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | -9.8% | open |
| 2026-10-19 | [[CTY]] | [[NELSEN ROBERT]] | $3.1M | 40 | -2.9% | open |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | +2.4% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +2.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
