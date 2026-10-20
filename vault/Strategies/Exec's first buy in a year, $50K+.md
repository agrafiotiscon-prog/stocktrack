---
type: "strategy"
key: "first_buy_exec"
signals: 5622
cagr: 0.0837428
spy_cagr: 0.110724
sharpe: 0.375907
max_drawdown: 0.606074
holdout_excess: 0.00992172
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,622 |
| 3-month excess vs SPY (mean / median) | +1.3% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.9% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +9.4% (p 0.017) |
| 2016+ excess /yr | +1.0% (p 0.825) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.9% | +11.1% | 0.21 | 0.56 | 55% | 0.86 | 24% | 3,269 | 5.2% |
| 63d | +8.4% | +11.1% | 0.38 | 0.56 | 61% | 1.10 | 33% | 1,590 | 2.5% |
| 126d | +8.4% | +11.1% | 0.38 | 0.56 | 58% | 1.10 | 48% | 822 | 1.3% |


Cost sensitivity (63-session hold): no costs +10.8%/yr, double costs +5.9%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.3% | +13.8% | -1.6% |
| 2007 | +5.8% | +5.1% | +0.6% |
| 2008 | -38.9% | -36.8% | -2.1% |
| 2009 | +56.8% | +26.4% | +30.4% |
| 2010 | +28.1% | +15.1% | +13.0% |
| 2011 | -6.9% | +1.9% | -8.8% |
| 2012 | +31.3% | +16.0% | +15.3% |
| 2013 | +33.0% | +32.3% | +0.7% |
| 2014 | +10.6% | +13.5% | -2.9% |
| 2015 | +0.3% | +1.2% | -0.9% |
| 2016 | +2.5% | +12.0% | -9.5% |
| 2017 | +19.8% | +21.7% | -1.9% |
| 2018 | -9.4% | -4.6% | -4.8% |
| 2019 | +18.3% | +31.2% | -12.9% |
| 2020 | +17.9% | +18.3% | -0.5% |
| 2021 | +5.3% | +28.7% | -23.4% |
| 2022 | -10.3% | -18.2% | +7.9% |
| 2023 | +22.0% | +26.2% | -4.2% |
| 2024 | +27.5% | +24.9% | +2.6% |
| 2025 | -0.7% | +17.7% | -18.4% |
| 2026 | -10.8% | +13.4% | -24.2% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-16 | [[BORR]] | [[Snowling Harvey Edward]] | $1.5M | 72 | -1.5% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-14 | [[IMSR]] | [[Irish Simon]] | $51K | 46 | +0.5% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +55.7% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +1.2% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.2% | open |
| 2026-10-07 | [[AGMB]] | [[Knotnerus Tim Jasper]] | $94K | 67 | -4.0% | open |
| 2026-10-06 | [[HRL]] | [[Newlands William A]] | $201K | 46 | +3.6% | open |
| 2026-10-01 | [[DKS]] | [[Barnes Matthew]] | $500K | 78 | +6.8% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -10.7% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -10.7% | open |
| 2026-09-30 | [[BPRE]] | [[Ruddy Jordan B]] | $60K | 70 | -2.6% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | -5.8% | open |
| 2026-09-28 | [[ZUMZ]] | [[ELLIS ADAM CHRISTOPHER]] | $134K | 44 | +1.3% | open |
| 2026-09-28 | [[INR]] | [[Baetz Cary D]] | $300K | 69 | +6.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
