# Strategy Card — ML Returns (ml_returns_1)

Brief: Ensemble ML model (LightGBM + small NN) predicting 1-day ahead returns using price/momentum/macro/sentiment features.

Universe: Highly liquid ETFs & futures (example: SPY, ES futures)

Backtest window: 2005-01-01 → 2024-12-31 (placeholder)

Live status: Model training pipeline tested in Colab; LLM-sentiment pipe running since 2025-11 (experimental)

Key metrics (placeholder):
- CAGR: 14.0%
- Volatility: 12.0%
- Sharpe: 1.17
- Max Drawdown: -16.2%

Risk controls:
- Confidence threshold for trades
- Volatility targeting
- Daily P&L stop and kill-switch

Notes:
Replace placeholder metrics with results from `scripts/aggregate_metrics.py` after you run backtests and aggregate daily returns.
