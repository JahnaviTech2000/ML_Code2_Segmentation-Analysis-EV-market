import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset (assuming you have already loaded and processed your data)
df = pd.read_csv('ev_sales.csv')

# Extract numerical columns for PCA
numerical_columns = ['2 W', '3 W', '4 W', 'BUS']
data_for_pca = df[numerical_columns]

# Check for missing values
print("Missing values before handling:")
print(data_for_pca.isnull().sum())

# Drop rows with missing values (if feasible)
data_for_pca.dropna(inplace=True)

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_pca)

# Perform PCA
pca = PCA(n_components=4)  # Example with 4 components, adjust as needed
principal_components = pca.fit_transform(scaled_data)

# Display PC values in terminal
print("Principal Component Values:")
for i in range(5):  # Print values for the first 5 samples (adjust as needed)
    print(f"Sample {i+1}: {principal_components[i]}")

# Print explained variance ratio
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)
