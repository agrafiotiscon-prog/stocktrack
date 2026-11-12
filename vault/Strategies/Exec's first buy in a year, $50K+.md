---
type: "strategy"
key: "first_buy_exec"
signals: 5620
cagr: 0.0917078
spy_cagr: 0.107767
sharpe: 0.404899
max_drawdown: 0.54717
holdout_excess: 0.00460389
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,620 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +0.9% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +11.4% (p 0.011) |
| 2016+ excess /yr | +0.5% (p 0.915) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +4.0% | +10.8% | 0.22 | 0.54 | 53% | 0.89 | -4.5% | 20% | 3,209 | 5.4% | -0.5% / -0.15 / 48% |
| 63d | +9.2% | +10.8% | 0.40 | 0.54 | 55% | 1.22 | -2.0% | 55% | 1,530 | 2.6% | +1.9% / 0.09 / 39% |
| 126d | +10.1% | +10.8% | 0.44 | 0.54 | 57% | 1.20 | -1.2% | 45% | 785 | 1.3% | +2.2% / 0.11 / 40% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.9%/yr, double costs +6.5%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2007 | +4.1% | +5.3% | -1.2% |
| 2008 | -29.1% | -36.8% | +7.7% |
| 2009 | +54.2% | +26.4% | +27.8% |
| 2010 | +25.5% | +15.1% | +10.4% |
| 2011 | -6.5% | +1.9% | -8.4% |
| 2012 | +30.1% | +16.0% | +14.1% |
| 2013 | +34.4% | +32.3% | +2.1% |
| 2014 | +6.6% | +13.5% | -6.9% |
| 2015 | +3.7% | +1.2% | +2.5% |
| 2016 | +1.2% | +12.0% | -10.8% |
| 2017 | +25.0% | +21.7% | +3.3% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +27.1% | +18.3% | +8.8% |
| 2021 | -4.8% | +28.7% | -33.5% |
| 2022 | -9.0% | -18.2% | +9.2% |
| 2023 | +22.2% | +26.2% | -4.0% |
| 2024 | +28.4% | +24.9% | +3.5% |
| 2025 | -10.3% | +17.7% | -28.0% |
| 2026 | -9.8% | +10.8% | -20.6% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 18 | +1.3% | +2.3% | 56% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[MP]] | [[Corbett Ryan]] | $199K | 61 | – | pending |
| 2026-11-12 | [[COHR]] | [[ANDERSON JAMES ROBERT]] | $997K | 62 | – | pending |
| 2026-11-12 | [[GSM]] | [[Levi Marco]] | $51K | 56 | – | pending |
| 2026-11-12 | [[CSQR]] | [[MULLEE SPENCER EDWARD]] | $247K | 41 | – | pending |
| 2026-11-10 | [[WW]] | [[BYE STEPHEN J]] | $138K | 68 | -2.5% | open |
| 2026-11-10 | [[UPBD]] | [[Young Scott A]] | $150K | 75 | +1.6% | open |
| 2026-11-10 | [[CNXN]] | [[Zafirovski Matthew David]] | $200K | 55 | -1.7% | open |
| 2026-11-10 | [[OBK]] | [[Crotwell Jim]] | $107K | 36 | -0.7% | open |
| 2026-11-09 | [[ROK]] | [[Moret Blake D]] | $1.5M | 53 | +2.0% | open |
| 2026-11-09 | [[WCC]] | [[Dev Indraneel]] | $504K | 60 | +1.0% | open |
| 2026-11-09 | [[FLOC]] | [[EDWARDS JOSEPH R]] | $798K | 76 | -2.1% | open |
| 2026-11-09 | [[DKNG]] | [[Ellingson Alan Wayne]] | $350K | 46 | +3.8% | open |
| 2026-11-09 | [[SOPH]] | [[Muken Ross]] | $137K | 53 | -7.1% | open |
| 2026-11-09 | [[CMCO]] | [[Wilson David J]] | $551K | 52 | +11.9% | open |
| 2026-11-09 | [[AUDC]] | [[ADLERSBERG SHABTAI]] | $126K | 38 | +1.6% | open |
| 2026-11-06 | [[KMI]] | [[KINDER RICHARD D]] | $15.0M | 53 | +2.7% | open |
| 2026-11-06 | [[TRNS]] | [[IRICK JAIME A]] | $230K | 59 | -5.7% | open |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | $1.0M | 69 | -7.6% | open |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | +4.4% | open |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | +8.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
