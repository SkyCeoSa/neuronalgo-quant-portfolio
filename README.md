# NeuronAlgo Quant Research Portfolio

Public, sanitized research demos and engineering notes from [NeuronAlgo](https://neuronalgo.com/).

NeuronAlgo develops algorithmic-trading software, research tooling, and software licenses. This repository is a curated public portfolio for technical review and collaboration. It is **not** NeuronAlgo's production trading infrastructure, does not provide portfolio management, and does not guarantee profit. Backtests and simulations here are historical or synthetic research artifacts; they do not predict future performance.

## What is in this repository

| Area | Evidence level | What it demonstrates | What it does not demonstrate |
| --- | --- | --- | --- |
| `projects/core/stat_arb_1/` | Deterministic toy backtest | Loading a tracked price fixture, deriving returns, and computing descriptive performance metrics | Pair selection, statistical-arbitrage validation, execution, or production readiness |
| `projects/smc-backtester/` | Deterministic toy backtest | A second reproducible return-series metrics example used as a public engineering smoke test | A complete Smart Money Concepts engine, live signals, or broker execution |
| `projects/rl-research-platform/` | Seeded simulation | A deterministic toy environment and policy loop suitable for testing research plumbing | A trained trading agent, market simulator, or deployable RL system |
| `projects/qlib-ml-pipeline/` | Optional exploratory notebook | A minimal, output-free Qlib environment/data-access workflow | Bundled market data, model weights, validated alpha, or production deployment |
| `projects/open-source-customizations/` | Design notes | Boundaries for future public integrations with open-source research tools | Bundled third-party code or completed integrations |
| `scripts/aggregate_metrics.py` | Utility | Reading explicitly generated demo metrics and rendering a local Markdown summary | A production reporting service |

The public [Proof page](https://neuronalgo.com/proof/) is separate evidence about NeuronAlgo and is not reproduced as raw account data in this repository.

## Repository map

```text
.
├── AGENTS.md                         # contributor/agent operating contract
├── README.md                         # repository overview and quick start
├── ONE-PAGER.md                      # concise public project summary
├── CONTRIBUTING.md                   # contribution and evidence rules
├── CODE_OF_CONDUCT.md                # collaboration standards
├── pyproject.toml                    # base dependencies + optional Qlib extra
├── launch_neuronalgo.sh              # safe local development bootstrap/check helper
├── projects/
│   ├── core/stat_arb_1/              # deterministic price-to-return metrics demo
│   ├── smc-backtester/               # deterministic public metrics demo
│   ├── rl-research-platform/         # seeded toy RL-style environment
│   ├── qlib-ml-pipeline/              # optional Qlib notebook and research notes
│   └── open-source-customizations/    # public design notes only
├── scripts/aggregate_metrics.py
├── tests/test_public_portfolio.py
└── .github/workflows/ci.yml
```

## Quick start

Requirements: Python 3.10+ and, for the helper script, Bash.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .

python projects/core/stat_arb_1/backtest.py
python projects/smc-backtester/backtest.py
python projects/rl-research-platform/example_agent.py
python -m unittest discover -s tests -v
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1` before running the Python commands.

The two backtest commands read the tracked `sample_data.csv` fixtures and print JSON to stdout. They do **not** write into the repository unless an output directory is explicitly requested, for example:

```bash
python projects/core/stat_arb_1/backtest.py --output-dir /tmp/neuronalgo-stat-arb-demo
```

`launch_neuronalgo.sh` is a convenience bootstrapper, not a trading launcher and not a repository generator. It only creates `.venv` when missing, installs declared dependencies, and optionally runs public checks:

```bash
./launch_neuronalgo.sh --check
```

It never creates proof data, credentials, market datasets, or production configuration.

## Dependencies

The base environment intentionally stays small:

- NumPy
- pandas

Install from the repository manifest:

```bash
python -m pip install .
```

Qlib is heavyweight and optional. To inspect the Qlib notebook locally:

```bash
python -m pip install ".[qlib]"
```

The repository does not bundle Qlib datasets. Configure a local Qlib dataset separately using the upstream Qlib documentation; large datasets, model weights, notebook outputs, and local caches must stay outside version control.

## Reproducibility and evidence boundaries

The public examples use four evidence categories deliberately:

1. **Toy demo** — small code intended to make one implementation idea inspectable. It is not a complete strategy.
2. **Simulation** — generated state transitions under explicit deterministic seeds. Simulated rewards are not market returns.
3. **Backtest example** — a deterministic calculation over tracked historical-style fixture data. It demonstrates code behavior, not future profitability.
4. **Production system** — operational software with deployment, monitoring, security, execution, and integration controls. **No production trading system is published in this repository.**

To keep public evidence reproducible:

- base smoke tests require no network access, live accounts, API keys, or production credentials;
- random fallback data is not used by the quick backtests;
- generated outputs are opt-in and ignored by Git;
- the Qlib notebook is stored without executed outputs and requires separately obtained local data;
- any metric shown by a demo is descriptive of its supplied fixture or simulation only.

Private NeuronAlgo WordPress code, Core services, parsers, execution/integration code, account identifiers, broker credentials, statements, trade tickets, raw provider data, private URLs, and operational logs are intentionally absent.

## Validation

The public CI runs the same lightweight checks a reviewer can run locally:

```bash
python -m pip install .
python -m unittest discover -s tests -v
python -m compileall -q projects scripts tests
bash -n launch_neuronalgo.sh
python projects/core/stat_arb_1/backtest.py
python projects/smc-backtester/backtest.py
python projects/rl-research-platform/example_agent.py
```

The test suite also checks public Markdown links/structure, placeholder removal, unsupported deployment wording, notebook output hygiene, deterministic fixtures, and obvious hard-coded secret assignments.

## Public links and collaboration

- Website: [neuronalgo.com](https://neuronalgo.com/)
- Public Proof page: [neuronalgo.com/proof/](https://neuronalgo.com/proof/)
- Founder LinkedIn: [linkedin.com/in/massah](https://www.linkedin.com/in/massah)

For public technical questions or collaboration proposals, open a GitHub issue. For a private introduction, use the founder's LinkedIn profile above. No email address is published or invented here.

## License

This repository is licensed under the [MIT License](LICENSE). Third-party datasets, libraries, and code retain their own licenses and are not relicensed by this repository.
