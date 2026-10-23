import pandas as pd
import random
from datetime import datetime, timedelta


# -----------------------------
# PRODUCT INFORMATION
# -----------------------------

products = {
    "Electronics": [
        ("Laptop", 55000, 45000),
        ("Smartphone", 30000, 24000),
        ("Headphones", 2500, 1700),
        ("Smartwatch", 5000, 3500),
        ("Keyboard", 1500, 900)
    ],

    "Clothing": [
        ("T-Shirt", 800, 400),
        ("Jeans", 1800, 1000),
        ("Jacket", 3000, 1900),
        ("Kurti", 1200, 650),
        ("Dress", 2200, 1300)
    ],

    "Home": [
        ("Mixer Grinder", 3500, 2500),
        ("Table Lamp", 1200, 700),
        ("Bedsheet", 1500, 800),
        ("Cookware Set", 2500, 1600),
        ("Chair", 4000, 2800)
    ],

    "Beauty": [
        ("Face Wash", 400, 220),
        ("Moisturizer", 600, 350),
        ("Perfume", 1800, 1100),
        ("Lipstick", 700, 350),
        ("Shampoo", 450, 250)
    ]
}


# -----------------------------
# CITY AND REGION INFORMATION
# -----------------------------

cities = {
    "South": [
        "Bengaluru",
        "Chennai",
        "Hyderabad",
        "Mysuru"
    ],

    "North": [
        "Delhi",
        "Jaipur",
        "Lucknow",
        "Chandigarh"
    ],

    "West": [
        "Mumbai",
        "Pune",
        "Ahmedabad",
        "Surat"
    ],

    "East": [
        "Kolkata",
        "Bhubaneswar",
        "Patna",
        "Guwahati"
    ]
}


# -----------------------------
# PAYMENT METHODS
# -----------------------------

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery"
]


# -----------------------------
# CREATE EMPTY LIST
# -----------------------------

records = []


# Starting date
start_date = datetime(2025, 1, 1)


# -----------------------------
# GENERATE 3000 ORDERS
# -----------------------------

for i in range(1, 3001):

    # Select category
    category = random.choice(
        list(products.keys())
    )

    # Select product
    product_name, price, cost = random.choice(
        products[category]
    )

    # Select region
    region = random.choice(
        list(cities.keys())
    )

    # Select city
    city = random.choice(
        cities[region]
    )

    # Quantity purchased
    quantity = random.randint(1, 4)

    # Discount
    discount = random.choice(
        [0, 5, 10, 15, 20]
    )

    # Random order date
    order_date = (
        start_date +
        timedelta(
            days=random.randint(0, 364)
        )
    )

    # Customer information
    customer_number = random.randint(1, 800)

    customer_id = (
        f"CUST{customer_number:04d}"
    )

    customer_name = (
        f"Customer {customer_number}"
    )

    # Payment method
    payment = random.choice(
        payment_methods
    )

    # Calculate sales
    gross_sales = price * quantity

    discount_amount = (
        gross_sales *
        (discount / 100)
    )

    sales = (
        gross_sales -
        discount_amount
    )

    # Calculate cost
    total_cost = cost * quantity

    # Calculate profit
    profit = (
        sales -
        total_cost
    )

    # Add record
    records.append([
        f"ORD{i:05d}",
        order_date.date(),
        customer_id,
        customer_name,
        product_name,
        category,
        quantity,
        price,
        cost,
        discount,
        sales,
        profit,
        city,
        region,
        payment
    ])


# -----------------------------
# COLUMN NAMES
# -----------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Product",
    "Category",
    "Quantity",
    "Unit_Price",
    "Unit_Cost",
    "Discount",
    "Sales",
    "Profit",
    "City",
    "Region",
    "Payment_Method"
]


# -----------------------------
# CREATE DATAFRAME
# -----------------------------

df = pd.DataFrame(
    records,
    columns=columns
)


# -----------------------------
# SAVE CSV FILE
# -----------------------------

df.to_csv(
    "data/ecommerce_raw.csv",
    index=False
)


# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("================================")
print("E-COMMERCE DATASET CREATED")
print("================================")

print()

print("Total Orders:", len(df))

print()

print("First 5 Records:")

print(df.head())

print()

print(
    "File saved as: data/ecommerce_raw.csv"
)