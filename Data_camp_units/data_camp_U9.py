#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:23:17 2020

@author: brett

Manipulating DataFrames in Pandas

"""

import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

os.chdir('/Users/brett/.spyder-py3/sandbox/Datasets')

# Positional and label indexing

election = pd.read_csv('pennsylvania2012_turnout.csv', index_col = 'county')

election.head()
election.columns

election.loc['Bedford']

x = 4

y = 4

print(election.iloc[x,y] == election.loc['Bedford','winner'])


## Indexing and column rearrangement

results = election[['winner','total','voters']]
results.head()

## Slicing rows

p_counties = election.loc['Perry':'Potter']
p_counties2 = election.loc['Potter':'Perry':-1] # Can slice in opposite order
p_counties.head()
p_counties2.head()

## Slicing columns

left_columns = election.loc[:,:'Obama']
middle_columns = election.loc[:,'Obama':'winner']
right_columns = election.loc[:,'Romney':]

## Subselecting DFs with lists

rows = ['Philadelphia', 'Centre', 'Fulton']
cols = ['winner', 'Obama', 'Romney']

three_counties = election.loc[rows,cols]
three_counties

## Thresholding data (using Booleans to subset data)

high_turnout = election.turnout > 70
high_turnout_df = election[high_turnout]
high_turnout_df

## Filtering columns using other columns

too_close = election.margin < 1
election.winner[too_close] = np.nan
election.info()

## Filtering using NaNs

titanic = pd.read_csv('titanic.csv')

df = titanic[['age','cabin']]
df.shape
print(df.dropna(how = 'any').shape) # if any NaNs are present drop whole row
print(df.dropna(how = 'all').shape) # if entire row is NaN, drop it
print(df.dropna(thresh = 1000, axis = 'columns').shape) # Drop any columns with 
    # more than 1000 NaNs

## Using apply to transform a column 
    
def to_celsius(F):
    return 5/9*(F - 32)

weather = pd.read_csv('pittsburgh2013.csv')

df_celsius = to_celsius(weather[['Mean TemperatureF', 'Mean Dew PointF']])
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

## Using .map() with a dictionary

red_vs_blue = {'Obama':'blue','Romney':'red'}

election['color'] = election.winner.map(red_vs_blue)
election.head()

## Using vectorized functions

turnout_zscore = zscore(election['turnout'])
print(type(turnout_zscore))
election['turnout_zscore'] = turnout_zscore
election.head()

## Index values and names
# Remember that indexs are immutable like dictionary keys!
    # You can't change individual indexes

sales = pd.read_csv('sales.csv')
sales.head()
sales.index = range(len(sales))
sales

## Changing the index of a DataFrame

sales = pd.read_csv('sales.csv', index_col = 'month')


new_idx = [x.upper() for x in sales.index]

sales.index = new_idx
sales

## Changing index name labels 

sales.index.name = 'MONTHS'
sales.columns.name = 'PRODUCTS'
sales

## Build the index first, then the DF

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales.index = months

## Extracting data with multiline indexing

sales2 = pd.read_csv('sales2.csv', index_col = ['state','month'])
sales2
print(sales2.loc[['CA','TX']])
print(sales2.loc['CA':'TX'])

## Setting/sorting multiline index

sales2 = pd.read_csv('sales2.csv')
sales2
sales2 = sales2.replace(np.nan, '', regex = True)
sales2 = sales2.set_index(['state','month'])
sales2 = sales2.sort_index()

## Using .loc with non-unique indexes

sales2 = pd.read_csv('sales2.csv') 
'''Stopped here. Need to reorganize the DF
to include the multiline index by month. Will look online for this'''

sales = sales2.set_index(['state'])

print(sales.loc['NY'])

## Index multiple levels with multiindexing

sales = sales2.set_index(['state','month'])

NY_month1 = sales.loc[('NY',1),:]

CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

all_month2 = sales.loc[(slice(None),2),:]

print(sales, CA_TX_month2, all_month2)
print(CA_TX_month2)
print(all_month2)

## Pivoting single variables

users = pd.read_csv('users.csv')

users_pivot = users.pivot(index = 'weekday', columns = 'city', 
                          values = 'visitors')
users_pivot

## Pivoting all variables

signups_pivot = users.pivot(index = 'weekday', columns = 'city', 
                            values = 'signups')

signups_pivot

pivot_all = users.pivot(index = 'weekday', columns = 'city')

pivot_all

# Stacking and unstacking I

users_multi = users.set_index(['city','weekday'])

by_weekday = users_multi.unstack(level = 'weekday')

by_weekday 

by_weekday = by_weekday.stack(level = 'weekday')

## Stacking and unstacking II

bycity = by_weekday.unstack(level = 'city')

bycity

print(bycity.stack(level = 'city'))

## Restoring the index order

newusers = bycity.stack(level = 'city')

newusers

newusers = newusers.swaplevel(0,1)

newusers = newusers.sort_index()

print(newusers.equals(by_weekday))

## Adding names for readability

visitors_by_city_weekday = users.pivot(index = 'weekday', columns = 'city', 
                                       values = 'visitors')

visitors_by_city_weekday = visitors_by_city_weekday.reset_index()

visitors_by_city_weekday

visitors = pd.melt(visitors_by_city_weekday, id_vars = ['weekday'], 
                   value_name = 'visitors')

visitors

## Going from wide to long

skinny = pd.melt(users, id_vars = ['weekday', 'city'])

skinny

## Obtaining key-value pairs with melt

users_idx = users.set_index(['city','weekday'])

users_idx

kv_pairs = pd.melt(users_idx, col_level = 0)

kv_pairs

## Setting up a pivot table

by_city_day = users.pivot(index = 'weekday', columns = 'city')

by_city_day

## Using other aggregations in pivot tables

count_by_weekday1 = users.pivot_table(index = 'weekday', aggfunc = 'count')

count_by_weekday1

count_by_weekday2 = users.pivot_table(index = 'weekday', aggfunc = len)

print(count_by_weekday1.equals(count_by_weekday2))

## Using margins in pivot tables

signups_and_visitors = users.pivot_table(index = 'weekday', aggfunc = sum)

signups_and_visitors

signups_and_visitors_total = users.pivot_table(index = 'weekday', 
                                               aggfunc = sum, margins = True)

signups_and_visitors_total

## Grouping by multiple columns

titanic = pd.read_csv('titanic.csv')

by_class = titanic.groupby('pclass')

count_by_class = by_class['survived'].count()

count_by_class

by_mult = titanic.groupby(['embarked','pclass'])

count_mult = by_mult['survived'].count()

count_mult

## Grouping by another series

life = pd.read_csv('gapminder_tidy.csv', index_col = 'Country')

regions = pd.read_csv('gapminder.csv', index_col = 'country')

life.columns
regions.columns
     
    # Will skip this since it's too much of a pain

## Computing multiple aggregates of multiple columns
    
by_class = titanic.groupby('pclass')

by_class_sub = by_class[['age','fare']]

aggregated = by_class_sub.agg(['max','median'])

print(aggregated.loc[:,('age','max')]) # This selects the main column and sub-
    # column

aggregated.head()

## Aggregating on index levels/fields

gapminder = pd.read_csv('gapminder_tidy.csv', index_col = ['Year','region',
                        'Country']).sort_index()
    
by_year_region = gapminder.groupby(level = ['Year', 'region'])

    # Make a function to calculate the spread

def spread(series):
    return series.max() - series.min()

aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

aggregated = by_year_region.agg(aggregator)

print(aggregated.tail())

## Grouping on a function of the index

sales = pd.read_csv('sales-feb-2015.csv', index_col = 'Date', parse_dates = True)

by_day = sales.groupby(sales.index.strftime('%a'))

units_sum = by_day['Units'].sum()

print(units_sum)

## Detecting outliers with Z-scores

# from scipy.stats import zscore

gapminder = pd.read_csv('gapminder_tidy.csv', index_col = 'Country')

standardized = gapminder.groupby('region')[['life',
                                'fertility']].transform(zscore)

outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

gm_outliers = gapminder.loc[outliers]

gm_outliers

## Filling missing data (imputation) by group

by_sex_class = titanic.groupby(['sex','pclass'])

def impute_median(series):
    
    return series.fillna(series.median())

titanic.age = by_sex_class['age'].transform(impute_median)

titanic.age.tail(10)

## Other transformations with .apply

regional = gapminder.groupby('region')

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})

reg_disp = regional.apply(disparity)

    # Function doesn't work; keep moving

## Grouping and filtering with .apply()

by_sex = titanic.groupby('sex')

def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()

c_surv_by_sex = by_sex.apply(c_deck_survival)

c_surv_by_sex

## Grouping and filtering with .filter()

by_company = sales.groupby('Company')

by_com_sum = by_company['Units'].sum()

by_com_sum

by_com_filt = by_company.filter(lambda g: g['Units'].sum() > 35)

by_com_filt

## Filtering and grouping with .map()

under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})


survived_mean1 = titanic.groupby(under10)['survived'].mean()

survived_mean2 = titanic.groupby([under10,'pclass'])['survived'].mean()

print(survived_mean1)
survived_mean2

## Using .value_counts() for ranking

medals = pd.read_csv('all_medalists.csv')

country_names = medals['NOC']

medal_counts = country_names.value_counts()

medal_counts.head(15)

## Using .pivot_table() to count medals by type

counted = medals.pivot_table(index = 'NOC', columns = 'Medal', 
                             values = 'Athlete', aggfunc = 'count')

counted['totals'] = counted.sum(axis = 'columns')

counted = counted.sort_values('totals', ascending = False)

counted.head(15)

## Applying .drop_duplicates()

ev_gen = medals[['Event_gender','Gender']]

ev_gen_uniques = ev_gen.drop_duplicates()

ev_gen_uniques

## Finding possible errors with .groupby()

medals_by_gender = medals.groupby(['Event_gender','Gender'])

medal_count_by_gender = medals_by_gender.count()

medal_count_by_gender

## Locating suspicious data

sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

suspect = medals[sus]

suspect

## Using .nunique() to rank by distinct sports

country_grouped = medals.groupby('NOC')

Nsports = country_grouped.Sport.nunique()

Nsports = Nsports.sort_values(ascending = False)

Nsports.head(15)

## Counting USA vs. USSR Cold War Olympic Sports

during_cold_war = (medals.Edition >= 1952) & (medals.Edition <= 1988)

is_usa_urs = medals.NOC.isin(['USA','URS'])

cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

country_grouped = cold_war_medals.groupby('NOC')

Nsports = country_grouped['Sport'].nunique().sort_values(ascending = False)

Nsports

## Counting USA vs. USSR Cold War Olympic Medals

medals_won_by_country = medals.pivot_table(index = 'Edition', columns = 'NOC',
                                           values = 'Athlete', 
                                           aggfunc = 'count')

cold_war_usa_urs_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]

most_medals = cold_war_usa_urs_medals.idxmax(axis = 'columns')

most_medals.value_counts()

most_medals

## Visualizing USA Medal Counts by Edition: Line Plot

usa = medals[medals['NOC'] == 'USA']

usa_medals_year = usa.groupby(['Edition','Medal'])['Athlete'].count()

usa_medals_year

usa_medals_year = usa_medals_year.unstack(level = 'Medal')

usa_medals_year.plot()

## Visualizing USA Medal Counts by Edition: Area Plot

usa_medals_year.plot.area()

## Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals

medals.Medal = pd.Categorical(values = medals.Medal, categories = 
                              ['Bronze','Silver','Gold'], ordered = True)

usa = medals[medals.NOC == 'USA']

usa_medals_year = usa.groupby(['Edition','Medal'])['Athlete'].count()

usa_medals_year = usa_medals_year.unstack(level = 'Medal')

usa_medals_year.plot.area()

## DONE! 




