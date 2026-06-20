import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print(df.head())