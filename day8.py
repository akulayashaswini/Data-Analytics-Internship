import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Top 10 Products by Sales:\n")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)