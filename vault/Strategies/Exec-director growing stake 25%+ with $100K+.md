---
type: "strategy"
key: "big_stake_up"
signals: 11402
cagr: 0.105919
spy_cagr: 0.110668
sharpe: 0.445691
max_drawdown: 0.653175
holdout_excess: 0.016554
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,402 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +0.2% |
| 2006-2015 excess /yr | +6.4% (p 0.031) |
| 2016+ excess /yr | +1.7% (p 0.680) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.0% | +11.1% | 0.22 | 0.55 | 54% | 1.06 | -5.9% | 24% | 4,249 | 6.4% | -1.8% / -0.23 / 50% |
| 63d | +10.6% | +11.1% | 0.45 | 0.55 | 65% | 1.30 | -1.7% | 52% | 1,651 | 2.7% | +2.3% / 0.11 / 33% |
| 126d | +7.7% | +11.1% | 0.35 | 0.55 | 64% | 1.24 | -3.9% | 48% | 837 | 1.3% | -0.2% / -0.08 / 45% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.4%/yr, double costs +7.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -4.9% | +5.1% | -10.1% |
| 2008 | -42.0% | -36.8% | -5.2% |
| 2009 | +56.5% | +26.4% | +30.1% |
| 2010 | +36.6% | +15.1% | +21.5% |
| 2011 | +7.2% | +1.9% | +5.3% |
| 2012 | +20.9% | +16.0% | +4.9% |
| 2013 | +49.0% | +32.3% | +16.7% |
| 2014 | +17.7% | +13.5% | +4.2% |
| 2015 | -7.9% | +1.2% | -9.2% |
| 2016 | +19.7% | +12.0% | +7.7% |
| 2017 | +18.5% | +21.7% | -3.2% |
| 2018 | -14.6% | -4.6% | -10.0% |
| 2019 | +43.9% | +31.2% | +12.7% |
| 2020 | +27.5% | +18.3% | +9.2% |
| 2021 | +4.0% | +28.7% | -24.8% |
| 2022 | -19.2% | -18.2% | -1.1% |
| 2023 | +16.6% | +26.2% | -9.6% |
| 2024 | +15.3% | +24.9% | -9.6% |
| 2025 | -0.3% | +17.7% | -18.0% |
| 2026 | +14.7% | +13.3% | +1.4% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | – | pending |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +2.2% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | +1.7% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.0% | open |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | $850K | 51 | +0.5% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -10.0% | open |
| 2026-10-13 | [[CTNT]] | [[Liu Huan]] | $330K | 49 | +13.2% | open |
| 2026-10-13 | [[RTSN]] | [[BERGER FRANKLIN M]] | $120K | 55 | +41.5% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Neitzel Julie]] | $175K | 56 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[Fine Carol F]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[SCHRIESHEIM ALAN]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[FEAM]] | [[vant Hoff Graham]] | $215K | 45 | -21.7% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +0.5% | open |
| 2026-10-09 | [[BPRE]] | [[KAMFAR RAMIN]] | $8.5M | 81 | -5.1% | open |
| 2026-10-08 | [[PHK]] | [[FLATTUM DAVID C]] | $249K | 46 | -1.4% | open |
| 2026-10-08 | [[PDI]] | [[FLATTUM DAVID C]] | $250K | 66 | +1.2% | open |
| 2026-10-08 | [[FUL]] | [[BAILLY R JEFFREY]] | $500K | 74 | +3.4% | open |
| 2026-10-06 | [[PSUS]] | [[ISRAEL RYAN]] | $9.6M | 68 | +0.6% | open |
| 2026-10-05 | [[BPRE]] | [[KAMFAR RAMIN]] | $3.4M | 73 | -2.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
