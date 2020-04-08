#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:40:32 2020

@author: brett

Merging DataFrames in Pandas
"""

import os
import pandas as pd

os.chdir('/Users/brett/.spyder-py3/Practice_code/Datasets')

## Reading DataFrames from multiple files in a loop

filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

dataframes = []

for f in filenames:
    dataframes.append(pd.read_csv(f))
    
print(dataframes[0].head())

gold = dataframes[0].copy()
silver = dataframes[1].copy()
bronze = dataframes[2].copy()

## Combining DataFrames from multiple data files

medals = gold.copy()

new_labels = ['NOC', 'Country', 'Gold']

medals.columns = new_labels

medals['Silver'] = silver['Total']

medals['Bronze'] = bronze['Total']

medals.head()

## Sorting DataFrame with the Index & columns

weather = pd.read_csv('pittsburgh2013.csv', parse_dates = True, index_col = 
                      'Date')

weather0 = weather.iloc[:,0]

weather1 = weather0.resample('M').max()

weather2 = weather1.sort_index()

weather3 = weather1.sort_index(ascending = False)

weather4 = weather1.sort_values('Max TemperatureF')

## Reindexing DataFrame from a list

year = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']

weather2 = weather1.reindex(year)

weather3 = weather1.reindex(year).ffill()

## Reindexing using another DataFrame Index

names_1981 = pd.read_csv('names1981.csv', index_col = 0)
names_1881 = pd.read_csv('names1881.csv', index_col = 0)

common_names = names_1981.reindex(names_1881.index)
    # Error: raise ValueError("cannot reindex from a duplicate axis")

names_1981[names_1981.index.duplicated()]

names_1981 = names_1981[~names_1981.index.duplicated()]
names_1881 = names_1881[~names_1881.index.duplicated()]

common_names = names_1981.reindex(names_1881.index)

common_names.shape

common_names = common_names.dropna()

common_names.shape

## Broadcasting in arithmetic formulas

temps_f = weather[['Min TemperatureF','Mean TemperatureF', 'Max TemperatureF']]

temps_c = (temps_f - 32) * 5/9

temps_c.columns = temps_c.columns.str.replace('F','C')

temps_c.head()

## Computing percentage growth of GDP

gdp = pd.read_csv('gdp_usa.csv', parse_dates = True, index_col = 'DATE')

post2008 = gdp['2008':]

yearly = post2008.resample('A').last()

yearly['growth'] = yearly.pct_change() * 100

## Converting currency of stocks

sp500 = pd.read_csv('sp500.csv', parse_dates = True, index_col = 'Date')

exchange = pd.read_csv('exchange.csv', index_col = 'Date', parse_dates = True)

dollars = sp500[['Open','Close']]

pounds = dollars.multiply(exchange['GBP/USD'], axis = 'rows')

## CH 2 ##

## Appending pandas Series

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', parse_dates = True, index_col = 'Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', parse_dates = True, index_col = 'Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', parse_dates = True, index_col = 'Date')

jan_units = jan['Units']
feb_units = feb['Units']
mar_units = mar['Units']

# Append/chain the units together:

quarter1 = quarter1.sort_index()

print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

print(quarter1.sum())

## Concatenating pandas Series along row axis

units = []

for month in [jan, feb, mar]:
    units.append(month['Units'])
    
quarter1 = pd.concat(units, axis='rows')   

print(quarter1.loc['jan 27, 2015':'feb 2, 2015']) 
    
## Appending DataFrames with ignore_index

names_1981 = pd.read_csv('names1981.csv')
names_1881 = pd.read_csv('names1881.csv')

names_1981['year'] = 1981
names_1881['year'] = 1881

combined_names = names_1881.append(names_1981, ignore_index=True)

names_1981.shape
names_1881.shape
combined_names.shape

# combined_names[combined_names['name']=='Morgan'] 

## Concatenating pandas DataFrames along column axis

weather = pd.read_csv('pittsburgh2013.csv', index_col='Date', parse_dates=True)

weather_max = weather['Max TemperatureF']

weather_mean = weather['Mean TemperatureF']

weather_list = [weather_max, weather_mean]

weather2 = pd.concat(weather_list, axis=1)

## Reading multiple files to build a DataFrame

medal_types = ['bronze', 'silver', 'gold']

medals = []

for medal in medal_types:
    
    file_name = "%s_top5.csv" % medal
    
    columns = ['Country', medal]
    
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', 
                           names=columns)
    
    medals.append(medal_df)
    
medals_df = pd.concat(medals, axis='columns')

medals_df

## Concatenating vertically to get MultiIndexed rows

medal_types = ['bronze', 'silver', 'gold']

medals = []

for medal in medal_types: 
    
    file_name = "%s_top5.csv" % medal
    
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    medals.append(medal_df)
    
medals = pd.concat(medals, keys=['bronze','silver','gold'])    

medals

## Slicing MultiIndexed DataFrames

medals_sorted = medals.sort_index(level=0)

print(medals_sorted.loc[('bronze','Germany')])
print(medals_sorted.loc['silver'])

idx = pd.IndexSlice # This alias is required when slicing on an inner index

medals_sorted.loc[idx[:, 'United Kingdom'], :]

## Concatenating horizontally to get MultiIndexed columns

sales = pd.read_csv('sales-feb-2015.csv', index_col='Date', parse_dates=True)

dataframes = [sales[sales['Product']=='Hardware'], sales[sales['Product']==
                    'Software'], sales[sales['Product']=='Service']]

february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 
                                               'Service'])

february.info()

idx = pd.IndexSlice

slice_2_8 = february.loc['Feb.2,2015':'Feb.8,2015', idx[:, 'Company']]

slice_2_8

## Concatenating DataFrames from a dict

month_list = [('january',jan), ('february',feb), ('march',mar)]

month_dict = {}

for month_name, month_data in month_list:
    
    month_dict[month_name] = month_data.groupby('Company').sum()
    
sales = pd.concat(month_dict)

sales

idx = pd.IndexSlice

sales.loc[idx[:, 'Mediacore'], :]

## Concatenating DataFrames with inner join

medal_types = ['bronze', 'silver', 'gold']

medals = []

for medal in medal_types:
    
    file_name = "%s_top5.csv" % medal
    
    medal_df = pd.read_csv(file_name, index_col='Country')

    medals.append(medal_df)

bronze = medals[0]
silver = medals[1]
gold = medals[2]

medal_list = [bronze, silver, gold]

medals2 = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, 
                    join='inner')

## Resampling & concatenating DataFrames with inner join

china = pd.read_csv('gdp_china.csv', index_col='Year', parse_dates=True)

us = pd.read_csv('gdp_usa.csv', index_col='DATE', parse_dates=True)

china_annual = china.resample('A').last().pct_change(10).dropna()

us_annual = us.resample('A').last().pct_change(10).dropna()

gdp = pd.concat([china_annual, us_annual], join='inner', axis=1)

print(gdp.resample('10A').last())

## CH 3 ##

## Using merge_asof()

auto = pd.read_csv('auto-mpg.csv')

oil = pd.read_csv('oil_price.csv')

auto['yr'] = pd.to_datetime(auto['yr'])

oil['Date'] = pd.to_datetime(oil['Date'])

merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

merged.tail()

yearly = merged.resample('A', on='Date')[['mpg', 'Price']].mean()

yearly

## CH 4 ##



