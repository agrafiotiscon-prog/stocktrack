---
type: "strategy"
key: "big_stake_up"
signals: 11413
cagr: 0.0892515
spy_cagr: 0.107784
sharpe: 0.388164
max_drawdown: 0.669115
holdout_excess: 0.0172159
---

# Exec/director growing stake 25%+ with $100K+

Rule key: `big_stake_up`. Liquid stocks only ($2+, $1M+/day), plan purchases excluded.

## Backtest

| Measure | Value |
|---|---|
| Signals | 11,413 |
| 3-month excess vs SPY (mean / median) | +0.8% / -0.5% |
| Beat SPY over 3 months | 48% |
| Entering one session later | +0.5% |
| vs surviving stocks | +1.1% |
| 2006-2015 excess /yr | +6.3% (p 0.035) |
| 2016+ excess /yr | +1.7% (p 0.668) |


## Simulated portfolio ($100K, 20 slots, after costs)

| Hold | CAGR | SPY | Sharpe | SPY Sharpe | Max DD | Beta | Alpha/yr | Years beating SPY | Trades | Costs/yr | Hedged with IWM (CAGR / Sharpe / Max DD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21d | +3.6% | +10.8% | 0.20 | 0.54 | 54% | 1.05 | -6.1% | 19% | 4,269 | 6.3% | -2.2% / -0.26 / 52% |
| 63d | +8.9% | +10.8% | 0.39 | 0.54 | 67% | 1.29 | -2.8% | 52% | 1,657 | 2.7% | +0.8% / -0.00 / 36% |
| 126d | +7.6% | +10.8% | 0.34 | 0.54 | 66% | 1.26 | -3.8% | 48% | 840 | 1.3% | -0.2% / -0.08 / 47% |


*Hedged* shorts the Russell 2000 ETF (IWM) against the invested fraction each day: what's left is the edge over small caps in general. Exploratory (borrow costs ignored).


Cost sensitivity (63-session hold): no costs +11.6%/yr, double costs +6.2%/yr.


### Year by year (63-session hold)

| Year | Strategy | SPY | Difference |
|---|---|---|---|
| 2006 | +14.2% | +13.8% | +0.3% |
| 2007 | -5.6% | +5.1% | -10.8% |
| 2008 | -43.3% | -36.8% | -6.5% |
| 2009 | +57.3% | +26.4% | +30.9% |
| 2010 | +35.2% | +15.1% | +20.1% |
| 2011 | +3.3% | +1.9% | +1.4% |
| 2012 | +17.9% | +16.0% | +1.9% |
| 2013 | +50.3% | +32.3% | +17.9% |
| 2014 | +17.2% | +13.5% | +3.8% |
| 2015 | -6.5% | +1.2% | -7.7% |
| 2016 | +17.1% | +12.0% | +5.1% |
| 2017 | +17.5% | +21.7% | -4.2% |
| 2018 | -16.8% | -4.6% | -12.2% |
| 2019 | +48.2% | +31.2% | +16.9% |
| 2020 | +21.5% | +18.3% | +3.2% |
| 2021 | -6.3% | +28.7% | -35.1% |
| 2022 | -16.6% | -18.2% | +1.6% |
| 2023 | +20.4% | +26.2% | -5.8% |
| 2024 | +5.8% | +24.9% | -19.1% |
| 2025 | +11.7% | +17.7% | -6.0% |
| 2026 | -0.6% | +8.2% | -8.9% |


## Live forward test

| Horizon | Matured | Mean vs SPY | Median | Beat SPY |
|---|---|---|---|---|
| 5 sessions | 77 | +0.1% | +0.1% | 53% |
| 21 sessions | 5 | -3.1% | -3.3% | 20% |


### Latest live signals

| Filed | Ticker | Insider | Value | Score | vs SPY so far | Status |
|---|---|---|---|---|---|---|
| 2026-11-20 | [[UPST]] | [[Gu Paul]] | $860K | 76 | – | pending |
| 2026-11-20 | [[HBCP]] | [[Hill Darren M]] | $315K | 53 | – | pending |
| 2026-11-20 | [[TJX]] | [[PINTOFF CRAIG ADAM]] | $200K | 45 | – | pending |
| 2026-11-20 | [[UPBD]] | [[LEWIS HAROLD G]] | $399K | 73 | – | pending |
| 2026-11-20 | [[AVEX]] | [[Morrison Christine M]] | $102K | 43 | – | pending |
| 2026-11-20 | [[OFRM]] | [[Morris Scott James]] | $142K | 69 | – | pending |
| 2026-11-20 | [[INOD]] | [[Massey Stewart R]] | $321K | 47 | – | pending |
| 2026-11-20 | [[ANNX]] | [[Carson William H]] | $122K | 26 | – | pending |
| 2026-11-20 | [[GLXY]] | [[Novogratz Michael]] | $4.9M | 84 | – | pending |
| 2026-11-20 | [[MED]] | [[Kiai Parsa]] | $1.1M | 53 | – | pending |
| 2026-11-20 | [[BHRB]] | [[Poillon Diane]] | $106K | 39 | – | pending |
| 2026-11-20 | [[PICS]] | [[Pruett William Rodney]] | $233K | 56 | – | pending |
| 2026-11-20 | [[PICS]] | [[Teixeira Linares Marcio Antonio]] | $299K | 59 | – | pending |
| 2026-11-19 | [[RMIX]] | [[HEYER ANDREW R]] | $183K | 70 | -4.1% | open |
| 2026-11-19 | [[CCB]] | [[HOVDE STEVEN D]] | $550K | 49 | +1.8% | open |
| 2026-11-19 | [[IRTC]] | [[TALWALKAR ABHIJIT Y]] | $764K | 51 | +2.8% | open |
| 2026-11-19 | [[BGS]] | [[Mills Robert D]] | $250K | 54 | +4.4% | open |
| 2026-11-19 | [[PLD]] | [[KELLY ALFRED F JR]] | $587K | 50 | +2.4% | open |
| 2026-11-19 | [[APC]] | [[HEYER ANDREW R]] | $279K | 46 | +4.1% | open |
| 2026-11-19 | [[BCML]] | [[PERDUE MICHAEL J]] | $151K | 44 | +1.5% | open |


```dataview
TABLE ticker, insider, score, abn_now AS "vs SPY so far", status
FROM "Signals"
WHERE contains(strategies, "big_stake_up")
SORT filed DESC
```

Back to [[What Works]].
