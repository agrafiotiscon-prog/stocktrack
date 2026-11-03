---
type: "strategy"
key: "score_40"
signals: 32319
cagr: 0.0600963
spy_cagr: 0.110756
sharpe: 0.288261
max_drawdown: 0.574297
holdout_excess: 0.0154221
---

# Live score 40+ (notable)

Rule key: `score_40`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 32,319 |
| 3-month excess vs SPY (mean / median) | +1.1% / -0.6% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.8% |
| vs surviving stocks | +1.2% |
| 2006-2015 excess /yr | +8.0% (p 0.010) |
| 2016+ excess /yr | +1.5% (p 0.714) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +6.6% | +11.1% | 0.31 | 0.56 | 59% | 1.26 | -4.7% | 33% | 4,873 | 8.6% | -0.9% / -0.12 / 59% |
| 63d | +6.0% | +11.1% | 0.29 | 0.56 | 57% | 1.24 | -5.2% | 38% | 1,660 | 2.6% | -1.9% / -0.19 / 57% |
| 126d | +5.1% | +11.1% | 0.26 | 0.56 | 68% | 1.19 | -5.7% | 33% | 840 | 1.4% | -2.9% / -0.27 / 57% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +8.8%/yr, double costs +3.3%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +12.7% | +13.8% | -1.1% |
| 2007 | -11.1% | +5.1% | -16.2% |
| 2008 | -19.3% | -36.8% | +17.5% |
| 2009 | +36.1% | +26.4% | +9.7% |
| 2010 | +31.8% | +15.1% | +16.8% |
| 2011 | -13.7% | +1.9% | -15.6% |
| 2012 | +22.0% | +16.0% | +6.0% |
| 2013 | +35.5% | +32.3% | +3.2% |
| 2014 | +0.7% | +13.5% | -12.8% |
| 2015 | -10.7% | +1.2% | -11.9% |
| 2016 | +21.1% | +12.0% | +9.1% |
| 2017 | +19.2% | +21.7% | -2.5% |
| 2018 | -19.6% | -4.6% | -15.0% |
| 2019 | +45.6% | +31.2% | +14.4% |
| 2020 | +10.3% | +18.3% | -8.1% |
| 2021 | +3.2% | +28.7% | -25.6% |
| 2022 | -20.4% | -18.2% | -2.3% |
| 2023 | +30.0% | +26.2% | +3.8% |
| 2024 | -10.3% | +24.9% | -35.2% |
| 2025 | -7.5% | +17.7% | -25.2% |
| 2026 | +9.3% | +13.7% | -4.5% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 23 | -1.4% | -0.3% | 39% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-02 | [[ASPE]] | [[ARCH Venture Fund X, L.P]] | $20.0M | 70 | – | pending |
| 2026-11-02 | [[ASPE]] | [[ARCH Venture Partners XIV, L.P]] | $18.0M | 70 | – | pending |
| 2026-11-02 | [[RSI]] | [[Winter Thomas]] | $118K | 42 | – | pending |
| 2026-11-02 | [[ROL]] | [[LOR INC]] | $50.0M | 41 | – | pending |
| 2026-11-02 | [[JBLU]] | [[BONEPARTH PETER]] | $300K | 47 | – | pending |
| 2026-11-02 | [[FCPT]] | [[Lenehan William H]] | $226K | 42 | – | pending |
| 2026-11-02 | [[ENPH]] | [[Kothandaraman Badrinarayanan]] | $268K | 41 | – | pending |
| 2026-11-02 | [[SEVN]] | [[Lorenzini Thomas J]] | $33K | 48 | – | pending |
| 2026-11-02 | [[SEVN]] | [[Jordan Matthew P]] | $66K | 40 | – | pending |
| 2026-11-02 | [[BBTX]] | [[Jeggle Helmut Wolfgang]] | $6.0M | 46 | – | pending |
| 2026-11-02 | [[BBT]] | [[Hughes William H III]] | $6K | 40 | – | pending |
| 2026-11-02 | [[OCFC]] | [[Katsoulis Nicos]] | $178K | 53 | – | pending |
| 2026-11-02 | [[LSTR]] | [[Lonegro Frank A]] | $715K | 57 | – | pending |
| 2026-10-30 | [[RAPP]] | [[HEALY JAMES]] | $20.4M | 87 | +0.8% | open |
| 2026-10-30 | [[FFIN]] | [[Denny Michael B]] | $100K | 42 | +2.7% | open |
| 2026-10-30 | [[BBT]] | [[Charnley Nina A]] | $11K | 57 | +4.9% | open |
| 2026-10-29 | [[DINO]] | [[MYERS FRANKLIN]] | $1.1M | 52 | -0.7% | open |
| 2026-10-29 | [[SCQCU]] | [[Das Soumen]] | $2.7M | 56 | +1.2% | open |
| 2026-10-29 | [[PNFP]] | [[INGRAM DAVID B]] | $992K | 43 | +2.4% | open |
| 2026-10-29 | [[HBAN]] | [[TORGOW GARY]] | $200K | 40 | +1.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "score_40")
SORT filed DESC
```

Back to [[What Works]].
