---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7836
cagr: 0.0980424
spy_cagr: 0.110525
sharpe: 0.418711
max_drawdown: 0.661595
holdout_excess: 0.0155029
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,836 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +10.0% (p 0.040) |
| 2016+ excess /yr | +1.6% (p 0.734) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +11.1% | 0.32 | 0.55 | 52% | 0.85 | -2.0% | 29% | 3,421 | 6.0% | +1.6% / 0.04 / 27% |
| 63d | +9.8% | +11.1% | 0.42 | 0.55 | 66% | 1.33 | -2.1% | 38% | 1,603 | 2.8% | +2.4% / 0.11 / 41% |
| 126d | +9.4% | +11.1% | 0.41 | 0.55 | 62% | 1.25 | -2.3% | 48% | 824 | 1.5% | +1.3% / 0.03 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.8%/yr, double costs +6.9%/yr.


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
| 2015 | -3.6% | +1.2% | -4.9% |
| 2016 | +23.6% | +12.0% | +11.6% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -7.5% | -4.6% | -2.9% |
| 2019 | +24.1% | +31.2% | -7.1% |
| 2020 | +0.7% | +18.3% | -17.7% |
| 2021 | +18.7% | +28.7% | -10.0% |
| 2022 | -20.3% | -18.2% | -2.1% |
| 2023 | +50.7% | +26.2% | +24.5% |
| 2024 | +34.2% | +24.9% | +9.3% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +12.1% | +13.7% | -1.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 2 | -7.6% | -0.3% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | – | pending |
| 2026-10-29 | [[TFC]] | [[Lyons Michael P]] | $1.2M | 66 | – | pending |
| 2026-10-28 | [[TTMI]] | [[Roks Edwin]] | $440K | 62 | -3.4% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +3.2% | open |
| 2026-10-27 | [[AIOK]] | [[Panagiotidis Petros Panagiotis]] | $1.1M | 51 | +8.0% | open |
| 2026-10-27 | [[STC]] | [[EPPINGER FREDERICK H]] | $133K | 65 | +3.8% | open |
| 2026-10-27 | [[NPB]] | [[Williams Charles Alan]] | $1.5M | 73 | -0.5% | open |
| 2026-10-27 | [[TIPT]] | [[Barnes Michael Gene]] | $502K | 29 | +3.1% | open |
| 2026-10-26 | [[THRM]] | [[Presley William T]] | $130K | 53 | +7.8% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -7.9% | open |
| 2026-10-20 | [[DX]] | [[Popenoe Smriti Laxman]] | $106K | 39 | -0.6% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +3.9% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -3.1% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | -16.3% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -5.7% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +2.4% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -12.7% | open |
| 2026-10-13 | [[HEI]] | [[MENDELSON VICTOR H]] | $175K | 69 | +10.5% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | -6.3% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | +1.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
