# Deployment / validation configuration

## Project type
This deliverable is a Jupyter Notebook analysis, not a web service. It does not need a public website unless the internship portal explicitly requests one.

## Reproducible environment
- Python: 3.10 or newer
- Dependencies: installed from `requirements.txt`
- Notebook: `notebooks/Task2_EDA_Superstore.ipynb`
- Input data: `data/Sample - Superstore.csv`

## Automated validation
`.github/workflows/eda-check.yml` runs on pushes and pull requests to `main`. It installs the listed dependencies and checks that the notebook file is valid JSON/Notebook format.

## How to verify
1. Push the repository to GitHub.
2. Open the repository's **Actions** tab.
3. Open the latest `EDA project checks` run.
4. Save a screenshot showing the successful run, or record the failure and fix it.
5. Do not describe this as a deployed web application; it is repository automation and validation.
