import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///Database/bluestock_mf.db")

# Load cleaned datasets
nav_df = pd.read_csv("Data/Processed/clean_nav.csv")
transactions_df = pd.read_csv("Data/Processed/clean_transactions.csv")
performance_df = pd.read_csv("Data/Processed/clean_performance.csv")

# Load into database tables
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("All data loaded successfully!")

fund_df = pd.read_csv("Data/Raw/01_fund_master.csv")
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)
