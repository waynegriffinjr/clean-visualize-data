import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                "Widget A", " Widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200",
              "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
             "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
    "region": ["North", "South", "north", "East", "South",
               "West", "east", "North", "South", "West"],
})

df = pd.DataFrame(messy)

# Standardize names/regions
df["product"] = df["product"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()

# Convert Types
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Handle missing product names
df = df.dropna(subset=["product"])

# Handle invalid sales
df.loc[df["sales"] < 0, "sales"] = pd.NA
df["sales"] = df["sales"].fillna(df["sales"].median())


# Store Cleaned Version
cleaned_df = df.copy()



# print(df.shape) # (rows, columns)
# print(df.dtypes) # Column types
# print(df.head()) # First 5 rows
# print(df.describe()) # Statistical summary
# print(df.info()) # Column names, types, non-null counts


# df = pd.DataFrame(messy)
# print("=== Raw Data ===")
# print(df)
# print(f"Shape: {df.shape}")
# print(f"Missing values: {df.isnull().sum()}")

# df.isna().sum()
# df[df["sales"] < 0]
# df["product"].unique()
# df["region"].unique()
# df[df["date"].isna()]


# print("Missing values:\n", df.isna().sum())
# print("\nInvalid sales:\n", df[df['sales'].isna()])
# print("\nNegative sales:\n", df[df['sales'] < 0])
# print("\nUnique products:\n", df['product'].unique())
# print("\nUnique regions:\n", df['region'].unique())
# print("\nInvalid dates:\n", df[df['date'].isna()])
# print("\nData types:\n", df.dtypes)


'''DATA HAS BEEN COMPLETELY CLEAN PER STAKEHOLDER REQUIREMENTS'''
#Bar Chart: Total sales by product:
plt.figure(figsize=(8, 5))
plt.bar(cleaned_df["product"], cleaned_df["sales"], color="steelblue")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout() # Prevents labels from being cut off
plt.savefig("sales-by-product.png", dpi=150) # Save to file
plt.show()

# Line chart daily trend:
plt.figure(figsize=(8, 5))
plt.plot(cleaned_df["date"], cleaned_df["sales"], marker="o", color="coral", linewidth=2)
plt.title("Daily Trend")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.grid(True, alpha=0.3) # Light gridlines for readability
plt.tight_layout()
plt.savefig("sales-daily-trend.png", dpi=150) # Save to file
plt.show()


# Histogram for Distribution:
plt.figure(figsize=(8, 5))
plt.hist(cleaned_df["sales"], bins=8, color="seagreen", edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Sales ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales_distribution_histogram.png", dpi=150) # Save to file
plt.show()


# print(df["product"].isna().sum())
# print(df[df["product"].isna()])
# print(df["product"].unique())