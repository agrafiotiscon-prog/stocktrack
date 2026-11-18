---
type: "strategy"
key: "ceo_cfo_100k"
signals: 7878
cagr: 0.0960155
spy_cagr: 0.107555
sharpe: 0.411877
max_drawdown: 0.661595
holdout_excess: 0.0129276
---

# CEO or CFO buying $100K+

Rule key: `ceo_cfo_100k`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 7,878 |
| 3-month excess vs SPY (mean / median) | +1.3% / -0.9% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +1.0% |
| vs surviving stocks | +1.6% |
| 2006-2015 excess /yr | +9.9% (p 0.043) |
| 2016+ excess /yr | +1.3% (p 0.775) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.4% | +10.8% | 0.31 | 0.54 | 51% | 0.86 | -2.0% | 29% | 3,428 | 6.0% | +1.5% / 0.03 / 25% |
| 63d | +9.6% | +10.8% | 0.41 | 0.54 | 66% | 1.33 | -2.0% | 43% | 1,609 | 2.8% | +2.4% / 0.11 / 40% |
| 126d | +8.0% | +10.8% | 0.36 | 0.54 | 62% | 1.23 | -3.2% | 43% | 826 | 1.4% | +0.4% / -0.04 / 54% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +12.6%/yr, double costs +6.7%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +16.0% | +13.3% | +2.7% |
| 2007 | -10.1% | +5.1% | -15.2% |
| 2008 | -38.8% | -36.8% | -2.0% |
| 2009 | +74.0% | +26.4% | +47.6% |
| 2010 | +32.8% | +15.1% | +17.8% |
| 2011 | -10.3% | +1.9% | -12.2% |
| 2012 | +16.9% | +16.0% | +0.9% |
| 2013 | +48.0% | +32.3% | +15.7% |
| 2014 | +11.8% | +13.5% | -1.7% |
| 2015 | -3.0% | +1.2% | -4.3% |
| 2016 | +21.9% | +12.0% | +9.9% |
| 2017 | +0.5% | +21.7% | -21.2% |
| 2018 | -7.4% | -4.6% | -2.9% |
| 2019 | +23.5% | +31.2% | -7.7% |
| 2020 | +2.9% | +18.3% | -15.4% |
| 2021 | +19.2% | +28.7% | -9.6% |
| 2022 | -20.3% | -18.2% | -2.1% |
| 2023 | +50.7% | +26.2% | +24.5% |
| 2024 | +34.2% | +24.9% | +9.3% |
| 2025 | -9.2% | +17.7% | -26.9% |
| 2026 | +8.4% | +8.2% | +0.1% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 45 | -1.1% | +0.6% | 53% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[ECC]] | [[Onorio Kenneth P]] | $104K | 45 | – | pending |
| 2026-11-17 | [[TEAM]] | [[Cannon-Brookes Michael]] | $2.0M | 39 | – | pending |
| 2026-11-17 | [[UPST]] | [[Gu Paul]] | $950K | 60 | – | pending |
| 2026-11-17 | [[LPG]] | [[HADJIPATERAS JOHN C]] | $961K | 55 | – | pending |
| 2026-11-16 | [[MX]] | [[LEE CHAE]] | $218K | 63 | -2.9% | open |
| 2026-11-16 | [[BRSP]] | [[Mazzei Michael]] | $1.0M | 58 | +0.8% | open |
| 2026-11-16 | [[MP]] | [[Corbett Ryan]] | $129K | 58 | -4.3% | open |
| 2026-11-16 | [[KURA]] | [[WILSON TROY EDWARD]] | $1.5M | 66 | -1.7% | open |
| 2026-11-16 | [[ADIG]] | [[Aarnes Robert B]] | $100K | 68 | -4.0% | open |
| 2026-11-16 | [[FPS]] | [[Niederpruem Gary John]] | $334K | 77 | -0.6% | open |
| 2026-11-16 | [[FPS]] | [[Ard Amy E]] | $300K | 75 | -0.6% | open |
| 2026-11-16 | [[OIG]] | [[Gregg Kenneth]] | $1.0M | 46 | -5.1% | open |
| 2026-11-16 | [[CTVA]] | [[KISSAM LUTHER C IV]] | $300K | 65 | -3.8% | open |
| 2026-11-16 | [[NSLR]] | [[Klein Mark D]] | $994K | 85 | -0.8% | open |
| 2026-11-16 | [[TEAM]] | [[Cannon-Brookes Michael]] | $2.0M | 39 | -4.2% | open |
| 2026-11-16 | [[HUBS]] | [[Halligan Brian]] | $5.0M | 70 | -3.5% | open |
| 2026-11-16 | [[CRMD]] | [[Todisco Joseph]] | $391K | 50 | -1.7% | open |
| 2026-11-16 | [[HOS]] | [[HORNBECK TODD M]] | $500K | 45 | -4.8% | open |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | -1.4% | open |
| 2026-11-13 | [[CTEV]] | [[Dalton Travis]] | $150K | 58 | -15.4% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "ceo_cfo_100k")
SORT filed DESC
```

Back to [[What Works]].
