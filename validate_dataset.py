from pathlib import Path
import pandas as pd

path = Path("data/Sample - Superstore.csv")
if not path.exists():
    print("Dataset not present yet. Add data/Sample - Superstore.csv to run data validation.")
    raise SystemExit(0)

df = pd.read_csv(path, encoding="latin1")
required = {"Sales", "Profit"}
missing = required - set(df.columns)
if missing:
    raise SystemExit(f"Dataset is missing expected columns: {sorted(missing)}")
print(f"Dataset validation passed: {len(df)} rows, {len(df.columns)} columns.")
print("Missing values by column:")
print(df.isna().sum().sort_values(ascending=False).to_string())
