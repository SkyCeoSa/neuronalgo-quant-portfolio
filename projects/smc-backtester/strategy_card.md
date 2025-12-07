# Strategy Card — Smart Money Concept Backtester (smc_1)

Brief: Rule-based SMC concept using short MA vs long MA as a proxy for smart-money directional bias. Modular indicator layer for adding Orderflow/Imbalance.

Universe: Single-symbol demo (extendable to multi-asset)

Backtest window: toy sample (use full data for production)

Key metrics (placeholder after run):
- CAGR: __REPLACE_ME__
- Volatility: __REPLACE_ME__
- Sharpe: __REPLACE_ME__
- Max Drawdown: __REPLACE_ME__

Risk Controls:
- Maximum position size per trade
- Daily loss limit
- Slippage model applied to execution during live

Roadmap:
- Add FVG detection module
- Implement BO/CHOCH detection
- Add transaction cost model per venue
