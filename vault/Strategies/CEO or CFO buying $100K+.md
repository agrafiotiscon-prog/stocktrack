---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7837
cagr: 0.100274
spy_cagr: 0.108918
sharpe: 0.426485
max_drawdown: 0.661595
holdout_excess: 0.0130958
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,837 |
| 3-month excess vs SPY (mean / median) | +1.3% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.0% |
| vs surviving stocks | +1.6% |
| 2006-2015 excess /yr | +9.8% (p 0.046) |
| 2016+ excess /yr | +1.3% (p 0.772) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +10.9% | 0.33 | 0.55 | 51% | 0.85 | -1.9% | 29% | 3,421 | 6.0% | +1.6% / 0.04 / 25% |
| 63d | +10.0% | +10.9% | 0.43 | 0.55 | 66% | 1.34 | -1.9% | 43% | 1,608 | 2.8% | +2.6% / 0.13 / 39% |
| 126d | +9.4% | +10.9% | 0.41 | 0.55 | 62% | 1.25 | -2.1% | 48% | 826 | 1.5% | +1.4% / 0.04 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +13.1%/yr, double costs +7.1%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.3% | +2.7% |
| 2007 | -10.1% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +74.0% | +26.4% | +47.6% |
| 2010 | +32.6% | +15.1% | +17.5% |
| 2011 | -10.2% | +1.9% | -12.1% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +12.8% | +13.5% | -0.7% |
| 2015 | -1.5% | +1.2% | -2.7% |
| 2016 | +24.2% | +12.0% | +12.3% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -5.9% | -4.6% | -1.4% |
| 2019 | +23.5% | +31.2% | -7.7% |
| 2020 | +2.9% | +18.3% | -15.5% |
| 2021 | +19.1% | +28.7% | -9.6% |
| 2022 | -20.3% | -18.2% | -2.1% |
| 2023 | +50.6% | +26.2% | +24.4% |
| 2024 | +34.0% | +24.9% | +9.1% |
| 2025 | -9.3% | +17.7% | -27.0% |
| 2026 | +10.9% | +10.8% | +0.0% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 21 | -0.5% | +0.6% | 57% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-12 | [[TH]] | [[Archer James Bradley]] | $313K | 43 | – | pending |
| 2026-11-12 | [[MP]] | [[Corbett Ryan]] | $199K | 61 | – | pending |
| 2026-11-12 | [[COHR]] | [[ANDERSON JAMES ROBERT]] | $997K | 62 | – | pending |
| 2026-11-12 | [[CSQR]] | [[MULLEE SPENCER EDWARD]] | $247K | 41 | – | pending |
| 2026-11-10 | [[WW]] | [[BYE STEPHEN J]] | $138K | 68 | -2.5% | open |
| 2026-11-10 | [[FLOC]] | [[EDWARDS JOSEPH R]] | $390K | 60 | -1.2% | open |
| 2026-11-10 | [[MX]] | [[LEE CHAE]] | $155K | 49 | +7.6% | open |
| 2026-11-09 | [[ADTN]] | [[STANTON THOMAS R]] | $601K | 65 | +1.3% | open |
| 2026-11-09 | [[ROK]] | [[Moret Blake D]] | $1.5M | 53 | +2.0% | open |
| 2026-11-09 | [[WCC]] | [[Dev Indraneel]] | $504K | 60 | +1.0% | open |
| 2026-11-09 | [[FLOC]] | [[EDWARDS JOSEPH R]] | $798K | 76 | -2.1% | open |
| 2026-11-09 | [[UPBD]] | [[Karam Fahmi]] | $300K | 71 | -0.1% | open |
| 2026-11-09 | [[LUMN]] | [[Johnson Kathleen E]] | $397K | 73 | -1.6% | open |
| 2026-11-09 | [[DKNG]] | [[Ellingson Alan Wayne]] | $350K | 46 | +3.8% | open |
| 2026-11-09 | [[AN]] | [[Szlosek Thomas A]] | $200K | 67 | -1.2% | open |
| 2026-11-09 | [[SOPH]] | [[CARDOZA GEORGE]] | $141K | 53 | -7.1% | open |
| 2026-11-09 | [[SOPH]] | [[Muken Ross]] | $137K | 53 | -7.1% | open |
| 2026-11-09 | [[CMCO]] | [[Wilson David J]] | $551K | 52 | +11.9% | open |
| 2026-11-09 | [[AUDC]] | [[ADLERSBERG SHABTAI]] | $126K | 38 | +1.6% | open |
| 2026-11-09 | [[MTDR]] | [[Foran Joseph Wm]] | $257K | 84 | +5.0% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
