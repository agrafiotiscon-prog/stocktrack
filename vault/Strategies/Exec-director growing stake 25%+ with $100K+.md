---
type: "strategy"
key: "big_stake_up"
signals: 11382
cagr: 0.0899578
spy_cagr: 0.109572
sharpe: 0.390506
max_drawdown: 0.669115
holdout_excess: 0.0175044
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,382 |
| 3-month excess vs SPY (mean / median) | +0.9% / -0.5% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.3% (p 0.035) |
| 2016+ excess /yr | +1.8% (p 0.663) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.1% | +11.0% | 0.22 | 0.55 | 54% | 1.05 | -5.7% | 24% | 4,266 | 6.4% | -1.8% / -0.23 / 48% |
| 63d | +9.0% | +11.0% | 0.39 | 0.55 | 67% | 1.29 | -2.9% | 48% | 1,656 | 2.7% | +0.8% / -0.01 / 37% |
| 126d | +7.7% | +11.0% | 0.35 | 0.55 | 66% | 1.25 | -3.8% | 48% | 840 | 1.3% | -0.3% / -0.09 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.7%/yr, double costs +6.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -5.6% | +5.1% | -10.8% |
| 2008 | -43.3% | -36.8% | -6.5% |
| 2009 | +57.3% | +26.4% | +30.9% |
| 2010 | +35.2% | +15.1% | +20.1% |
| 2011 | +7.2% | +1.9% | +5.3% |
| 2012 | +17.8% | +16.0% | +1.8% |
| 2013 | +50.2% | +32.3% | +17.9% |
| 2014 | +17.2% | +13.5% | +3.8% |
| 2015 | -7.1% | +1.2% | -8.3% |
| 2016 | +17.1% | +12.0% | +5.1% |
| 2017 | +17.5% | +21.7% | -4.2% |
| 2018 | -16.8% | -4.6% | -12.3% |
| 2019 | +48.2% | +31.2% | +16.9% |
| 2020 | +21.5% | +18.3% | +3.2% |
| 2021 | -6.7% | +28.7% | -35.4% |
| 2022 | -19.4% | -18.2% | -1.2% |
| 2023 | +16.7% | +26.2% | -9.4% |
| 2024 | +7.6% | +24.9% | -17.3% |
| 2025 | +11.3% | +17.7% | -6.4% |
| 2026 | +3.1% | +11.5% | -8.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 17 | -0.0% | +0.3% | 53% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-09 | [[GFS]] | [[LAZAR JACK R]] | $380K | 57 | – | pending |
| 2026-11-09 | [[ADM]] | [[McAtee David R II]] | $197K | 45 | – | pending |
| 2026-11-09 | [[OBIO]] | [[Pacitti David]] | $100K | 59 | – | pending |
| 2026-11-09 | [[FLOC]] | [[EDWARDS JOSEPH R]] | $798K | 76 | – | pending |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | – | pending |
| 2026-11-09 | [[NLY]] | [[Wede Scott]] | $940K | 52 | – | pending |
| 2026-11-09 | [[MTDR]] | [[Foran Joseph Wm]] | $257K | 84 | – | pending |
| 2026-11-06 | [[CVS]] | [[Shah Prem S]] | $2.0M | 54 | -0.7% | open |
| 2026-11-06 | [[TRNS]] | [[IRICK JAIME A]] | $230K | 59 | -0.6% | open |
| 2026-11-06 | [[YPF]] | [[Francos Guillermo Alberto]] | $356K | 32 | -2.1% | open |
| 2026-11-06 | [[LKQ]] | [[GOVE SUE]] | $201K | 65 | +0.3% | open |
| 2026-11-06 | [[AGMB]] | [[Epstein David R]] | $104K | 42 | -3.6% | open |
| 2026-11-05 | [[FLOC]] | [[Fairbanks Jonathan B]] | $293K | 47 | +5.1% | open |
| 2026-11-05 | [[ETRA]] | [[ORBIMED ADVISORS LLC]] | $3.6M | 53 | +4.0% | open |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | -1.1% | open |
| 2026-11-05 | [[FBRT]] | [[Byrne Richard J]] | $998K | 65 | -2.4% | open |
| 2026-11-05 | [[SYY]] | [[Ondrof Thomas Gerard]] | $192K | 45 | +2.0% | open |
| 2026-11-05 | [[SPXC]] | [[Deck Brian A]] | $493K | 49 | +1.1% | open |
| 2026-11-05 | [[TTMI]] | [[Ali Wajid]] | $632K | 57 | +6.7% | open |
| 2026-11-05 | [[LBTYA]] | [[Rodriguez Enrique]] | $2.0M | 73 | +1.8% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
