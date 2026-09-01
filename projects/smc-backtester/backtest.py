"""Deterministic public metrics demo for the SMC research directory.

The current public code does not implement Smart Money Concepts trading logic.
It provides a reproducible price-to-return calculation used by smoke tests and
writes nothing unless ``--output-dir`` is supplied.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd

ANNUALIZATION = 252.0
DEFAULT_INPUT = Path(__file__).with_name("sample_data.csv")


def load_returns(path: Path) -> np.ndarray:
    """Load finite returns from a CSV containing ``ret`` or positive ``price``."""
    if not path.is_file():
        raise FileNotFoundError(f"Input fixture not found: {path}")

    frame = pd.read_csv(path)
    if "ret" in frame.columns:
        series = pd.to_numeric(frame["ret"], errors="coerce")
    elif "price" in frame.columns:
        prices = pd.to_numeric(frame["price"], errors="coerce")
        if prices.isna().any() or (prices <= 0).any():
            raise ValueError("price values must be finite positive numbers")
        series = prices.pct_change().dropna()
    else:
        raise ValueError("input CSV must contain a 'ret' or 'price' column")

    returns = series.dropna().to_numpy(dtype=float)
    if returns.size < 2:
        raise ValueError("at least two return observations are required")
    if not np.isfinite(returns).all():
        raise ValueError("returns must be finite")
    if (returns <= -1.0).any():
        raise ValueError("simple returns must be greater than -1.0")
    return returns


def compute_metrics(returns: Sequence[float]) -> dict[str, float | int]:
    """Compute deterministic descriptive metrics for a simple return series."""
    values = np.asarray(returns, dtype=float)
    if values.ndim != 1 or values.size < 2 or not np.isfinite(values).all():
        raise ValueError("returns must be a one-dimensional finite series with at least two values")
    if (values <= -1.0).any():
        raise ValueError("simple returns must be greater than -1.0")

    mean = float(np.mean(values))
    vol = float(np.std(values, ddof=1))
    hit_rate = float(np.mean(values > 0.0))
    sharpe = 0.0 if vol == 0.0 else mean / vol * float(np.sqrt(ANNUALIZATION))

    equity = np.cumprod(1.0 + values)
    running_peak = np.maximum.accumulate(equity)
    max_drawdown = float(np.min(equity / running_peak - 1.0))

    return {
        "n": int(values.size),
        "mean": mean,
        "vol": vol,
        "hit_rate": hit_rate,
        "sharpe_annual": sharpe,
        "max_drawdown": max_drawdown,
    }


def write_outputs(output_dir: Path, returns: np.ndarray, metrics: dict[str, float | int]) -> None:
    """Write derived review artifacts only when the caller explicitly opts in."""
    output_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"ret": returns}).to_csv(output_dir / "daily_returns.csv", index=False)
    (output_dir / "metrics.json").write_text(
        json.dumps(metrics, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="CSV containing ret or price")
    parser.add_argument("--output-dir", type=Path, help="optional directory for derived CSV/JSON output")
    args = parser.parse_args(argv)

    returns = load_returns(args.input)
    metrics = compute_metrics(returns)
    if args.output_dir is not None:
        write_outputs(args.output_dir, returns, metrics)

    print(json.dumps(metrics, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
