# 💎 CreditIQ — AI-Powered Credit Risk Assessment & Underwriting Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.3+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-v2.0+-eb5424)](https://xgboost.readthedocs.io/)
[![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-success)](https://shap.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Enterprise-grade Machine Learning system for automated Probability of Default (PD) scoring, Explainable AI (XAI) risk attribution, and portfolio underwriting analytics.**

---

## 📌 Executive Summary & Business Impact

Credit risk assessment is a foundational pillar of banking and fintech operations. Inaccurate default prediction directly inflates Non-Performing Assets (NPAs), while opaque "black-box" models violate regulatory compliance frameworks (**Basel II/III, FCRA, ECOA**).

**CreditIQ** bridges the gap between high-accuracy predictive modeling and regulatory explainability:
- **Reduces Credit Underwriting Latency** by providing instant Probability of Default (PD) scoring.
- **Ensures Model Transparency** via individual-level **SHAP (SHapley Additive exPlanations)** waterfall attributions, pinpointing the exact factors driving credit approval or rejection.
- **Empowers Applicants** through an automated **What-If Sensitivity Engine** that identifies actionable steps to improve creditworthiness.
- **Scales Enterprise Operations** with high-throughput batch CSV scoring and portfolio risk distribution analytics.

---

## 🚀 Live Demo & Quick Launch

- **Live Streamlit Cloud Demo**: [Launch CreditIQ on Streamlit Cloud](https://share.streamlit.io/)
- **Repository**: [github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System](https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System)

---

## 📊 Model Performance & Benchmarking

Four candidate architectures were trained and evaluated on 150,000+ historical lending records from the *Give Me Some Credit* dataset, with **SMOTE (Synthetic Minority Over-sampling Technique)** applied to address severe class imbalance (~6.7% baseline default rate):

| Model Architecture | AUC-ROC | Accuracy | Precision | Recall | F1-Score | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Random Forest (Regularized)** | **0.8438** | **94.59%** | **0.5829** | **0.6577** | **0.6181** | 🏆 **Production Primary** |
| **Gradient Boosting Classifier** | 0.8421 | 78.89% | 0.2037 | 0.7459 | 0.3200 | Candidate |
| **XGBoost Classifier** | 0.8280 | 82.42% | 0.2189 | 0.6389 | 0.3261 | Candidate |
| **Logistic Regression (Baseline)** | 0.7988 | 78.41% | 0.1867 | 0.6684 | 0.2919 | Baseline |

> **Key Takeaway**: The regularized Random Forest model delivers superior discrimination (**0.8438 AUC-ROC**) with optimal precision-recall balance for real-world risk management.

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
│ Streamlit Cloud UI     │ <── │ Explainable AI Engine  │ <── │ Trained Ensembles      │
│ • Real-time Scoring    │     │ • SHAP TreeExplainer   │     │ • Random Forest        │
│ • What-If Simulator    │     │ • Waterfall Plots      │     │ • XGBoost / GBDT       │
│ • Batch CSV Underwrite │     │ • Feature Importance   │     │ • StandardScaler       │
└────────────────────────┘     └────────────────────────┘     └────────────────────────┘
```

---

## ✨ Key Platform Features

### 1. 🎯 Real-Time Underwriting & Probability of Default
- Interactive multi-factor input sidebar covering demographics, income, revolving credit utilization, open loans, real estate lines, and delinquency history (30-59, 60-89, 90+ days past due).
- Instant multi-tier risk classification:
  - 🟢 **MINIMAL Risk** (0–20% Default Prob) → *Full Auto-Approval*
  - 🟡 **LOW Risk** (20–40% Default Prob) → *Standard Approval*
  - 🟠 **MODERATE Risk** (40–60% Default Prob) → *Manual Review Required*
  - 🔴 **HIGH Risk** (60–80% Default Prob) → *Advisory Rejection*
  - 🚨 **CRITICAL Risk** (80–100% Default Prob) → *Immediate Denial*

### 2. 🔍 Explainable AI (XAI) via SHAP Waterfall
- Transparent, per-applicant feature attribution showing which variables drove the score up or down.
- Meets adverse action explanation requirements under lending regulations.

### 3. 🧪 Interactive What-If Scenario Engine
- Simulates counterfactual adjustments (e.g. paying down credit card utilization to 20% or clearing late payments).
- Ranks recommendations by predicted percentage-point risk reduction.

### 4. 📁 Batch Portfolio Underwriting & Analytics
- Upload bulk applicant CSV datasets for instant enterprise-scale assessment.
- Interactive Plotly portfolio risk distribution visualization and one-click annotated CSV export.

### 5. 💾 Compliance Audit Trail & Historical Decision Log
- Persistent logging of credit assessments with timestamps, metrics, and underwriting decisions.
- Exportable audit trail for risk reporting and quality assurance.

---

## 🛠️ Tech Stack & ATS Keywords

- **Core Language**: Python 3.10+
- **Machine Learning**: Scikit-Learn, XGBoost, Ensemble Learning, Random Forest, Gradient Boosting, Logistic Regression, SMOTE (`imbalanced-learn`)
- **Model Explainability & XAI**: SHAP (SHapley Additive exPlanations), TreeExplainer, Waterfall Attribution Plots
- **Data Engineering & Analysis**: Pandas, NumPy, Feature Engineering, Outlier Treatment, Missing Value Imputation
- **Data Visualization**: Plotly Graph Objects, Matplotlib, Seaborn
- **Application & Cloud Deployment**: Streamlit, Streamlit Cloud, Git LFS Optimization

---

## 💼 ATS-Optimized Resume Bullet Points

> *Feel free to copy-paste these high-impact bullet points into your resume:*

- **AI Credit Risk Assessment & Underwriting System (CreditIQ) | Machine Learning & Streamlit**
  - Engineered an end-to-end credit risk assessment system on 150,000+ historical lending records, developing an ensemble Random Forest model achieving **0.844 AUC-ROC** and **94.6% accuracy**.
  - Implemented **SMOTE** to resolve severe class imbalance (6.7% default rate) and engineered custom solvency features (*IncomePerDependent*, *TotalLatePayments*) improving predictive recall to 65.8%.
  - Integrated **Explainable AI (XAI)** using **SHAP TreeExplainer** to generate waterfall attribution plots, ensuring model transparency and compliance with lending regulations (FCRA/ECOA).
  - Built an interactive **Streamlit** dashboard featuring real-time risk classification, a counterfactual **What-If simulation engine**, batch portfolio CSV underwriting, and audit logging.
  - Optimized model serialization and memory footprint from 419MB to **6.5MB**, enabling sub-second inference and zero-latency deployment on Streamlit Cloud.

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

4. **Launch the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```
   *The application will open automatically at `http://localhost:8501`.*

---

## ☁️ Deploying to Streamlit Cloud (Step-by-Step)

1. Fork or push this repository to your GitHub account: `https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System`
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with your GitHub account.
3. Click **"New app"** (or **"Create app"**).
4. Configure the deployment settings:
   - **Repository**: `abhishekkaware007/AI-Credit-Risk-Assessment-System`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py` (or `app.py`)
5. Click **"Deploy!"** — Streamlit will automatically install `requirements.txt` and launch your live web application in seconds.

---

## 👤 Author & Contact

**Abhishek Kaware**
- **GitHub**: [@abhishekkaware007](https://github.com/abhishekkaware007)
- **Project Repository**: [AI-Credit-Risk-Assessment-System](https://github.com/abhishekkaware007/AI-Credit-Risk-Assessment-System)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
