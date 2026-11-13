# Conclusion

In this assignment, the Palmer Penguins dataset was explored and prepared for machine learning using different data preprocessing techniques.

First, the dataset was loaded and explored to understand its structure, columns, and data types. Missing values were handled using median imputation for numerical columns and mode imputation for categorical columns. Duplicate records were checked and removed where necessary.

Categorical data was standardized, and outliers were investigated using boxplots and the IQR method. Visualizations such as histograms, bar charts, boxplots, and a correlation heatmap were created to understand the dataset.

A new feature named `bill_length_to_depth_ratio` was created using existing columns. Label Encoding and One-Hot Encoding were applied to categorical data. Min-Max Scaling and Standardization were also performed on selected numerical features.

Finally, the processed dataset was checked for missing values and duplicate records and saved as `penguins_final_cleaned.csv`.

This assignment provided practical experience in data cleaning, data visualization, feature engineering, encoding, and feature scaling. Proper preprocessing helps improve data quality and prepares the dataset for building reliable machine learning models.