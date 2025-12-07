# Smart Money Concept Backtester (SMC Backtester)

هدف: پلتفرم بک‌تست قانون‌محور بر اساس سیگنال‌های Smart Money (FVG, BOS/CHOCH, Orderflow indicators) که به‌صورت ماژولار قابل توسعه است.

فایل‌های مهم:
- backtest.py — اسکریپت نمونه اجرا
- sample_data.csv — دادهٔ نمونه برای تست سریع
- indicators/ — پیاده‌سازی اندیکاتورها (پوشه)
- example.ipynb — نوت‌بوک راهنما
- results/ — خروجی‌های بک‌تست (equity curves, metrics)
- strategy_card.md — کارت استراتژی

نحوه اجرا (محلی):
1. نصب dependencies: `pip install -r ../../requirements.txt`
2. اجرا سریع: `python backtest.py --quick`
3. خروجی daily_returns.csv در همان پوشه تولید می‌شود؛ سپس `scripts/aggregate_metrics.py` را اجرا کن.
