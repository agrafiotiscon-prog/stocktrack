---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7673
cagr: 0.0935869
spy_cagr: 0.110494
sharpe: 0.39282
max_drawdown: 0.655689
holdout_excess: 0.0152907
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,673 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.8% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +1.0% |
| 2006-2015 excess /yr | +9.2% (p 0.066) |
| 2016+ excess /yr | +1.5% (p 0.738) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Years beating SPY | Trades | Costs/yr |
|---|---|---|---|---|---|---|---|---|---|
| 21d | +5.8% | +11.0% | 0.29 | 0.55 | 51% | 0.88 | 29% | 3,361 | 5.9% |
| 63d | +9.4% | +11.0% | 0.39 | 0.55 | 66% | 1.12 | 38% | 1,591 | 2.8% |
| 126d | +4.8% | +11.0% | 0.25 | 0.55 | 67% | 1.12 | 24% | 824 | 1.4% |


Cost sensitivity (63-session hold): no costs +12.4%/yr, double costs +6.6%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.0% | +13.3% | +1.7% |
| 2007 | -9.3% | +5.1% | -14.4% |
| 2008 | -40.8% | -36.8% | -4.0% |
| 2009 | +79.6% | +26.4% | +53.2% |
| 2010 | +29.0% | +15.1% | +14.0% |
| 2011 | -7.0% | +1.9% | -8.9% |
| 2012 | +19.9% | +16.0% | +3.9% |
| 2013 | +43.5% | +32.3% | +11.2% |
| 2014 | +9.7% | +13.5% | -3.7% |
| 2015 | -3.4% | +1.2% | -4.7% |
| 2016 | +18.9% | +12.0% | +6.9% |
| 2017 | +3.0% | +21.7% | -18.8% |
| 2018 | -10.9% | -4.6% | -6.3% |
| 2019 | +17.7% | +31.2% | -13.6% |
| 2020 | +29.0% | +18.3% | +10.7% |
| 2021 | +15.5% | +28.7% | -13.2% |
| 2022 | -20.2% | -18.2% | -2.0% |
| 2023 | +51.0% | +26.2% | +24.8% |
| 2024 | +24.6% | +24.9% | -0.3% |
| 2025 | -18.6% | +17.7% | -36.4% |
| 2026 | +12.9% | +13.4% | -0.5% |


## Live forward test

0 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -0.9% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | +2.0% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -6.2% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +55.7% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -3.9% | open |
| 2026-10-13 | [[HEI, HEI.A]] | [[MENDELSON VICTOR H]] | $175K | 69 | +4.7% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | +1.2% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | -1.2% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +5.9% | open |
| 2026-10-02 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -6.0% | open |
| 2026-10-01 | [[GTLB]] | [[Staples William]] | $125K | 23 | +5.7% | open |
| 2026-10-01 | [[CRESY]] | [[Elsztain Alejandro Gustavo]] | $199K | 41 | -0.5% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -10.7% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -10.7% | open |
| 2026-09-30 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -4.4% | open |
| 2026-09-29 | [[GME]] | [[Cohen Ryan]] | $10.6M | 70 | +7.6% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | -5.8% | open |
| 2026-09-28 | [[INBX]] | [[Lappe Mark]] | $999K | 60 | -15.1% | open |
| 2026-09-28 | [[INR]] | [[Baetz Cary D]] | $300K | 69 | +6.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
