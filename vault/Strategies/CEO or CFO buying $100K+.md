---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7839
cagr: 0.0961162
spy_cagr: 0.110594
sharpe: 0.412388
max_drawdown: 0.661595
holdout_excess: 0.0160841
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,839 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +9.8% (p 0.046) |
| 2016+ excess /yr | +1.6% (p 0.725) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.5% | +11.1% | 0.32 | 0.55 | 52% | 0.86 | -2.1% | 29% | 3,418 | 6.0% | +1.6% / 0.04 / 29% |
| 63d | +9.6% | +11.1% | 0.41 | 0.55 | 66% | 1.32 | -2.3% | 38% | 1,602 | 2.8% | +2.3% / 0.11 / 41% |
| 126d | +9.1% | +11.1% | 0.40 | 0.55 | 62% | 1.25 | -2.6% | 48% | 824 | 1.5% | +1.3% / 0.03 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.6%/yr, double costs +6.7%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.3% | +2.7% |
| 2007 | -10.1% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +71.8% | +26.4% | +45.5% |
| 2010 | +34.6% | +15.1% | +19.6% |
| 2011 | -10.3% | +1.9% | -12.2% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +11.5% | +13.5% | -1.9% |
| 2015 | -3.6% | +1.2% | -4.8% |
| 2016 | +23.6% | +12.0% | +11.6% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -7.5% | -4.6% | -2.9% |
| 2019 | +24.1% | +31.2% | -7.1% |
| 2020 | +0.7% | +18.3% | -17.7% |
| 2021 | +18.7% | +28.7% | -10.0% |
| 2022 | -19.6% | -18.2% | -1.4% |
| 2023 | +50.7% | +26.2% | +24.5% |
| 2024 | +34.2% | +24.9% | +9.3% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +8.3% | +13.7% | -5.4% |


## Live forward test

2 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -0.1% | open |
| 2026-10-20 | [[DX]] | [[Popenoe Smriti Laxman]] | $106K | 39 | +0.9% | open |
| 2026-10-19 | [[APLD]] | [[Cummins Wes]] | $1.0M | 60 | -1.1% | open |
| 2026-10-15 | [[FLSC]] | [[Cha Albert]] | $3.0M | 70 | -1.0% | open |
| 2026-10-14 | [[INBX]] | [[Lappe Mark]] | $849K | 47 | +7.4% | open |
| 2026-10-14 | [[TDIC]] | [[Seto Wai Yue]] | $600K | 58 | -17.6% | open |
| 2026-10-13 | [[RTSN]] | [[Keller Eric L]] | $250K | 57 | +33.1% | open |
| 2026-10-13 | [[GME]] | [[Cohen Ryan]] | $22.8M | 71 | -8.5% | open |
| 2026-10-13 | [[HEI]] | [[MENDELSON VICTOR H]] | $175K | 69 | +2.0% | open |
| 2026-10-13 | [[SAR]] | [[Oberbeck Christian L]] | $446K | 61 | -7.5% | open |
| 2026-10-08 | [[IMMR]] | [[Singer Eric]] | $293K | 44 | +0.3% | open |
| 2026-10-02 | [[GME]] | [[Cohen Ryan]] | $17.1M | 79 | +0.7% | open |
| 2026-10-02 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | -1.4% | open |
| 2026-10-01 | [[GTLB]] | [[Staples William]] | $125K | 23 | +12.1% | open |
| 2026-10-01 | [[CRESY]] | [[Elsztain Alejandro Gustavo]] | $199K | 41 | +2.0% | open |
| 2026-10-01 | [[XENE]] | [[Kelly Thomas Patrick]] | $560K | 71 | -8.2% | open |
| 2026-10-01 | [[XENE]] | [[MORTIMER IAN]] | $1.1M | 77 | -8.2% | open |
| 2026-09-30 | [[NYAX]] | [[Nechmad Yair]] | $2.1M | 62 | +0.2% | open |
| 2026-09-29 | [[GME]] | [[Cohen Ryan]] | $10.6M | 70 | +2.3% | open |
| 2026-09-28 | [[DMRA]] | [[Jarrett Jennifer]] | $253K | 44 | +2.9% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
