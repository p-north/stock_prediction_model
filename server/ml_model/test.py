import yfinance as yf
import pandas as pd

# downloading data
data = yf.download("MSFT", start="2024-01-01", end="2024-12-31")

data.to_csv('msft_1_year_data.csv');

print("CSV file 'msft_1_year_data.csv' created successfully!")
