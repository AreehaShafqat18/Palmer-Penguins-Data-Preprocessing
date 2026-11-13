
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("penguins.csv")

# First five records
print("First Five Records:")
print(df.head())

# Last five records
print("\nLast Five Records:")
print(df.tail())

# Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Column names and data types
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Numerical statistics
print("\nNumerical Statistics:")
print(df.describe())

# Categorical statistics
print("\nCategorical Statistics:")
print(df.describe(include="object"))
