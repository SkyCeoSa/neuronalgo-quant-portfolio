# Contributing

Thanks for considering a contribution to the NeuronAlgo Quant Research Portfolio. This repository is deliberately small and public: contributions should improve reproducibility, research clarity, or public-safe engineering evidence without importing private production material.

## Appropriate contributions

Good contributions include:

- deterministic research examples and tests;
- corrections to methodology or documentation;
- small public-safe utilities;
- reproducibility improvements;
- evidence-bound wording and clearer limitations;
- fixes to CI, dependency declarations, or local setup.

Please do not add production trading integrations, broker/account connectivity, private NeuronAlgo code, credentials, raw statements, trade tickets, private URLs, unsanitized logs, proprietary datasets, generated notebook outputs, model weights, or third-party code without compatible attribution and licensing.

## Set up the base environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .
```

Qlib is optional and is not part of the base smoke-test path:

```bash
python -m pip install ".[qlib]"
```

Qlib market data must be configured locally and must not be committed.

## Validate before opening a PR

```bash
python -m unittest discover -s tests -v
python -m compileall -q projects scripts tests
bash -n launch_neuronalgo.sh
python projects/core/stat_arb_1/backtest.py
python projects/smc-backtester/backtest.py
python projects/rl-research-platform/example_agent.py
```

The smoke demos should not create tracked files. If a demo needs generated output, require an explicit output directory and keep it ignored by Git.

## Research and financial claims

Use precise evidence labels. State whether a result is a toy example, simulation, backtest, or externally verified public evidence. Do not describe a component as deployable or production software unless the repository itself contains the operational controls and validation supporting that statement.

Backtests and simulations must include limitations and must never be presented as predictions or guarantees of future profit. NeuronAlgo develops algorithmic-trading software, research, and licenses; this repository is not a portfolio-management service.

## Dependencies and code style

- Keep base dependencies minimal.
- Put heavyweight research tooling in optional dependency groups when practical.
- Do not invent version pins without a compatibility reason supported by the repository.
- Prefer deterministic inputs and explicit seeds.
- Keep base tests offline and independent of credentials or live accounts.
- Use clear Python type hints/docstrings where they improve reviewability.

## Pull requests

Use a focused feature branch from `main`. Explain what changed, what evidence supports the change, and which validation commands were run. Keep generated artifacts and unrelated refactors out of the PR.

## Security and private information

Do not post secrets or private account information in an issue or pull request. If you discover a security issue that requires sensitive details, use GitHub's private security-reporting mechanism if it is available for the repository. Otherwise contact the repository owner privately through the [founder LinkedIn profile](https://www.linkedin.com/in/massah) before disclosing sensitive material publicly.
