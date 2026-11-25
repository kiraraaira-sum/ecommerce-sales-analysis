import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

df = pd.read_csv("ecommerce_sales_dataset.csv")
print(df.columns.tolist())
conn = sqlite3.connect("ecommerce.db")
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

print(df.head())
print(df.shape)
print(df.info())
print(df.duplicated().sum())
print(df.describe())
print(df["Category"].value_counts())
print(df["City"].value_counts())

revenue_by_category = df.groupby("Category")["Revenue"].sum()
revenue_percentage = (revenue_by_category / df["Revenue"].sum()) * 100
revenue_by_product = df.groupby("Product")["Revenue"].sum()
discount_analysis = df.groupby("Discount")["Revenue"].agg(
    ["mean", "sum", "count"]
)
revenue_by_city = df.groupby("City")["Revenue"].sum()

print(revenue_by_category.sort_values(ascending=False))
print(revenue_percentage.sort_values(ascending=False))
print(revenue_by_product.sort_values(ascending=False).head(10))
print(discount_analysis)
print(revenue_by_city.sort_values(ascending=False))

discount_analysis["mean"].plot(kind="bar")
plt.title("Average Revenue by Discount")
plt.xlabel("Discount")
plt.ylabel("Average revenue")
plt.xticks(rotation=0)
plt.show()

revenue_by_city.sort_values(ascending=False).plot(kind="bar")
plt.title("Total Revenue by City")
plt.xlabel("City") 
plt.ylabel("Total revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

city_analysis = revenue_by_city.sort_values(ascending=False)
city_percentage = (city_analysis / df["Revenue"].sum()) * 100

payment_analysis = df.groupby("Payment_Method")["Revenue"].agg(
    ["sum", "count", "mean"]
)
rating_analysis = df.groupby("Rating")["Revenue"].agg(
    ["sum", "mean", "count"]
)

print("TOP 5 CITIES by REVENUE:")
print("\nRevenue Percentage:")
print(city_analysis.head(5))
print(city_percentage.head(5))
print(payment_analysis.sort_values("sum", ascending=False))
print(rating_analysis)

payment_analysis["sum"].sort_values(ascending=False).plot(kind="bar")
plt.title("Total Revenue by Payment method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df["Month"] = df["Order_Date"].str[:7]
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print(monthly_revenue)

monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
category_revenue.plot(kind="bar")
plt.title("Revenue by category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

query = """
SELECT
    Category,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Product,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 10;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    City,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY City
ORDER BY Total_Revenue DESC
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Payment_Method,
    SUM(Revenue) AS Total_Revenue,
    COUNT(*) AS Total_Transactions,
    AVG(Revenue) AS Average_Revenue
FROM sales
GROUP BY Payment_Method
ORDER BY Total_Revenue DESC;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    SUBSTR(Order_date, 1, 7) AS Month,
    SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Customer_ID,
    SUM(Revenue) AS Total_spent
FROM sales
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    AVG(Revenue) AS Average_Order_Value
FROM sales;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Discount,
    AVG(Revenue) AS Average_Revenue,
    SUM(Revenue) AS Total_Revenue,
    COUNT(*) AS Transactions
FROM sales
GROUP BY Discount
ORDER BY Discount;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Customer_ID,
    COUNT(*) AS Total_Transactions,
    SUM(Revenue) AS Total_Spent,
    AVG(Revenue) AS Average_Order_Value
FROM sales
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;
"""
result = pd.read_sql_query(query, conn)
print(result)

query = """
SELECT
    Customer_ID,
    SUM(Revenue) AS Total_Spent
FROM sales
GROUP BY Customer_ID
ORDER BY Total_Spent DESC;
"""

customer_analysis = pd.read_sql_query(query, conn)

customer_analysis["Customer_Segment"] = pd.cut(
    customer_analysis["Total_Spent"],
    bins=[0, 50000, 100000, float("inf")],
    labels=["Low Value", "Medium Value", "High Value"]
)

print(customer_analysis.head(10))
print("\nCustomer Segment:")
print(customer_analysis["Customer_Segment"].value_counts())

segment_counts = customer_analysis["Customer_Segment"].value_counts()

segment_counts.plot(kind="bar")

plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

customer_analysis.to_csv("customer_segmentation.csv", index=False)

print("Customer segmentation berhasil disimpan!")