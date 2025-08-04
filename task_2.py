import numpy as np
import pandas as pd


# for analysis data
df = pd.read_csv(r'C:\Users\ektas\OneDrive\Desktop\kaggle\marketing_campaign (1).csv', sep='\t')
print(df)
# print(df.columns)
# print(df.info)
# print(df.describe())
# print(df.shape)
# print(df.dtypes)
# print(df.size)
# print()

# for analysis data ends

# Identify and handle missing values
print(df.isnull().sum())

# Identify and handle missing values ends

# drops all rows with at least one missing value
df['Income'] = df['Income'].fillna(df['Income'].median())
df = df.dropna()
# print(df.isnull().sum())

# drops all rows with at least one missing value ends


# Drop duplicate values : 1.check is their any duplicate values
drop_dup=df.duplicated().sum()
print(drop_dup)
df = df.drop_duplicates()
print(df)

# Drop duplicate values ends


# Standardize text values
print(df['Education'].nunique())
print(df['Marital_Status'].nunique())
df['Education'] = df['Education'].str.strip().str.lower()
df['Education'] = df['Education'].replace({
    '2n cycle': 'undergraduate',
    'basic': 'basic',
    'graduation': 'graduate',
    'master': 'postgraduate',
    'phd': 'doctorate'
})


df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].replace({
    'married': 'married',
    'together': 'married',
    'single': 'single',
    'divorced': 'divorced',
    'widow': 'widowed',
    'widowed': 'widowed',
    'alone': 'single',
    'absurd': 'single',
    'yolo': 'single'
})
print(df[['Education','Marital_Status']])
print(df['Education'].value_counts())
print(df['Marital_Status'].value_counts())
print(df)
# Standardize text values ends


# Rename column headers to be clean and uniform (e.g., lowercase, no spaces).
df.columns = (
    df.columns
    .str.strip()                  #remove extra whitespaces from Start and end
    .str.lower()                  # convert all column names into lowercase
    .str.replace(' ', '_')        # remove space from underscore (_)
    .str.replace('-', '_')        #replace hyphen (-) from  underscore(_)
    .str.replace(r'[^\w]', '', regex=True)  # Remove special characters (like !, @, ., /)
)
print(df)
# Rename column headers to be clean and uniform (e.g., lowercase, no spaces).ends

# Check and fix data types.
df['dt_customer'] = pd.to_datetime(df['dt_customer'],format='%d-%m-%Y')
print(df.dtypes)

# Check and fix data types ends




