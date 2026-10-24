---
type: "strategy"
key: "opportunistic"
signals: 9631
cagr: 0.121306
spy_cagr: 0.114649
sharpe: 0.544547
max_drawdown: 0.493928
holdout_excess: -0.0292959
---

# Opportunistic insiders (Cohen-Malloy-Pomorski)

Rule key: `opportunistic`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 9,631 |
| 3-month excess vs SPY (mean / median) | +0.3% / -1.0% |
| Beat SPY over 3 months | 46% |
| Entering one session later | +0.2% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +6.5% (p 0.056) |
| 2016+ excess /yr | -2.9% (p 0.420) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +11.5% | 0.22 | 0.58 | 54% | 0.81 | -4.6% | 32% | 3,621 | 8.0% | -4.1% / -0.48 / 62% |
| 63d | +12.1% | +11.5% | 0.54 | 0.58 | 49% | 1.08 | +1.1% | 47% | 1,446 | 3.5% | +1.8% / 0.09 / 36% |
| 126d | +10.0% | +11.5% | 0.45 | 0.58 | 52% | 1.08 | -1.0% | 42% | 741 | 1.7% | +0.5% / -0.01 / 36% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +15.8%/yr, double costs +8.8%/yr.


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
| 2020 | +4.5% | +18.3% | -13.9% |
| 2021 | +35.5% | +28.7% | +6.8% |
| 2022 | -23.9% | -18.2% | -5.7% |
| 2023 | +35.9% | +26.2% | +9.8% |
| 2024 | +7.4% | +24.9% | -17.5% |
| 2025 | -2.9% | +17.7% | -20.6% |
| 2026 | +47.3% | +13.7% | +33.7% |


## Live forward test

7 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-22 | [[VKI]] | [[BANK OF AMERICA CORP -DE-]] | $843 | 28 | -1.9% | open |
| 2026-10-22 | [[NMCO]] | [[BANK OF AMERICA CORP -DE-]] | $974 | 40 | -2.4% | open |
| 2026-10-22 | [[NBH]] | [[BANK OF AMERICA CORP -DE-]] | $845 | 28 | -1.2% | open |
| 2026-10-22 | [[LEO]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | -1.1% | open |
| 2026-10-22 | [[DSM]] | [[BANK OF AMERICA CORP -DE-]] | $1K | 40 | -0.8% | open |
| 2026-10-22 | [[NMCO]] | [[Jones Nathaniel T]] | $4K | 40 | -2.4% | open |
| 2026-10-20 | [[NXG]] | [[Sunderland Todd]] | $46K | 26 | -2.1% | open |
| 2026-10-20 | [[ISBA]] | [[Bourland Jill]] | $300 | 13 | +4.8% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +0.1% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +3.6% | open |
| 2026-10-13 | [[HEI]] | [[Hildebrandt Mark H]] | $175K | 53 | +2.0% | open |
| 2026-10-13 | [[HEI]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +2.0% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | +0.3% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +2.0% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -10.4% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +16.4% | open |
| 2026-10-01 | [[LILA]] | [[MALONE JOHN C]] | $199K | 24 | -3.4% | open |
| 2026-10-01 | [[TPL]] | [[HORIZON KINETICS ASSET MANAGEMENT LLC]] | $1K | 8 | +1.8% | open |
| 2026-09-30 | [[KBDC]] | [[ROBO JAMES L]] | $1.9M | 49 | +1.6% | open |
| 2026-09-30 | [[KOD]] | [[667, L.P]] | $63.4M | 82 | -7.6% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "opportunistic")
SORT filed DESC
```

Back to [[What Works]].
