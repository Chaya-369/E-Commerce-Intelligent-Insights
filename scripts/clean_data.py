import pandas as pd


# -----------------------------------
# 1. LOAD THE RAW DATA
# -----------------------------------

df = pd.read_csv(
    "data/ecommerce_raw.csv"
)


# -----------------------------------
# 2. DISPLAY BASIC INFORMATION
# -----------------------------------

print("================================")
print("RAW DATA INFORMATION")
print("================================")

print()

print("Number of rows:", len(df))

print()

print("Columns:")

print(df.columns.tolist())

print()


# -----------------------------------
# 3. CHECK MISSING VALUES
# -----------------------------------

print("================================")
print("MISSING VALUES")
print("================================")

print()

print(df.isnull().sum())

print()


# -----------------------------------
# 4. CHECK DUPLICATE RECORDS
# -----------------------------------

print("================================")
print("DUPLICATE RECORDS")
print("================================")

print()

print(
    "Duplicate rows:",
    df.duplicated().sum()
)

print()


# -----------------------------------
# 5. REMOVE DUPLICATES
# -----------------------------------

df = df.drop_duplicates()


# -----------------------------------
# 6. REMOVE MISSING VALUES
# -----------------------------------

df = df.dropna()


# -----------------------------------
# 7. CONVERT ORDER DATE
# -----------------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)


# -----------------------------------
# 8. CREATE YEAR COLUMN
# -----------------------------------

df["Year"] = (
    df["Order_Date"].dt.year
)


# -----------------------------------
# 9. CREATE MONTH NUMBER
# -----------------------------------

df["Month"] = (
    df["Order_Date"].dt.month
)


# -----------------------------------
# 10. CREATE MONTH NAME
# -----------------------------------

df["Month_Name"] = (
    df["Order_Date"].dt.month_name()
)


# -----------------------------------
# 11. CALCULATE PROFIT MARGIN
# -----------------------------------

df["Profit_Margin"] = (
    df["Profit"] /
    df["Sales"]
) * 100


# -----------------------------------
# 12. ROUND NUMBERS
# -----------------------------------

df["Sales"] = df["Sales"].round(2)

df["Profit"] = df["Profit"].round(2)

df["Profit_Margin"] = (
    df["Profit_Margin"].round(2)
)


# -----------------------------------
# 13. REMOVE INVALID QUANTITIES
# -----------------------------------

df = df[
    df["Quantity"] > 0
]


# -----------------------------------
# 14. REMOVE INVALID SALES
# -----------------------------------

df = df[
    df["Sales"] > 0
]


# -----------------------------------
# 15. SAVE CLEANED DATA
# -----------------------------------

df.to_csv(
    "data/ecommerce_cleaned.csv",
    index=False
)


# -----------------------------------
# 16. DISPLAY FINAL RESULT
# -----------------------------------

print("================================")
print("DATA CLEANING COMPLETED")
print("================================")

print()

print(
    "Final number of rows:",
    len(df)
)

print()

print(
    "Final number of columns:",
    len(df.columns)
)

print()

print("Cleaned columns:")

print(df.columns.tolist())

print()

print(
    "Saved file:"
)

print(
    "data/ecommerce_cleaned.csv"
)