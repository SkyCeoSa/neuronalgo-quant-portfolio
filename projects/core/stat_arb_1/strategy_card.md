# Research Card — Stat-Arb Metrics Demo

**Public maturity:** toy backtest / metrics plumbing  
**Data:** tracked `sample_data.csv` price fixture  
**Execution:** none  
**Live-account integration:** none

## Current evidence

The public script deterministically converts the fixture's positive `price` series to simple returns and reports observation count, mean daily return, daily volatility, positive-return rate, an annualized mean/volatility ratio, and maximum drawdown of the derived equity curve.

These metrics validate only that the public calculation is reproducible. They do not establish that a statistical-arbitrage hypothesis is valid, profitable, robust, or suitable for deployment.

## What a real stat-arb research claim would additionally require

- an explicit universe and pair-selection rule;
- stationarity/cointegration methodology and multiple-testing controls;
- train/validation/test separation;
- transaction-cost, slippage, borrow, and capacity assumptions;
- parameter-sensitivity and regime analysis;
- out-of-sample or forward evidence;
- execution and operational risk controls for any production claim.

None of those requirements should be inferred from this toy fixture.

## Risk statement

Historical or simulated calculations do not predict future performance. This repository provides software/research examples, not portfolio management or guaranteed returns.
