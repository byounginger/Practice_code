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



