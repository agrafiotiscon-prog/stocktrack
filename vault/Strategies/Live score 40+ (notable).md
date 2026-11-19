---
type: "strategy"
key: "score_40"
signals: 32386
cagr: 0.0521824
spy_cagr: 0.107784
sharpe: 0.261181
max_drawdown: 0.574298
holdout_excess: 0.0134632
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,386 |
| 3-month excess vs SPY (mean / median) | +1.0% / -0.7% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +7.8% (p 0.012) |
| 2016+ excess /yr | +1.3% (p 0.748) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.2% | +10.8% | 0.33 | 0.54 | 56% | 1.26 | -3.8% | 38% | 4,883 | 8.7% | -0.1% / -0.06 / 55% |
| 63d | +5.2% | +10.8% | 0.26 | 0.54 | 57% | 1.23 | -5.5% | 38% | 1,668 | 2.7% | -2.4% / -0.22 / 59% |
| 126d | +4.6% | +10.8% | 0.24 | 0.54 | 68% | 1.20 | -5.8% | 33% | 840 | 1.3% | -3.1% / -0.29 / 59% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.0%/yr, double costs +2.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -11.1% | +5.1% | -16.2% |
| 2008 | -19.3% | -36.8% | +17.5% |
| 2009 | +35.8% | +26.4% | +9.5% |
| 2010 | +34.7% | +15.1% | +19.6% |
| 2011 | -14.4% | +1.9% | -16.3% |
| 2012 | +19.1% | +16.0% | +3.1% |
| 2013 | +37.5% | +32.3% | +5.2% |
| 2014 | -1.0% | +13.5% | -14.4% |
| 2015 | -7.9% | +1.2% | -9.2% |
| 2016 | +20.1% | +12.0% | +8.1% |
| 2017 | +17.6% | +21.7% | -4.1% |
| 2018 | -16.7% | -4.6% | -12.1% |
| 2019 | +45.0% | +31.2% | +13.8% |
| 2020 | +9.3% | +18.3% | -9.0% |
| 2021 | +5.5% | +28.7% | -23.2% |
| 2022 | -28.2% | -18.2% | -10.0% |
| 2023 | +31.1% | +26.2% | +4.9% |
| 2024 | -15.0% | +24.9% | -39.9% |
| 2025 | -6.1% | +17.7% | -23.8% |
| 2026 | +3.2% | +8.2% | -5.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 162 | +0.2% | +0.9% | 57% |
| 21 sessions | 3 | -6.0% | -8.5% | 33% |


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
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | – | pending |
| 2026-11-18 | [[BA]] | [[JOHRI AKHIL]] | $500K | 49 | – | pending |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | $65K | 70 | – | pending |
| 2026-11-18 | [[KGS]] | [[HOGAN RANDALL J]] | $494K | 71 | – | pending |
| 2026-11-18 | [[CRMD]] | [[Kaplan Myron]] | $122K | 44 | – | pending |
| 2026-11-18 | [[CRC]] | [[Bremner Andrew B]] | $100K | 42 | – | pending |
| 2026-11-18 | [[FUN]] | [[JAFFER REHAN]] | $6.4M | 68 | – | pending |
| 2026-11-18 | [[SJT]] | [[OLIVER ERIC L]] | $2.6M | 41 | – | pending |
| 2026-11-18 | [[NPCE]] | [[Huennekens R Scott]] | $104K | 62 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
