---
type: "strategy"
key: "all_liquid"
signals: 67450
cagr: 0.0493045
spy_cagr: 0.109148
sharpe: 0.249961
max_drawdown: 0.610006
holdout_excess: 0.00144513
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,450 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.3% (p 0.019) |
| 2016+ excess /yr | +0.1% (p 0.968) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.9% | +10.9% | 0.32 | 0.55 | 61% | 1.22 | -3.9% | 38% | 4,991 | 9.2% | -1.5% / -0.16 / 68% |
| 63d | +4.9% | +10.9% | 0.25 | 0.55 | 61% | 1.15 | -5.7% | 48% | 1,677 | 2.7% | -3.4% / -0.35 / 70% |
| 126d | +7.0% | +10.9% | 0.33 | 0.55 | 54% | 1.15 | -3.8% | 33% | 840 | 1.5% | -1.8% / -0.19 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +7.9%/yr, double costs +2.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +24.3% | +13.8% | +10.4% |
| 2007 | -7.8% | +5.1% | -13.0% |
| 2008 | -22.2% | -36.8% | +14.6% |
| 2009 | +52.7% | +26.4% | +26.4% |
| 2010 | +21.7% | +15.1% | +6.6% |
| 2011 | -10.5% | +1.9% | -12.4% |
| 2012 | +21.5% | +16.0% | +5.6% |
| 2013 | +38.8% | +32.3% | +6.5% |
| 2014 | +1.8% | +13.5% | -11.7% |
| 2015 | +6.1% | +1.2% | +4.8% |
| 2016 | +15.1% | +12.0% | +3.1% |
| 2017 | +23.8% | +21.7% | +2.1% |
| 2018 | -10.3% | -4.6% | -5.7% |
| 2019 | +8.0% | +31.2% | -23.2% |
| 2020 | +36.1% | +18.3% | +17.8% |
| 2021 | -9.4% | +28.7% | -38.2% |
| 2022 | -35.7% | -18.2% | -17.6% |
| 2023 | +24.8% | +26.2% | -1.3% |
| 2024 | -15.1% | +24.9% | -40.0% |
| 2025 | -14.4% | +17.7% | -32.1% |
| 2026 | +1.6% | +10.8% | -9.2% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 255 | +0.8% | +1.3% | 61% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[STWD]] | [[Pollack Jonathan Lee]] | $2.0M | 67 | – | pending |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | – | pending |
| 2026-11-13 | [[FRPH]] | [[Baker John D. III]] | $930 | 10 | – | pending |
| 2026-11-13 | [[INDI]] | [[ALDRICH DAVID J]] | $299K | 47 | – | pending |
| 2026-11-13 | [[CTRI]] | [[Patton Charles R]] | $250K | 55 | – | pending |
| 2026-11-13 | [[IOND]] | [[Abbate Michael]] | $1.3M | 53 | – | pending |
| 2026-11-13 | [[TRS]] | [[Tredwell Daniel P]] | $3K | 13 | – | pending |
| 2026-11-13 | [[FISN]] | [[Muller Elizabeth]] | $22K | 48 | – | pending |
| 2026-11-13 | [[CRVS]] | [[Arcara Jeffrey]] | $50K | 45 | – | pending |
| 2026-11-13 | [[ZLAB]] | [[GAYNOR RICHARD]] | $33K | 6 | – | pending |
| 2026-11-13 | [[CTEV]] | [[Dalton Travis]] | $150K | 58 | – | pending |
| 2026-11-13 | [[UPST]] | [[Gu Paul]] | $1.0M | 63 | – | pending |
| 2026-11-13 | [[GLP]] | [[Global GP LLC]] | $442K | 27 | – | pending |
| 2026-11-13 | [[MRBK]] | [[Warriner Kenneth Thomas]] | $16K | 30 | – | pending |
| 2026-11-13 | [[FUN]] | [[JAFFER REHAN]] | $9.2M | 72 | – | pending |
| 2026-11-13 | [[NXRT]] | [[McGraner Matt]] | $100K | 40 | – | pending |
| 2026-11-13 | [[AEBI]] | [[Schroeder Henning]] | $12K | 30 | – | pending |
| 2026-11-13 | [[ARR]] | [[Macauley Desmond]] | $12K | 28 | – | pending |
| 2026-11-13 | [[BW]] | [[Moeller Philip D]] | $14K | 42 | – | pending |
| 2026-11-13 | [[BW]] | [[Tato Joseph A]] | $53K | 45 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
