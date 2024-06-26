import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('location.csv')
vehicles_data = df[['Type of Vehicles', 'c) Motor cycles']].dropna()  # Drop rows where c) Motor cycles data is missing

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(data=vehicles_data, y='Type of Vehicles', x='c) Motor cycles', palette='viridis')
plt.xlabel('Number of Motorcycles', fontsize=14, family='serif')
plt.ylabel('Type of Vehicles', fontsize=14, family='serif')
plt.xticks(fontsize=12, family='serif')
plt.yticks(fontsize=12, family='serif')
plt.title('Frequency of Motorcycles by Type of Vehicles', fontsize=16, family='serif', weight='bold', pad=12)
plt.tight_layout()

# Show plot
plt.show()
