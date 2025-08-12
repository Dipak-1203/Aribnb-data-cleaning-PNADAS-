import pandas as pd

file_path = r"C:\Users\dp394\OneDrive\Desktop\pyhton Libraries\Pandas\project\airbnb.csv"
df= pd.read_csv(file_path)
print(df.head())

df.drop(columns=['reviews per month',
       'review rate number', 'calculated host listings count',
       'availability 365', 'house_rules', 'license', 'id']  , inplace=True)

print(df.columns)
print(df.shape)

# RENAMING THE COLUMNS
df.rename(columns={"NAME" : "Name"} , inplace=True)
print(df.columns)
new_columns_name=[]
for i in df.columns:
    new_columns_name.append(i.upper())
    
print(new_columns_name)

new_columns_data = df.copy()
new_columns_data.columns = new_columns_name
print(new_columns_data)

# DROPPING DUPLICATES

print(df.duplicated().sum()) # actule count of duplicates
print(df.duplicated().value_counts()) # give the actule count of true and false
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())

#REMOVE THE NaN VALUES FROM THE DATA SET 

df.drop(columns=['last review'],inplace=True)
df.dropna(inplace=True)
print(df.isna().sum()) # give every columns NaN Values count 


# CLEANING INDIVIDUAL COLUMNS
df['host_identity_verified'].str.upper()
df['host_identity_verified'] = df['host_identity_verified'].str.upper()
df['instant_bookable'].apply(lambda x: 1 if x == True else 0)
df['instant_bookable'] = df['instant_bookable'].apply(lambda x: 1 if x == True else 0)
new_columns_data = df['instant_bookable']
df.reset_index(inplace=True)
df.drop(columns=['index'],inplace=True)
print(new_columns_data)
print(df.head(10))


# REPLACE $ INTO ''

df["price"].str.replace("$", "")
df["price"] = df["price"].str.replace("$", "") # here we remove $ sign
#here we remove comma ,
df["price"].str.replace(",", "")
df["price"] = df["price"].str.replace(",", "") 
df['price'] = df['price'].astype(int)
print(type(df['price'][4]))
new_columns_data = df['price']
print(new_columns_data.head(5))


# SAVE FILE

df.to_csv("AIRBNB CLEANIN.CSV")

