---
type: "strategy"
key: "all_liquid"
signals: 67571
cagr: 0.0461761
spy_cagr: 0.107784
sharpe: 0.238275
max_drawdown: 0.609756
holdout_excess: 0.0017366
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,571 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.3% (p 0.020) |
| 2016+ excess /yr | +0.2% (p 0.962) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.2% | +10.8% | 0.30 | 0.54 | 61% | 1.24 | -4.5% | 38% | 4,997 | 9.1% | -1.9% / -0.19 / 66% |
| 63d | +4.6% | +10.8% | 0.24 | 0.54 | 61% | 1.15 | -5.8% | 48% | 1,680 | 2.7% | -3.5% / -0.36 / 71% |
| 126d | +6.8% | +10.8% | 0.32 | 0.54 | 54% | 1.15 | -3.8% | 33% | 840 | 1.5% | -1.7% / -0.19 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +7.6%/yr, double costs +1.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +24.3% | +13.8% | +10.4% |
| 2007 | -7.9% | +5.1% | -13.0% |
| 2008 | -24.8% | -36.8% | +12.0% |
| 2009 | +53.0% | +26.4% | +26.7% |
| 2010 | +21.7% | +15.1% | +6.6% |
| 2011 | -10.2% | +1.9% | -12.1% |
| 2012 | +22.6% | +16.0% | +6.6% |
| 2013 | +38.9% | +32.3% | +6.6% |
| 2014 | +1.8% | +13.5% | -11.7% |
| 2015 | +6.1% | +1.2% | +4.8% |
| 2016 | +15.1% | +12.0% | +3.1% |
| 2017 | +24.5% | +21.7% | +2.8% |
| 2018 | -10.2% | -4.6% | -5.6% |
| 2019 | +8.0% | +31.2% | -23.2% |
| 2020 | +36.1% | +18.3% | +17.8% |
| 2021 | -10.2% | +28.7% | -38.9% |
| 2022 | -35.7% | -18.2% | -17.6% |
| 2023 | +24.8% | +26.2% | -1.3% |
| 2024 | -15.1% | +24.9% | -40.0% |
| 2025 | -14.4% | +17.7% | -32.1% |
| 2026 | -2.3% | +8.2% | -10.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 335 | +0.2% | +0.9% | 58% |
| 21 sessions | 21 | -3.5% | +2.6% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-18 | [[USAR]] | [[BLITZER MICHAEL]] | $3.0M | 51 | – | pending |
| 2026-11-18 | [[RMIX]] | [[Johnston Bretton A]] | $12K | 58 | – | pending |
| 2026-11-18 | [[RMIX]] | [[Rees-Jones David]] | $731K | 76 | – | pending |
| 2026-11-18 | [[EQPT]] | [[Schlacks William J]] | $145K | 64 | – | pending |
| 2026-11-18 | [[EQPT]] | [[Schlacks Jabbok]] | $250K | 69 | – | pending |
| 2026-11-18 | [[OIG]] | [[DEUTSCH ROBERT V]] | $106K | 54 | – | pending |
| 2026-11-18 | [[RMIX]] | [[Matteson Mark R]] | $55K | 64 | – | pending |
| 2026-11-18 | [[RMIX]] | [[Jones Mark Alan]] | $50K | 53 | – | pending |
| 2026-11-18 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.2M | 45 | – | pending |
| 2026-11-18 | [[ANAB]] | [[EcoR1 Capital, LLC]] | $17.2M | 48 | – | pending |
| 2026-11-18 | [[BH]] | [[BIGLARI, SARDAR]] | $2.2M | 50 | – | pending |
| 2026-11-18 | [[HAWK]] | [[Finelli Francis Alphonse]] | $49K | 38 | – | pending |
| 2026-11-18 | [[LEO]] | [[Saba Capital Management, L.P]] | $204K | 23 | – | pending |
| 2026-11-18 | [[HFRO]] | [[Saba Capital Management, L.P]] | $1.3M | 35 | – | pending |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | – | pending |
| 2026-11-18 | [[BA]] | [[JOHRI AKHIL]] | $500K | 49 | – | pending |
| 2026-11-18 | [[GLP]] | [[Global GP LLC]] | $312K | 25 | – | pending |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | $65K | 70 | – | pending |
| 2026-11-18 | [[KGS]] | [[HOGAN RANDALL J]] | $494K | 71 | – | pending |
| 2026-11-18 | [[PEBK]] | [[PRICE BILLY L JR DR]] | $8K | 15 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
