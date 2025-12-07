# Example notebook cells (copy into Colab / Jupyter)

## Cell 1 — نصب وابستگی‌ها (Colab)
!pip install qlib pandas numpy scikit-learn lightgbm matplotlib

## Cell 2 — آماده‌سازی محیط و لود داده (نمونه)
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
# نمونه بارگذاری CSV:
df = pd.read_csv('/content/data/sample_prices.csv', parse_dates=['date']).set_index('date')
df.head()

## Cell 3 — feature engineering ساده
df['ret'] = df['close'].pct_change()
df['mom_5'] = df['close'].pct_change(5)
df['vol_10'] = df['ret'].rolling(10).std()

## Cell 4 — تقسیم زمانی و آموزش مدل
from lightgbm import LGBMRegressor
tscv = TimeSeriesSplit(n_splits=5)
X = df[['mom_5','vol_10']].dropna()
y = df['ret'].shift(-1).loc[X.index]
model = LGBMRegressor()
model.fit(X.iloc[:-200], y.iloc[:-200])

## Cell 5 — ارزیابی و خروجی نمودار
pred = model.predict(X.iloc[-200:])
(df['close'].iloc[-200:] / df['close'].iloc[-200:].iloc[0]).plot()
