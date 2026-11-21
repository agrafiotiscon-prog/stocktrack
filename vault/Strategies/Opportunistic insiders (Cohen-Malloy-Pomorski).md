---
type: "strategy"
key: "opportunistic"
signals: 9666
cagr: 0.134951
spy_cagr: 0.111258
sharpe: 0.591211
max_drawdown: 0.497034
holdout_excess: -0.0278666
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,666 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.1% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.7% |
| 2006-2015 excess /yr | +6.5% (p 0.058) |
| 2016+ excess /yr | -2.8% (p 0.443) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.6% | +11.1% | 0.21 | 0.56 | 52% | 0.80 | -4.6% | 21% | 3,635 | 8.0% | -4.0% / -0.48 / 62% |
| 63d | +13.5% | +11.1% | 0.59 | 0.56 | 50% | 1.09 | +2.6% | 47% | 1,449 | 3.5% | +3.2% / 0.21 / 31% |
| 126d | +10.1% | +11.1% | 0.45 | 0.56 | 56% | 1.18 | -1.1% | 37% | 743 | 1.7% | +1.0% / 0.04 / 46% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +17.2%/yr, double costs +10.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2008 | -2.8% | -34.6% | +31.8% |
| 2009 | +25.1% | +26.4% | -1.3% |
| 2010 | +29.2% | +15.1% | +14.1% |
| 2011 | +3.7% | +1.9% | +1.8% |
| 2012 | +16.4% | +16.0% | +0.4% |
| 2013 | +40.2% | +32.3% | +7.9% |
| 2014 | +10.1% | +13.5% | -3.3% |
| 2015 | -11.0% | +1.2% | -12.3% |
| 2016 | +18.2% | +12.0% | +6.2% |
| 2017 | +6.9% | +21.7% | -14.8% |
| 2018 | -6.3% | -4.6% | -1.8% |
| 2019 | +28.1% | +31.2% | -3.1% |
| 2020 | +6.6% | +18.3% | -11.7% |
| 2021 | +38.1% | +28.7% | +9.4% |
| 2022 | -25.2% | -18.2% | -7.0% |
| 2023 | +50.2% | +26.2% | +24.0% |
| 2024 | +11.6% | +24.9% | -13.3% |
| 2025 | -0.5% | +17.7% | -18.2% |
| 2026 | +49.6% | +8.2% | +41.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 64 | +0.9% | +1.7% | 66% |
| 21 sessions | 7 | +6.6% | +6.4% | 100% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[ALTO]] | [[NATHAN GILBERT E]] | $81K | 26 | – | pending |
| 2026-11-20 | [[CWBC]] | [[BARTLEIN ROBERT]] | $73K | 35 | – | pending |
| 2026-11-20 | [[SEI]] | [[TEAGUE AJ]] | $31K | 47 | – | pending |
| 2026-11-20 | [[NXG]] | [[Sunderland Todd]] | $42K | 35 | – | pending |
| 2026-11-20 | [[CION]] | [[BRESNER GREGG A]] | $48K | 39 | – | pending |
| 2026-11-20 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $266K | 23 | – | pending |
| 2026-11-20 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 73 | – | pending |
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | -4.1% | open |
| 2026-11-19 | [[SCM]] | [[Ladd Robert T]] | $197K | 44 | +0.5% | open |
| 2026-11-19 | [[BSM]] | [[Carter Thomas L Jr]] | $338K | 40 | +2.6% | open |
| 2026-11-19 | [[APC]] | [[HEYER ANDREW R]] | $279K | 46 | +4.1% | open |
| 2026-11-19 | [[ORRF]] | [[BROWN SARAH M]] | $10K | 16 | +1.9% | open |
| 2026-11-19 | [[SEI]] | [[TEAGUE AJ]] | $10K | 15 | -3.5% | open |
| 2026-11-19 | [[CWBC]] | [[GILL JAGROOP]] | $294K | 31 | +3.3% | open |
| 2026-11-19 | [[MTDR]] | [[Foran Joseph Wm]] | $127K | 74 | +2.8% | open |
| 2026-11-18 | [[ANAB]] | [[EcoR1 Capital, LLC]] | $17.2M | 48 | +2.8% | open |
| 2026-11-18 | [[BH]] | [[BIGLARI, SARDAR]] | $2.2M | 50 | +3.4% | open |
| 2026-11-18 | [[SGP]] | [[RA CAPITAL MANAGEMENT, L.P]] | $32K | 17 | +8.8% | open |
| 2026-11-18 | [[NCDL]] | [[Miranda Kenneth M]] | $17K | 21 | +5.5% | open |
| 2026-11-18 | [[UMH]] | [[Carus Jeffrey A]] | $14K | 45 | +6.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
