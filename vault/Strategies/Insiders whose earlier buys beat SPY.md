---
type: "strategy"
key: "proven_insider"
signals: 20084
cagr: 0.129009
spy_cagr: 0.11135
sharpe: 0.527923
max_drawdown: 0.601494
holdout_excess: 0.00385895
---

# Insiders whose earlier buys beat SPY

Rule key: `proven_insider`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 20,084 |
| 3-month excess vs SPY (mean / median) | +0.7% / -0.9% |
| Beat SPY over 3 months | 47% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.0% (p 0.022) |
| 2016+ excess /yr | +0.4% (p 0.906) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +7.6% | +11.1% | 0.35 | 0.56 | 52% | 1.09 | -3.0% | 29% | 4,538 | 8.6% | -0.5% / -0.14 / 45% |
| 63d | +12.9% | +11.1% | 0.53 | 0.56 | 60% | 1.22 | +0.9% | 48% | 1,612 | 3.1% | +4.3% / 0.27 / 30% |
| 126d | +9.1% | +11.1% | 0.41 | 0.56 | 57% | 1.12 | -1.8% | 43% | 817 | 1.5% | +0.5% / -0.04 / 39% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +16.3%/yr, double costs +9.4%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +15.5% | +13.9% | +1.7% |
| 2007 | +4.3% | +5.1% | -0.8% |
| 2008 | -19.2% | -36.8% | +17.6% |
| 2009 | +24.8% | +26.4% | -1.6% |
| 2010 | +42.2% | +15.1% | +27.1% |
| 2011 | +7.7% | +1.9% | +5.8% |
| 2012 | +14.9% | +16.0% | -1.1% |
| 2013 | +39.1% | +32.3% | +6.8% |
| 2014 | +13.8% | +13.5% | +0.3% |
| 2015 | -13.8% | +1.2% | -15.0% |
| 2016 | +25.3% | +12.0% | +13.3% |
| 2017 | +11.2% | +21.7% | -10.5% |
| 2018 | -12.9% | -4.6% | -8.3% |
| 2019 | +30.6% | +31.2% | -0.6% |
| 2020 | +38.8% | +18.3% | +20.5% |
| 2021 | +14.5% | +28.7% | -14.2% |
| 2022 | -25.4% | -18.2% | -7.2% |
| 2023 | +40.3% | +26.2% | +14.1% |
| 2024 | +15.7% | +24.9% | -9.2% |
| 2025 | +25.0% | +17.7% | +7.3% |
| 2026 | +6.9% | +10.8% | -3.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 84 | +2.4% | +2.3% | 68% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-17 | [[BW]] | [[BRC Group Holdings, Inc]] | $212K | 66 | – | pending |
| 2026-11-16 | [[JOF]] | [[Saba Capital Management, L.P]] | $73K | 18 | – | pending |
| 2026-11-16 | [[LEO]] | [[Saba Capital Management, L.P]] | $796K | 31 | – | pending |
| 2026-11-16 | [[KODK]] | [[Katz Philippe D]] | $25K | 20 | – | pending |
| 2026-11-16 | [[CTVA]] | [[PAGE GREGORY R]] | $185K | 57 | – | pending |
| 2026-11-16 | [[LPTH]] | [[Rubin Shmuel]] | $19K | 31 | – | pending |
| 2026-11-16 | [[CTVA]] | [[KISSAM LUTHER C IV]] | $300K | 65 | – | pending |
| 2026-11-16 | [[NSLR]] | [[Klein Mark D]] | $994K | 85 | – | pending |
| 2026-11-16 | [[EVLV]] | [[Charlton Kevin M]] | $40K | 23 | – | pending |
| 2026-11-16 | [[SENS]] | [[ROEDER DOUGLAS A]] | $176K | 33 | – | pending |
| 2026-11-16 | [[SEI]] | [[TEAGUE AJ]] | $35K | 19 | – | pending |
| 2026-11-16 | [[CACC]] | [[Quinn Sean Edward]] | $252K | 54 | – | pending |
| 2026-11-16 | [[BW]] | [[Frymyer Cameron M]] | $42K | 58 | – | pending |
| 2026-11-16 | [[NTWK]] | [[GHAURI NAJEEB]] | $22K | 30 | – | pending |
| 2026-11-16 | [[DGICA]] | [[DONEGAL MUTUAL INSURANCE CO]] | $285K | 23 | – | pending |
| 2026-11-16 | [[DX]] | [[BOSTON BYRON L]] | $50K | 46 | – | pending |
| 2026-11-16 | [[DX]] | [[Popenoe Smriti Laxman]] | $26K | 43 | – | pending |
| 2026-11-16 | [[ECOR]] | [[Errico Thomas J]] | $54K | 24 | – | pending |
| 2026-11-13 | [[STWD]] | [[STERNLICHT BARRY S]] | $14.7M | 87 | +1.3% | open |
| 2026-11-13 | [[FRPH]] | [[Baker John D. III]] | $930 | 10 | -0.2% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "proven_insider")
SORT filed DESC
```

Back to [[What Works]].
