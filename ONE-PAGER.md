# NeuronAlgo Quant Research Portfolio — One Page

## Purpose

This public repository is a sanitized technical portfolio for reviewers, collaborators, incubators, sponsors, and potential research partners. It shows small reproducible examples of NeuronAlgo's research and software-engineering approach without publishing private production systems or live-account data.

NeuronAlgo develops algorithmic-trading software, research tooling, and software licenses. It is not providing portfolio management through this repository, and no code, backtest, simulation, or metric here guarantees profit or predicts future performance.

## What reviewers can reproduce

- Two deterministic price-to-return backtest/metrics demos using tracked CSV fixtures.
- A seeded toy RL-style environment with deterministic episode results.
- A lightweight aggregate-metrics utility for explicitly generated local demo outputs.
- An optional, output-free Qlib notebook that documents its separate local-data requirement.
- A dependency manifest, smoke-test suite, and GitHub Actions workflow for the lightweight public surface.

## Evidence boundary

This repository does **not** contain NeuronAlgo's production WordPress implementation, private Core services, parser or execution code, live-account integrations, raw financial-provider exports, credentials, account identifiers, broker statements, trade tickets, model weights, or private operational logs.

The examples are research artifacts. A toy demo is not a complete strategy; a simulation is not live trading; a backtest is not forward performance; and this repository contains no production trading deployment.

## Review path

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .
python -m unittest discover -s tests -v
python projects/core/stat_arb_1/backtest.py
python projects/smc-backtester/backtest.py
python projects/rl-research-platform/example_agent.py
```

## Public references

- [NeuronAlgo website](https://neuronalgo.com/)
- [Public Proof page](https://neuronalgo.com/proof/)
- [Founder LinkedIn](https://www.linkedin.com/in/massah)

Public technical questions and collaboration proposals are welcome through GitHub Issues. Private introductions can use the founder's LinkedIn profile.
