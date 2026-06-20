import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nTop 5 Categories by Sales:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))