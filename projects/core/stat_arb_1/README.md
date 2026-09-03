# Stat-Arb Metrics Demo

This directory contains a small deterministic **research plumbing demo**. It reads the tracked `sample_data.csv` price fixture, converts prices to simple daily returns, and reports descriptive metrics.

Despite the historical directory name, the public code does **not** implement pair discovery, cointegration testing, spread construction, transaction costs, order management, or live execution. It should therefore not be treated as a validated statistical-arbitrage strategy.

## Run

From the repository root:

```bash
python projects/core/stat_arb_1/backtest.py
```

The command prints JSON and writes nothing by default. To save review artifacts explicitly:

```bash
python projects/core/stat_arb_1/backtest.py --output-dir /tmp/neuronalgo-stat-arb-demo
```

Generated output contains only derived fixture returns and metrics and is ignored when written under an `outputs/` directory.

## Evidence boundary

The tracked CSV is a tiny public fixture used for deterministic code review. Metrics computed from it are not performance evidence for a live system and do not predict future returns.
