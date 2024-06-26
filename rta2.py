import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('RTA Dataset.csv')


df.fillna('Unknown', inplace=True)

cross_tab = pd.crosstab(df['Sex_of_driver'], df['Type_of_vehicle'])


print(cross_tab)


cross_tab_norm = cross_tab.div(cross_tab.sum(axis=1), axis=0)

cross_tab_norm.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')
plt.title('Proportion of Vehicle Types Driven by Gender')
plt.xlabel('Sex of Driver')
plt.ylabel('Proportion')
plt.legend(title='Type of Vehicle', bbox_to_anchor=(0.85, 0.8), loc='upper left')
plt.xticks(rotation=0)
plt.show()
