#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:54:02 2020

@author: brett

Data Camp Unit 7

All about cleaning data
"""

# Simple loading and viewing

import pandas as pd
import os

os.chdir('/Users/brett/.spyder-py3/sandbox')

df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.info())

# Calculating summary statistics

print(df.describe())
print(df['Street Frontage'].describe())

print(df['Borough'].head())

print(df['Borough'].value_counts(dropna = False))

print(df['State'].value_counts(dropna = False))

print(df['Site Fill'].value_counts(dropna = False))

## Visualizing variables with histograms

import matplotlib.pyplot as plt

print(df['Existing Zoning Sqft'].describe())
    # Remember describe for descriptive stats since it can detect outliers
        # e.g. mean and median are far apart

df['Existing Zoning Sqft'].plot(kind = 'hist', rot = 70, logx = True, 
  logy = True)
plt.show()

df.columns

df.boxplot(column = 'Initial Cost', by = 'Borough', rot =90)
plt.show()

## This isn't working because it looks like the initial cost column has been
    # reformatted
    
## Visualizing with scatter plots

df.plot(kind = 'scatter', rot = 70, x = 'Initial Cost', y = 'Total Est. Fee')
plt.show()

## Reshaping data with melt

airquality = pd.read_csv('airquality.csv')

print(airquality.head())
print(airquality.tail())

airquality_melt = pd.melt(airquality, id_vars = 'Month')

print(airquality_melt.head())

## Customizing melt

airquality_melt = pd.melt(airquality, id_vars = 'Month', var_name = 'Measurement',
                          value_name = 'Value')

print(airquality_melt.head())

## Pivot data
    # Remember that it's the opposite of melting data
    
airquality_pivot = airquality_melt.pivot_table(index = 'Month', columns = 'Measurement',
                                               values = 'Value')

print(airquality_pivot.head())

## Reset the indexing of a df 

print(airquality_pivot.index)

airquality_pivot_reset = airquality_pivot.reset_index()

print(airquality_pivot_reset.index)

print(airquality_pivot_reset.head())

## Pivoting duplicate values on the mean using aggfunc = np.mean

import numpy as np

airquality_pivot = airquality_melt.pivot_table(index = 'Month', columns = 'Measurement',
                                               values = 'Value', aggfunc = np.mean)

print(airquality_pivot.head())

airquality_pivot = airquality_pivot.reset_index()

print(airquality_pivot.head())

## Splitting columns with .str

tb = pd.read_csv('tb.csv')

print(tb.head())

tb_melt = pd.melt(tb, id_vars = ['country', 'year'])

print(tb_melt.head())

tb_melt['gender'] = tb_melt.variable.str[0]

tb_melt['age_group'] = tb_melt.variable.str[1:]

print(tb_melt.head())

## Splitting columns with .get() or .split()

ebola = pd.read_csv('ebola.csv')

print(ebola.head())

ebola_melt = pd.melt(ebola, id_vars = ['Date', 'Day'], var_name = 'type_country',
                     value_name = 'counts')

print(ebola_melt.head())

ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

ebola_melt['cases'] = ebola_melt.str_split.str.get(0)

ebola_melt['country'] = ebola_melt.str_split.str.get(1)

## Concatenating rows

uber1 = pd.read_csv('uber1.csv')
uber2 = pd.read_csv('uber2.csv')
uber3 = pd.read_csv('uber3.csv')

full_uber = pd.concat([uber1, uber2, uber3]) # Remember that to concat you have
    # to pass a list

print(full_uber.shape)
print(full_uber.head())

## Concatenating columns

print(ebola_melt.head())
print(ebola_melt.shape)

status_country = ebola_melt[['cases', 'country']]
ebola_melt2 = ebola_melt.iloc[:, :5]

print(status_country.head())
print(ebola_melt2.head())

ebola_tidy = pd.concat([ebola_melt2, status_country], axis = 1)

print(ebola_tidy.shape)
print(ebola_tidy.head())

## Using glob() to match with * and pull all csv files in the cwd

import glob

pattern = '*.csv'

csv_files = glob.glob(pattern)

print(csv_files)

csv2 = pd.read_csv(csv_files[1])

print(csv2.head())

## Iterating through files and concatenating them into a list

frames = []

pattern2 = 'uber*.csv'

csv_files = glob.glob(pattern2)

for csv in csv_files:
    
    df = pd.read_csv(csv)
    
    frames.append(df)
    
uber = pd.concat(frames)

print(uber.shape)
print(uber.head())

### 1-to-1 data merging

site = pd.read_csv('site.csv')
visited = pd.read_csv('visited.csv')

print(site.head())
print(visited.head())

o2o = pd.merge(left = site, right = visited, left_on = 'name', right_on = 'site')

print(o2o)

## Many-to-1 data merging

visited2 = pd.read_csv('visited2.csv')

m2o = pd.merge(left = site, right = visited2, left_on = 'name', right_on = 'site')

print(m2o)

## Many-to-many data merging

survey = pd.read_csv('survey.csv')

names = [site, survey, visited]

for i in names:
    print(i)
    
m2m = pd.merge(left = survey, right = visited, left_on = 'taken', right_on = 'ident')

print(m2m.head())
print(site)

m2m2 = pd.merge(left = m2m, right = site, left_on = 'site', right_on = 'name')

print(m2m2.head())

## Converting data types

tips = pd.read_csv('tips.csv')

tips.columns
print(tips.info())

tips.sex = tips.sex.astype('category')

tips.smoker = tips.smoker.astype('category')

## Converting to numeric data

tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors = 'coerce')

tips['tip'] = pd.to_numeric(tips['tip'], errors = 'coerce')

print(tips.info())

## String parsing with regex

import re

prog = re.compile('\d{3}-\d{3}-\d{4}')

result = prog.match('545-323-2332')

print(bool(result))

## Extracting numericals with regex

matches = re.findall('\d+', 'I would like 4 bananas, 10 grapes, and 4, no 5 scoops')
print(matches)

## More pattern matching

# $123.45
# Australia
# 123-767-5309

pattern1 = bool(re.match(pattern = '\$\d{3}\.\d{2}', string = '$123.45'))
pattern2 = bool(re.match(pattern = '[A-Za-z]+', string = 'Australia'))
pattern3 = bool(re.match(pattern = '\d+-\d+-\d{4}', string = '123-767-5309'))


print(pattern1)
print(pattern2)
print(pattern3)

## Using some functions to clean data; will work on the tips data

print(tips.sex.head())

def recode_gender(gender):
    
    if gender == 'Female':
        return 0
    
    elif gender == 'Male':
        return 0
    
    else:
        return np.nan

tips['sex_recoded'] = tips.sex.apply(recode_gender)

print(tips.head())

## Lambda functions to clean data

print(tips.columns)
print(tips.tip)

tips['total_bill_recoded'] = tips.total_bill.apply(lambda x: x.replace('$', ''))
    # This doesn't work, only because there's no $ in the dataset. 
    
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])
    # Again, no $

## Dropping duplicates
    
# Create the new DataFrame: tracks
tracks = billboard[['year', 'artist', 'track', 'time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())

## Filling missing data with the mean

# Using airquality from above

print(airquality.columns)

oz_mean = airquality.Ozone.mean()

# use fillna to fill with the above variable

airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

print(airquality.info())

## Testing data with assert

assert ebola.notnull().all().all()

assert (ebola >= 0).all().all()

## Tying it all together

gapminder2 = pd.read_csv('gapminder_V2.csv')

print(gapminder2.describe())
print(gapminder2.shape)
print(gapminder2.columns)

import matplotlib.pyplot as plt

gapminder2.plot(kind = 'scatter', x = '1800', y = '1899')

plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

xlim = (20, 55)
ylim = (20, 55)

plt.show()

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

print(gapminder2.columns)
g1800s = gapminder2.iloc[:, 1:]
gapminder2.shape
g1800s.shape
g1800s.iloc[:,217]

assert g1800s.columns[217] == 'Life expectancy'

assert g1800s.iloc[:, 0:217].apply(check_null_or_valid, axis = 1).all().all()

assert g1800s['Life expectancy'].value_counts()[217] == 1    
    # There appear to be duplicates here
    
## Reshaping the data
gap_melt = pd.melt(gapminder2, id_vars = 'Life expectancy')

print(gap_melt.head())

gap_melt.columns = ['country', 'year', 'life_expectancy']

gap_melt.year = pd.to_numeric(gap_melt['year'])

assert gap_melt.country.dtypes == np.object

assert gap_melt.year.dtypes == np.int64

assert gap_melt.life_expectancy.dtypes == np.float64

## Check country spellings in the dataset

countries = gap_melt['country']

countries = countries.drop_duplicates()

pattern = '^[A-Za-z \.]+$'

mask = countries.str.contains(pattern)

mask_inverse = ~mask

invalid_countries = countries[mask_inverse]

print(invalid_countries)

## Further processing

assert pd.notnull(gap_melt.country).all()

assert pd.notnull(gap_melt.year).all()

gap_melt = gap_melt.dropna()

print(gap_melt.shape)

## Plotting this stuff

plt.subplot(2,1,1)

gap_melt.life_expectancy.plot(kind = 'hist')

gap_agg = gap_melt.groupby('year')['life_expectancy'].mean()

print(gap_agg.head())

plt.subplot(2,1,2)

gap_agg.plot()

plt.title = 'Life expectancy over the years'
plt.xlabel = 'Years'
plt.ylabel = 'Life expectancy'

plt.tight_layout()
plt.show()

## Done!
