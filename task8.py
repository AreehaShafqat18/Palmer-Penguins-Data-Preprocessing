
import pandas as pd

class LabelEncoder:
    def __init__(self):
        self.classes_ = None

    def fit(self, values):
        unique_values = pd.Series(values).dropna().unique()
        self.classes_ = pd.Index(unique_values)
        return self

    def transform(self, values):
        if self.classes_ is None:
            raise ValueError("LabelEncoder has not been fitted yet.")
        mapping = {category: idx for idx, category in enumerate(self.classes_)}
        return pd.Series(values).map(mapping).fillna(-1).astype(int).to_numpy()

    def fit_transform(self, values):
        return self.fit(values).transform(values)

# Load the feature-engineered dataset
df = pd.read_csv("penguins_feature_engineered.csv")

# 1. Identify categorical columns
categorical_columns = df.select_dtypes(
    include=["object", "category", "string"]
).columns

print("Categorical Columns:")
print(list(categorical_columns))

# 2. Show dataset before encoding
print("\nDATASET BEFORE ENCODING:")
print(df[["species", "island", "sex"]].head())

# 3. Apply Label Encoding to sex
label_encoder = LabelEncoder()
df["sex_encoded"] = label_encoder.fit_transform(df["sex"])

print("\nLabel Encoding Mapping:")
for number, category in enumerate(label_encoder.classes_):
    print(category, "=", number)

# 4. Apply One-Hot Encoding to island
df = pd.get_dummies(
    df,
    columns=["island"],
    dtype=int
)


print("\nColumns after One-Hot Encoding:")
print(df.columns.tolist())

# 5. Show dataset after encoding
print("\nDATASET AFTER ENCODING:")
print(df.head())

# 6. Save encoded dataset
df.to_csv("penguins_encoded.csv", index=False)

print("\nEncoding completed successfully!")
print("Encoded dataset saved as penguins_encoded.csv")
