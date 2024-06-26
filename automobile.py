import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data from CSV into a DataFrame (replace 'your_file.csv' with your actual file path)
df = pd.read_csv('automobile.csv')

# Inspect the data
print(df.head())
print(df['Make'].value_counts())
# Select only the numeric columns for computing the mean
numeric_cols = ['Age', 'No of Dependents', 'Salary', 'Wife Salary', 'Total Salary', 'Price']

# Group by 'Make' and calculate the mean of numeric columns
make_stats = df.groupby('Make')[numeric_cols].mean()
print(make_stats)
# Plotting the heat map
plt.figure(figsize=(14, 10))
sns.heatmap(make_stats, annot=True, cmap='viridis', linewidths=.5)

# Add a title
plt.title('Average Attributes by Car Make')

# Show the plot
plt.show()
