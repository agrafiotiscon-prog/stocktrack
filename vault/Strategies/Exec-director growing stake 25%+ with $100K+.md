---
type: "strategy"
key: "big_stake_up"
signals: 11383
cagr: 0.105875
spy_cagr: 0.110756
sharpe: 0.444886
max_drawdown: 0.646382
holdout_excess: 0.0185077
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,383 |
| 3-month excess vs SPY (mean / median) | +0.9% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.4% (p 0.031) |
| 2016+ excess /yr | +1.9% (p 0.646) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.0% | +11.1% | 0.22 | 0.56 | 54% | 1.05 | -5.9% | 24% | 4,260 | 6.4% | -1.9% / -0.24 / 49% |
| 63d | +10.6% | +11.1% | 0.44 | 0.56 | 65% | 1.30 | -1.7% | 52% | 1,652 | 2.7% | +2.2% / 0.10 / 32% |
| 126d | +7.6% | +11.1% | 0.34 | 0.56 | 64% | 1.25 | -4.1% | 48% | 840 | 1.3% | -0.4% / -0.10 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.4%/yr, double costs +7.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -4.3% | +5.1% | -9.5% |
| 2008 | -40.9% | -36.8% | -4.1% |
| 2009 | +55.6% | +26.4% | +29.3% |
| 2010 | +36.6% | +15.1% | +21.5% |
| 2011 | +7.2% | +1.9% | +5.3% |
| 2012 | +20.9% | +16.0% | +4.9% |
| 2013 | +49.0% | +32.3% | +16.7% |
| 2014 | +17.7% | +13.5% | +4.2% |
| 2015 | -7.9% | +1.2% | -9.2% |
| 2016 | +20.4% | +12.0% | +8.4% |
| 2017 | +18.5% | +21.7% | -3.2% |
| 2018 | -14.6% | -4.6% | -10.0% |
| 2019 | +43.8% | +31.2% | +12.6% |
| 2020 | +27.5% | +18.3% | +9.1% |
| 2021 | +3.9% | +28.7% | -24.8% |
| 2022 | -19.2% | -18.2% | -1.0% |
| 2023 | +16.4% | +26.2% | -9.8% |
| 2024 | +13.6% | +24.9% | -11.3% |
| 2025 | -0.3% | +17.7% | -18.0% |
| 2026 | +14.1% | +13.7% | +0.3% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 5 | -8.5% | -11.6% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | – | pending |
| 2026-10-29 | [[XYL]] | [[KOCH D CHRISTIAN]] | $986K | 52 | +1.1% | open |
| 2026-10-29 | [[TFC]] | [[Lyons Michael P]] | $1.2M | 66 | -0.8% | open |
| 2026-10-28 | [[TTMI]] | [[Ali Wajid]] | $902K | 61 | -6.8% | open |
| 2026-10-28 | [[HXL]] | [[KEATING NEAL J]] | $242K | 46 | -0.5% | open |
| 2026-10-28 | [[HBAN]] | [[ROLLINS JAMES D III]] | $254K | 46 | +0.6% | open |
| 2026-10-28 | [[ACN]] | [[Sweet Julie Spellman]] | $3.0M | 78 | +9.6% | open |
| 2026-10-27 | [[NPB]] | [[Boer Carrie L]] | $185K | 65 | -1.1% | open |
| 2026-10-26 | [[THRM]] | [[MASCARENAS PAUL ANTHONY]] | $533K | 61 | +5.4% | open |
| 2026-10-22 | [[RAPP]] | [[PAUL STEVEN M]] | $974K | 77 | -8.5% | open |
| 2026-10-22 | [[RAPP]] | [[MARAGANORE JOHN]] | $249K | 71 | -8.5% | open |
| 2026-10-21 | [[FBK]] | [[INGRAM ORRIN H II]] | $1.5M | 49 | +3.3% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -2.9% | open |
| 2026-10-21 | [[CRF]] | [[Bradshaw Joshua]] | $118K | 53 | +0.4% | open |
| 2026-10-19 | [[IAM]] | [[Rachlin Evan Lockwood]] | $11.5M | 60 | -16.3% | open |
| 2026-10-16 | [[PEP]] | [[POHLAD ROBERT C]] | $23.7M | 62 | +6.4% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -6.5% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -1.7% | open |
| 2026-10-15 | [[CXM]] | [[WARD JR STEPHEN M]] | $850K | 51 | +13.2% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -6.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
