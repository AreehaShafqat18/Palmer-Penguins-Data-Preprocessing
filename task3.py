
# TASK 3: Identify and Remove Duplicate Records

import pandas as pd

# 1. Load the cleaned dataset from Task 2
df = pd.read_csv("penguins_cleaned.csv")

# 2. Identify duplicate rows
print("Duplicate Records:")
print(df.duplicated())

# 3. Count total duplicate rows
duplicates_before = df.duplicated().sum()

print("\nTotal Duplicates Before Removal:")
print(duplicates_before)

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Verify duplicate removal
duplicates_after = df.duplicated().sum()

print("\nTotal Duplicates After Removal:")
print(duplicates_after)

# 6. Display dataset shape
print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# 7. Save the final dataset
df.to_csv("penguins_no_duplicates.csv", index=False)

print("\nDataset saved successfully!")
