---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7826
cagr: 0.0971197
spy_cagr: 0.109342
sharpe: 0.415856
max_drawdown: 0.661595
holdout_excess: 0.0138897
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,826 |
| 3-month excess vs SPY (mean / median) | +1.4% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.1% |
| vs surviving stocks | +1.7% |
| 2006-2015 excess /yr | +10.0% (p 0.041) |
| 2016+ excess /yr | +1.4% (p 0.760) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +10.9% | 0.32 | 0.55 | 52% | 0.85 | -2.0% | 29% | 3,427 | 6.0% | +1.5% / 0.03 / 25% |
| 63d | +9.7% | +10.9% | 0.42 | 0.55 | 66% | 1.33 | -2.1% | 43% | 1,606 | 2.8% | +2.3% / 0.11 / 41% |
| 126d | +9.4% | +10.9% | 0.41 | 0.55 | 62% | 1.25 | -2.1% | 48% | 825 | 1.5% | +1.4% / 0.04 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.7%/yr, double costs +6.8%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.3% | +2.7% |
| 2007 | -10.1% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +74.0% | +26.4% | +47.6% |
| 2010 | +34.6% | +15.1% | +19.6% |
| 2011 | -10.3% | +1.9% | -12.2% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +11.5% | +13.5% | -1.9% |
| 2015 | -6.7% | +1.2% | -8.0% |
| 2016 | +23.6% | +12.0% | +11.6% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -7.4% | -4.6% | -2.9% |
| 2019 | +23.5% | +31.2% | -7.7% |
| 2020 | +2.9% | +18.3% | -15.4% |
| 2021 | +18.8% | +28.7% | -9.9% |
| 2022 | -20.3% | -18.2% | -2.1% |
| 2023 | +50.7% | +26.2% | +24.5% |
| 2024 | +34.2% | +24.9% | +9.3% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +12.0% | +11.5% | +0.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 14 | -3.5% | +0.6% | 50% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-10 | [[MX]] | [[LEE CHAE]] | $155K | 49 | – | pending |
| 2026-11-09 | [[ADTN]] | [[STANTON THOMAS R]] | $601K | 65 | – | pending |
| 2026-11-09 | [[ROK]] | [[Moret Blake D]] | $1.5M | 53 | – | pending |
| 2026-11-09 | [[WCC]] | [[Dev Indraneel]] | $504K | 60 | – | pending |
| 2026-11-09 | [[FLOC]] | [[EDWARDS JOSEPH R]] | $798K | 76 | – | pending |
| 2026-11-09 | [[UPBD]] | [[Karam Fahmi]] | $300K | 71 | – | pending |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | – | pending |
| 2026-11-09 | [[DKNG]] | [[Ellingson Alan Wayne]] | $350K | 46 | – | pending |
| 2026-11-09 | [[AN]] | [[Szlosek Thomas A]] | $200K | 67 | – | pending |
| 2026-11-09 | [[SOPH]] | [[CARDOZA GEORGE]] | $141K | 53 | – | pending |
| 2026-11-09 | [[SOPH]] | [[Muken Ross]] | $137K | 53 | – | pending |
| 2026-11-09 | [[CMCO]] | [[Wilson David J]] | $551K | 52 | – | pending |
| 2026-11-09 | [[AUDC]] | [[ADLERSBERG SHABTAI]] | $126K | 38 | – | pending |
| 2026-11-09 | [[MTDR]] | [[Foran Joseph Wm]] | $257K | 84 | – | pending |
| 2026-11-06 | [[TRNS]] | [[IRICK JAIME A]] | $230K | 59 | -0.6% | open |
| 2026-11-06 | [[KMT]] | [[Chowbey Sanjay]] | $165K | 42 | +1.2% | open |
| 2026-11-05 | [[MTDR]] | [[Calvert Christopher P]] | $105K | 50 | -2.3% | open |
| 2026-11-05 | [[BXMT]] | [[Johnson Timothy Steven]] | $1.0M | 69 | -5.1% | open |
| 2026-11-05 | [[LBRT]] | [[Gusek Ron]] | $377K | 65 | +5.6% | open |
| 2026-11-05 | [[GLXY]] | [[Novogratz Michael]] | $9.9M | 75 | -1.1% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
