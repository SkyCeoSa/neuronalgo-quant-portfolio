# Seeded RL-Style Research Toy

This directory contains a deterministic toy environment and policy loop. It exists to demonstrate reproducible state transitions and experiment plumbing; it is not a trained trading agent or a market simulator.

## Run

```bash
python projects/rl-research-platform/example_agent.py
```

The script uses an explicit NumPy random generator seed, runs a simple deterministic policy against synthetic state transitions, and prints a JSON episode summary. Re-running with the same seed produces the same result.

No market data, network service, broker account, credential, model weight, or live execution path is used.

## Evidence boundary

Synthetic rewards are implementation-test values, not financial returns. A future RL trading study would require a well-defined environment, leakage-safe historical data, transaction costs, baseline comparisons, train/validation/test separation, stability checks across seeds, and operational controls before any stronger claim could be supported.
