import requests
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:

        response = requests.get(
            url,
            verify=False,
            timeout=30
        )

        data = response.json()

        nav_data = data["data"]

        df = pd.DataFrame(nav_data)

        file_path = f"Data/Raw/{fund_name}_live_nav.csv"

        df.to_csv(
            file_path,
            index=False
        )

        print(f"Saved: {file_path}")
        print(f"Rows: {df.shape[0]}")

    except Exception as e:

        print(f"Error fetching {fund_name}")
        print(e)