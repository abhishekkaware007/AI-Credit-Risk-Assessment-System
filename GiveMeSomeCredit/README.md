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

## Notes

- Adjust dependency list above to match your environment or add a `requirements.txt` file.
- If `app.py` depends on Flask or FastAPI, install `flask` or `fastapi[all]` accordingly.

## License

Include a license file if you intend to open-source this project.
