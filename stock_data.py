import yfinance as yf
import pandas as pd

# List of stocks (you can add more later)
stocks = ["TATAMOTORS.NS", "RELIANCE.NS", "INFY.NS", "HDFCBANK.NS"]

all_data = []

for s in stocks:
    print(f"Downloading data for {s}...")
    
    data = yf.download(s, start="2015-01-01", end="2024-12-31")

    # ✅ Fix MultiIndex columns (IMPORTANT)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    # Add company name
    data["Company"] = s

    # Reset index to get Date column
    data.reset_index(inplace=True)

    all_data.append(data)

# Combine all stocks
final_df = pd.concat(all_data, ignore_index=True)

# Save CSV
final_df.to_csv("stock_data.csv", index=False)

print("✅ Multiple stock dataset created successfully!")