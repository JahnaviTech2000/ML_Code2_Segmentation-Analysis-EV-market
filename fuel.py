import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV into a DataFrame (replace 'fuel.csv' with your actual file path)
df = pd.read_csv('fuel.csv')

# Summing up the counts for each column (fuel type)
fuel_counts = df.sum(axis=0)

# Plotting the data as a pie chart with different colors
plt.figure(figsize=(10, 8))  

# Define colors for the pie chart
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange', 'purple','lightpink', 'lightgrey', 'yellowgreen', 'cyan', 'teal', 'lavender','lightseagreen', 'mediumorchid', 'deepskyblue', 'salmon', 'limegreen']

# Plotting the pie chart
wedges, texts, autotexts = plt.pie(fuel_counts, labels=None, autopct='', colors=colors, startangle=140)

# Adding labels and percentage to legend
plt.legend(wedges, [f'{label} ({value:.1f}%)' for label, value in zip(fuel_counts.index, fuel_counts / fuel_counts.sum() * 100)],
           title="Fuel Types", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 0.9))

# Add a title
plt.title('Distribution of Vehicle Fuel Types')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Display the plot
plt.show()
