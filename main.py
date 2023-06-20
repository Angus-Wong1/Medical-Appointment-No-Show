import pandas as pd

df = pd.read_csv('data.csv')

print(df.isnull().sum()) # prints amount of null per col

#print(df.fillna(df.median(),inplace=True)) # Fill missing values with the median of the column

df.drop_duplicates(inplace=True)

df.to_csv('cleaned_data.csv',index=False)

