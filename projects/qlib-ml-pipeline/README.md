# Qlib ML Pipeline (Colab-ready)

**هدف:** نشان دادن یک جریان کاری کامل ML روی داده‌های مالی با استفاده از Qlib (یا نسخه light-weight مشابه) در محیط Google Colab یا محلی.

## چه چیزی داخل این فولدر هست
- notebook_instructions.md — توضیح گام‌به‌گام برای Colab
- example_notebook_cells.md — نمونه سلول‌های نوت‌بوک برای اجرا
- results/ — نمودارها و خروجی‌ها (اضافه کن بعد از اجرا)
- roadmap.md — کارهای بعدی

## اجرا در Colab (خلاصه)
1. باز کن Google Colab و یک نوت‌بوک جدید بساز.
2. سلول اول: نصب وابستگی‌ها (نمونه در example_notebook_cells.md)
3. لود دیتاست نمونه یا متصل شدن به دیتای خودتان
4. اجرا pipeline: feature engineering → train → validate → export results
5. خروجی‌ها (equity curve، confusion matrix، feature importance) را در `results/` آپلود کن.

## نوت‌بوک نمونه: نکات
- حتما point-in-time data handling را رعایت کن (snapshot، no-lookahead)
- از cross-validation زمانی (time-series CV) استفاده کن
- نتایج را به‌صورت HTML (nbconvert) خروجی بگیر و در GitHub Actions آپلود کن
