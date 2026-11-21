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
| 5 sessions | 61 | -0.3% | +0.6% | 57% |
| 21 sessions | 3 | -3.5% | -6.7% | 33% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[UPST]] | [[Gu Paul]] | $860K | 76 | – | pending |
| 2026-11-20 | [[EQPT]] | [[Schlacks Jabbok]] | $180K | 65 | – | pending |
| 2026-11-20 | [[UPBD]] | [[LEWIS HAROLD G]] | $399K | 73 | – | pending |
| 2026-11-20 | [[HPP]] | [[COLEMAN VICTOR J]] | $75K | 62 | – | pending |
| 2026-11-20 | [[OFRM]] | [[Morris Scott James]] | $142K | 69 | – | pending |
| 2026-11-20 | [[GLXY]] | [[Novogratz Michael]] | $4.9M | 84 | – | pending |
| 2026-11-20 | [[SEI]] | [[Ramachandran Kyle S]] | $160K | 61 | – | pending |
| 2026-11-20 | [[SEI]] | [[Brock Amanda M]] | $269K | 68 | – | pending |
| 2026-11-20 | [[SEI]] | [[Zartler William A]] | $212K | 65 | – | pending |
| 2026-11-20 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 73 | – | pending |
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | -4.1% | open |
| 2026-11-19 | [[PAL]] | [[Schraudenbach John]] | $78K | 66 | -0.5% | open |
| 2026-11-19 | [[PAL]] | [[COL DOUGLAS L]] | $84K | 66 | -0.5% | open |
| 2026-11-19 | [[HPP]] | [[COLEMAN VICTOR J]] | $81K | 62 | -3.2% | open |
| 2026-11-19 | [[HMH]] | [[McGee Thomas W]] | $1.6M | 76 | +3.5% | open |
| 2026-11-19 | [[EFC]] | [[Vranos Michael W]] | $2.1M | 62 | +3.9% | open |
| 2026-11-19 | [[MTDR]] | [[Foran Joseph Wm]] | $127K | 74 | +2.8% | open |
| 2026-11-18 | [[RMIX]] | [[Rees-Jones David]] | $731K | 76 | -15.0% | open |
| 2026-11-18 | [[EQPT]] | [[Schlacks William J]] | $145K | 64 | -5.6% | open |
| 2026-11-18 | [[EQPT]] | [[Schlacks Jabbok]] | $250K | 69 | -5.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
