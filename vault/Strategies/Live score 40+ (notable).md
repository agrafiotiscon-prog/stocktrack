---
type: "strategy"
key: "score_40"
signals: 32311
cagr: 0.0595145
spy_cagr: 0.109148
sharpe: 0.286169
max_drawdown: 0.571525
holdout_excess: 0.0130353
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,311 |
| 3-month excess vs SPY (mean / median) | +1.0% / -0.7% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.2% |
| 2006-2015 excess /yr | +7.8% (p 0.011) |
| 2016+ excess /yr | +1.3% (p 0.755) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.8% | +10.9% | 0.32 | 0.55 | 58% | 1.25 | -4.3% | 33% | 4,879 | 8.7% | -0.7% / -0.10 / 61% |
| 63d | +6.0% | +10.9% | 0.29 | 0.55 | 57% | 1.25 | -5.2% | 38% | 1,662 | 2.6% | -2.0% / -0.20 / 57% |
| 126d | +5.3% | +10.9% | 0.26 | 0.55 | 69% | 1.17 | -5.1% | 24% | 840 | 1.3% | -2.7% / -0.27 / 51% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.7%/yr, double costs +3.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -8.8% | +5.1% | -13.9% |
| 2008 | -19.8% | -36.8% | +17.0% |
| 2009 | +31.4% | +26.4% | +5.0% |
| 2010 | +31.7% | +15.1% | +16.7% |
| 2011 | -13.6% | +1.9% | -15.5% |
| 2012 | +16.7% | +16.0% | +0.7% |
| 2013 | +34.7% | +32.3% | +2.4% |
| 2014 | +2.1% | +13.5% | -11.4% |
| 2015 | -7.8% | +1.2% | -9.0% |
| 2016 | +20.5% | +12.0% | +8.5% |
| 2017 | +20.6% | +21.7% | -1.1% |
| 2018 | -18.0% | -4.6% | -13.4% |
| 2019 | +42.3% | +31.2% | +11.1% |
| 2020 | +11.1% | +18.3% | -7.2% |
| 2021 | +3.9% | +28.7% | -24.8% |
| 2022 | -20.2% | -18.2% | -2.0% |
| 2023 | +27.8% | +26.2% | +1.6% |
| 2024 | -11.3% | +24.9% | -36.2% |
| 2025 | -5.7% | +17.7% | -23.4% |
| 2026 | +9.3% | +10.8% | -1.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 117 | +0.6% | +1.5% | 63% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-13 | [[STWD]] | [[Pollack Jonathan Lee]] | $2.0M | 67 | – | pending |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | – | pending |
| 2026-11-13 | [[INDI]] | [[ALDRICH DAVID J]] | $299K | 47 | – | pending |
| 2026-11-13 | [[CTRI]] | [[Patton Charles R]] | $250K | 55 | – | pending |
| 2026-11-13 | [[IOND]] | [[Abbate Michael]] | $1.3M | 53 | – | pending |
| 2026-11-13 | [[FISN]] | [[Muller Elizabeth]] | $22K | 48 | – | pending |
| 2026-11-13 | [[CRVS]] | [[Arcara Jeffrey]] | $50K | 45 | – | pending |
| 2026-11-13 | [[CTEV]] | [[Dalton Travis]] | $150K | 58 | – | pending |
| 2026-11-13 | [[UPST]] | [[Gu Paul]] | $1.0M | 63 | – | pending |
| 2026-11-13 | [[FUN]] | [[JAFFER REHAN]] | $9.2M | 72 | – | pending |
| 2026-11-13 | [[NXRT]] | [[McGraner Matt]] | $100K | 40 | – | pending |
| 2026-11-13 | [[BW]] | [[Moeller Philip D]] | $14K | 42 | – | pending |
| 2026-11-13 | [[BW]] | [[Tato Joseph A]] | $53K | 45 | – | pending |
| 2026-11-13 | [[AKAM]] | [[LEIGHTON F THOMSON]] | $2.6M | 52 | – | pending |
| 2026-11-13 | [[CAT]] | [[MacLennan David]] | $209K | 43 | – | pending |
| 2026-11-13 | [[FF]] | [[Bedell Donald C]] | $113K | 68 | – | pending |
| 2026-11-13 | [[FF]] | [[Butcher Pamela R]] | $28K | 62 | – | pending |
| 2026-11-13 | [[FF]] | [[Polet Roeland]] | $136K | 81 | – | pending |
| 2026-11-13 | [[KGS]] | [[Holloway Gretchen Lynn]] | $50K | 46 | – | pending |
| 2026-11-13 | [[FF]] | [[SPARKS ROSE]] | $30K | 71 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
