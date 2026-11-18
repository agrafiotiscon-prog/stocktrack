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
| 5 sessions | 48 | +1.7% | +1.9% | 73% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[LPG]] | [[HADJIPATERAS JOHN C]] | $961K | 55 | – | pending |
| 2026-11-17 | [[PEPG]] | [[RA CAPITAL MANAGEMENT, L.P]] | $43.1M | 61 | – | pending |
| 2026-11-16 | [[KODK]] | [[Katz Philippe D]] | $25K | 20 | -0.6% | open |
| 2026-11-16 | [[NSLR]] | [[Klein Mark D]] | $994K | 85 | -0.8% | open |
| 2026-11-16 | [[SENS]] | [[ROEDER DOUGLAS A]] | $176K | 33 | -10.3% | open |
| 2026-11-16 | [[SEI]] | [[TEAGUE AJ]] | $35K | 19 | +1.0% | open |
| 2026-11-16 | [[ORRF]] | [[Joiner Cindy Jeannette]] | $11K | 15 | -1.5% | open |
| 2026-11-16 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $285K | 23 | +0.4% | open |
| 2026-11-13 | [[FCPT]] | [[Lenehan William H]] | $150K | 39 | -0.6% | open |
| 2026-11-13 | [[AKAM]] | [[LEIGHTON F THOMSON]] | $2.6M | 52 | +1.7% | open |
| 2026-11-13 | [[CAT]] | [[MacLennan David]] | $209K | 43 | -0.6% | open |
| 2026-11-13 | [[IONS]] | [[Hayden Michael R]] | $148K | 37 | -7.5% | open |
| 2026-11-13 | [[TXO]] | [[SIMPSON BOB R]] | $945K | 34 | -2.6% | open |
| 2026-11-13 | [[CCNE]] | [[Peduzzi Michael D]] | $18K | 30 | -0.7% | open |
| 2026-11-13 | [[BW]] | [[Young Kenneth M]] | $44K | 54 | +4.2% | open |
| 2026-11-13 | [[CCNE]] | [[POWELL JEFFREY S]] | $20K | 17 | -0.7% | open |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | $680K | 62 | +0.5% | open |
| 2026-11-12 | [[IOSP]] | [[PARRETTE LESLIE J]] | $27K | 23 | +1.2% | open |
| 2026-11-12 | [[MTDR]] | [[Foran Joseph Wm]] | $123K | 75 | -2.2% | open |
| 2026-11-12 | [[ECL]] | [[MacLennan David]] | $185K | 29 | +1.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
