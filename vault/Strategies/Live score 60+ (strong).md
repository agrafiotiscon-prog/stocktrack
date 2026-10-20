---
type: "strategy"
key: "score_60"
signals: 7208
cagr: 0.112285
spy_cagr: 0.110437
sharpe: 0.462516
max_drawdown: 0.614119
holdout_excess: 0.0195511
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,208 |
| 3-month excess vs SPY (mean / median) | +1.7% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.4% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +7.5% (p 0.065) |
| 2016+ excess /yr | +2.0% (p 0.716) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.7% | +11.0% | 0.24 | 0.55 | 62% | 0.92 | -4.0% | 33% | 3,303 | 6.2% | +0.4% / -0.05 / 59% |
| 63d | +11.2% | +11.0% | 0.46 | 0.55 | 61% | 1.24 | -0.1% | 62% | 1,583 | 3.0% | +3.6% / 0.20 / 32% |
| 126d | +11.4% | +11.0% | 0.47 | 0.55 | 65% | 1.13 | +0.6% | 57% | 822 | 1.6% | +3.5% / 0.20 / 43% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.9%/yr, double costs +8.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +17.9% | +13.3% | +4.6% |
| 2007 | -12.3% | +5.1% | -17.4% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +14.9% |
| 2010 | +32.4% | +15.1% | +17.4% |
| 2011 | -2.9% | +1.9% | -4.8% |
| 2012 | +19.3% | +16.0% | +3.3% |
| 2013 | +44.2% | +32.3% | +11.9% |
| 2014 | +9.5% | +13.5% | -4.0% |
| 2015 | -12.5% | +1.2% | -13.7% |
| 2016 | +25.4% | +12.0% | +13.4% |
| 2017 | +25.3% | +21.7% | +3.6% |
| 2018 | -16.6% | -4.6% | -12.0% |
| 2019 | +51.8% | +31.2% | +20.5% |
| 2020 | +22.3% | +18.3% | +4.0% |
| 2021 | +0.2% | +28.7% | -28.5% |
| 2022 | -6.3% | -18.2% | +11.8% |
| 2023 | +38.2% | +26.2% | +12.0% |
| 2024 | +3.5% | +24.9% | -21.4% |
| 2025 | +24.2% | +17.7% | +6.5% |
| 2026 | +2.1% | +13.3% | -11.2% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | – | pending |
| 2026-10-19 | [[BPRE]] | [[KAMFAR RAMIN]] | $2.4M | 64 | – | pending |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +2.2% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | +1.7% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.0% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.5% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Fine Carol F]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[CHERUVATATH NANDAKUMAR]] | $175K | 62 | +4.8% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +0.5% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +1.2% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -6.2% | open |
| 2026-10-06 | [[PSUS]] | [[ISRAEL RYAN]] | $9.6M | 68 | +0.6% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +3.4% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
