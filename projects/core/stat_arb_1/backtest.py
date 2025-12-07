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
