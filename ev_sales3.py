import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('ev_sales.csv')

# Drop rows with missing values (if necessary)
df.dropna(inplace=True)

# Extract numerical columns for clustering
numerical_columns = ['2 W', '3 W', '4 W', 'BUS']
data_for_clustering = df[numerical_columns]

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_clustering)

# Initialize lists to store inertia and silhouette scores
inertia_values = []
silhouette_scores = []
k_range = range(2, 11)  # Range of K values to test

# Iterate over each K value
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    
    # Append inertia and silhouette score to lists
    inertia_values.append(kmeans.inertia_)
    if k > 1:
        silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))

# Plot the Elbow curve
plt.figure(figsize=(10, 6))
plt.plot(k_range, inertia_values, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal K')
plt.xticks(k_range)
plt.grid(True)
plt.show()

# Plot Silhouette scores (optional)
if len(silhouette_scores) > 0:
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, silhouette_scores, marker='o', linestyle='-', color='g')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score For Optimal K')
    plt.xticks(k_range)
    plt.grid(True)
    plt.show()
