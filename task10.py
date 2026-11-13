
import pandas as pd

# Load the final processed dataset
df = pd.read_csv("penguins_scaled.csv")

# 1. Display final dataset
print("FINAL DATASET:")
print(df.to_string())

# 2. Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

total_missing = df.isnull().sum().sum()
print("\nTotal Missing Values:", total_missing)

# 3. Check duplicate records
total_duplicates = df.duplicated().sum()
print("\nTotal Duplicate Records:", total_duplicates)

# 4. Display final rows and columns
print("\nFINAL DATASET SHAPE:")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# 5. Save final dataset
df.to_csv("penguins_final_cleaned.csv", index=False)

print("\nFinal dataset saved successfully!")
print("File Name: penguins_final_cleaned.csv")
