---
type: "strategy"
key: "opportunistic"
signals: 9638
cagr: 0.119569
spy_cagr: 0.114475
sharpe: 0.537588
max_drawdown: 0.493928
holdout_excess: -0.030008
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,638 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.1% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.0% |
| 2006-2015 excess /yr | +6.5% (p 0.058) |
| 2016+ excess /yr | -3.0% (p 0.409) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.7% | +11.4% | 0.21 | 0.58 | 54% | 0.81 | -4.7% | 32% | 3,622 | 8.0% | -4.1% / -0.49 / 62% |
| 63d | +12.0% | +11.4% | 0.54 | 0.58 | 49% | 1.08 | +0.9% | 47% | 1,446 | 3.5% | +1.7% / 0.08 / 38% |
| 126d | +10.0% | +11.4% | 0.45 | 0.58 | 52% | 1.08 | -1.0% | 42% | 741 | 1.7% | +0.5% / -0.01 / 36% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +15.7%/yr, double costs +8.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2008 | -2.4% | -34.6% | +32.2% |
| 2009 | +22.7% | +26.4% | -3.7% |
| 2010 | +29.8% | +15.1% | +14.7% |
| 2011 | +4.0% | +1.9% | +2.1% |
| 2012 | +17.1% | +16.0% | +1.1% |
| 2013 | +40.3% | +32.3% | +8.0% |
| 2014 | +10.5% | +13.5% | -2.9% |
| 2015 | -11.0% | +1.2% | -12.3% |
| 2016 | +18.2% | +12.0% | +6.2% |
| 2017 | +5.2% | +21.7% | -16.5% |
| 2018 | -9.1% | -4.6% | -4.5% |
| 2019 | +29.0% | +31.2% | -2.3% |
| 2020 | +1.7% | +18.3% | -16.7% |
| 2021 | +35.5% | +28.7% | +6.8% |
| 2022 | -23.8% | -18.2% | -5.6% |
| 2023 | +35.8% | +26.2% | +9.7% |
| 2024 | +7.5% | +24.9% | -17.4% |
| 2025 | -2.8% | +17.7% | -20.5% |
| 2026 | +46.8% | +13.3% | +33.6% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.8% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.7% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Hildebrandt Mark H]] | $175K | 53 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.8% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.1% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +1.5% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -8.1% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +3.4% | open |
| 2026-10-01 | [[LILA]] | [[MALONE JOHN C]] | $199K | 24 | -6.1% | open |
| 2026-10-01 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $1K | 8 | +2.9% | open |
| 2026-09-30 | [[KBDC]] | [[ROBO JAMES L]] | $1.9M | 49 | -3.0% | open |
| 2026-09-30 | [[KOD]] | [[667, L.P]] | $63.4M | 82 | -4.5% | open |
| 2026-09-30 | [[LEN]] | [[BUFFETT WARREN E]] | $53.9M | 70 | -5.6% | open |
| 2026-09-30 | [[ANIX]] | [[Catelani Michael]] | $16K | 46 | -11.2% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +4.5% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +4.5% | open |
| 2026-09-28 | [[LLYVK]] | [[MALONE JOHN C]] | $2.9M | 36 | -2.2% | open |
| 2026-09-28 | [[ACOG]] | [[Opaleye Management Inc]] | $271K | 25 | -2.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
