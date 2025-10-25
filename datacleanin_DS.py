import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("energyconsumption.csv")

# Info about dataset
print("\n--- Info ---")
df.info()   # this prints itself

# First 5 rows
print("\n--- Head ---")
print(df.head())

# Categorical vs Numerical
cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']

print("\nCategorical columns:", cat_col)
print("Numerical columns:", num_col)

# Duplicates
print("\n--- Duplicates ---")
print(df.duplicated())
print("Total duplicates:", df.duplicated().sum())
#df.plot(x="Customer_ID", y=' Units_Consumed', kind='line')
#df.plot.area(alpha=0.4)
#df.plot.bar()
#print(df.columns)
#print(df.describe())
#df.plot.hist(bins=50)
#df.plot.box()
#df.plot.hexbin(x ='Customer_ID', y =' Units_Consumed', gridsize = 25, cmap ='Oranges')
#df.plot.kde()
#df.plot(title='Customer_ID', xlabel='Index', ylabel=' Units_Consumed', grid=True)
#df.plot(figsize=(12, 6), title='Month', xlabel='Index', ylabel='Bill_Amount', grid=True)
df.plot.bar(stacked=True, figsize=(10, 6), title='City', xlabel='Index', ylabel='Customer_ID', grid=True)
plt.show()
