# Optional Qlib Research Notebook

This directory contains a small **exploratory** notebook for reviewers who already have a local [Qlib](https://github.com/microsoft/qlib) environment and dataset. It is not a deployed ML service, a validated alpha model, or a production trading pipeline.

## Install the optional dependency

From the repository root:

```bash
python -m pip install ".[qlib]"
```

Qlib datasets are intentionally not bundled. Configure a local dataset using Qlib's upstream documentation and keep downloaded data outside this repository. The sanitized notebook checks for a conventional local data directory and fails with a clear message if the data is absent; it does not download data automatically.

## Notebook hygiene

`notebooks/QLIB_NA_WORKFLOW.ipynb` is committed with:

- no executed outputs;
- no credentials, tokens, account identifiers, or private URLs;
- no model weights or generated reports;
- no bundled market data;
- an explicit local-data prerequisite.

The base GitHub Actions job does not install Qlib because it is a heavyweight optional tool and a meaningful Qlib run requires separately prepared market data. Base CI instead validates the notebook JSON and its output-free state.

## Evidence boundary

A working Qlib environment only demonstrates research tooling. Any future model-performance claim would need an identified dataset, exact split rules, feature definitions, labels, transaction-cost assumptions, hyperparameters, baselines, out-of-sample evaluation, and reproducibility metadata. A backtest cannot guarantee or predict future returns.
