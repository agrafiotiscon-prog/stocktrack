---
type: "strategy"
key: "all_liquid"
signals: 67484
cagr: 0.0609782
spy_cagr: 0.110756
sharpe: 0.292644
max_drawdown: 0.573686
holdout_excess: 0.00326997
---

# Every discretionary insider buy

Rule key: `all_liquid`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 67,484 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +6.4% (p 0.017) |
| 2016+ excess /yr | +0.3% (p 0.928) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.0% | +11.1% | 0.32 | 0.56 | 61% | 1.21 | -3.9% | 38% | 4,980 | 9.2% | -1.3% / -0.15 / 67% |
| 63d | +6.1% | +11.1% | 0.29 | 0.56 | 57% | 1.17 | -4.9% | 43% | 1,663 | 2.6% | -2.3% / -0.25 / 63% |
| 126d | +7.0% | +11.1% | 0.33 | 0.56 | 54% | 1.15 | -3.9% | 33% | 840 | 1.5% | -1.7% / -0.19 / 56% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +9.0%/yr, double costs +3.4%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.9% | +13.8% | +9.0% |
| 2007 | -5.0% | +5.1% | -10.1% |
| 2008 | -27.7% | -36.8% | +9.1% |
| 2009 | +54.7% | +26.4% | +28.3% |
| 2010 | +21.8% | +15.1% | +6.7% |
| 2011 | -9.5% | +1.9% | -11.4% |
| 2012 | +23.9% | +16.0% | +7.9% |
| 2013 | +37.5% | +32.3% | +5.2% |
| 2014 | +5.3% | +13.5% | -8.2% |
| 2015 | +7.0% | +1.2% | +5.7% |
| 2016 | +21.2% | +12.0% | +9.2% |
| 2017 | +15.3% | +21.7% | -6.4% |
| 2018 | -14.7% | -4.6% | -10.1% |
| 2019 | +15.0% | +31.2% | -16.2% |
| 2020 | +44.6% | +18.3% | +26.3% |
| 2021 | +0.3% | +28.7% | -28.4% |
| 2022 | -41.7% | -18.2% | -23.6% |
| 2023 | +22.9% | +26.2% | -3.3% |
| 2024 | -13.0% | +24.9% | -37.9% |
| 2025 | -1.1% | +17.7% | -18.8% |
| 2026 | +1.0% | +13.7% | -12.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 21 | +1.1% | +2.8% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | – | pending |
| 2026-10-28 | [[ACN]] | [[Price Paula A]] | $200K | 46 | – | pending |
| 2026-10-27 | [[PDI]] | [[Morris Sonya]] | $82K | 41 | – | pending |
| 2026-10-27 | [[LRN]] | [[Haggart Dylan G]] | $12.2M | 50 | – | pending |
| 2026-10-27 | [[SRRK]] | [[AKKARAJU SRINIVAS]] | $12.0M | 48 | – | pending |
| 2026-10-27 | [[LYCA]] | [[Venrock Healthcare Capital Partners III, L.P]] | $37.7M | 57 | – | pending |
| 2026-10-27 | [[AIOK]] | [[Panagiotidis Petros Panagiotis]] | $1.1M | 51 | – | pending |
| 2026-10-27 | [[LEO]] | [[Saba Capital Management, L.P]] | $72K | 18 | – | pending |
| 2026-10-27 | [[DSM]] | [[Saba Capital Management, L.P]] | $111K | 20 | – | pending |
| 2026-10-27 | [[MSM]] | [[JACOBSON MITCHELL]] | $29.0M | 63 | – | pending |
| 2026-10-27 | [[STC]] | [[Matz Deborah Jane]] | $44K | 63 | – | pending |
| 2026-10-27 | [[NMCO]] | [[Robert Young L]] | $249K | 50 | – | pending |
| 2026-10-27 | [[NUV]] | [[Robert Young L]] | $300K | 39 | – | pending |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | – | pending |
| 2026-10-27 | [[NXP]] | [[Robert Young L]] | $300K | 39 | – | pending |
| 2026-10-27 | [[CTEV]] | [[ARES MANAGEMENT LLC]] | $1.7M | 36 | – | pending |
| 2026-10-27 | [[CRBG]] | [[NIPPON LIFE INSURANCE CO]] | $20.2M | 25 | – | pending |
| 2026-10-27 | [[BHRB]] | [[WILSON DAVID]] | $7K | 27 | – | pending |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | $50K | 65 | – | pending |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | $185K | 65 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "all_liquid")
SORT filed DESC
```

Back to [[What Works]].
