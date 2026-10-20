---
type: "strategy"
key: "score_60"
signals: 7311
cagr: 0.0794229
spy_cagr: 0.109914
sharpe: 0.354924
max_drawdown: 0.597533
holdout_excess: 0.00864389
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,311 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.6% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.1% |
| vs surviving stocks | +0.7% |
| 2006-2015 excess /yr | +7.2% (p 0.064) |
| 2016+ excess /yr | +0.9% (p 0.876) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.6% | +11.0% | 0.20 | 0.55 | 64% | 0.88 | 33% | 3,295 | 6.0% |
| 63d | +7.9% | +11.0% | 0.35 | 0.55 | 60% | 1.13 | 52% | 1,577 | 2.9% |
| 126d | +9.9% | +11.0% | 0.42 | 0.55 | 62% | 1.11 | 43% | 821 | 1.5% |


Cost sensitivity (63-session hold): no costs +10.7%/yr, double costs +5.0%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +13.7% | +11.9% | +1.8% |
| 2007 | -15.2% | +5.1% | -20.3% |
| 2008 | -25.2% | -36.8% | +11.6% |
| 2009 | +40.6% | +26.4% | +14.2% |
| 2010 | +31.6% | +15.1% | +16.6% |
| 2011 | -7.9% | +1.9% | -9.8% |
| 2012 | +18.3% | +16.0% | +2.3% |
| 2013 | +45.8% | +32.3% | +13.5% |
| 2014 | +10.3% | +13.5% | -3.1% |
| 2015 | -14.9% | +1.2% | -16.2% |
| 2016 | +24.3% | +12.0% | +12.4% |
| 2017 | +22.0% | +21.7% | +0.3% |
| 2018 | -17.3% | -4.6% | -12.7% |
| 2019 | +43.3% | +31.2% | +12.1% |
| 2020 | +27.1% | +18.3% | +8.8% |
| 2021 | +6.5% | +28.7% | -22.3% |
| 2022 | -9.7% | -18.2% | +8.5% |
| 2023 | +24.4% | +26.2% | -1.8% |
| 2024 | -1.5% | +24.9% | -26.4% |
| 2025 | +10.0% | +17.7% | -7.7% |
| 2026 | -17.2% | +13.4% | -30.6% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +1.7% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -1.5% | open |
| 2026-10-15 | [[BPRE]] | [[Ruddy Jordan B]] | $44K | 63 | -1.5% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-14 | [[BPRE]] | [[KAMFAR RAMIN]] | $5.5M | 73 | -2.7% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.9% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.7% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +1.2% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +0.9% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -4.0% | open |
| 2026-10-06 | [[PSUS]] | [[ISRAEL RYAN]] | $9.6M | 68 | +0.5% | open |
| 2026-10-05 | [[LEN]] | [[BERKSHIRE HATHAWAY INC]] | $192.6M | 70 | +3.7% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +5.9% | open |
| 2026-10-02 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -6.0% | open |
| 2026-10-01 | [[GME]] | [[Turner Nat]] | $255K | 66 | +9.4% | open |
| 2026-10-01 | [[HELP]] | [[Cavers Greg]] | $39K | 60 | -13.7% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
