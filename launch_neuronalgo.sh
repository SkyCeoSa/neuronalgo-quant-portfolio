#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

WITH_QLIB=0
RUN_CHECKS=0

usage() {
  cat <<'EOF'
Usage: ./launch_neuronalgo.sh [--with-qlib] [--check]

Safe local development bootstrap for the public research portfolio.

  --with-qlib  Also install the optional pyqlib dependency group.
  --check      Run the deterministic public validation commands after setup.
  -h, --help   Show this help text.

The script creates .venv only when it does not already exist. It never overwrites
tracked repository files and never creates credentials, proof data, market data,
or production configuration.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-qlib)
      WITH_QLIB=1
      ;;
    --check)
      RUN_CHECKS=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

PYTHON_BIN="${PYTHON:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "Python executable not found: $PYTHON_BIN" >&2
  exit 1
fi

if [[ ! -d .venv ]]; then
  "$PYTHON_BIN" -m venv .venv
fi

if [[ -x .venv/bin/python ]]; then
  VENV_PYTHON=".venv/bin/python"
elif [[ -x .venv/Scripts/python.exe ]]; then
  VENV_PYTHON=".venv/Scripts/python.exe"
else
  echo "Unable to find the Python executable inside .venv" >&2
  exit 1
fi

"$VENV_PYTHON" -m pip install .

if [[ "$WITH_QLIB" -eq 1 ]]; then
  "$VENV_PYTHON" -m pip install ".[qlib]"
  echo "Qlib installed. Configure a local Qlib dataset separately; datasets are not bundled here."
fi

if [[ "$RUN_CHECKS" -eq 1 ]]; then
  "$VENV_PYTHON" -m unittest discover -s tests -v
  "$VENV_PYTHON" -m compileall -q projects scripts tests
  bash -n "$0"
  "$VENV_PYTHON" projects/core/stat_arb_1/backtest.py
  "$VENV_PYTHON" projects/smc-backtester/backtest.py
  "$VENV_PYTHON" projects/rl-research-platform/example_agent.py
fi

echo "Public research environment is ready in .venv."
