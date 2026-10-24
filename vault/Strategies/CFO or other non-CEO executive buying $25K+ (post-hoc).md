---
type: "strategy"
key: "cfo_exec_25k"
signals: 8037
cagr: 0.137911
spy_cagr: 0.110825
sharpe: 0.548831
max_drawdown: 0.586893
holdout_excess: 0.0541909
---

# CFO or other non-CEO executive buying $25K+ (post-hoc)

Rule key: `cfo_exec_25k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,037 |
| 3-month excess vs SPY (mean / median) | +2.0% / -0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +1.7% |
| vs surviving stocks | +2.2% |
| 2006-2015 excess /yr | +8.8% (p 0.037) |
| 2016+ excess /yr | +5.4% (p 0.148) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.4% | +11.1% | 0.35 | 0.56 | 50% | 0.92 | -1.8% | 33% | 3,672 | 6.6% | +2.1% / 0.09 / 30% |
| 63d | +13.8% | +11.1% | 0.55 | 0.56 | 59% | 1.23 | +1.8% | 52% | 1,635 | 3.1% | +5.5% / 0.35 / 22% |
| 126d | +11.4% | +11.1% | 0.47 | 0.56 | 58% | 1.20 | -0.1% | 43% | 830 | 1.5% | +3.1% / 0.17 / 26% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.7%/yr, double costs +11.0%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.6% | +13.8% | +2.8% |
| 2007 | -1.0% | +5.1% | -6.1% |
| 2008 | -34.1% | -36.8% | +2.7% |
| 2009 | +94.7% | +26.4% | +68.3% |
| 2010 | +32.2% | +15.1% | +17.1% |
| 2011 | -10.1% | +1.9% | -12.0% |
| 2012 | +23.2% | +16.0% | +7.2% |
| 2013 | +45.5% | +32.3% | +13.2% |
| 2014 | +2.2% | +13.5% | -11.3% |
| 2015 | -5.7% | +1.2% | -6.9% |
| 2016 | +29.3% | +12.0% | +17.3% |
| 2017 | +17.3% | +21.7% | -4.4% |
| 2018 | -12.5% | -4.6% | -7.9% |
| 2019 | +43.3% | +31.2% | +12.1% |
| 2020 | +17.1% | +18.3% | -1.3% |
| 2021 | +28.4% | +28.7% | -0.3% |
| 2022 | -14.0% | -18.2% | +4.2% |
| 2023 | +20.0% | +26.2% | -6.2% |
| 2024 | +33.0% | +24.9% | +8.1% |
| 2025 | +20.8% | +17.7% | +3.0% |
| 2026 | +1.3% | +13.7% | -12.3% |


## Live forward test

1 buys logged so far; none have matured yet.


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | – | pending |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | – | pending |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -0.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cfo_exec_25k")
SORT filed DESC
```

Back to [[What Works]].
