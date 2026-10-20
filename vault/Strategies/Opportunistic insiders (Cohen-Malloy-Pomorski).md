---
type: "strategy"
key: "opportunistic"
signals: 9521
cagr: 0.111846
spy_cagr: 0.114538
sharpe: 0.51343
max_drawdown: 0.518253
holdout_excess: -0.0333744
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,521 |
| 3-month excess vs SPY (mean / median) | +0.4% / -1.0% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.3% |
| vs surviving stocks | +0.2% |
| 2006-2015 excess /yr | +6.2% (p 0.085) |
| 2016+ excess /yr | -3.3% (p 0.343) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.4% | +11.5% | 0.20 | 0.58 | 53% | 0.74 | 26% | 3,620 | 7.9% |
| 63d | +11.2% | +11.5% | 0.51 | 0.58 | 52% | 0.90 | 37% | 1,442 | 3.3% |
| 126d | +8.7% | +11.5% | 0.40 | 0.58 | 54% | 0.97 | 32% | 737 | 1.6% |


Cost sensitivity (63-session hold): no costs +14.5%/yr, double costs +7.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2008 | -1.6% | -34.6% | +33.0% |
| 2009 | +23.4% | +26.4% | -3.0% |
| 2010 | +25.4% | +15.1% | +10.4% |
| 2011 | -3.0% | +1.9% | -4.9% |
| 2012 | +18.1% | +16.0% | +2.1% |
| 2013 | +37.1% | +32.3% | +4.8% |
| 2014 | +8.7% | +13.5% | -4.7% |
| 2015 | -10.0% | +1.2% | -11.2% |
| 2016 | +23.7% | +12.0% | +11.7% |
| 2017 | -2.3% | +21.7% | -24.0% |
| 2018 | -10.4% | -4.6% | -5.8% |
| 2019 | +16.9% | +31.2% | -14.3% |
| 2020 | +14.7% | +18.3% | -3.7% |
| 2021 | +33.0% | +28.7% | +4.3% |
| 2022 | -20.8% | -18.2% | -2.7% |
| 2023 | +16.9% | +26.2% | -9.3% |
| 2024 | +11.6% | +24.9% | -13.3% |
| 2025 | -0.6% | +17.7% | -18.3% |
| 2026 | +57.4% | +13.4% | +44.0% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.7% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.9% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.2% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +0.9% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -8.3% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +3.7% | open |
| 2026-10-01 | [[LILA]] | [[MALONE JOHN C]] | $199K | 24 | -6.3% | open |
| 2026-10-01 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $1K | 8 | +2.3% | open |
| 2026-09-30 | [[KBDC]] | [[ROBO JAMES L]] | $1.9M | 49 | -3.2% | open |
| 2026-09-30 | [[KOD]] | [[667, L.P]] | $63.4M | 82 | -5.4% | open |
| 2026-09-30 | [[LEN]] | [[BUFFETT WARREN E]] | $53.9M | 70 | -5.3% | open |
| 2026-09-30 | [[ANIX]] | [[Catelani Michael]] | $16K | 46 | -9.6% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +4.0% | open |
| 2026-09-29 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $340 | 8 | +4.0% | open |
| 2026-09-28 | [[LLYVK]] | [[MALONE JOHN C]] | $2.9M | 36 | -2.0% | open |
| 2026-09-28 | [[ACOG]] | [[Opaleye Management Inc]] | $271K | 25 | -3.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
