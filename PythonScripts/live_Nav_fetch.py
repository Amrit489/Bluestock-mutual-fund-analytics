import requests
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.mfapi.in/mf/125497"

response = requests.get(
    url,
    verify=False,
    timeout=30
)

data = response.json()

# Extract NAV history
nav_data = data["data"]

# Convert to DataFrame
df = pd.DataFrame(nav_data)

print("Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Save CSV
df.to_csv(
    "Data/Raw/sbi_small_cap_live_nav.csv",
    index=False
)

print("\nCSV Saved Successfully!")