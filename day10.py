import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Dataset Shape:")
print(df.shape)

print("\nNumber of Categories:")
print(df["Category"].nunique())

print("\nNumber of Sub-Categories:")
print(df["Sub-Category"].nunique())

print("\nNumber of Regions:")
print(df["Region"].nunique())

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())