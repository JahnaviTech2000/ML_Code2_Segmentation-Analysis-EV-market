import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('RTA Dataset.csv')


df.fillna('Unknown', inplace=True)


plt.figure(figsize=(12, 8))


sns.countplot(data=df, y='Type_of_vehicle', palette='viridis', order=df['Type_of_vehicle'].value_counts().index)
plt.title('Frequency of Each Type of Vehicle')
plt.xlabel('Frequency')
plt.ylabel('Type of Vehicle')

plt.show()
