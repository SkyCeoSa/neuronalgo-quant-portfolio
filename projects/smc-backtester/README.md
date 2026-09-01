# SMC Research Metrics Demo

This public directory is a deterministic **metrics smoke test** plus design notes for possible Smart Money Concepts research. The current Python file does not implement order blocks, liquidity sweeps, imbalance detection, entries, exits, position sizing, or broker execution.

The tracked `sample_data.csv` contains a tiny `date,price` fixture. The script converts those prices to simple returns and computes descriptive metrics so reviewers can reproduce code behavior without network access or random fallback data.

## Run

```bash
python projects/smc-backtester/backtest.py
```

The default command prints JSON only. Generated review artifacts are opt-in:

```bash
python projects/smc-backtester/backtest.py --output-dir /tmp/neuronalgo-smc-demo
```

## Interpretation

The directory name describes a research direction, not completed evidence. The current output must not be described as an SMC strategy result, a live signal, or a production trading system. Metrics from this fixture do not predict future performance.
