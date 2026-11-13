
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the encoded dataset
df = pd.read_csv("penguins_encoded.csv")

# Select two numerical features (not the target variable)
features = ["bill_length_mm", "body_mass_g"]

# Keep original values for comparison
comparison = df[features].copy()

# Apply Min-Max Scaling
minmax_scaler = MinMaxScaler()
minmax_values = minmax_scaler.fit_transform(df[features])

# Apply Standardization
standard_scaler = StandardScaler()
standard_values = standard_scaler.fit_transform(df[features])

# Add scaled columns to the dataset
for i, column in enumerate(features):
    df[column + "_minmax"] = minmax_values[:, i]
    df[column + "_standardized"] = standard_values[:, i]

# Create comparison table
comparison["bill_length_minmax"] = df["bill_length_mm_minmax"]
comparison["bill_length_standardized"] = df["bill_length_mm_standardized"]

comparison["body_mass_minmax"] = df["body_mass_g_minmax"]
comparison["body_mass_standardized"] = df["body_mass_g_standardized"]

print("BEFORE AND AFTER SCALING:")
print(comparison.head(10).round(3))

# Save scaled dataset
df.to_csv("penguins_scaled.csv", index=False)

print("\nFeature scaling completed successfully!")
print("Scaled dataset saved as penguins_scaled.csv")
