import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV into a DataFrame (replace 'ev_cars.csv' with your actual file path)
df = pd.read_csv('ev_cars.csv')

# Group by 'Make' and calculate the mean of 'Electric Range' and 'Base MSRP'
make_stats = df.groupby('Make')[['Electric Range', 'Base MSRP']].mean().reset_index()

# Normalize the data for better heatmap visualization
make_stats['Electric Range'] = (make_stats['Electric Range'] - make_stats['Electric Range'].min()) / (make_stats['Electric Range'].max() - make_stats['Electric Range'].min())
make_stats['Base MSRP'] = (make_stats['Base MSRP'] - make_stats['Base MSRP'].min()) / (make_stats['Base MSRP'].max() - make_stats['Base MSRP'].min())

# Melt the DataFrame to long format
make_stats_melted = make_stats.melt(id_vars='Make', var_name='Metric', value_name='Value')

# Pivot the melted DataFrame
make_stats_pivot = make_stats_melted.pivot(index='Make', columns='Metric', values='Value')

# Plotting the heat map
plt.figure(figsize=(14, 10))
sns.heatmap(make_stats_pivot, annot=True, cmap='viridis')

# Add a title
plt.title('Heat Map of Average Electric Range and Base MSRP by Car Make')

# Show the plot

plt.show()
