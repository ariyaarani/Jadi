# Author: Mohammad Reza Arani

import pandas as pd

input_file = "products.csv"
df = pd.read_csv(input_file)

df["Total Price"] = df["Price"] * df["Quantity"]

total_sum = df["Total Price"].sum()
print(f"Total value of all products: {total_sum}")


