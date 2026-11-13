
# TASK 5: Detect and Handle Outliers

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load standardized dataset from Task 4
df = pd.read_csv("penguins_standardized.csv")

# Select two numerical columns
columns = ["flipper_length_mm", "body_mass_g"]

print("Selected Numerical Columns:")
print(columns)

# 2. Generate boxplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for i, column in enumerate(columns):
    sns.boxplot(y=df[column], ax=axes[i])
    axes[i].set_title(f"Boxplot of {column}")
    axes[i].set_ylabel(column)

plt.tight_layout()

# Save boxplots
plt.savefig("outputs/task5_boxplots.png")
plt.show()

# 3. Calculate IQR and identify outliers
print("\nIQR OUTLIER ANALYSIS")

for column in columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print("\nColumn:", column)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of Outliers:", len(outliers))

    print("Outlier Values:")
    print(outliers[["species", column]].to_string(index=False))

    # Decision: Retain plausible biological observations
    print("Decision: Retain values for investigation.")
    print("Reason: Unusual penguin measurements may represent")
    print("natural differences between penguin species.")

# 4. Save reviewed dataset without deleting outliers
df.to_csv("penguins_outliers_reviewed.csv", index=False)

print("\nOutlier analysis completed!")
print("Original observations have been retained.")
