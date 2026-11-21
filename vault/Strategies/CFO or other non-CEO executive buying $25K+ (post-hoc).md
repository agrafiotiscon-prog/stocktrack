---
type: "strategy"
key: "cfo_exec_25k"
signals: 8031
cagr: 0.131566
spy_cagr: 0.107784
sharpe: 0.526908
max_drawdown: 0.564049
holdout_excess: 0.0501621
---

# CFO or other non-CEO executive buying $25K+ (post-hoc)

Rule key: `cfo_exec_25k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,031 |
| 3-month excess vs SPY (mean / median) | +1.9% / -0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +1.6% |
| vs surviving stocks | +2.2% |
| 2006-2015 excess /yr | +8.7% (p 0.041) |
| 2016+ excess /yr | +5.0% (p 0.183) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.8% | +10.8% | 0.32 | 0.54 | 50% | 0.92 | -2.1% | 29% | 3,678 | 6.6% | +1.6% / 0.04 / 36% |
| 63d | +13.2% | +10.8% | 0.53 | 0.54 | 56% | 1.21 | +1.6% | 52% | 1,636 | 3.1% | +5.0% / 0.31 / 22% |
| 126d | +13.3% | +10.8% | 0.53 | 0.54 | 59% | 1.22 | +1.8% | 57% | 832 | 1.6% | +5.0% / 0.30 / 23% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.0%/yr, double costs +10.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.9% | +13.8% | +3.1% |
| 2007 | +0.9% | +5.1% | -4.3% |
| 2008 | -32.0% | -36.8% | +4.8% |
| 2009 | +91.6% | +26.4% | +65.3% |
| 2010 | +30.0% | +15.1% | +14.9% |
| 2011 | -7.0% | +1.9% | -8.9% |
| 2012 | +22.2% | +16.0% | +6.2% |
| 2013 | +41.7% | +32.3% | +9.4% |
| 2014 | +3.5% | +13.5% | -10.0% |
| 2015 | -3.3% | +1.2% | -4.5% |
| 2016 | +29.9% | +12.0% | +17.9% |
| 2017 | +19.0% | +21.7% | -2.7% |
| 2018 | -11.6% | -4.6% | -7.1% |
| 2019 | +33.5% | +31.2% | +2.2% |
| 2020 | +15.9% | +18.3% | -2.4% |
| 2021 | +27.2% | +28.7% | -1.5% |
| 2022 | -15.6% | -18.2% | +2.5% |
| 2023 | +9.6% | +26.2% | -16.6% |
| 2024 | +30.9% | +24.9% | +6.0% |
| 2025 | +23.4% | +17.7% | +5.7% |
| 2026 | +1.6% | +8.2% | -6.7% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 50 | +1.5% | +1.6% | 58% |
| 21 sessions | 1 | -3.3% | -3.3% | 0% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[HBCP]] | [[Hill Darren M]] | $315K | 53 | – | pending |
| 2026-11-20 | [[ARR]] | [[Harper Gordon]] | $27K | 46 | – | pending |
| 2026-11-20 | [[AVEX]] | [[Morrison Christine M]] | $102K | 43 | – | pending |
| 2026-11-20 | [[FLG]] | [[Smith Lee Matthew]] | $50K | 43 | – | pending |
| 2026-11-20 | [[UAMY]] | [[Bardswich Lloyd]] | $25K | 25 | – | pending |
| 2026-11-19 | [[HMH]] | [[McGee Thomas W]] | $1.6M | 76 | +3.5% | open |
| 2026-11-19 | [[EFC]] | [[Vranos Michael W]] | $2.1M | 62 | +3.9% | open |
| 2026-11-18 | [[RMIX]] | [[Jones Mark Alan]] | $50K | 53 | -15.0% | open |
| 2026-11-18 | [[FPS]] | [[Lund Inez]] | $65K | 70 | -13.6% | open |
| 2026-11-18 | [[CGON]] | [[Kalofonos Isabel]] | $299K | 65 | +1.0% | open |
| 2026-11-18 | [[OFRM]] | [[Foraker John M]] | $104K | 53 | +7.6% | open |
| 2026-11-18 | [[LWLG]] | [[Graffam Fred]] | $29K | 31 | -9.4% | open |
| 2026-11-18 | [[SLRC]] | [[GROSS MICHAEL S]] | $226K | 30 | +4.5% | open |
| 2026-11-18 | [[PAM]] | [[Mariani Gustavo]] | $1.4M | 75 | +2.9% | open |
| 2026-11-18 | [[PAM]] | [[Mindlin Damian Miguel]] | $1.5M | 65 | +2.9% | open |
| 2026-11-17 | [[MP]] | [[Corbett Ryan]] | $92K | 56 | +3.6% | open |
| 2026-11-17 | [[ECC]] | [[Onorio Kenneth P]] | $104K | 45 | +7.6% | open |
| 2026-11-17 | [[FISN]] | [[Muller Richard]] | $32K | 43 | +8.1% | open |
| 2026-11-17 | [[ATEC]] | [[Koning John Todd]] | $99K | 48 | +1.9% | open |
| 2026-11-17 | [[NPCE]] | [[Williams Patrick F]] | $99K | 56 | -1.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cfo_exec_25k")
SORT filed DESC
```

Back to [[What Works]].
