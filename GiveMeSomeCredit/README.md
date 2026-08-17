# CreditIQ — AI-Powered Credit Risk Assessment System

This directory contains the machine learning analysis notebooks, training datasets, and Streamlit application for the CreditIQ credit risk assessment platform.

## Directory Contents

- `01_EDA.ipynb`: Exploratory data analysis, distributions, and correlation analysis.
- `02_preprocessing.ipynb`: Data cleaning, outlier handling, and feature engineering.
- `03_model_training.ipynb`: Multi-model training (Random Forest, XGBoost, Gradient Boosting, Logistic Regression) with SMOTE class balancing.
- `04_evaluation.ipynb`: Comprehensive model evaluation, ROC-AUC curves, confusion matrices, and feature importance.
- `app.py`: Streamlit dashboard implementation.
- `cs-training.csv`, `cs-test.csv`, `sampleEntry.csv`: Lending dataset files.
- `requirements.txt`: Subdirectory Python dependencies.

## Running Locally

```bash
streamlit run app.py
```
