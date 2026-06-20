import pandas as pd

df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nSummary Statistics:")
print(df.describe())