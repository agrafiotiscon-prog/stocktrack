---
type: "strategy"
key: "first_buy_exec"
signals: 5624
cagr: 0.0994221
spy_cagr: 0.109357
sharpe: 0.433386
max_drawdown: 0.536232
holdout_excess: 0.00578285
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,624 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.0% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +11.3% (p 0.012) |
| 2016+ excess /yr | +0.6% (p 0.894) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.8% | +10.9% | 0.21 | 0.55 | 54% | 0.88 | -4.8% | 20% | 3,200 | 5.4% | -0.5% / -0.15 / 48% |
| 63d | +9.9% | +10.9% | 0.43 | 0.55 | 54% | 1.20 | -1.4% | 55% | 1,522 | 2.6% | +2.7% / 0.16 / 39% |
| 126d | +10.0% | +10.9% | 0.44 | 0.55 | 56% | 1.17 | -1.3% | 50% | 783 | 1.3% | +2.2% / 0.11 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.6%/yr, double costs +7.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2007 | +4.1% | +5.3% | -1.2% |
| 2008 | -27.6% | -36.8% | +9.2% |
| 2009 | +49.0% | +26.4% | +22.7% |
| 2010 | +29.6% | +15.1% | +14.6% |
| 2011 | -5.1% | +1.9% | -7.0% |
| 2012 | +30.1% | +16.0% | +14.1% |
| 2013 | +34.4% | +32.3% | +2.1% |
| 2014 | +6.5% | +13.5% | -7.0% |
| 2015 | +6.8% | +1.2% | +5.5% |
| 2016 | +3.1% | +12.0% | -8.9% |
| 2017 | +24.2% | +21.7% | +2.5% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +29.2% | +18.3% | +10.8% |
| 2021 | -4.1% | +28.7% | -32.9% |
| 2022 | -5.6% | -18.2% | +12.5% |
| 2023 | +22.5% | +26.2% | -3.6% |
| 2024 | +31.2% | +24.9% | +6.3% |
| 2025 | -9.5% | +17.7% | -27.2% |
| 2026 | -12.9% | +13.3% | -26.1% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | +1.7% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.0% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | -0.4% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +41.5% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +0.5% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.1% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -6.2% | open |
| 2026-10-06 | [[HRL]] | [[Newlands William A]] | $201K | 46 | +3.8% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +7.1% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -9.7% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -9.7% | open |
| 2026-09-30 | [[BPRE]] | [[Ruddy Jordan B]] | $60K | 70 | -2.6% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | -6.7% | open |
| 2026-09-28 | [[ZUMZ]] | [[ELLIS ADAM CHRISTOPHER]] | $134K | 44 | +1.0% | open |
| 2026-09-28 | [[INR]] | [[Baetz Cary D]] | $300K | 69 | +7.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
