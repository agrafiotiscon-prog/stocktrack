---
type: findings
updated: 2026-10-20
backtest: 2026-10-20
---

# Findings: does following insider buys work?

*Written 2026-10-20 from the run-2 backtest (397,834 purchase filings, 2006 to September 2026) after an
adversarial code review. The generated numbers are in [[What Works]] and [[2026-10-20 Backtest]]. This
note is the interpretation. It isn't regenerated, so update it by hand when the evidence changes.*

## The short answer

**Insider buys carry real information, but copying them hasn't beaten the S&P 500 since 2016 once you pay
trading costs.**

1. **There is an edge relative to similar stocks.** In the 3 months after an insider buy is filed, the
   stock beats an index of comparable surviving stocks by about **+2.7% a year**. That holds in both
   2006-2015 and 2016+ (t ≈ 3 in each) and in 17 of 21 years.
2. **Against the S&P 500 it has faded.** +7.9% a year in 2006-2015 (p 0.006), +1.0% since 2016 (p 0.78).
   Most of the difference is that small stocks as a group badly trailed the large-cap S&P 500 in the last
   decade, and insider buys are mostly in small stocks.
3. **Much of the move happens before you can act.** Between the insider's trade and the first open after
   the filing, the stock is already up about **+1.3%** on average.
4. **A typical insider buy loses to the market.** The *average* is pulled up by a few big winners. The
   *median* stock trails SPY by 0.9% over 3 months, and only 47% beat it.
5. **After costs, real portfolios roughly tie SPY with far more risk.** A $100K account holding up to 20
   positions earned 5-12% a year against SPY's 11%, with 50-74% drawdowns. Costs take about 3% a year.
   Hedging out small caps (short IWM) leaves at best +2-4% a year with low Sharpe ratios.
6. **Survivorship flatters all of this.** Free price data only covers companies still listed today: about
   half of all insider buys can't be priced. If those did like a typical priced buy, the average 3-month
   result drops from +0.9% to -0.1%.

## What works best (the strongest leads)

Ranked by how consistent the evidence is, not by the size of the number:

| Lead | Edge vs comparable stocks | Consistency | Status |
|---|---|---|---|
| **CFO buys** | +8.4%/yr | 18 of 21 years; beats the typical insider buy (Holm p 0.01) | best lead; on the [[Findings#Open experiments\|forward test]] |
| **Other executives (not CEO)** | +6.0%/yr | 19 of 21 years; beats the typical buy (Holm p 0.02) | strong lead; on the forward test |
| **3+ insiders buying within 14 days** | +6.1%/yr | 19 of 21 years | good, not significant after correction |
| **Buying after a 30%+ run-up** | +14.3%/yr | 16 of 21 years, very volatile | intriguing, the opposite of "buy the dip" |
| **Live score 60+** | +4.5%/yr | 14 of 21 years | the best portfolio after hedging (+3.6%/yr) |

CFOs know the numbers best, and the data agrees. CEO buys are only middling (+4.1%/yr, 15 of 21 years),
perhaps because CEOs also buy to signal confidence.

## What doesn't work

- **Buying the dip** (after a 30%+ drop): looks great on averages (+4.2% per trade) thanks to a few penny-stock
  rebounds, but the portfolio test shows no edge and a 74% drawdown.
- **Routine insiders** (buying in the same month every year): about -3% a year vs comparable stocks, which
  matches the academic finding that routine trades carry no information.
- **Owners filing as "Other"** (neither officer, director nor 10% owner): -4.6% a year, positive in only 6 of
  21 years, and significantly worse than the typical buy.
- **Copying every insider buy:** -2.8% a year once hedged, after costs.
- **Big-ticket buys ($1M+)** are no better than small ones. **New positions** aren't either.
- **Past winners:** an insider's earlier good record didn't reliably predict their next buy.
- **Dividend-reinvestment and plan purchases:** no edge (expected; they aren't decisions).

## How much to trust this

- **Strict verdict: nothing earned ✅.** The pre-registered rule needs a Holm-corrected win against SPY
  in *both* decades, and nothing passed. The leads above come from comparisons against similar stocks and
  against the typical insider buy, which are fairer but weren't the pre-registered headline.
- **The leads were found by looking at this data**, so this data can't confirm them. They are written down in
  `data/backtest/hypotheses.json` and will be judged only on new buys in the forward test.
- Prices exist only for survivors; the adjustment is for market beta only (no size/value factors); trading
  costs are assumed, not measured.
- An independent code review found about 30 issues, including data parsing, look-ahead in benchmarks, and
  statistics. All were fixed before run 2 (see `data/backtest/CHANGES.md`). The headline barely moved, which
  is reassuring.

## Open experiments

The daily routine logs every qualifying new buy to `data/picks.csv` before its outcome exists, then tracks
it for a year. These need roughly 100 matured 3-month outcomes each, so expect answers from early 2027:

- [[CFO or other non-CEO executive buying $25K+ (post-hoc)]]: does the CFO/executive edge hold out of sample?
- [[Insider buying after a 30%+ run-up (post-hoc)]]: is the run-up effect real or noise?
- Do "Other"-role and routine buys keep lagging?
- Does the live score's 60+ bucket keep beating its 0-39 bucket?

Ideas not yet tested: a size-matched benchmark (market cap); short the Russell 2000 only when the market is
falling; combining CFO and cluster signals; delisted-stock prices from a paid data source to remove the
survivorship bias.

## The bottom line for a trader

Treat an insider buy as **one useful clue, not a trade signal**. The clues worth weighting are a CFO or
other executive buying, several insiders buying together, and buying into strength. The ones to discount
are routine buyers, "Other" filers, and dip-buying in penny stocks. None of this beats an index fund after
costs on its own. *This is research, not investment advice.*
