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
