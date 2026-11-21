---
type: "strategy"
key: "first_buy_exec"
signals: 5640
cagr: 0.090853
spy_cagr: 0.106338
sharpe: 0.401993
max_drawdown: 0.54717
holdout_excess: 0.00528525
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,640 |
| 3-month excess vs SPY (mean / median) | +1.3% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.9% |
| vs surviving stocks | +1.6% |
| 2006-2015 excess /yr | +11.4% (p 0.011) |
| 2016+ excess /yr | +0.5% (p 0.903) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +10.6% | 0.21 | 0.54 | 53% | 0.89 | -4.6% | 20% | 3,211 | 5.4% | -0.5% / -0.15 / 47% |
| 63d | +9.1% | +10.6% | 0.40 | 0.54 | 55% | 1.22 | -2.0% | 55% | 1,532 | 2.5% | +2.1% / 0.10 / 39% |
| 126d | +10.3% | +10.6% | 0.45 | 0.54 | 57% | 1.20 | -0.8% | 50% | 786 | 1.3% | +2.6% / 0.14 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.8%/yr, double costs +6.4%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2007 | +4.1% | +5.3% | -1.2% |
| 2008 | -29.1% | -36.8% | +7.7% |
| 2009 | +54.2% | +26.4% | +27.8% |
| 2010 | +25.5% | +15.1% | +10.4% |
| 2011 | -6.5% | +1.9% | -8.4% |
| 2012 | +30.1% | +16.0% | +14.1% |
| 2013 | +34.4% | +32.3% | +2.1% |
| 2014 | +6.6% | +13.5% | -6.9% |
| 2015 | +5.2% | +1.2% | +4.0% |
| 2016 | -0.1% | +12.0% | -12.1% |
| 2017 | +25.0% | +21.7% | +3.3% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +28.1% | +18.3% | +9.8% |
| 2021 | -5.6% | +28.7% | -34.3% |
| 2022 | -11.5% | -18.2% | +6.6% |
| 2023 | +22.5% | +26.2% | -3.6% |
| 2024 | +32.4% | +24.9% | +7.5% |
| 2025 | -11.9% | +17.7% | -29.6% |
| 2026 | -10.0% | +8.2% | -18.3% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 50 | -0.7% | -0.1% | 48% |
| 21 sessions | 4 | -3.3% | -3.3% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[HBCP]] | [[Hill Darren M]] | $315K | 53 | – | pending |
| 2026-11-20 | [[AVEX]] | [[Morrison Christine M]] | $102K | 43 | – | pending |
| 2026-11-20 | [[SEI]] | [[Ramachandran Kyle S]] | $160K | 61 | – | pending |
| 2026-11-20 | [[SEI]] | [[Zartler William A]] | $212K | 65 | – | pending |
| 2026-11-19 | [[BGS]] | [[Mills Robert D]] | $250K | 54 | +4.4% | open |
| 2026-11-19 | [[ARR]] | [[ULM SCOTT]] | $52K | 39 | +2.6% | open |
| 2026-11-19 | [[AVK]] | [[MAITLAND TRACY V]] | $203K | 55 | +1.6% | open |
| 2026-11-19 | [[EFC]] | [[Vranos Michael W]] | $2.1M | 62 | +3.9% | open |
| 2026-11-18 | [[RMIX]] | [[Jones Mark Alan]] | $50K | 53 | -15.0% | open |
| 2026-11-18 | [[ECC]] | [[Majewski Thomas P]] | $118K | 68 | +9.4% | open |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | $65K | 70 | -13.6% | open |
| 2026-11-18 | [[CGON]] | [[Kuan Arthur]] | $2.4M | 72 | +1.0% | open |
| 2026-11-18 | [[CGON]] | [[Kalofonos Isabel]] | $299K | 65 | +1.0% | open |
| 2026-11-18 | [[EFC]] | [[Penn Laurence]] | $107K | 44 | +8.2% | open |
| 2026-11-18 | [[RILY]] | [[RILEY BRYANT R]] | $117K | 38 | -2.9% | open |
| 2026-11-17 | [[ATEC]] | [[Koning John Todd]] | $99K | 48 | +1.9% | open |
| 2026-11-17 | [[PRAA]] | [[FREDRICKSON STEVEN D]] | $295K | 57 | -5.4% | open |
| 2026-11-17 | [[RDW]] | [[Cannito Peter Anthony Jr]] | $100K | 39 | -13.0% | open |
| 2026-11-17 | [[NPCE]] | [[Williams Patrick F]] | $99K | 56 | -1.2% | open |
| 2026-11-17 | [[NPCE]] | [[Becker Joel]] | $99K | 55 | -1.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
