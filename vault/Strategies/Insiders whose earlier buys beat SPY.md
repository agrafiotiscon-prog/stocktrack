---
type: "strategy"
key: "proven_insider"
signals: 19835
cagr: 0.106586
spy_cagr: 0.112966
sharpe: 0.453189
max_drawdown: 0.547209
holdout_excess: 0.00735548
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 19,835 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.4% |
| 2006-2015 excess /yr | +6.3% (p 0.009) |
| 2016+ excess /yr | +0.7% (p 0.818) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.7% | +11.3% | 0.32 | 0.57 | 49% | 1.02 | 24% | 4,542 | 8.5% |
| 63d | +10.7% | +11.3% | 0.45 | 0.57 | 55% | 1.12 | 43% | 1,611 | 3.1% |
| 126d | +11.4% | +11.3% | 0.49 | 0.57 | 51% | 1.06 | 38% | 817 | 1.6% |


Cost sensitivity (63-session hold): no costs +13.9%/yr, double costs +7.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.3% | +13.9% | +2.5% |
| 2007 | -4.1% | +5.1% | -9.3% |
| 2008 | -6.3% | -36.8% | +30.5% |
| 2009 | +35.5% | +26.4% | +9.1% |
| 2010 | +40.2% | +15.1% | +25.2% |
| 2011 | -0.6% | +1.9% | -2.5% |
| 2012 | +17.5% | +16.0% | +1.5% |
| 2013 | +40.1% | +32.3% | +7.8% |
| 2014 | +11.8% | +13.5% | -1.7% |
| 2015 | -10.1% | +1.2% | -11.4% |
| 2016 | +15.4% | +12.0% | +3.4% |
| 2017 | +7.2% | +21.7% | -14.5% |
| 2018 | -11.8% | -4.6% | -7.2% |
| 2019 | +14.6% | +31.2% | -16.6% |
| 2020 | +6.1% | +18.3% | -12.2% |
| 2021 | +13.1% | +28.7% | -15.7% |
| 2022 | -21.9% | -18.2% | -3.8% |
| 2023 | +39.0% | +26.2% | +12.8% |
| 2024 | +12.3% | +24.9% | -12.6% |
| 2025 | +22.8% | +17.7% | +5.1% |
| 2026 | +7.4% | +13.4% | -6.0% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[SAH]] | [[Rusnak Paul P]] | $752K | 28 | -2.3% | open |
| 2026-10-16 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | -1.7% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.9% | open |
| 2026-10-13 | [[PCQ]] | [[BANK OF AMERICA CORP -DE-]] | $16K | 30 | +1.9% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +1.2% | open |
| 2026-10-09 | [[NEOG]] | [[Nassif Mikheal]] | $6K | 44 | -1.0% | open |
| 2026-10-09 | [[MWA]] | [[Healy Brian C]] | $30K | 8 | +2.2% | open |
| 2026-10-09 | [[SAH]] | [[Rusnak Paul P]] | $819K | 29 | +5.1% | open |
| 2026-10-08 | [[CET]] | [[Hill John C]] | $28K | 32 | +0.9% | open |
| 2026-10-07 | [[SAH]] | [[Rusnak Paul P]] | $67K | 17 | +4.9% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.7M | 32 | +4.0% | open |
| 2026-10-06 | [[DYN]] | [[Posner Brian S]] | $40K | 27 | -1.8% | open |
| 2026-10-06 | [[SAH]] | [[Rusnak Paul P]] | $1.3M | 31 | +4.0% | open |
| 2026-10-06 | [[AEF]] | [[Clark Anthony S]] | $19K | 31 | -8.3% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +3.7% | open |
| 2026-10-05 | [[NXRT]] | [[McGraner Matt]] | $201K | 32 | -4.4% | open |
| 2026-10-05 | [[IBKR]] | [[Conkling Lori A]] | $2K | 0 | -7.4% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +5.9% | open |
| 2026-10-01 | [[RMT]] | [[CLARK CHRISTOPHER D]] | $13K | 27 | -7.2% | open |
| 2026-10-01 | [[GTLB]] | [[Staples William]] | $125K | 23 | +5.7% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
