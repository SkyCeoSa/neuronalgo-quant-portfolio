# Research Card — Qlib ML Workflow

**Public maturity:** optional exploratory notebook  
**Bundled dataset:** none  
**Bundled trained model:** none  
**Production deployment:** outside repository scope

## Research question

Can Qlib provide a reproducible public framework for future factor/model experiments once an explicit public dataset and protocol are selected?

The current notebook establishes only environment initialization and local dataset access. It intentionally does not publish a performance result.

## Evidence required for a model study

Before reporting an ML strategy result, record at minimum:

- dataset source/version and instrument universe;
- feature and label definitions;
- train/validation/test dates;
- model class and hyperparameters;
- random seeds where relevant;
- transaction costs and execution assumptions;
- baseline comparisons;
- IC/return/drawdown metrics with definitions;
- sensitivity and out-of-sample checks.

Numerical targets can be useful as research gates, but a target is not an observed result. Do not turn aspirational thresholds into claims.

## Risk statement

ML backtests are vulnerable to leakage, multiple testing, regime dependence, cost assumptions, and overfitting. Historical results do not predict or guarantee future returns.
