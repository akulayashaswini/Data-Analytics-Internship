import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Sales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))