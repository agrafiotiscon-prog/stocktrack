---
type: "strategy"
key: "proven_insider"
signals: 20141
cagr: 0.124546
spy_cagr: 0.111785
sharpe: 0.510198
max_drawdown: 0.614357
holdout_excess: 0.004467
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,141 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.6% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.1% (p 0.018) |
| 2016+ excess /yr | +0.4% (p 0.892) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.8% | +11.2% | 0.36 | 0.56 | 52% | 1.10 | -2.9% | 33% | 4,541 | 8.6% | -0.3% / -0.12 / 46% |
| 63d | +12.5% | +11.2% | 0.51 | 0.56 | 61% | 1.23 | +0.5% | 52% | 1,613 | 3.2% | +3.9% / 0.24 / 39% |
| 126d | +8.9% | +11.2% | 0.40 | 0.56 | 57% | 1.15 | -2.3% | 38% | 818 | 1.5% | +0.4% / -0.05 / 44% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +15.8%/yr, double costs +9.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.9% | +13.9% | +3.0% |
| 2007 | +1.5% | +5.1% | -3.6% |
| 2008 | -22.3% | -36.8% | +14.5% |
| 2009 | +23.9% | +26.4% | -2.5% |
| 2010 | +33.4% | +15.1% | +18.3% |
| 2011 | +11.4% | +1.9% | +9.5% |
| 2012 | +15.6% | +16.0% | -0.4% |
| 2013 | +33.3% | +32.3% | +1.0% |
| 2014 | +17.6% | +13.5% | +4.2% |
| 2015 | -15.7% | +1.2% | -16.9% |
| 2016 | +20.7% | +12.0% | +8.7% |
| 2017 | +8.7% | +21.7% | -13.0% |
| 2018 | -13.9% | -4.6% | -9.3% |
| 2019 | +28.7% | +31.2% | -2.6% |
| 2020 | +33.0% | +18.3% | +14.7% |
| 2021 | +13.7% | +28.7% | -15.1% |
| 2022 | -27.8% | -18.2% | -9.6% |
| 2023 | +37.9% | +26.2% | +11.8% |
| 2024 | +21.8% | +24.9% | -3.1% |
| 2025 | +38.3% | +17.7% | +20.5% |
| 2026 | +14.9% | +11.5% | +3.4% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 47 | +2.8% | +2.7% | 77% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[LBTYA]] | [[MALONE JOHN C]] | $1.5M | 53 | – | pending |
| 2026-11-09 | [[NXRT]] | [[McGraner Matt]] | $199K | 44 | – | pending |
| 2026-11-09 | [[NXRT]] | [[Richards Paul]] | $103K | 49 | – | pending |
| 2026-11-09 | [[GFS]] | [[LAZAR JACK R]] | $380K | 57 | – | pending |
| 2026-11-09 | [[NATR]] | [[PRESCOTT GROUP CAPITAL MANAGEMENT, L.L.C]] | $2.8M | 44 | – | pending |
| 2026-11-09 | [[MTDR]] | [[Stetson Glenn W]] | $51K | 53 | – | pending |
| 2026-11-09 | [[MTDR]] | [[Appel Shelley F]] | $68K | 60 | – | pending |
| 2026-11-09 | [[OBIO]] | [[Hochman David P]] | $25K | 41 | – | pending |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | – | pending |
| 2026-11-09 | [[CPS]] | [[Banas Jonathan P]] | $17K | 28 | – | pending |
| 2026-11-09 | [[AN]] | [[Szlosek Thomas A]] | $200K | 67 | – | pending |
| 2026-11-09 | [[LKFN]] | [[BARTELS ROBERT E JR]] | $117K | 30 | – | pending |
| 2026-11-09 | [[TTMI]] | [[FRANKLIN PHILIP G]] | $310K | 52 | – | pending |
| 2026-11-09 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $622K | 27 | – | pending |
| 2026-11-09 | [[MTDR]] | [[Foran Joseph Wm]] | $257K | 84 | – | pending |
| 2026-11-06 | [[MDGL]] | [[BAKER BROS. ADVISORS LP]] | $35.0M | 48 | +3.7% | open |
| 2026-11-06 | [[DSM]] | [[Saba Capital Management, L.P]] | $555 | 8 | -1.3% | open |
| 2026-11-06 | [[JOF]] | [[Saba Capital Management, L.P]] | $299K | 26 | -1.0% | open |
| 2026-11-06 | [[KOD]] | [[BAKER BROS. ADVISORS LP]] | $24.3M | 45 | +3.8% | open |
| 2026-11-06 | [[MTDR]] | [[Elsener William Thomas]] | $46K | 48 | -1.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
