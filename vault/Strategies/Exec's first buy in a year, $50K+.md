---
type: "strategy"
key: "first_buy_exec"
signals: 5614
cagr: 0.0914799
spy_cagr: 0.10821
sharpe: 0.404292
max_drawdown: 0.54717
holdout_excess: 0.00497207
---

# Exec's first buy in a year, $50K+

Rule key: `first_buy_exec`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 5,614 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.3% |
| Beat SPY over 3 months | 49% |
| Entering one session later | +1.0% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +11.4% (p 0.011) |
| 2016+ excess /yr | +0.5% (p 0.908) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.9% | +10.8% | 0.21 | 0.54 | 54% | 0.88 | -4.6% | 20% | 3,212 | 5.4% | -0.5% / -0.15 / 48% |
| 63d | +9.1% | +10.8% | 0.40 | 0.54 | 55% | 1.21 | -2.0% | 55% | 1,528 | 2.5% | +1.9% / 0.09 / 43% |
| 126d | +10.4% | +10.8% | 0.45 | 0.54 | 57% | 1.20 | -1.0% | 45% | 784 | 1.3% | +2.4% / 0.13 / 41% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.8%/yr, double costs +6.6%/yr.


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
| 2017 | +25.2% | +21.7% | +3.5% |
| 2018 | -5.8% | -4.6% | -1.3% |
| 2019 | +32.5% | +31.2% | +1.3% |
| 2020 | +29.1% | +18.3% | +10.7% |
| 2021 | -4.2% | +28.7% | -32.9% |
| 2022 | -6.9% | -18.2% | +11.3% |
| 2023 | +22.6% | +26.2% | -3.6% |
| 2024 | +31.0% | +24.9% | +6.1% |
| 2025 | -10.8% | +17.7% | -28.5% |
| 2026 | -15.7% | +11.5% | -27.2% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 11 | +2.0% | +3.4% | 64% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-06 | [[KMI]] | [[KINDER RICHARD D]] | $15.0M | 53 | – | pending |
| 2026-11-06 | [[TRNS]] | [[IRICK JAIME A]] | $230K | 59 | – | pending |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | $1.0M | 69 | -2.9% | open |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | -0.1% | open |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | -4.7% | open |
| 2026-11-05 | [[FBRT]] | [[Byrne Richard J]] | $998K | 65 | -3.2% | open |
| 2026-11-05 | [[UPBD]] | [[Karam Fahmi]] | $100K | 64 | -1.1% | open |
| 2026-11-05 | [[LBTYA]] | [[Rodriguez Enrique]] | $2.0M | 73 | +3.3% | open |
| 2026-11-05 | [[LBTYA]] | [[FRIES MICHAEL T]] | $1.0M | 66 | +3.3% | open |
| 2026-11-04 | [[PAM]] | [[Zuberbuhler Adolfo Fernando]] | $207K | 55 | +0.8% | open |
| 2026-11-04 | [[PRLB]] | [[Krishna Suresh]] | $52K | 49 | +1.5% | open |
| 2026-11-04 | [[UPBD]] | [[Khouri Halim]] | $251K | 70 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[Wooters Rebecca]] | $99K | 67 | +1.3% | open |
| 2026-11-04 | [[UPBD]] | [[Kumar Balaji]] | $50K | 61 | +1.3% | open |
| 2026-11-04 | [[AN]] | [[Manley Michael Mark]] | $1.0M | 71 | +1.1% | open |
| 2026-11-02 | [[BANC]] | [[WOLFF JARED M]] | $100K | 39 | -0.6% | open |
| 2026-11-02 | [[BLX]] | [[Diaz Adriana Lizzeth]] | $94K | 38 | +1.8% | open |
| 2026-11-02 | [[LSTR]] | [[Lonegro Frank A]] | $715K | 57 | -0.4% | open |
| 2026-10-30 | [[OCFC]] | [[Barrett Patrick Sean]] | $90K | 37 | +3.4% | open |
| 2026-10-29 | [[UTMD]] | [[CORNWELL KEVIN L]] | $67K | 35 | +10.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "first_buy_exec")
SORT filed DESC
```

Back to [[What Works]].
