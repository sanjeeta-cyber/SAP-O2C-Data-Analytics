import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# ---- BASIC OUTPUT ----
print("Total Revenue:", df["Revenue"].sum())

print("\nRevenue by Customer:\n")
print(df.groupby("Customer")["Revenue"].sum())

print("\nRevenue by Product:\n")
print(df.groupby("Product")["Revenue"].sum())

# ---- GRAPH 1: Customer Revenue ----
df.groupby("Customer")["Revenue"].sum().plot(kind='bar')
plt.title("Revenue by Customer")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- GRAPH 2: Product Revenue ----
df.groupby("Product")["Revenue"].sum().plot(kind='bar')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- GRAPH 3: Monthly Sales Trend ----
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()