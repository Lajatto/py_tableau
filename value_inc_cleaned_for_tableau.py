# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:13:05 2023

@author: rbben
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <--- format to read csv

data = pd.read_csv('transaction.csv', sep=';')

#sumary of the data. This is to check the data types too! 
data.info()

#working with calculations 

#computations 

#CostPerTransaction Column Calculation 

#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
SellingPricePerItem = data['SellingPricePerItem']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding computation columns to the dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#Using the round function

roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#change column type 

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
my_date = day+'-'+data['Month']+'-'+year

#return new column for date into data
data['date'] = my_date

#using split to split the client keywords field
#new_var = column.str.split('sep', expand = true)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns from the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientContract'] = split_col[2]

#using the replace function to remove the square brackets

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['ClientContract'] = data['ClientAge'].str.replace(']', '')

#using the lower function to change item to lowercase 

data['ItemDescription'] = data['ItemDescription'].str.lower()

#merging datasets
#bringing in a new dataset into our existing one 

seasons = pd.read_csv('value_inc_seasons.csv', sep=';') 

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping a few columns 
# df = df.drop('columname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Year', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Month', axis = 1)

#dropping multiple columns in one line 
#data = data.drop(['Year', 'Month'], axis = 1)

#exporting CSV

data.to_csv('value_inc_transactions_cleaned.csv', index = False)
