# AI Credit Risk Assessment

This repository contains the `GiveMeSomeCredit` project: a credit risk assessment demo with EDA, preprocessing, model training, and a small app.

## Structure

- `01_EDA.ipynb` — exploratory data analysis
- `02_preprocessing.ipynb` — data cleaning and feature engineering
- `03_model_training.ipynb` — model training and saving
- `04_evaluation.ipynb` — model evaluation and results
- `app.py` — minimal app to serve model predictions (run with `python app.py`)
- `cs-training.csv`, `cs-test.csv`, `sampleEntry.csv` — example datasets
- `models/` — saved model artifacts and `evaluation_results.csv`

## Quickstart

1. Create and activate a virtual environment (recommended):

   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies. If there is no `requirements.txt`, install common packages used by this project:

   pip install -U pip
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter

3. Open the notebooks with Jupyter:

   jupyter notebook

4. Run the app (if `app.py` exists and is configured):

   python app.py

## Deploy to Streamlit Cloud

1. Push your repository to GitHub (branch `main`).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "New app", select the repository `abhishekkaware007/AI-Credit-Risk-Assessment-System`, branch `main`, and set the main file path to `GiveMeSomeCredit/app.py`.
4. Ensure a `requirements.txt` file exists at `GiveMeSomeCredit/requirements.txt` (this repo includes one).
5. If your models are large, either track them with Git LFS or host them externally and download at runtime (recommended). Streamlit Cloud may not fetch very large files directly from Git.
6. Click "Deploy". Streamlit will install dependencies and launch the app.

Troubleshooting:
- If Streamlit fails to start, check the app logs on the Streamlit Cloud dashboard.
- Ensure `streamlit` is listed in `requirements.txt` and the main file path is correct.


## Notes

- Adjust dependency list above to match your environment or add a `requirements.txt` file.
- If `app.py` depends on Flask or FastAPI, install `flask` or `fastapi[all]` accordingly.

## License

Include a license file if you intend to open-source this project.
