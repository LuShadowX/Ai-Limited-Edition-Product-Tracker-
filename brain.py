import pandas as pd
print("Waking up the System Brain")
df=pd.read_csv("sneaker_data.csv")
print(df.head())
print(df.info())
print("Initial Data Cleaning")
df['Sale Price']=df['Sale Price'].str.replace('$','').str.replace(',','').astype(float)
df['Retail Price']=df['Retail Price'].str.replace('$','').str.replace(',','').astype(float)
print("Data Cleaning is done. Checking again")
print(df.info())
print(df[['Sale Price','Retail Price']].dtypes)

