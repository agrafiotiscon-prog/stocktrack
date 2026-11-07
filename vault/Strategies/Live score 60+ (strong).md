---
type: "strategy"
key: "score_60"
signals: 7189
cagr: 0.105882
spy_cagr: 0.109342
sharpe: 0.441953
max_drawdown: 0.612357
holdout_excess: 0.0180999
---

# Live score 60+ (strong)

Rule key: `score_60`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,189 |
| 3-month excess vs SPY (mean / median) | +1.6% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.4% |
| vs surviving stocks | +1.8% |
| 2006-2015 excess /yr | +6.9% (p 0.097) |
| 2016+ excess /yr | +1.8% (p 0.735) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.7% | +10.9% | 0.24 | 0.55 | 62% | 0.92 | -4.0% | 33% | 3,303 | 6.2% | +0.3% / -0.05 / 59% |
| 63d | +10.6% | +10.9% | 0.44 | 0.55 | 61% | 1.22 | -0.5% | 57% | 1,586 | 2.9% | +2.8% / 0.15 / 31% |
| 126d | +12.5% | +10.9% | 0.51 | 0.55 | 63% | 1.12 | +1.8% | 57% | 822 | 1.6% | +4.4% / 0.26 / 42% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.6%/yr, double costs +7.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.4% | +13.3% | +3.1% |
| 2007 | -11.8% | +5.1% | -16.9% |
| 2008 | -29.0% | -36.8% | +7.8% |
| 2009 | +41.3% | +26.4% | +14.9% |
| 2010 | +30.2% | +15.1% | +15.1% |
| 2011 | -2.9% | +1.9% | -4.8% |
| 2012 | +14.5% | +16.0% | -1.4% |
| 2013 | +48.3% | +32.3% | +16.0% |
| 2014 | +7.4% | +13.5% | -6.1% |
| 2015 | -12.9% | +1.2% | -14.2% |
| 2016 | +28.9% | +12.0% | +16.9% |
| 2017 | +28.0% | +21.7% | +6.3% |
| 2018 | -10.8% | -4.6% | -6.3% |
| 2019 | +47.2% | +31.2% | +16.0% |
| 2020 | +18.4% | +18.3% | +0.1% |
| 2021 | -1.2% | +28.7% | -30.0% |
| 2022 | -8.9% | -18.2% | +9.3% |
| 2023 | +34.5% | +26.2% | +8.3% |
| 2024 | +2.2% | +24.9% | -22.7% |
| 2025 | +23.3% | +17.7% | +5.6% |
| 2026 | +0.3% | +11.5% | -11.2% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 14 | -0.5% | +2.2% | 64% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[LKQ]] | [[GOVE SUE]] | $201K | 65 | – | pending |
| 2026-11-06 | [[MTDR]] | [[Erman Bryan A]] | $46K | 67 | – | pending |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | $1.0M | 69 | -2.9% | open |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | -0.1% | open |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | -4.7% | open |
| 2026-11-05 | [[FBRT]] | [[Byrne Richard J]] | $998K | 65 | -3.2% | open |
| 2026-11-05 | [[UPBD]] | [[Karam Fahmi]] | $100K | 64 | -1.1% | open |
| 2026-11-05 | [[LBTYA]] | [[Rodriguez Enrique]] | $2.0M | 73 | +3.3% | open |
| 2026-11-05 | [[LBTYA]] | [[FRIES MICHAEL T]] | $1.0M | 66 | +3.3% | open |
| 2026-11-04 | [[ASPE]] | [[ORBIMED ADVISORS LLC]] | $15.0M | 80 | -1.2% | open |
| 2026-11-04 | [[LRN]] | [[Shepherd Brian A]] | $1.7M | 66 | -2.6% | open |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[MARINO GLENN P]] | $393K | 73 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | $99K | 67 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | $50K | 61 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[BROWN JEFFREY J]] | $400K | 65 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[LANGENSTEIN MOLLY]] | $50K | 64 | +1.3% | open |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | +1.1% | open |
| 2026-11-04 | [[AN]] | [[Manley Michael Mark]] | $1.0M | 71 | +1.1% | open |
| 2026-11-04 | [[LSCC]] | [[Tamer Ford]] | $1.0M | 65 | +7.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_60")
SORT filed DESC
```

Back to [[What Works]].
