---
type: "strategy"
key: "opportunistic"
signals: 9661
cagr: 0.122435
spy_cagr: 0.11325
sharpe: 0.548752
max_drawdown: 0.493905
holdout_excess: -0.0289608
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,661 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.1% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +6.6% (p 0.052) |
| 2016+ excess /yr | -2.9% (p 0.426) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.1% | +11.3% | 0.23 | 0.57 | 52% | 0.81 | -4.2% | 32% | 3,638 | 8.0% | -3.9% / -0.46 / 60% |
| 63d | +12.2% | +11.3% | 0.55 | 0.57 | 49% | 1.09 | +1.3% | 47% | 1,447 | 3.5% | +1.8% / 0.09 / 35% |
| 126d | +10.1% | +11.3% | 0.45 | 0.57 | 52% | 1.08 | -0.8% | 47% | 741 | 1.7% | +0.5% / -0.01 / 35% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.0%/yr, double costs +8.9%/yr.


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
| 2015 | -8.8% | +1.2% | -10.0% |
| 2016 | +18.2% | +12.0% | +6.2% |
| 2017 | +5.2% | +21.7% | -16.5% |
| 2018 | -9.1% | -4.6% | -4.5% |
| 2019 | +28.9% | +31.2% | -2.3% |
| 2020 | +4.4% | +18.3% | -13.9% |
| 2021 | +35.5% | +28.7% | +6.7% |
| 2022 | -24.0% | -18.2% | -5.8% |
| 2023 | +36.0% | +26.2% | +9.8% |
| 2024 | +8.0% | +24.9% | -16.9% |
| 2025 | -3.0% | +17.7% | -20.7% |
| 2026 | +46.4% | +11.5% | +34.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 17 | +1.9% | +2.1% | 88% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[KYN]] | [[Baker James C]] | $331K | 54 | – | pending |
| 2026-11-06 | [[MTDR]] | [[Elsener William Thomas]] | $46K | 48 | – | pending |
| 2026-11-05 | [[BXMT]] | [[NASSAU HENRY N]] | $114K | 41 | -2.9% | open |
| 2026-11-05 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | $3.6M | 53 | +1.0% | open |
| 2026-11-05 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $282K | 23 | -0.5% | open |
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | $15.0M | 80 | -1.2% | open |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | $400K | 65 | +1.3% | open |
| 2026-11-04 | [[TBBK]] | [[Cohn Matthew]] | $46K | 22 | +3.6% | open |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | +1.1% | open |
| 2026-11-04 | [[UMH]] | [[Carus Jeffrey A]] | $8K | 32 | +0.1% | open |
| 2026-11-03 | [[SIRI]] | [[BERKSHIRE HATHAWAY INC]] | $26.9M | 40 | +7.4% | open |
| 2026-11-03 | [[BBTX]] | [[RA CAPITAL MANAGEMENT, L.P]] | $46.6M | 74 | +2.2% | open |
| 2026-11-03 | [[FFIN]] | [[Edwards Murray Hamilton]] | $24K | 32 | -1.0% | open |
| 2026-11-02 | [[FCPT]] | [[Lenehan William H]] | $226K | 42 | +2.4% | open |
| 2026-10-30 | [[PKBK]] | [[PANTILIONE VITO S]] | $43K | 33 | +2.7% | open |
| 2026-10-30 | [[FFIN]] | [[Denny Michael B]] | $100K | 42 | +1.6% | open |
| 2026-10-30 | [[BHRB]] | [[McLaughlin Shawn Patrick]] | $36K | 20 | +1.6% | open |
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | -11.2% | open |
| 2026-10-29 | [[BMN]] | [[BANK OF AMERICA CORP -DE-]] | $71K | 36 | +7.8% | open |
| 2026-10-29 | [[SHBI]] | [[LAMON JOHN]] | $8K | 14 | +1.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
