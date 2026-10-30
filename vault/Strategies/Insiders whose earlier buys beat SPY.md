---
type: "strategy"
key: "proven_insider"
signals: 20169
cagr: 0.089958
spy_cagr: 0.112525
sharpe: 0.394825
max_drawdown: 0.609637
holdout_excess: 0.00578577
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,169 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +5.7% (p 0.027) |
| 2016+ excess /yr | +0.6% (p 0.861) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +8.1% | +11.3% | 0.37 | 0.56 | 52% | 1.10 | -2.7% | 29% | 4,544 | 8.6% | -0.0% / -0.10 / 43% |
| 63d | +9.0% | +11.3% | 0.39 | 0.56 | 61% | 1.18 | -2.4% | 48% | 1,615 | 3.1% | +0.8% / -0.01 / 50% |
| 126d | +9.6% | +11.3% | 0.43 | 0.56 | 56% | 1.12 | -1.5% | 48% | 819 | 1.6% | +0.8% / -0.01 / 31% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.6%/yr, double costs +5.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.0% | +3.0% |
| 2007 | -0.0% | +5.1% | -5.1% |
| 2008 | -20.0% | -36.8% | +16.8% |
| 2009 | +15.4% | +26.4% | -11.0% |
| 2010 | +39.2% | +15.1% | +24.2% |
| 2011 | +7.8% | +1.9% | +5.9% |
| 2012 | +21.3% | +16.0% | +5.3% |
| 2013 | +39.8% | +32.3% | +7.5% |
| 2014 | +16.3% | +13.5% | +2.9% |
| 2015 | -15.1% | +1.2% | -16.3% |
| 2016 | +26.8% | +12.0% | +14.8% |
| 2017 | +10.0% | +21.7% | -11.7% |
| 2018 | -16.6% | -4.6% | -12.1% |
| 2019 | +10.4% | +31.2% | -20.8% |
| 2020 | +10.0% | +18.3% | -8.4% |
| 2021 | +6.1% | +28.7% | -22.6% |
| 2022 | -25.8% | -18.2% | -7.6% |
| 2023 | +31.9% | +26.2% | +5.8% |
| 2024 | +12.3% | +24.9% | -12.6% |
| 2025 | +17.8% | +17.7% | +0.1% |
| 2026 | +10.9% | +13.7% | -2.8% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 17 | +1.2% | +1.7% | 76% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 | [[DSM]] | [[Saba Capital Management, L.P]] | $11K | 9 | – | pending |
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | – | pending |
| 2026-10-29 | [[UTMD]] | [[CORNWELL KEVIN L]] | $67K | 35 | – | pending |
| 2026-10-29 | [[BMN]] | [[BANK OF AMERICA CORP -DE-]] | $71K | 36 | – | pending |
| 2026-10-29 | [[BBT]] | [[Callahan Mary Anne]] | $97K | 54 | – | pending |
| 2026-10-28 | [[DSM]] | [[Saba Capital Management, L.P]] | $77K | 18 | +1.4% | open |
| 2026-10-28 | [[HXL]] | [[KEATING NEAL J]] | $242K | 46 | -0.2% | open |
| 2026-10-27 | [[SRRK]] | [[AKKARAJU SRINIVAS]] | $12.0M | 48 | +1.1% | open |
| 2026-10-27 | [[LEO]] | [[Saba Capital Management, L.P]] | $72K | 18 | +0.3% | open |
| 2026-10-27 | [[DSM]] | [[Saba Capital Management, L.P]] | $111K | 20 | +1.4% | open |
| 2026-10-27 | [[MSM]] | [[JACOBSON MITCHELL]] | $29.0M | 63 | +2.4% | open |
| 2026-10-27 | [[PEBO]] | [[Smith Dwight Eric]] | $12K | 17 | +1.3% | open |
| 2026-10-26 | [[STC]] | [[BRADLEY C ALLEN JR]] | $95K | 50 | +3.4% | open |
| 2026-10-26 | [[KRRO]] | [[Lynx1 Capital Management LP]] | $885K | 34 | +11.3% | open |
| 2026-10-26 | [[THRM]] | [[MASCARENAS PAUL ANTHONY]] | $533K | 61 | +7.8% | open |
| 2026-10-26 | [[LEO]] | [[Saba Capital Management, L.P]] | $369K | 27 | +0.9% | open |
| 2026-10-26 | [[TCBX]] | [[Bobbora William]] | $40K | 24 | -0.8% | open |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | +9.0% | open |
| 2026-10-23 | [[THFF]] | [[McDonald James O]] | $6K | 14 | -0.3% | open |
| 2026-10-22 | [[LEO]] | [[Saba Capital Management, L.P]] | $263K | 25 | +1.7% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
