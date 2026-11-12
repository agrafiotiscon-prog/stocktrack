---
type: "strategy"
key: "opportunistic"
signals: 9651
cagr: 0.13449
spy_cagr: 0.112776
sharpe: 0.592308
max_drawdown: 0.497034
holdout_excess: -0.0287798
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,651 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.1% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.7% |
| 2006-2015 excess /yr | +6.4% (p 0.061) |
| 2016+ excess /yr | -2.9% (p 0.428) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +11.3% | 0.22 | 0.57 | 53% | 0.80 | -4.5% | 26% | 3,638 | 8.0% | -4.2% / -0.50 / 63% |
| 63d | +13.4% | +11.3% | 0.59 | 0.57 | 50% | 1.10 | +2.4% | 47% | 1,448 | 3.5% | +2.9% / 0.18 / 31% |
| 126d | +10.5% | +11.3% | 0.47 | 0.57 | 52% | 1.07 | -0.3% | 47% | 742 | 1.7% | +0.8% / 0.02 / 34% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +17.2%/yr, double costs +10.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2008 | -2.4% | -34.6% | +32.2% |
| 2009 | +22.7% | +26.4% | -3.7% |
| 2010 | +29.8% | +15.1% | +14.7% |
| 2011 | +4.0% | +1.9% | +2.1% |
| 2012 | +17.1% | +16.0% | +1.1% |
| 2013 | +41.1% | +32.3% | +8.8% |
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
| 2025 | -5.1% | +17.7% | -22.8% |
| 2026 | +54.7% | +10.8% | +43.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 26 | +1.9% | +2.1% | 81% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | $745K | 37 | +14.1% | open |
| 2026-11-10 | [[BSM]] | [[Carter Thomas L Jr]] | $686K | 44 | +0.2% | open |
| 2026-11-10 | [[EGBN]] | [[Newell Eric R]] | $50K | 41 | +0.2% | open |
| 2026-11-10 | [[TXO]] | [[SIMPSON BOB R]] | $3.1M | 41 | -0.8% | open |
| 2026-11-10 | [[BOTJ]] | [[ADDISON LEWIS C]] | $2K | 14 | -2.3% | open |
| 2026-11-10 | [[GOOD]] | [[Gerson Gary]] | $86K | 60 | +0.1% | open |
| 2026-11-10 | [[MTDR]] | [[Ehrman Monika U]] | $17K | 42 | +1.3% | open |
| 2026-11-10 | [[LBTYA]] | [[MALONE JOHN C]] | $1.5M | 53 | +4.2% | open |
| 2026-11-09 | [[UFCS]] | [[MILLIGAN GEORGE D]] | $237K | 32 | +1.7% | open |
| 2026-11-09 | [[MTDR]] | [[Appel Shelley F]] | $68K | 60 | +5.0% | open |
| 2026-11-09 | [[MTCH]] | [[Schiffman Glenn]] | $97K | 27 | +4.0% | open |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | -1.6% | open |
| 2026-11-09 | [[AN]] | [[Szlosek Thomas A]] | $200K | 67 | -1.2% | open |
| 2026-11-09 | [[BOTJ]] | [[BRYANT WILLIAM C III]] | $17K | 17 | +0.7% | open |
| 2026-11-09 | [[LKFN]] | [[BARTELS ROBERT E JR]] | $117K | 30 | -1.8% | open |
| 2026-11-09 | [[CZNC]] | [[Shattuck Katherine W]] | $198 | 0 | -2.5% | open |
| 2026-11-09 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $622K | 27 | -0.5% | open |
| 2026-11-09 | [[MTDR]] | [[Foran Joseph Wm]] | $257K | 84 | +5.0% | open |
| 2026-11-06 | [[KYN]] | [[Baker James C]] | $331K | 54 | +2.3% | open |
| 2026-11-06 | [[MTDR]] | [[Elsener William Thomas]] | $46K | 48 | +3.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
