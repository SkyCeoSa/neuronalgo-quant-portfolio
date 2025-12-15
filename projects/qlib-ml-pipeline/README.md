QLIB_NA_WORKFLOW — Complete Qlib ML + Backtest Pipeline

This repository contains a full, production-ready workflow for building, training, and backtesting quantitative trading models using Microsoft Qlib.
The notebook is designed to run 100% in Google Colab, with automated setup, workflow generation, MLflow tracking, and backtesting.

🚀 Features
✅ 1. Automated Environment Setup

Clean installation of Qlib

Build extensions

Version validation

Colab-friendly paths

✅ 2. Modular Workflow Configuration

Uses fully configurable YAML-driven structure including:

Market settings

Dataset + Handler

Model configuration

Training parameters

Forecast horizon

Backtest configuration

This makes the notebook suitable for production ML pipelines or research workflows.

✅ 3. Dataset Handling

Auto-download

Initialization of Qlib data

Automatic directory structure

✅ 4. Model Training + MLflow Tracking

Saves experiment logs

Saves model artifacts

Tracks metrics (IC, IR, etc.)

Reproducible workflow generation

✅ 5. Full Backtest Engine

Integrated backtest includes:

Predict → Trade pipeline

Portfolio metrics

Plotting and visualization

Automatic report storage

✅ 6. Ready for Deployment

Outputs include:

Workflow YAML

Model weights

Predictions

Backtest results

Performance charts

📂 Project Structure
QLIB_NA_WORKFLOW.ipynb
├── workflows/
│   ├── config.yaml
│   ├── model/
│   └── dataset/
├── mlflow/
│   └── runs/
├── results/
│   ├── predictions/
│   ├── backtest/
│   └── metrics/
└── README.md

▶️ How to Run (Colab)

Upload notebook

Run cell #1 (Setup)

Set your custom paths (optional)

Generate workflow

Train model

Backtest & evaluate results

📊 Outputs

This workflow automatically generates:

predictions.pkl

train_log.txt

backtest_report.json

Equity & drawdown charts

MLflow experiment logs

Workflow config files

✨ Who Is This For?

This project is ideal for:

Quant researchers

Algo traders

ML engineers entering finance

Students building trading portfolios

Anyone building ML workflows with Qlib

📜 License

MIT 

📧 Contact

For collaboration or professional inquiries:
NeuronAlgo Research
(https://www.linkedin.com/in/massah)
