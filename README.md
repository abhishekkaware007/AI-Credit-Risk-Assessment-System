# 💎 CreditIQ — AI-Powered Credit Risk Assessment & Underwriting Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.3+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-v2.0+-eb5424)](https://xgboost.readthedocs.io/)
[![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-success)](https://shap.readthedocs.io/)

CreditIQ is an end-to-end Machine Learning web platform designed to evaluate loan applicant default risk in real time, generate interpretable risk factor attributions via Explainable AI (XAI), simulate counterfactual credit improvement pathways, and process bulk underwriting portfolios.

---

## 📌 Project Overview

Credit risk modeling is essential for financial institutions to assess borrower solvency, mitigate default losses, and maintain underwriting consistency. CreditIQ provides an automated underwriting intelligence dashboard powered by ensemble learning and model explainability frameworks:

- **Automated Default Probability Scoring**: Calculates applicant Probability of Default (PD) and assigns structured risk tiers (*Minimal, Low, Moderate, High, Critical*).
- **Explainable AI (XAI)**: Leverages SHAP (SHapley Additive exPlanations) waterfall plots to provide granular transparency into why a specific risk score was produced.
- **Counterfactual What-If Engine**: Identifies specific financial adjustments (such as reducing revolving utilization or clearing overdue accounts) to lower default probability.
- **Batch Underwriting**: Supports bulk CSV applicant scoring, aggregate risk metrics, and downloadable portfolio reports.
- **Audit Trail Logging**: Stores assessment history with timestamps and financial snapshots for compliance tracking.

---

## 🚀 Live Demo & Repository

- **Live Application**: [Launch CreditIQ on Streamlit Cloud](https://creditiq-risk.streamlit.app/)
- **GitHub Repository**: [abhishekkaware007/AI-Credit-Risk-Assessment-System](https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System)

---

## 📊 Model Evaluation & Benchmarks

Four machine learning architectures were trained on 150,000+ historical lending records from the *Give Me Some Credit* dataset. Class imbalance (~6.7% default rate) was handled using **SMOTE (Synthetic Minority Over-sampling Technique)**:

| Model Architecture | AUC-ROC | Accuracy | Precision | Recall | F1-Score | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Random Forest (Regularized)** | **0.8438** | **94.59%** | **0.5829** | **0.6577** | **0.6181** | 🏆 **Production Model** |
| **Gradient Boosting Classifier** | 0.8421 | 78.89% | 0.2037 | 0.7459 | 0.3200 | Candidate |
| **XGBoost Classifier** | 0.8280 | 82.42% | 0.2189 | 0.6389 | 0.3261 | Candidate |
| **Logistic Regression** | 0.7988 | 78.41% | 0.1867 | 0.6684 | 0.2919 | Baseline |

---

## 🏗️ System Architecture & ML Pipeline

```text
┌────────────────────────┐     ┌────────────────────────┐     ┌────────────────────────┐
│  Raw Lending Data      │ ──> │ Feature Engineering    │ ──> │ Class Balancing        │
│  (150,000+ Records)    │     │ • TotalLatePayments    │     │ • SMOTE Resampling     │
│                        │     │ • IncomePerDependent   │     │ • Outlier Filtering    │
└────────────────────────┘     └────────────────────────┘     └────────────────────────┘
                                                                           │
                                                                           ▼
┌────────────────────────┐     ┌────────────────────────┐     ┌────────────────────────┐
│ Streamlit UI           │ <── │ Explainable AI Engine  │ <── │ Trained Ensembles      │
│ • Real-time Scoring    │     │ • SHAP TreeExplainer   │     │ • Random Forest        │
│ • What-If Simulator    │     │ • Waterfall Plots      │     │ • XGBoost / GBDT       │
│ • Batch Underwriting   │     │ • Feature Importance   │     │ • StandardScaler       │
└────────────────────────┘     └────────────────────────┘     └────────────────────────┘
```

---

## ✨ Key Features

### 1. Real-Time Applicant Underwriting
- Multi-parameter inputs: Age, Monthly Income, Debt Ratio, Credit Card Utilization, Open Loans, Real Estate Loans, and Delinquency History (30-59, 60-89, 90+ days past due).
- Automated categorization:
  - 🟢 **MINIMAL Risk** (0–20% Default Prob) → Recommend Full Approval
  - 🟡 **LOW Risk** (20–40% Default Prob) → Standard Approval & Review
  - 🟠 **MODERATE Risk** (40–60% Default Prob) → Enhanced Review / Collateral Required
  - 🔴 **HIGH Risk** (60–80% Default Prob) → Reject Under Standard Terms
  - 🚨 **CRITICAL Risk** (80–100% Default Prob) → Immediate Denial

### 2. SHAP Feature Attribution (Explainable AI)
- Generates individual waterfall attribution charts demonstrating the exact directional contribution of each feature to the final prediction.

### 3. What-If Scenario Simulator
- Evaluates hypothetical improvements to the applicant's financial profile and ranks recommendations by predicted risk reduction percentage points.

### 4. Batch Processing & Portfolio Distribution
- Accepts CSV uploads of applicant datasets for instant scoring.
- Displays risk distribution charts across portfolio tiers with downloadable result exports.

### 5. Audit Logging & Export
- Logs applicant assessments with timestamps, inputs, and risk decisions.
- Supports historical viewing and one-click CSV export.

---

## 📁 Repository Structure

```text
AI-Credit-Risk-Assessment-System/
├── GiveMeSomeCredit/
│   ├── 01_EDA.ipynb               # Exploratory data analysis
│   ├── 02_preprocessing.ipynb      # Data cleaning & feature engineering
│   ├── 03_model_training.ipynb     # Model training with SMOTE
│   ├── 04_evaluation.ipynb         # Evaluation & ROC-AUC comparison
│   ├── cs-training.csv            # Training dataset
│   ├── cs-test.csv                # Test dataset
│   ├── app.py                     # Streamlit application
│   └── requirements.txt           # Subdirectory dependencies
├── models/
│   ├── random_forest.pkl          # Primary production model
│   ├── xgboost.pkl                # XGBoost model artifact
│   ├── gradient_boosting.pkl      # Gradient boosting model artifact
│   ├── logistic_regression.pkl    # Logistic regression baseline
│   ├── scaler.pkl                 # Feature standard scaler
│   └── evaluation_results.csv     # Model metric comparison summary
├── streamlit_app.py               # Root deployment entrypoint
├── app.py                         # Root execution alias
├── requirements.txt               # Production dependencies
└── README.md                      # Project documentation
```

---

## 🛠️ Tech Stack

- **Programming Language**: Python 3.10+
- **Machine Learning**: Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE)
- **Model Explainability**: SHAP (TreeExplainer)
- **Data Manipulation**: Pandas, NumPy
- **Visualizations**: Plotly, Matplotlib, Seaborn
- **Application Framework**: Streamlit

---

## 💻 Local Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System.git
   cd AI-Credit-Risk-Assessment-System
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**:
   ```bash
   streamlit run streamlit_app.py
   ```
   *The app will be accessible locally at `http://localhost:8501`.*

---

## ☁️ Deployment on Streamlit Community Cloud

1. Push or fork this repository to your GitHub account.
2. Sign in to **[share.streamlit.io](https://share.streamlit.io)** using your GitHub credentials.
3. Click **"New app"** and enter the following configuration:
   - **Repository**: `abhishekkaware007/AI-Credit-Risk-Assessment-System`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
4. Click **"Deploy!"**.

---

## 👤 Author

**Abhishek Kaware**
- **GitHub**: [@abhishekkaware007](https://github.com/abhishekkaware007)
- **Repository**: [AI-Credit-Risk-Assessment-System](https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System)
