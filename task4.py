
# TASK 4: Handle Inconsistent Categorical Data

import pandas as pd

# 1. Load dataset from Task 3
df = pd.read_csv("penguins_no_duplicates.csv")

# Make a copy
cleaned_df = df.copy()

# 2. Identify categorical columns
categorical_columns = cleaned_df.select_dtypes(
    include=["object", "category", "string"]
).columns

print("Categorical Columns:")
print(list(categorical_columns))

# 3. Display unique values before cleaning
print("\nUNIQUE VALUES BEFORE CLEANING:")

for column in categorical_columns:
    print(f"\n{column}:")
    print(cleaned_df[column].unique())

# 4. Check and standardize categorical values
print("\nSTANDARDIZATION RESULTS:")

for column in categorical_columns:

    # Store original values
    before = cleaned_df[column].copy()

    # Remove extra spaces and standardize capitalization
    cleaned_df[column] = (
        cleaned_df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # Check whether values changed
    changed = before.fillna("<MISSING>") != cleaned_df[column].fillna("<MISSING>")

    print(f"\nColumn: {column}")
    print("Values changed:", changed.sum())

    if changed.any():
        examples = pd.DataFrame({
            "Before": before[changed],
            "After": cleaned_df.loc[changed, column]
        })
        print(examples.head())

# 5. Display unique values after cleaning
print("\nUNIQUE VALUES AFTER CLEANING:")

for column in categorical_columns:
    print(f"\n{column}:")
    print(cleaned_df[column].unique())

# 6. Save standardized dataset
cleaned_df.to_csv("penguins_standardized.csv", index=False)

print("\nStandardized dataset saved successfully!")
