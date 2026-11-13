
import pandas as pd

# Load the dataset
df = pd.read_csv("penguins_outliers_reviewed.csv")

# Create a new feature
df["bill_length_to_depth_ratio"] = (
    df["bill_length_mm"] / df["bill_depth_mm"]
)

# Display original and new columns
print("Feature Engineering Results:")
print(df[[
    "bill_length_mm",
    "bill_depth_mm",
    "bill_length_to_depth_ratio"
]].head(10))

# Save the new dataset
df.to_csv("penguins_feature_engineered.csv", index=False)

print("\nNew feature created successfully!")
print("Dataset saved as penguins_feature_engineered.csv")
