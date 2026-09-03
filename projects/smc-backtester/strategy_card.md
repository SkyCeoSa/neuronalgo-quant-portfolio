# Research Card — SMC Direction

**Public maturity:** design note + deterministic metrics smoke test  
**Current data:** tracked miniature price fixture  
**Implemented SMC signal logic:** none  
**Live execution:** none

## Research hypothesis

A future public research experiment could formalize selected market-structure concepts—such as swing structure, displacement, liquidity events, or imbalance definitions—into deterministic rules that can be tested without discretionary chart interpretation.

That hypothesis is **not** implemented by the current `backtest.py`. The current script exists to make fixture loading, return derivation, metric computation, and CI behavior reproducible.

## Evidence required before stronger claims

A substantive SMC study would need precise event definitions, timestamp-safe market data, transaction-cost assumptions, leakage controls, train/test separation where parameters are learned, sensitivity analysis, and out-of-sample evaluation. Any partner-facing claim must point to those artifacts directly.

## Risk statement

A backtest, even when fully implemented, would remain historical evidence with limitations. It would not guarantee or predict future returns.
