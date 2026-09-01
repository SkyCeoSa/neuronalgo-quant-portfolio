# Qlib Notebook Companion Notes

These snippets explain the sanitized notebook. They are **not** part of the base CI path because Qlib is optional and meaningful runs require a separately configured local dataset.

## Initialize from local data

```python
from pathlib import Path

import qlib
from qlib.config import REG_CN

provider_uri = Path.home() / ".qlib" / "qlib_data" / "cn_data"
if not provider_uri.exists():
    raise FileNotFoundError(
        "Qlib dataset not found. Follow the upstream Qlib data setup and keep datasets outside this repository."
    )

qlib.init(provider_uri=str(provider_uri), region=REG_CN)
```

The notebook deliberately does not download data, call a private endpoint, or read credentials.

## Before adding a model experiment

A reproducible experiment should state the dataset/version, universe, feature expressions, labels, exact time splits, costs, model parameters, seeds, baselines, and metric definitions. Store only small aggregate outputs when they are needed for review; do not commit raw datasets, model weights, or executed notebook output.

Any reported backtest would remain historical research evidence, not a forecast or guarantee of future performance.
