---
type: "strategy"
key: "opportunistic"
signals: 9631
cagr: 0.123836
spy_cagr: 0.114475
sharpe: 0.555668
max_drawdown: 0.488957
holdout_excess: -0.0288132
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,631 |
| 3-month excess vs SPY (mean / median) | +0.4% / -1.0% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.3% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.5% (p 0.056) |
| 2016+ excess /yr | -2.9% (p 0.428) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +11.4% | 0.22 | 0.58 | 54% | 0.81 | -4.6% | 32% | 3,621 | 8.0% | -4.0% / -0.47 / 61% |
| 63d | +12.4% | +11.4% | 0.56 | 0.58 | 49% | 1.07 | +1.4% | 47% | 1,447 | 3.5% | +2.0% / 0.11 / 34% |
| 126d | +10.2% | +11.4% | 0.46 | 0.58 | 52% | 1.09 | -0.9% | 58% | 741 | 1.7% | +0.7% / 0.01 / 36% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.2%/yr, double costs +9.1%/yr.


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
| 2017 | +5.2% | +21.7% | -16.5% |
| 2018 | -9.1% | -4.6% | -4.5% |
| 2019 | +29.0% | +31.2% | -2.3% |
| 2020 | +8.7% | +18.3% | -9.7% |
| 2021 | +32.2% | +28.7% | +3.5% |
| 2022 | -24.5% | -18.2% | -6.3% |
| 2023 | +37.8% | +26.2% | +11.6% |
| 2024 | +10.1% | +24.9% | -14.8% |
| 2025 | -3.0% | +17.7% | -20.7% |
| 2026 | +46.7% | +13.3% | +33.4% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-20 | [[NXG]] | [[Sunderland Todd]] | $46K | 26 | – | pending |
| 2026-10-20 | [[ISBA]] | [[Bourland Jill]] | $300 | 13 | – | pending |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.6% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.9% | open |
| 2026-10-13 | [[HEI]] | [[Hildebrandt Mark H]] | $175K | 53 | +3.4% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +3.4% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -0.4% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +1.9% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -8.6% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +6.8% | open |
| 2026-10-01 | [[LILA]] | [[MALONE JOHN C]] | $199K | 24 | -4.7% | open |
| 2026-10-01 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $1K | 8 | +1.8% | open |
| 2026-09-30 | [[KBDC]] | [[ROBO JAMES L]] | $1.9M | 49 | -2.0% | open |
| 2026-09-30 | [[KOD]] | [[667, L.P]] | $63.4M | 82 | -3.2% | open |
| 2026-09-30 | [[LEN]] | [[BUFFETT WARREN E]] | $53.9M | 70 | -2.5% | open |
| 2026-09-30 | [[ANIX]] | [[Catelani Michael]] | $16K | 46 | -9.1% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +3.4% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +3.4% | open |
| 2026-09-28 | [[LLYVK]] | [[MALONE JOHN C]] | $2.9M | 36 | -0.1% | open |
| 2026-09-28 | [[ACOG]] | [[Opaleye Management Inc]] | $271K | 25 | -1.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
