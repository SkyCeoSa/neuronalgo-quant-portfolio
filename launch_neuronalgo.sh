#!/usr/bin/env bash
set -e

ROOT="$(pwd)"
echo "Creating NeuronAlgo scaffold in $ROOT"

# create basic folders
mkdir -p {projects/core/stat_arb_1,projects/core/vol_model_1,projects/core/ml_returns_1,projects/satellite,projects/experimental,notebooks,scripts,papers,linkedin_posts,outreach,data,proof/statements,proof/certificates,.github/workflows}

# .gitignore for data
cat > data/.gitignore <<'GIT'
*
!.gitignore
GIT

# README placeholder
cat > README.md <<'MD'
# NeuronAlgo — Portfolio (Scaffold)
__REPLACE_ME_README__
MD

# ONE-PAGER placeholder
cat > ONE-PAGER.md <<'MD'
# NeuronAlgo — One Pager
__REPLACE_ME_ONE_PAGER__
MD

# sample strategy card
cat > projects/core/stat_arb_1/strategy_card.md <<'MD'
# StrategyCard — Stat-Arb 1
__REPLACE_ME_STRATEGY_CARD__
MD

# sample backtest script
cat > projects/core/stat_arb_1/backtest.py <<'PY'
#!/usr/bin/env python3
"""
Quick smoke backtest for CI. Usage:
python backtest.py --quick
"""
import pandas as pd
import numpy as np
import argparse, os

def simple_strategy(df):
    df['ma'] = df['price'].rolling(3,min_periods=1).mean()
    df['pos'] = (df['price'] < df['ma']).astype(int)
    df['ret'] = df['price'].pct_change().fillna(0)
    df['strat_ret'] = df['pos'].shift(1) * df['ret']
    return df

def ann_stats(r, periods=252):
    r = r.dropna()
    if len(r)==0:
        return {'CAGR':0,'Vol':0,'Sharpe':0,'MaxDD':0}
    cumul = (1+r).prod()
    years = len(r)/periods
    cagr = cumul**(1/years)-1 if years>0 else 0
    vol = r.std()*np.sqrt(periods)
    sharpe = cagr/vol if vol>0 else 0
    dd = (1+r).cumprod()
    drawdown = dd.cummax() - dd
    return {'CAGR':cagr,'Vol':vol,'Sharpe':sharpe,'MaxDD':drawdown.max()}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--quick', action='store_true')
    args = p.parse_args()
    data_path = os.path.join(os.path.dirname(__file__),'sample_data.csv')
    if not os.path.exists(data_path):
        # create tiny synthetic
        df = pd.DataFrame({'date':pd.date_range('2024-11-01', periods=10, freq='B'),
                           'price':100 + np.cumsum(np.random.randn(10))})
        df.to_csv(data_path, index=False)
    df = pd.read_csv(data_path, parse_dates=['date'])
    df = simple_strategy(df)
    s = ann_stats(df['strat_ret'])
    print('Stats:', s)
    df[['date','strat_ret']].to_csv(os.path.join(os.path.dirname(__file__),'daily_returns.csv'), index=False)

if __name__=='__main__':
    main()
PY
chmod +x projects/core/stat_arb_1/backtest.py

# sample data
cat > projects/core/stat_arb_1/sample_data.csv <<'CSV'
date,price
2024-11-01,100
2024-11-04,101
2024-11-05,100.5
2024-11-06,102
2024-11-07,101.5
CSV

# scripts: aggregate_metrics.py
cat > scripts/aggregate_metrics.py <<'PY'
#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys, argparse
def ann_stats(returns, periods=252):
    r = returns.dropna()
    if len(r)==0:
        return {}
    cumul = (1+r).prod()
    years = len(r)/periods
    cagr = cumul**(1/years)-1 if years>0 else 0
    vol = r.std()*np.sqrt(periods)
    sharpe = cagr/vol if vol>0 else 0
    dd = (1+r).cumprod()
    drawdown = dd.cummax() - dd
    return {'CAGR':cagr,'Vol':vol,'Sharpe':sharpe,'MaxDD':drawdown.max()}
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', default='projects/core/stat_arb_1/daily_returns.csv')
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    res = ann_stats(df.iloc[:,1])
    print(res)
PY
chmod +x scripts/aggregate_metrics.py

# GitHub Actions validate.yml (basic)
cat > .github/workflows/validate.yml <<'YML'
name: Validate & Build

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install pandas numpy jupyter nbconvert pytest
      - name: Run quick backtest
        working-directory: projects/core/stat_arb_1
        run: python backtest.py --quick || true
      - name: Convert notebooks
        run: |
          mkdir -p html-output
          jupyter nbconvert --to html notebooks/*.ipynb --output-dir=html-output || true
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: research-artifacts
          path: html-output
YML

# linkedin & outreach templates
cat > linkedin_posts/hero.md <<'MD'
NeuronAlgo — productized, risk-governed quant modules for incubators & prop-desks (Dubai/Oman).

We present Core (investable), Satellite (enhancers), and Experimental (research) modules. DM or email founder@__REPLACE_ME__ for pilot terms.
MD

cat > outreach/dm_accelerator.md <<'MD'
Hi [Name],
I'm Sadegh, founder of NeuronAlgo... (short template)
MD

echo "Scaffold created."
