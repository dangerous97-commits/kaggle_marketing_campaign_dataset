import pandas as pd

# for reading datetime

df=pd.read_csv(r'C:\Users\ektas\OneDrive\Documents\marketing_kaggle_clean.csv')
df['dt_customer'] = pd.to_datetime(df['dt_customer'])
# print(df.dtypes)

# for reading datetime ends


# for reading first time 'datetime'

df=pd.read_csv(r'C:\Users\ektas\OneDrive\Documents\marketing_campaign_kaggle.csv')
df['dt_customer'] = pd.to_datetime(df['dt_customer'],format='%d-%m-%Y')
df.to_csv(r'C:\Users\ektas\OneDrive\Documents\marketing_kaggle_clean.csv')
print(df.dtypes)

# Check and fix data types (e.g.,date as datetime).
df['dt_customer'] = pd.to_datetime(df['dt_customer'],format='%d-%m-%Y')
print(df.dtypes)

