import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer  # Import imputer to handle missing values

# Load the dataset
df = pd.read_csv('ev_sales.csv')

# Check for missing values
print("Missing values before handling:")
print(df.isnull().sum())

# Drop rows with missing values (if feasible)
df.dropna(inplace=True)

# Check again for missing values after dropping
print("Missing values after dropping:")
print(df.isnull().sum())

# Extract numerical columns for clustering
numerical_columns = ['2 W', '3 W', '4 W', 'BUS']
data_for_clustering = df[numerical_columns]

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_clustering)

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)  # Example with 4 clusters
cluster_labels = kmeans.fit_predict(scaled_data)

# Add cluster labels to the original dataframe
df['Cluster'] = cluster_labels

# Visualize the clusters (pairwise plots for the numerical columns)
sns.pairplot(df, hue='Cluster', vars=numerical_columns, palette='viridis')
plt.suptitle('K-Means Clustering with 4 Clusters', y=1.02)
plt.show()

