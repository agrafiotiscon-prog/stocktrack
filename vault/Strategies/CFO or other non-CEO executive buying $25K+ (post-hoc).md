---
type: "strategy"
key: "cfo_exec_25k"
signals: 8017
cagr: 0.139236
spy_cagr: 0.109572
sharpe: 0.553559
max_drawdown: 0.564045
holdout_excess: 0.0504001
---

# CFO or other non-CEO executive buying $25K+ (post-hoc)

Rule key: `cfo_exec_25k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

> [!warning] Post-hoc idea
> This rule was written after seeing the backtest, so the backtest numbers below are in-sample and can't confirm it. Only the live forward test counts. See [[Findings]] and `data/backtest/hypotheses.json`.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,017 |
| 3-month excess vs SPY (mean / median) | +2.0% / -0.1% |
| Beat SPY over 3 months | 50% |
| Entering one session later | +1.7% |
| vs surviving stocks | +2.2% |
| 2006-2015 excess /yr | +8.8% (p 0.038) |
| 2016+ excess /yr | +5.0% (p 0.178) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.0% | +11.0% | 0.33 | 0.55 | 50% | 0.92 | -2.0% | 29% | 3,677 | 6.6% | +1.7% / 0.05 / 35% |
| 63d | +13.9% | +11.0% | 0.55 | 0.55 | 56% | 1.22 | +2.1% | 52% | 1,635 | 3.1% | +5.5% / 0.35 / 20% |
| 126d | +11.6% | +11.0% | 0.48 | 0.55 | 58% | 1.20 | +0.1% | 43% | 830 | 1.5% | +3.1% / 0.17 / 25% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.8%/yr, double costs +11.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.9% | +13.8% | +3.1% |
| 2007 | +0.9% | +5.1% | -4.3% |
| 2008 | -32.0% | -36.8% | +4.8% |
| 2009 | +91.1% | +26.4% | +64.7% |
| 2010 | +30.2% | +15.1% | +15.2% |
| 2011 | -12.3% | +1.9% | -14.2% |
| 2012 | +22.1% | +16.0% | +6.1% |
| 2013 | +43.2% | +32.3% | +10.9% |
| 2014 | +1.1% | +13.5% | -12.3% |
| 2015 | -3.1% | +1.2% | -4.3% |
| 2016 | +27.0% | +12.0% | +15.0% |
| 2017 | +17.4% | +21.7% | -4.4% |
| 2018 | -12.4% | -4.6% | -7.9% |
| 2019 | +52.0% | +31.2% | +20.7% |
| 2020 | +16.9% | +18.3% | -1.4% |
| 2021 | +28.5% | +28.7% | -0.3% |
| 2022 | -13.3% | -18.2% | +4.9% |
| 2023 | +19.7% | +26.2% | -6.5% |
| 2024 | +32.5% | +24.9% | +7.6% |
| 2025 | +20.6% | +17.7% | +2.8% |
| 2026 | +1.5% | +11.5% | -9.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 5 | -0.6% | +2.1% | 60% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | $207K | 55 | – | pending |
| 2026-11-04 | [[HGV]] | [[Wang Mark D]] | $499K | 46 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | $99K | 67 | – | pending |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | $50K | 61 | – | pending |
| 2026-11-04 | [[AN]] | [[EDMUNDS C COLEMAN]] | $101K | 48 | – | pending |
| 2026-11-04 | [[AN]] | [[Szlosek Thomas A]] | $300K | 65 | – | pending |
| 2026-11-03 | [[STRZ]] | [[MACDONALD SCOTT D]] | $56K | 48 | +2.2% | open |
| 2026-11-03 | [[MAA]] | [[Hill Adrian]] | $100K | 31 | +1.5% | open |
| 2026-11-03 | [[PMN]] | [[Cashman Neil]] | $39K | 44 | +2.7% | open |
| 2026-11-02 | [[BLX]] | [[Diaz Adriana Lizzeth]] | $94K | 38 | -1.0% | open |
| 2026-10-30 | [[OCFC]] | [[Barrett Patrick Sean]] | $90K | 37 | +4.1% | open |
| 2026-10-27 | [[NPB]] | [[Long Joseph B]] | $50K | 65 | -0.4% | open |
| 2026-10-27 | [[KIO]] | [[Takao Justin]] | $78K | 51 | +2.8% | open |
| 2026-10-26 | [[TCBX]] | [[Bobbora William]] | $40K | 24 | -0.3% | open |
| 2026-10-23 | [[NXG]] | [[Swank Jerry V]] | $439K | 64 | -0.9% | open |
| 2026-10-23 | [[NXG]] | [[Nelson Blake]] | $40K | 68 | -0.9% | open |
| 2026-10-21 | [[RAPP]] | [[Ignelzi Troy A]] | $144K | 54 | -1.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "cfo_exec_25k")
SORT filed DESC
```

Back to [[What Works]].
