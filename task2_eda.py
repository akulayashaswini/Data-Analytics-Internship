import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(
    r"C:\Users\Yashaswini\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

# -------------------------------
# 1. Orders by Category
# -------------------------------
print("Orders by Category:")
category_count = df["Category"].value_counts()
print(category_count)

category_count.plot(kind="bar")
plt.title("Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")
plt.show()

# -------------------------------
# 2. Total Sales by Category
# -------------------------------
print("\nTotal Sales by Category:")
sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)

sales_by_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 3. Total Profit by Category
# -------------------------------
print("\nTotal Profit by Category:")
profit_by_category = df.groupby("Category")["Profit"].sum()
print(profit_by_category)

profit_by_category.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# -------------------------------
# 4. Total Sales by Region
# -------------------------------
print("\nTotal Sales by Region:")
sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)

sales_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 5. Total Profit by Region
# -------------------------------
print("\nTotal Profit by Region:")
profit_by_region = df.groupby("Region")["Profit"].sum()
print(profit_by_region)

profit_by_region.plot(kind="bar")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()