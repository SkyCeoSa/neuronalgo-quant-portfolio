# Smart Money Concept Backtester (SMC Backtester)

A modular rule-based backtester demonstrating Smart Money Concepts (SMC) indicators.

## Contents
- `backtest.py` — sample rule engine (smoke test)
- `sample_data.csv` — toy dataset for quick verification
- `indicators/` — custom indicator modules
- `strategy_card.md` — one-page summary template

## Quick run
```bash
python backtest.py --quick
Outputs:

daily_returns.csv

equity_curve.csv

Production checklist
Use point-in-time vendor data

Add slippage & transaction cost models

Add liquidity and capacity constraints

Document sensitivity and parameter ranges