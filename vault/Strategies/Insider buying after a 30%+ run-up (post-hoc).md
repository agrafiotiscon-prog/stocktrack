---
type: "strategy"
key: "momentum_buy"
signals: 3948
cagr: 0.20241
spy_cagr: 0.110437
sharpe: 0.834237
max_drawdown: 0.416334
holdout_excess: 0.213412
---

# Insider buying after a 30%+ run-up (post-hoc)

Rule key: `momentum_buy`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 3,948 |
| 3-month excess vs SPY (mean / median) | +2.7% / -1.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +2.2% |
| vs surviving stocks | +2.6% |
| 2006-2015 excess /yr | +9.8% (p 0.154) |
| 2016+ excess /yr | +21.3% (p 0.021) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +12.0% | +11.0% | 0.65 | 0.55 | 46% | 0.47 | +6.2% | 33% | 2,016 | 6.5% | +8.3% / 0.58 / 31% |
| 63d | +20.2% | +11.0% | 0.83 | 0.55 | 42% | 0.93 | +10.5% | 57% | 1,240 | 3.1% | +13.9% / 0.80 / 25% |
| 126d | +16.2% | +11.0% | 0.60 | 0.55 | 56% | 1.15 | +5.8% | 57% | 749 | 2.0% | +9.4% / 0.48 / 38% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +22.3%/yr, double costs +17.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +9.9% | +13.3% | -3.4% |
| 2007 | +13.7% | +5.1% | +8.5% |
| 2008 | -20.3% | -36.8% | +16.5% |
| 2009 | +76.8% | +26.4% | +50.5% |
| 2010 | +17.9% | +15.1% | +2.8% |
| 2011 | -6.4% | +1.9% | -8.3% |
| 2012 | +13.0% | +16.0% | -3.0% |
| 2013 | +54.5% | +32.3% | +22.2% |
| 2014 | -3.7% | +13.5% | -17.1% |
| 2015 | -11.1% | +1.2% | -12.3% |
| 2016 | +8.6% | +12.0% | -3.4% |
| 2017 | +31.3% | +21.7% | +9.6% |
| 2018 | +29.9% | -4.6% | +34.5% |
| 2019 | +25.4% | +31.2% | -5.8% |
| 2020 | +132.0% | +18.3% | +113.7% |
| 2021 | +36.8% | +28.7% | +8.0% |
| 2022 | -8.4% | -18.2% | +9.8% |
| 2023 | +1.1% | +26.2% | -25.0% |
| 2024 | +6.4% | +24.9% | -18.5% |
| 2025 | +87.4% | +17.7% | +69.7% |
| 2026 | +16.0% | +13.3% | +2.7% |


## Live forward test

0 buys logged so far; none have matured yet.


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "momentum_buy")
SORT filed DESC
```

Back to [[What Works]].
