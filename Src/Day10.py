#Task 1
import pandas as pd
df = pd.read_csv("sample_orders.csv")
print(df.head())
print(df.isna().sum())
print(df.fillna(0))
print( df["quantity"].fillna(df["quantity"].median()))
print(df.duplicated().sum())
print(df.drop_duplicates())

#Task 2
print(df.dtypes)
print(df["price"].astype(str))
print(df["price"].str.replace("$",""))
print(df["quantity"].astype(float))


#Task 3
print(df["product"].str.strip())
print(df["product"].str.lower())
print(df["customer_name"].unique().sum())

