---
type: "strategy"
key: "contrarian"
signals: 8134
cagr: 0.0167198
spy_cagr: 0.108549
sharpe: 0.174638
max_drawdown: 0.72227
holdout_excess: -0.0582116
---

# Insider buying after a 30%+ drop

Rule key: `contrarian`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 8,134 |
| 3-month excess vs SPY (mean / median) | +5.2% / +2.0% |
| Beat SPY over 3 months | 53% |
| Entering one session later | +4.8% |
| vs surviving stocks | +3.8% |
| 2006-2015 excess /yr | +13.7% (p 0.149) |
| 2016+ excess /yr | -5.8% (p 0.407) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +2.5% | +10.9% | 0.17 | 0.54 | 72% | 1.14 | -6.9% | 33% | 2,248 | 6.1% | +0.9% / 0.04 / 66% |
| 63d | +1.7% | +10.9% | 0.17 | 0.54 | 72% | 1.56 | -9.6% | 19% | 1,183 | 3.3% | -2.2% / -0.08 / 67% |
| 126d | +5.8% | +10.9% | 0.29 | 0.54 | 66% | 1.62 | -6.2% | 48% | 714 | 2.0% | +0.1% / 0.02 / 71% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +5.0%/yr, double costs -1.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +22.1% | +9.7% | +12.4% |
| 2007 | +4.5% | +5.1% | -0.7% |
| 2008 | -44.1% | -36.8% | -7.3% |
| 2009 | +24.9% | +26.4% | -1.4% |
| 2010 | +21.5% | +15.1% | +6.4% |
| 2011 | -8.2% | +1.9% | -10.1% |
| 2012 | +29.1% | +16.0% | +13.1% |
| 2013 | +24.0% | +32.3% | -8.3% |
| 2014 | -2.0% | +13.5% | -15.5% |
| 2015 | -21.6% | +1.2% | -22.8% |
| 2016 | +38.5% | +12.0% | +26.5% |
| 2017 | +15.0% | +21.7% | -6.7% |
| 2018 | -11.5% | -4.6% | -6.9% |
| 2019 | +31.1% | +31.2% | -0.1% |
| 2020 | +14.9% | +18.3% | -3.4% |
| 2021 | -10.2% | +28.7% | -38.9% |
| 2022 | -44.4% | -18.2% | -26.2% |
| 2023 | +10.2% | +26.2% | -15.9% |
| 2024 | -7.9% | +24.9% | -32.8% |
| 2025 | +4.6% | +17.7% | -13.1% |
| 2026 | +2.2% | +10.8% | -8.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 27 | +1.8% | +1.8% | 70% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[LRMR]] | [[Hamilton Thomas Edward]] | $187K | 70 | – | pending |
| 2026-11-12 | [[HPP]] | [[BORTZ JON E]] | $680K | 62 | – | pending |
| 2026-11-12 | [[HPP]] | [[COLEMAN VICTOR J]] | $182K | 62 | – | pending |
| 2026-11-12 | [[LRMR]] | [[BEN-MAIMON CAROLE]] | $50K | 63 | – | pending |
| 2026-11-12 | [[LRMR]] | [[THOMAS FRANK E]] | $22K | 60 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Truitt Joseph]] | $10K | 57 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Harlow John B. Jr]] | $50K | 71 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Celano Michael]] | $50K | 62 | – | pending |
| 2026-11-12 | [[LRMR]] | [[Shankar Gopi]] | $14K | 52 | – | pending |
| 2026-11-12 | [[KGS]] | [[Montana Margaret C]] | $44K | 24 | – | pending |
| 2026-11-12 | [[OFIX]] | [[Juniper Investment Company, LLC]] | $5.1M | 47 | – | pending |
| 2026-11-12 | [[BW]] | [[Howe Alan B]] | $5K | 32 | – | pending |
| 2026-11-12 | [[FMC]] | [[Tack Luc Jules R]] | $14K | 14 | – | pending |
| 2026-11-12 | [[ILPT]] | [[PHELAN KEVIN C]] | $12K | 27 | – | pending |
| 2026-11-12 | [[STVN]] | [[FEDERICI WILLIAM J]] | $274K | 58 | – | pending |
| 2026-11-12 | [[ALNY]] | [[Sigal Charles Elliott]] | $244K | 58 | – | pending |
| 2026-11-12 | [[ADTN]] | [[STANTON THOMAS R]] | $172K | 54 | – | pending |
| 2026-11-12 | [[ALNY]] | [[SCHULMAN AMY W]] | $300K | 47 | – | pending |
| 2026-11-12 | [[NSLR]] | [[Mazur Marc]] | $30K | 36 | – | pending |
| 2026-11-12 | [[BDSX]] | [[SCHULER JACK W]] | $1.0M | 40 | – | pending |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "contrarian")
SORT filed DESC
```

Back to [[What Works]].
