
# TASK 6: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("penguins_outliers_reviewed.csv")

# Set a clean visualization style
sns.set_style("whitegrid")


# --------------------------------
# VISUALIZATION 1: HISTOGRAM
# --------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="body_mass_g",
    bins=20,
    kde=True
)

plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.savefig("outputs/task6_histogram.png")
plt.show()


# --------------------------------
# VISUALIZATION 2: BAR CHART
# --------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="species",
    order=df["species"].value_counts().index
)

plt.title("Number of Penguins by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.savefig("outputs/task6_bar_chart.png")
plt.show()


# --------------------------------
# VISUALIZATION 3: BOXPLOT
# --------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="species",
    y="body_mass_g"
)

plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")

plt.tight_layout()
plt.savefig("outputs/task6_boxplot.png")
plt.show()


# --------------------------------
# VISUALIZATION 4: CORRELATION HEATMAP
# --------------------------------

numerical_df = df.select_dtypes(include="number")

correlation = numerical_df.corr()

plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Numerical Features")

plt.tight_layout()
plt.savefig("outputs/task6_heatmap.png")
plt.show()


# --------------------------------
# DISPLAY ADDITIONAL INFORMATION
# --------------------------------

print("\nSPECIES FREQUENCY:")
print(df["species"].value_counts())

print("\nAVERAGE BODY MASS BY SPECIES:")
print(df.groupby("species")["body_mass_g"].mean().round(2))

print("\nCORRELATION WITH BODY MASS:")
print(correlation["body_mass_g"].sort_values(ascending=False))

print("\nAll four visualizations saved successfully!")

# TASK 6: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("penguins_outliers_reviewed.csv")

# Set a clean visualization style
sns.set_style("whitegrid")


# --------------------------------
# VISUALIZATION 1: HISTOGRAM
# --------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="body_mass_g",
    bins=20,
    kde=True
)

plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.savefig("outputs/task6_histogram.png")
plt.show()


# --------------------------------
# VISUALIZATION 2: BAR CHART
# --------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="species",
    order=df["species"].value_counts().index
)

plt.title("Number of Penguins by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.savefig("outputs/task6_bar_chart.png")
plt.show()


# --------------------------------
# VISUALIZATION 3: BOXPLOT
# --------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="species",
    y="body_mass_g"
)

plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")

plt.tight_layout()
plt.savefig("outputs/task6_boxplot.png")
plt.show()


# --------------------------------
# VISUALIZATION 4: CORRELATION HEATMAP
# --------------------------------

numerical_df = df.select_dtypes(include="number")

correlation = numerical_df.corr()

plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Numerical Features")

plt.tight_layout()
plt.savefig("outputs/task6_heatmap.png")
plt.show()


# --------------------------------
# DISPLAY ADDITIONAL INFORMATION
# --------------------------------

print("\nSPECIES FREQUENCY:")
print(df["species"].value_counts())

print("\nAVERAGE BODY MASS BY SPECIES:")
print(df.groupby("species")["body_mass_g"].mean().round(2))

print("\nCORRELATION WITH BODY MASS:")
print(correlation["body_mass_g"].sort_values(ascending=False))

print("\nAll four visualizations saved successfully!")
