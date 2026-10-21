---
type: "strategy"
key: "score_60"
signals: 7193
cagr: 0.111632
spy_cagr: 0.110594
sharpe: 0.460294
max_drawdown: 0.619337
holdout_excess: 0.0203495
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,193 |
| 3-month excess vs SPY (mean / median) | +1.7% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.4% |
| vs surviving stocks | +1.8% |
| 2006-2015 excess /yr | +7.4% (p 0.070) |
| 2016+ excess /yr | +2.0% (p 0.706) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.7% | +11.1% | 0.24 | 0.55 | 62% | 0.92 | -4.0% | 33% | 3,298 | 6.2% | +0.4% / -0.05 / 59% |
| 63d | +11.2% | +11.1% | 0.46 | 0.55 | 62% | 1.24 | -0.1% | 62% | 1,584 | 3.0% | +3.5% / 0.20 / 32% |
| 126d | +11.5% | +11.1% | 0.47 | 0.55 | 65% | 1.13 | +0.7% | 57% | 822 | 1.6% | +3.6% / 0.20 / 43% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.8%/yr, double costs +8.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.4% | +13.3% | +3.1% |
| 2007 | -13.5% | +5.1% | -18.6% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +15.0% |
| 2010 | +32.4% | +15.1% | +17.4% |
| 2011 | -2.9% | +1.9% | -4.8% |
| 2012 | +19.3% | +16.0% | +3.3% |
| 2013 | +45.0% | +32.3% | +12.7% |
| 2014 | +7.3% | +13.5% | -6.1% |
| 2015 | -12.5% | +1.2% | -13.7% |
| 2016 | +25.2% | +12.0% | +13.2% |
| 2017 | +25.3% | +21.7% | +3.6% |
| 2018 | -16.6% | -4.6% | -12.0% |
| 2019 | +53.5% | +31.2% | +22.2% |
| 2020 | +23.9% | +18.3% | +5.5% |
| 2021 | +0.4% | +28.7% | -28.4% |
| 2022 | -6.3% | -18.2% | +11.8% |
| 2023 | +38.3% | +26.2% | +12.1% |
| 2024 | +3.6% | +24.9% | -21.3% |
| 2025 | +24.1% | +17.7% | +6.4% |
| 2026 | +2.5% | +13.7% | -11.2% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | -2.3% | open |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | +0.8% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +3.5% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | +3.5% | open |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +2.2% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -3.7% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -0.7% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.4% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -1.9% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.7% | open |
| 2026-10-13 | [[HEI]] | [[MENDELSON VICTOR H]] | $175K | 69 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[Fine Carol F]] | $175K | 69 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[CHERUVATATH NANDAKUMAR]] | $175K | 62 | +3.4% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | -4.4% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -4.3% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +0.9% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +2.1% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -0.9% | open |
| 2026-10-06 | [[PSUS]] | [[ISRAEL RYAN]] | $9.6M | 68 | -0.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
