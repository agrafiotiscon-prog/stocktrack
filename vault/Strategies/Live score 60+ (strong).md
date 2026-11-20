---
type: "strategy"
key: "score_60"
signals: 7212
cagr: 0.105251
spy_cagr: 0.107555
sharpe: 0.439872
max_drawdown: 0.612357
holdout_excess: 0.0166326
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,212 |
| 3-month excess vs SPY (mean / median) | +1.5% / -0.7% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.3% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +6.8% (p 0.101) |
| 2016+ excess /yr | +1.7% (p 0.754) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.3% | +10.8% | 0.22 | 0.54 | 63% | 0.92 | -4.2% | 33% | 3,303 | 6.1% | +0.0% / -0.08 / 59% |
| 63d | +10.5% | +10.8% | 0.44 | 0.54 | 61% | 1.22 | -0.4% | 52% | 1,590 | 2.9% | +3.0% / 0.16 / 31% |
| 126d | +12.2% | +10.8% | 0.50 | 0.54 | 63% | 1.12 | +1.7% | 57% | 825 | 1.6% | +4.3% / 0.25 / 44% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.6%/yr, double costs +7.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.4% | +13.3% | +3.1% |
| 2007 | -11.8% | +5.1% | -16.9% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +14.9% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -0.5% | +1.9% | -2.4% |
| 2012 | +13.4% | +16.0% | -2.6% |
| 2013 | +48.3% | +32.3% | +16.0% |
| 2014 | +6.1% | +13.5% | -7.3% |
| 2015 | -12.7% | +1.2% | -13.9% |
| 2016 | +28.9% | +12.0% | +16.9% |
| 2017 | +28.0% | +21.7% | +6.3% |
| 2018 | -10.8% | -4.6% | -6.3% |
| 2019 | +47.2% | +31.2% | +16.0% |
| 2020 | +16.2% | +18.3% | -2.2% |
| 2021 | -1.8% | +28.7% | -30.5% |
| 2022 | -6.9% | -18.2% | +11.3% |
| 2023 | +35.5% | +26.2% | +9.3% |
| 2024 | +1.6% | +24.9% | -23.3% |
| 2025 | +19.6% | +17.7% | +1.9% |
| 2026 | +2.2% | +8.2% | -6.1% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 55 | +0.0% | +1.0% | 56% |
| 21 sessions | 2 | -1.9% | +4.6% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | – | pending |
| 2026-11-19 | [[PAL]] | [[Schraudenbach John]] | $78K | 66 | – | pending |
| 2026-11-19 | [[PAL]] | [[COL DOUGLAS L]] | $84K | 66 | – | pending |
| 2026-11-19 | [[HPP]] | [[COLEMAN VICTOR J]] | $81K | 62 | – | pending |
| 2026-11-19 | [[HMH]] | [[McGee Thomas W]] | $1.6M | 76 | – | pending |
| 2026-11-19 | [[EFC]] | [[Vranos Michael W]] | $2.1M | 62 | – | pending |
| 2026-11-19 | [[MTDR]] | [[Foran Joseph Wm]] | $127K | 74 | – | pending |
| 2026-11-18 | [[RMIX]] | [[Rees-Jones David]] | $731K | 76 | -12.5% | open |
| 2026-11-18 | [[EQPT]] | [[Schlacks William J]] | $145K | 64 | -5.2% | open |
| 2026-11-18 | [[EQPT]] | [[Schlacks Jabbok]] | $250K | 69 | -5.2% | open |
| 2026-11-18 | [[RMIX]] | [[Matteson Mark R]] | $55K | 64 | -12.5% | open |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | +8.0% | open |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | $65K | 70 | -4.0% | open |
| 2026-11-18 | [[KGS]] | [[HOGAN RANDALL J]] | $494K | 71 | +0.4% | open |
| 2026-11-18 | [[FUN]] | [[JAFFER REHAN]] | $6.4M | 68 | +1.1% | open |
| 2026-11-18 | [[NPCE]] | [[Huennekens R Scott]] | $104K | 62 | +0.2% | open |
| 2026-11-18 | [[CGON]] | [[Kuan Arthur]] | $2.4M | 72 | +0.4% | open |
| 2026-11-18 | [[CGON]] | [[Kalofonos Isabel]] | $299K | 65 | +0.4% | open |
| 2026-11-18 | [[OFRM]] | [[Morris Scott James]] | $100K | 67 | +5.9% | open |
| 2026-11-18 | [[OFRM]] | [[PEIROS LARRY]] | $301K | 68 | +5.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
