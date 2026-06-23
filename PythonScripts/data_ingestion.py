import pandas as pd
from pathlib import Path

raw_data_path = Path("Data/Raw")

csv_files = sorted(raw_data_path.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    try:
        df = pd.read_csv(file)

        print("\n" + "=" * 70)
        print(f"DATASET: {file.name}")
        print("=" * 70)

        print(f"Shape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"\nError reading {file.name}")
        print(f"Reason: {e}")
