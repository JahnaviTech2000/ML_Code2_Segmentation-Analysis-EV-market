import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Extract Type of Vehicles and a) Scooters columns
df= pd.read_csv('location.csv')
vehicles_data = df[['Type of Vehicles', 'a) Scooters']].dropna()  # Drop rows where a) Scooters data is missing

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(data=vehicles_data, y='Type of Vehicles', x='a) Scooters', palette='viridis')
plt.xlabel('Number of Scooters', fontsize=14, family='serif')
plt.ylabel('Type of Vehicles', fontsize=14, family='serif')
plt.xticks(fontsize=12, family='serif')
plt.yticks(fontsize=12, family='serif')
plt.title('Frequency of Scooters by Type of Vehicles', fontsize=16, family='serif', weight='bold', pad=12)
plt.tight_layout()

# Show plot
plt.show()
