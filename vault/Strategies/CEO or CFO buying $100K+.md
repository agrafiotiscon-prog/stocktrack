---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7826
cagr: 0.0971197
spy_cagr: 0.109342
sharpe: 0.415856
max_drawdown: 0.661595
holdout_excess: 0.0138897
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,826 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +10.0% (p 0.041) |
| 2016+ excess /yr | +1.4% (p 0.760) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +10.9% | 0.32 | 0.55 | 52% | 0.85 | -2.0% | 29% | 3,427 | 6.0% | +1.5% / 0.03 / 25% |
| 63d | +9.7% | +10.9% | 0.42 | 0.55 | 66% | 1.33 | -2.1% | 43% | 1,606 | 2.8% | +2.3% / 0.11 / 41% |
| 126d | +9.4% | +10.9% | 0.41 | 0.55 | 62% | 1.25 | -2.1% | 48% | 825 | 1.5% | +1.4% / 0.04 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.7%/yr, double costs +6.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.3% | +2.7% |
| 2007 | -10.1% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +74.0% | +26.4% | +47.6% |
| 2010 | +34.6% | +15.1% | +19.6% |
| 2011 | -10.3% | +1.9% | -12.2% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +11.5% | +13.5% | -1.9% |
| 2015 | -6.7% | +1.2% | -8.0% |
| 2016 | +23.6% | +12.0% | +11.6% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -7.4% | -4.6% | -2.9% |
| 2019 | +23.5% | +31.2% | -7.7% |
| 2020 | +2.9% | +18.3% | -15.4% |
| 2021 | +18.8% | +28.7% | -9.9% |
| 2022 | -20.3% | -18.2% | -2.1% |
| 2023 | +50.7% | +26.2% | +24.5% |
| 2024 | +34.2% | +24.9% | +9.3% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +12.0% | +11.5% | +0.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 9 | -5.1% | -0.3% | 44% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | $207K | 55 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | – | pending |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | – | pending |
| 2026-11-04 | [[AN]] | [[Manley Michael Mark]] | $1.0M | 71 | – | pending |
| 2026-11-04 | [[LSCC]] | [[Tamer Ford]] | $1.0M | 65 | – | pending |
| 2026-11-04 | [[INTC]] | [[TAN LIP BU]] | $9.7M | 64 | – | pending |
| 2026-11-03 | [[SITE]] | [[BLACK DOUG]] | $1.0M | 62 | +0.1% | open |
| 2026-11-03 | [[STRZ]] | [[Hirsch Jeffrey]] | $111K | 55 | +2.2% | open |
| 2026-11-02 | [[FCPT]] | [[Lenehan William H]] | $226K | 42 | -0.6% | open |
| 2026-11-02 | [[ENPH]] | [[Kothandaraman Badrinarayanan]] | $268K | 41 | +9.7% | open |
| 2026-11-02 | [[LSTR]] | [[Lonegro Frank A]] | $715K | 57 | +0.8% | open |
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | -8.9% | open |
| 2026-10-29 | [[TFC]] | [[Lyons Michael P]] | $1.2M | 66 | +1.9% | open |
| 2026-10-28 | [[TTMI]] | [[Roks Edwin]] | $440K | 62 | -18.8% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +10.7% | open |
| 2026-10-27 | [[AIOK]] | [[Panagiotidis Petros Panagiotis]] | $1.1M | 51 | -35.5% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +7.8% | open |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | $1.5M | 73 | -0.4% | open |
| 2026-10-27 | [[TIPT]] | [[Barnes Michael Gene]] | $502K | 29 | +7.8% | open |
| 2026-10-26 | [[THRM]] | [[Presley William T]] | $130K | 53 | +4.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
