import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Top 10 Products by Profit:\n")

top_profit = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

print(top_profit)