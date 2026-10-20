---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7846
cagr: 0.0971444
spy_cagr: 0.110437
sharpe: 0.416021
max_drawdown: 0.658732
holdout_excess: 0.0160695
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,846 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +0.8% |
| 2006-2015 excess /yr | +9.8% (p 0.045) |
| 2016+ excess /yr | +1.6% (p 0.725) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +11.0% | 0.32 | 0.55 | 52% | 0.86 | -2.2% | 29% | 3,414 | 6.0% | +1.4% / 0.02 / 29% |
| 63d | +9.7% | +11.0% | 0.42 | 0.55 | 66% | 1.32 | -2.2% | 38% | 1,601 | 2.8% | +2.5% / 0.12 / 39% |
| 126d | +7.6% | +11.0% | 0.35 | 0.55 | 62% | 1.24 | -3.7% | 43% | 823 | 1.4% | -0.1% / -0.08 / 54% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.7%/yr, double costs +6.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.5% | +13.3% | +2.2% |
| 2007 | -10.0% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +71.8% | +26.4% | +45.5% |
| 2010 | +34.6% | +15.1% | +19.6% |
| 2011 | -10.3% | +1.9% | -12.2% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +11.6% | +13.5% | -1.9% |
| 2015 | -4.2% | +1.2% | -5.4% |
| 2016 | +24.7% | +12.0% | +12.7% |
| 2017 | +3.2% | +21.7% | -18.5% |
| 2018 | -7.2% | -4.6% | -2.6% |
| 2019 | +24.1% | +31.2% | -7.1% |
| 2020 | +0.7% | +18.3% | -17.7% |
| 2021 | +18.7% | +28.7% | -10.0% |
| 2022 | -19.6% | -18.2% | -1.4% |
| 2023 | +49.4% | +26.2% | +23.2% |
| 2024 | +34.0% | +24.9% | +9.2% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +8.4% | +13.3% | -4.9% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -2.0% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | +2.5% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -10.0% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +41.5% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.5% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.8% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +0.5% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.1% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +6.3% | open |
| 2026-10-02 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -6.6% | open |
| 2026-10-01 | [[GTLB]] | [[Staples William]] | $125K | 23 | +5.3% | open |
| 2026-10-01 | [[CRESY]] | [[Elsztain Alejandro Gustavo]] | $199K | 41 | +0.3% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -9.7% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -9.7% | open |
| 2026-09-30 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -5.0% | open |
| 2026-09-29 | [[GME]] | [[Cohen Ryan]] | $10.6M | 70 | +8.0% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | -6.7% | open |
| 2026-09-28 | [[INBX]] | [[Lappe Mark]] | $999K | 60 | -14.7% | open |
| 2026-09-28 | [[INR]] | [[Baetz Cary D]] | $300K | 69 | +7.3% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
