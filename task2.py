
# TASK 2: Identify and Handle Missing Values

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("penguins.csv")

# Make a copy of original dataset
cleaned_df = df.copy()

# 2. Identify missing values per column
print("MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# 3. Calculate total and percentage of missing values
total_missing = df.isnull().sum().sum()
total_cells = df.size
missing_percentage = (total_missing / total_cells) * 100

print("\nTotal Missing Values:", total_missing)
print("Overall Missing Percentage:", round(missing_percentage, 2), "%")

# Missing values report for each column
missing_report = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Missing Percentage": (df.isnull().mean() * 100).round(2)
})

print("\nMissing Values Report:")
print(missing_report)

# 4. Visualize missing values using a bar chart
plt.figure(figsize=(10, 5))

missing_counts = df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]

sns.barplot(x=missing_counts.index, y=missing_counts.values)

plt.title("Missing Values Per Column")
plt.xlabel("Columns")
plt.ylabel("Number of Missing Values")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart in outputs folder
plt.savefig("outputs/task2_missing_values.png")
plt.show()

# 5. Handle numerical missing values using MEDIAN
numerical_columns = cleaned_df.select_dtypes(
    include=np.number
).columns

for column in numerical_columns:
    median_value = cleaned_df[column].median()
    cleaned_df[column] = cleaned_df[column].fillna(median_value)

# 6. Handle categorical missing values using MODE
categorical_columns = cleaned_df.select_dtypes(
    include="object"
).columns

for column in categorical_columns:
    mode_value = cleaned_df[column].mode()

    if not mode_value.empty:
        cleaned_df[column] = cleaned_df[column].fillna(mode_value[0])

# 7. Display missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING")
print(cleaned_df.isnull().sum())

print("\nTotal Missing Values After Cleaning:",
      cleaned_df.isnull().sum().sum())

# 8. Save cleaned dataset
cleaned_df.to_csv("penguins_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
