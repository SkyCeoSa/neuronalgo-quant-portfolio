# AGENTS.md

## Repository purpose

`neuronalgo-quant-portfolio` is a public, sanitized research and engineering portfolio. It exists to make a small set of NeuronAlgo research examples reproducible and reviewable without exposing private production systems.

NeuronAlgo develops algorithmic-trading software, research tooling, and software licenses. This repository is not portfolio management, does not provide trade execution, and must not imply guaranteed or predictive returns.

## Technology stack

- Python 3.10+
- NumPy and pandas for lightweight public demos
- `unittest` from the Python standard library for smoke/contract tests
- Bash for the optional local bootstrap/check helper
- Jupyter notebook JSON for one optional Qlib example
- Qlib (`pyqlib`) as an optional heavyweight research dependency only
- GitHub Actions for public CI

## Setup

Base environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .
```

Optional Qlib environment:

```bash
python -m pip install ".[qlib]"
```

Qlib datasets are external local research inputs and are never committed.

## Validation commands

Run before proposing changes:

```bash
python -m unittest discover -s tests -v
python -m compileall -q projects scripts tests
bash -n launch_neuronalgo.sh
python projects/core/stat_arb_1/backtest.py
python projects/smc-backtester/backtest.py
python projects/rl-research-platform/example_agent.py
```

Base tests and smoke demos must work without network access, credentials, live accounts, or production services.

## Architecture

- `projects/core/stat_arb_1/`: deterministic price-fixture metrics demo; not a complete stat-arb implementation.
- `projects/smc-backtester/`: deterministic return-series metrics demo; not a complete SMC implementation.
- `projects/rl-research-platform/`: seeded toy environment/policy loop.
- `projects/qlib-ml-pipeline/`: optional Qlib notebook and research notes; no bundled data or model artifacts.
- `projects/open-source-customizations/`: design notes only; no bundled third-party implementation.
- `scripts/`: public-safe local utilities.
- `tests/`: deterministic smoke, content-hygiene, link, notebook, and secret-assignment checks.
- `.github/workflows/`: lightweight public CI.

## Conventions

1. Prefer deterministic fixtures and explicit seeds. Never silently replace missing data with random data.
2. Demo commands are read-only by default. Generated output requires an explicit destination and must remain ignored.
3. Label evidence accurately: toy demo, simulation, backtest, or production system are not interchangeable terms.
4. A backtest or simulation must not be described as a prediction or guarantee of future performance.
5. Keep base dependencies minimal; use optional groups for heavyweight research tools.
6. Keep notebooks committed without outputs, credentials, large data, model weights, or user-specific absolute paths.
7. Do not add third-party code unless its license and attribution are compatible with the repository's MIT license.

## Protected/private areas

Never copy or reconstruct any private NeuronAlgo production material here, including:

- WordPress theme/plugin implementation details beyond public website links;
- private Core/service code or parser implementation;
- live-account, broker, execution, licensing, entitlement, or credential integrations;
- account identifiers, statements, trade tickets, raw provider exports, private URLs, or unsanitized logs;
- credentials, secrets, tokens, private keys, or environment values;
- proprietary datasets, generated HTML reports, model weights, or private evidence bundles.

The public Proof page may be linked, but its raw underlying account/provider data must not be copied into this repository.

## Environment variables

The base repository requires **no environment variables**. Do not introduce production credential variable names merely for examples. If a future public-only integration genuinely requires configuration, document variable names only and provide no values or production endpoints.

## Git workflow

- Branch from the current `main`.
- Keep PRs focused on public research/readiness concerns.
- Preserve unrelated content and the MIT license.
- Use draft PRs while validation or review is incomplete.
- Do not merge, deploy, publish financial evidence, or mutate production systems from this repository workflow.
