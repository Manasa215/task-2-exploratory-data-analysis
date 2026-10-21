# Task 2 — Exploratory Data Analysis (EDA)

## Project overview
This project explores the Sample Superstore retail dataset using Python, Pandas, Matplotlib, and Seaborn. It investigates sales and profit distributions, category performance, monthly trends, possible outliers, numeric correlations, and the relationship between discounts and profit.

## Dataset
Download the Sample Superstore CSV from:
- Kaggle: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- Alternative public CSV source: https://github.com/leonism/sample-superstore

Save the downloaded CSV as `data/Sample - Superstore.csv`. Do not upload customer-identifiable or restricted data. This is a public sample dataset.

## Project structure
```text
.
├── data/
│   └── Sample - Superstore.csv        # Add downloaded dataset here
├── notebooks/
│   └── Task2_EDA_Superstore.ipynb
├── outputs/                           # Save exported charts/results here if required
├── deployment/
│   └── deployment-config.md
├── evidence/
│   └── rollback/
│       └── ROLLBACK_EVIDENCE_TEMPLATE.md
├── .github/workflows/
│   └── eda-check.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Tools
- Python 3.10+
- Jupyter Notebook
- pandas, numpy
- matplotlib, seaborn

## Setup and run in Jupyter
1. Install Python and Jupyter, or use Google Colab.
2. Download the dataset and put it at `data/Sample - Superstore.csv`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start Jupyter from the project root:
   ```bash
   jupyter notebook
   ```
5. Open `notebooks/Task2_EDA_Superstore.ipynb`.
6. Run every cell from top to bottom. If working in Google Colab, upload the CSV and adjust `DATA_PATH` to the uploaded file location.
7. Review every chart and its observation. Replace generic prompts with specific findings from your results.
8. Save the notebook with outputs and export charts/screenshots if your mentor requests them.

## Analysis workflow
1. Load the CSV and inspect dimensions, column types, missing values, duplicates, and descriptive statistics.
2. Convert date and numeric columns to appropriate data types.
3. Remove exact duplicate rows only, while reporting the count. Missing values are not automatically deleted from the full dataset.
4. Create at least five visualizations:
   - Sales histogram
   - Total profit by category
   - Monthly sales line chart
   - Numeric boxplots with IQR flags
   - Numeric correlation heatmap
   - Discount versus profit scatter plot
5. Write an observation under every chart.
6. Add three final insights that are supported by the actual output.
7. Write a short conclusion and note limitations.

## Findings and outcome
Complete this section after running the notebook. Do not leave unverified example claims.
- **Insight 1:** [Insert a finding supported by your category chart/table.]
- **Insight 2:** [Insert a finding supported by your monthly trend.]
- **Insight 3:** [Insert a finding supported by your outlier/correlation/scatter analysis.]
- **Outcome:** [Summarize what the analysis helped you understand.]

## Quality checks / deployment configuration
This is a notebook-based analysis project, not a hosted web application. The included GitHub Actions workflow installs dependencies and performs basic repository checks on pushes and pull requests. It is a lightweight automation/validation configuration; it does not publish a web app. If the internship specifically expects a hosted application deployment, confirm the required platform with your mentor before claiming deployment.

## Rollback evidence
See `evidence/rollback/ROLLBACK_EVIDENCE_TEMPLATE.md`. Make a test commit, record its commit hash, and demonstrate reverting it on a separate test branch or a safe copy of the repository. Capture screenshots of the commit history and successful revert. Never delete or overwrite the only copy of your project to demonstrate rollback.