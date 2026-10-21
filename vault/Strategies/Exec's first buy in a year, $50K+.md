---
type: "strategy"
key: "first_buy_exec"
signals: 5625
cagr: 0.095461
spy_cagr: 0.109357
sharpe: 0.418514
max_drawdown: 0.54717
holdout_excess: 0.00634307
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,625 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.0% |
| vs surviving stocks | +1.8% |
| 2006-2015 excess /yr | +11.2% (p 0.013) |
| 2016+ excess /yr | +0.6% (p 0.884) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.9% | +10.9% | 0.21 | 0.55 | 54% | 0.88 | -4.7% | 20% | 3,204 | 5.4% | -0.4% / -0.14 / 48% |
| 63d | +9.5% | +10.9% | 0.42 | 0.55 | 55% | 1.21 | -1.8% | 55% | 1,525 | 2.6% | +2.3% / 0.12 / 39% |
| 126d | +10.3% | +10.9% | 0.45 | 0.55 | 57% | 1.21 | -1.2% | 50% | 784 | 1.3% | +2.5% / 0.14 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.3%/yr, double costs +7.0%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2007 | +4.1% | +5.3% | -1.2% |
| 2008 | -29.1% | -36.8% | +7.7% |
| 2009 | +47.9% | +26.4% | +21.6% |
| 2010 | +29.6% | +15.1% | +14.6% |
| 2011 | -5.1% | +1.9% | -7.0% |
| 2012 | +30.1% | +16.0% | +14.1% |
| 2013 | +34.4% | +32.3% | +2.1% |
| 2014 | +6.5% | +13.5% | -6.9% |
| 2015 | +3.4% | +1.2% | +2.2% |
| 2016 | +1.3% | +12.0% | -10.7% |
| 2017 | +25.2% | +21.7% | +3.5% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +29.1% | +18.3% | +10.7% |
| 2021 | -4.2% | +28.7% | -32.9% |
| 2022 | -5.6% | -18.2% | +12.5% |
| 2023 | +22.6% | +26.2% | -3.6% |
| 2024 | +31.0% | +24.9% | +6.1% |
| 2025 | -9.4% | +17.7% | -27.2% |
| 2026 | -12.9% | +13.3% | -26.2% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | +3.5% | open |
| 2026-10-19 | [[APLD]] | [[Zhang Jason Gechen]] | $5.7M | 71 | +3.5% | open |
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -3.7% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.4% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | -2.5% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +39.9% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | -4.4% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -0.4% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -0.9% | open |
| 2026-10-06 | [[HRL]] | [[Newlands William A]] | $201K | 46 | +4.3% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.3% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -7.0% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -7.0% | open |
| 2026-09-30 | [[BPRE]] | [[Ruddy Jordan B]] | $60K | 70 | -1.7% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | -0.3% | open |
| 2026-09-28 | [[ZUMZ]] | [[ELLIS ADAM CHRISTOPHER]] | $134K | 44 | +0.1% | open |
| 2026-09-28 | [[INR]] | [[Baetz Cary D]] | $300K | 69 | +8.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
