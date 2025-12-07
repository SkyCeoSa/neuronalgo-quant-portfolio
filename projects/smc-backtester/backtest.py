#!/usr/bin/env python3
# Simple SMC-style rule-based backtest (smoke test)
import pandas as pd
import numpy as np
import argparse, os

def load_data(path='sample_data.csv'):
    df = pd.read_csv(path, parse_dates=['date']).sort_values('date')
    return df

def smc_indicator(df):
    # dummy SMC-like signal: price vs short MA crossover + volatility filter
    df['ma5'] = df['price'].rolling(5,min_periods=1).mean()
    df['ma20'] = df['price'].rolling(20,min_periods=1).mean()
    df['signal'] = 0
    df.loc[df['ma5'] > df['ma20'], 'signal'] = 1
    df.loc[df['ma5'] < df['ma20'], 'signal'] = -1
    return df

def simple_exec(df):
    df['ret'] = df['price'].pct_change().fillna(0)
    df['strat_ret'] = df['signal'].shift(1) * df['ret']
    return df

def ann_stats(r, periods=252):
    r = r.dropna()
    if len(r)==0:
        return {}
    cumul = (1+r).prod()
    years = len(r)/periods
    cagr = cumul**(1/years)-1 if years>0 else 0
    vol = r.std()*np.sqrt(periods)
    sharpe = cagr/vol if vol>0 else 0
    dd = (1+r).cumprod()
    drawdown = dd.cummax() - dd
    return {'CAGR':cagr, 'Vol':vol, 'Sharpe':sharpe, 'MaxDD':drawdown.max()}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='sample_data.csv')
    parser.add_argument('--quick', action='store_true')
    args = parser.parse_args()

    if not os.path.exists(args.data):
        # create toy sample
        dates = pd.date_range('2024-11-01', periods=60, freq='B')
        prices = 100 + np.cumsum(np.random.randn(len(dates)))
        pd.DataFrame({'date':dates, 'price':prices}).to_csv(args.data, index=False)

    df = load_data(args.data)
    df = smc_indicator(df)
    df = simple_exec(df)
    metrics = ann_stats(df['strat_ret'])
    print("Backtest metrics:", metrics)
    df[['date','strat_ret']].to_csv('daily_returns.csv', index=False)
    # save equity curve for quick visual (optional)
    df['cum_strat'] = (1+df['strat_ret']).cumprod()
    df[['date','cum_strat']].to_csv('equity_curve.csv', index=False)

if __name__ == '__main__':
    main()
