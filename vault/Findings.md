---
type: findings
updated: 2026-10-21
backtest: 2026-10-21
---

# Findings: does following insider buys work?

*Written 2026-10-21 from the run-4 backtest (394,831 purchase filings, 2006 to September 2026) after three rounds of
adversarial code review. The generated numbers are in [[What Works]] and [[2026-10-21 Backtest]]. This note is the
interpretation. It isn't regenerated, so update it by hand when the evidence changes.*

## The short answer

**Insider buys carry real information, but copying them hasn't beaten the S&P 500 since 2016 once you pay
trading costs.**

1. **There is an edge relative to similar stocks.** In the 3 months after an insider buy is filed, the stock
   beats an index of comparable surviving stocks by about **+5.6% a year**. That holds in both 2006-2015 (+5.7%,
   t 3.8) and 2016+ (+5.5%, t 4.5), and in 19 of 21 years (2007 and 2021 were negative).
2. **Against the S&P 500 it has faded.** +7.9% a year in 2006-2015 (p 0.006), +1.1% since 2016 (p 0.77).
   The gap between the two comparisons is mostly the size effect: insider buys are mostly in small stocks, and
   small stocks badly trailed the large-cap S&P 500 in the last decade.
3. **Much of the move happens before you can act.** Between the insider's trade and the first open after the
   filing, the stock is already up about **+1.3%** on average.
4. **A typical insider buy loses to the market.** The *average* is pulled up by a few big winners. The *median*
   stock trails SPY by 0.9% over 3 months, and only 47% beat it. Even against comparable stocks only 49% win.
5. **After costs, real portfolios roughly tie SPY with far more risk.** A $100K account holding up to 20 positions
   earned 2-12% a year for the pre-registered strategies against SPY's 11%, with 49-74% drawdowns. Costs take about
   3% a year. Hedging out small caps (short IWM) leaves at best about +3.5% a year with low Sharpe ratios (0.2).
6. **Survivorship flatters all of this.** Free price data only covers companies still listed today: about half of
   all insider buys can't be priced. If those did like a typical priced buy, the average 3-month result drops from
   +0.9% to -0.1%.
7. **The same stocks a year later don't do this.** Over the same kind of 3-month window a year after the buy, the
   stocks trailed SPY by 0.4%, so the post-buy result is +1.0% to +1.3% better than the stock's own normal.

## What works best (the strongest leads)

Ranked by how consistent the evidence is, not by the size of the number:

| Lead | Edge vs comparable stocks | Consistency | Status |
|---|---|---|---|
| **CFO buys** | +11.5%/yr | 19 of 21 years, all 11 since 2016; beats the typical buy by +5.6%/yr (Holm p 0.01) | best lead; on the [[Findings#Open experiments\|forward test]] |
| **Other executives (not CEO)** | +8.8%/yr | 20 of 21 years; beats the typical buy by +3.2%/yr (Holm p 0.02) | strong lead; on the forward test |
| **3+ insiders buying within 14 days** | +9.1%/yr | 19 of 21 years | good, not significant vs the typical buy after correction |
| **Buying after a 30%+ run-up** | +17.5%/yr | 17 of 21 years, very volatile | intriguing, the opposite of "buy the dip"; on the forward test |
| **Live score 60+** | +6.3%/yr | 17 of 21 years | the best pre-registered portfolio after hedging (+3.5%/yr) |

CFOs know the numbers best, and the data agrees. CEO buys are only middling (+7.1%/yr against comparable stocks,
which is no better than the typical buy at +5.6%; 15 of 21 years), perhaps because CEOs also buy to signal
confidence.

## What doesn't work

- **Buying the dip** (after a 30%+ drop): looks fine on averages thanks to a few penny-stock rebounds, but it isn't
  significant against comparable stocks (p 0.12), and the portfolio test shows no edge and a 74% drawdown.
- **Owners filing as "Other"** (neither officer, director nor 10% owner): -1.7% a year against comparable stocks,
  positive in only 8 of 21 years, and 7.2% a year worse than the typical buy (Holm p 0.02).
- **Routine insiders** (buying in the same month every year): -0.4% a year against comparable stocks, about 6% a
  year worse than the typical buy (not significant after correction). This matches the academic finding that
  routine trades carry no information.
- **Copying every insider buy:** -2.7% a year once hedged, after costs.
- **Big-ticket buys ($1M+)** are no better than small ones. **New positions** aren't either.
- **Past winners:** an insider's earlier good record didn't predict their next buy (+0.0% vs the typical buy).
- **Dividend-reinvestment and plan purchases:** no edge beyond the typical buy (expected; they aren't decisions).

## How much to trust this

- **Strict verdict: nothing earned ✅.** The pre-registered rule needs a Holm-corrected win against SPY in *both*
  decades, and nothing passed. The leads above come from comparisons against similar stocks and against the typical
  insider buy, which are fairer but weren't the pre-registered headline.
- **The leads were found by looking at this data**, so this data can't confirm them. They are written down in
  `data/backtest/hypotheses.json` and will be judged only on new buys in the forward test.
- Prices exist only for survivors; the adjustment is for market beta only (no size/value factors); trading costs
  are assumed, not measured.
- **Three independent code reviews** found more than 50 issues in data parsing, look-ahead, the comparison index
  and statistics. All were fixed, and each run is logged in `data/backtest/CHANGES.md`. The edge against SPY barely
  moved through all of it (+4.3% a year). The edge against comparable stocks moved as the comparison index was
  corrected: +2.7% (run 2), +6.4% (run 3), +5.6% (run 4). Run 4 uses the stricter of two reasonable conventions
  for the overnight reaction to a filing, so treat the edge as roughly +5-6% a year.

## Open experiments

The daily routine logs every qualifying new buy to `data/picks.csv` before its outcome exists, then tracks it for a
year. Insiders buying the same company on the same day count once. These need roughly 100 matured 3-month outcomes
each, so expect answers from early-to-mid 2027:

- [[CFO or other non-CEO executive buying $25K+ (post-hoc)]]: does the CFO/executive edge hold out of sample?
- [[Insider buying after a 30%+ run-up (post-hoc)]]: is the run-up effect real or noise?
- Do "Other"-role and routine buys keep lagging?
- Does the live score's 60+ bucket keep beating its 0-39 bucket?

Ideas not yet tested: a size-matched benchmark (market cap); short the Russell 2000 only when the market is falling;
combining CFO and cluster signals; delisted-stock prices from a paid data source to remove the survivorship bias.

## The bottom line for a trader

Treat an insider buy as **one useful clue, not a trade signal**. The clues worth weighting are a CFO or other
executive buying, several insiders buying together, and buying into strength. The ones to discount are routine
buyers, "Other" filers, and dip-buying in penny stocks. None of this beats an index fund after costs on its own.
*This is research, not investment advice.*
