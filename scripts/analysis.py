import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------
# LOAD CLEANED DATA
# --------------------------------

df = pd.read_csv(
    "data/ecommerce_cleaned.csv"
)


# --------------------------------
# TOTAL SALES
# --------------------------------

total_sales = df["Sales"].sum()


# --------------------------------
# TOTAL PROFIT
# --------------------------------

total_profit = df["Profit"].sum()


# --------------------------------
# TOTAL ORDERS
# --------------------------------

total_orders = df["Order_ID"].nunique()


# --------------------------------
# TOTAL CUSTOMERS
# --------------------------------

total_customers = df["Customer_ID"].nunique()


# --------------------------------
# AVERAGE ORDER VALUE
# --------------------------------

average_order_value = (
    total_sales / total_orders
)


# --------------------------------
# DISPLAY RESULTS
# --------------------------------

print("======================================")
print("     E-COMMERCE BUSINESS INSIGHTS")
print("======================================")

print()

print(
    f"Total Sales: ₹{total_sales:,.2f}"
)

print(
    f"Total Profit: ₹{total_profit:,.2f}"
)

print(
    f"Total Orders: {total_orders}"
)

print(
    f"Total Customers: {total_customers}"
)

print(
    f"Average Order Value: ₹{average_order_value:,.2f}"
)
# --------------------------------
# SALES BY CATEGORY
# --------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)


print()

print("======================================")
print("        SALES BY CATEGORY")
print("======================================")

print()

print(category_sales)
# --------------------------------
# PROFIT BY CATEGORY
# --------------------------------

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(
        ascending=False
    )
)


print()

print("======================================")
print("        PROFIT BY CATEGORY")
print("======================================")

print()

print(category_profit)
# --------------------------------
# SALES BY REGION
# --------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)


print()

print("======================================")
print("          SALES BY REGION")
print("======================================")

print()

print(region_sales)
# --------------------------------
# TOP 10 PRODUCTS
# --------------------------------

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)


print()

print("======================================")
print("          TOP 10 PRODUCTS")
print("======================================")

print()

print(top_products)
# --------------------------------
# SALES BY CATEGORY CHART
# --------------------------------

category_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Sales by Product Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "charts/sales_by_category.png"
)

plt.close()
# --------------------------------
# SALES BY REGION CHART
# --------------------------------

region_sales.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "charts/sales_by_region.png"
)

plt.close()
# --------------------------------
# MONTHLY SALES ANALYSIS
# --------------------------------

# Monthly Sales Analysis

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.strftime("%b"))["Sales"]
    .sum()
)

month_order = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("charts/monthly_sales.png")

plt.close()

print("\nMonthly Sales:")
print(monthly_sales)


print()

print("======================================")
print("          MONTHLY SALES")
print("======================================")

print()

print(monthly_sales)
# --------------------------------
# MONTHLY SALES CHART
# --------------------------------

monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.xticks(
    range(1, 13)
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "charts/monthly_sales.png"
)

plt.close()
# Customer Analysis

customer_sales = (
    df.groupby("Customer_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Spending:")
print(customer_sales)
# Repeat Customer Analysis

customer_orders = (
    df.groupby("Customer_ID")["Order_ID"]
    .nunique()
)

repeat_customers = customer_orders[customer_orders > 1]

one_time_customers = customer_orders[customer_orders == 1]

print("\nCustomer Purchase Analysis:")
print("Total Customers:", len(customer_orders))
print("One-Time Customers:", len(one_time_customers))
print("Repeat Customers:", len(repeat_customers))
# Customer Segmentation

customer_sales_all = (
    df.groupby("Customer_ID")["Sales"]
    .sum()
)

def customer_segment(sales):
    if sales >= 10000:
        return "High Value"
    elif sales >= 5000:
        return "Regular"
    else:
        return "Occasional"


customer_segments = customer_sales_all.apply(customer_segment)

segment_counts = customer_segments.value_counts()

print("\nCustomer Segmentation:")
print(segment_counts)
# Customer Segmentation Chart

segment_counts = customer_segments.value_counts()

segment_counts.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/customer_segmentation.png")

plt.close()
# Product Performance Analysis

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Best-Selling Products:")
print(product_sales.head(10))
# Top 10 Best-Selling Products Chart

top_10_products = product_sales.head(10)

top_10_products = top_10_products.sort_values(ascending=True)

top_10_products.plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Best-Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("charts/top_10_products.png")

plt.close()
# Least-Selling Products

least_selling_products = (
    product_sales
    .sort_values(ascending=True)
    .head(10)
)

print("\n10 Least-Selling Products:")
print(least_selling_products)
# Least-Selling Products Chart

least_selling_products = least_selling_products.sort_values(ascending=True)

least_selling_products.plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("10 Least-Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("charts/least_selling_products.png")

plt.close()