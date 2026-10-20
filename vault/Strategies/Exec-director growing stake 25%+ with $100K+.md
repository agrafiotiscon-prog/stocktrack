---
type: "strategy"
key: "big_stake_up"
signals: 11223
cagr: 0.116807
spy_cagr: 0.110724
sharpe: 0.475202
max_drawdown: 0.611805
holdout_excess: 0.0177063
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,223 |
| 3-month excess vs SPY (mean / median) | +0.9% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.5% |
| 2006-2015 excess /yr | +6.6% (p 0.035) |
| 2016+ excess /yr | +1.8% (p 0.659) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.0% | +11.1% | 0.18 | 0.56 | 55% | 1.04 | 19% | 4,227 | 6.3% |
| 63d | +11.7% | +11.1% | 0.48 | 0.56 | 61% | 1.18 | 48% | 1,651 | 2.8% |
| 126d | +6.8% | +11.1% | 0.32 | 0.56 | 66% | 1.18 | 48% | 838 | 1.3% |


Cost sensitivity (63-session hold): no costs +14.3%/yr, double costs +9.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +10.2% | +13.8% | -3.7% |
| 2007 | -4.3% | +5.1% | -9.5% |
| 2008 | -31.8% | -36.8% | +5.0% |
| 2009 | +48.4% | +26.4% | +22.0% |
| 2010 | +33.1% | +15.1% | +18.0% |
| 2011 | +9.6% | +1.9% | +7.7% |
| 2012 | +28.2% | +16.0% | +12.2% |
| 2013 | +49.1% | +32.3% | +16.8% |
| 2014 | +9.9% | +13.5% | -3.6% |
| 2015 | -9.1% | +1.2% | -10.3% |
| 2016 | +24.7% | +12.0% | +12.7% |
| 2017 | +18.6% | +21.7% | -3.1% |
| 2018 | -13.5% | -4.6% | -8.9% |
| 2019 | +43.3% | +31.2% | +12.1% |
| 2020 | +13.7% | +18.3% | -4.6% |
| 2021 | +8.9% | +28.7% | -19.8% |
| 2022 | -16.5% | -18.2% | +1.7% |
| 2023 | +21.3% | +26.2% | -4.8% |
| 2024 | +19.4% | +24.9% | -5.5% |
| 2025 | +2.7% | +17.7% | -15.1% |
| 2026 | +18.3% | +13.4% | +4.9% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +1.7% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -1.5% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | $850K | 51 | +0.1% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -6.2% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | +13.5% | open |
| 2026-10-13 | [[RTSN]] | [[BERGER FRANKLIN M]] | $120K | 55 | +55.7% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.7% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Neitzel Julie]] | $175K | 56 | +4.7% | open |
| 2026-10-13 | [[FEAM]] | [[vant Hoff Graham]] | $215K | 45 | -19.5% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +1.2% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PHK]] | [[FLATTUM DAVID C]] | $249K | 46 | -1.3% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +0.9% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-06 | [[PSUS]] | [[ISRAEL RYAN]] | $9.6M | 68 | +0.5% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |
| 2026-10-01 | [[GME]] | [[Turner Nat]] | $255K | 66 | +9.4% | open |
| 2026-10-01 | [[ORCL]] | [[RUSCKOWSKI STEPHEN H]] | $3.5M | 57 | -7.8% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
