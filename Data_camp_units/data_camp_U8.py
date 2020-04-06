#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:36:20 2020

@author: brett

Data Camp Unit 8

Pandas Foundations
"""

import os

os.chdir('/Users/brett/.spyder-py3/sandbox/Datasets')

### Converting a df to a numpy array

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('world_population.csv')

df_values = df1.values

np_log10 = np.log10(df_values)

df_log10 = np.log10(df1)

[print(x, 'has type', type(eval(x))) for x in ['df1', 'df_values', 'np_log10', 'df_log10']]

### Zip lists to build DFs

list_keys = ['Country', 'Total'] 

list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]

zipper = list(zip(list_keys, list_values))

print(zipper)

dta = dict(zipper)

print(dta)

df = pd.DataFrame(dta)

print(df)

### Change the column headers

labels = list(['Place', 'Pop'])

df.columns = labels

print(df)

### Broadcasting to fill rows of a DF

cities = ['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 
          'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 
          'Hannastown', 'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 
          'Great bend']

state = 'PA'

dta = {'state':state, 'cities':cities}

df = pd.DataFrame(dta)

print(df)

### Delimiters, headers and extensions

df1 = pd.read_csv('messy_stock_data.tsv')

print(df1.head())

df2 = pd.read_csv('messy_stock_data.tsv', header = 3, delimiter = ' ', 
                  comment = '#')

print(df2.head())            

### Plotting DFs

df = pd.read_csv('weather_data_austin_2010.csv')
df.head()
df = df.iloc[:,:3]

df.plot()
plt.show()

df.plot(subplots = True)

df.columns

df['DewPoint'].plot()

column_list2 = ['Temperature', 'DewPoint']

df[column_list2].plot()

pd.DataFrame()

### Pandas scatter plots

df = pd.read_csv('auto-mpg.csv')
df.head()

df.plot(kind = 'scatter', x = 'hp', y = 'mpg')
plt.title('fuel efficiency')
plt.xlabel('hp')
plt.ylabel('mpg')
plt.show()

### Pandas hist, cdf, pdf

# For PDFs, normed = True
# For CDFs, normed = True and cumulative = True

df = pd.read_csv('tips.csv')
df.columns

df['fraction'] = df['tip']/df['total_bill']

df.head()

fig, axes = plt.subplots(nrows = 2, ncols = 1)
df.fraction.plot(ax = axes[0], kind = 'hist', bins = 30, normed = True, 
                 range = (0,0.3))
df.fraction.plot(ax = axes[1], kind = 'hist', bins = 30, normed = True, 
                 range = (0,0.3), cumulative = True)
plt.show()

### More plotting with min and mean methods

df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

df.head()
df.columns

print(df['Engineering'].min())
print(df['Engineering'].max())

mean = df.mean(axis = 'columns')

mean.plot()
plt.show()

### Plotting quantiles

df = pd.read_csv('life_expectancy_at_birth.csv')

df.columns

print(df['2015'].count())

print(df.quantile([0.05,0.95]))

years = ['1800','1850','1900','1950','2000']

df[years].plot(kind = 'box')
plt.show()

### Filtering, then counting

df.head()
df.columns

df[df['Life expectancy'] == 'Algeria'].count()

### Separating and summarizing

df = pd.read_csv('auto-mpg.csv')

global_mean = df.mean()
global_std = df.std()

df.columns

us_df = df[df['origin'] == 'US']

us_mean = us_df.mean()
us_std = us_df.std()

print(us_mean - global_mean)
print(us_std - global_std)

### Separating and plotting

titanic = pd.read_csv('titanic.csv')

titanic.columns

fig, axes = plt.subplots(nrows = 3, ncols = 1)
titanic.loc[titanic['pclass'] == 1].plot(ax = axes[0], y = 'fare', kind = 'box')
titanic.loc[titanic['pclass'] == 2].plot(ax = axes[1], y = 'fare', kind = 'box')
titanic.loc[titanic['pclass'] == 3].plot(ax = axes[2], y = 'fare', kind = 'box')
plt.show()

### Reading and slicing times


'''Remember that you can parse date/time with a few arguments to pd.read_csv()
'''

#df1 = pd.read_csv(filename, parse_dates = ['date'])
#df2 = pd.read_csv(filename, parse_dates = True, index_col = 'Date')

### Creating and using a DateTime index

'''You can convert a list of date/time strings into an index and merge this 
with an existing df'''

#time_format = '%Y-%m-%d %H:%M'
#
#my_datetimes = pd.to_datetime(datelist, format = time_format)
#
#time_series = pd.Series(temperature_list, index = my_datetimes)

### DateTime partial string indexing and slicing

df0 = pd.read_csv('date_index.csv', parse_dates = True, index_col = 'Date')
df0 = df0.rename(columns = {'Unnamed: 1': 'Temperature'})
df0

df1 = df0.loc['2010-01-01':'2010-01-02']
df2 = df0.loc['2010-12-31']

### Reindexing

'''To merge rows from different dfs, you may need to reindex them. If there
are missing values (or rows not shared) it may input NaN. Thus, you'll have to 
use method = 'ffill' to forward fill it'''

df3 = df2.reindex(df1.index)

df4 = df2.reindex(df1.index, method = 'ffill')

### Resampling and frequency

df = pd.read_csv('weather_data_austin_2010.csv', parse_dates = True,
                 index_col = 'Date')

df1 = df.Temperature.resample('6h').mean()
df2 = df.Temperature.resample('D').count()
df1.head()
df2.head()

### Separating and resampling

august = df['Temperature']['2010-August']
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature']['2010-February']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

### Rolling mean and frequency

unsmoothed = df['Temperature']['2010-08-01':'2010-08-15']

smoothed = unsmoothed.rolling(window = 24).mean()

august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

august.plot(kind = 'line')
plt.show()

### Resample and roll with it

august = df['Temperature']['2010-08']

daily_highs = august.resample('D').max()

daily_highs_smooth = daily_highs.rolling(window = 7).mean()
daily_highs_smooth
daily_highs

### Method chaining and filtering

df = pd.read_csv('austin_airport_departure_data_2015_july.csv', parse_dates = 
                 True, index_col = 'Date (MM/DD/YYYY)')

df.columns = df.columns.str.strip() # Strip whitespace from column names

dallas = df['Destination Airport'].str.contains('DAL')

daily_departures = dallas.resample('D').sum()

stats = daily_departures.describe()
stats

### Missing values and interpolation

ts1 = pd.read_csv('ts1.csv', parse_dates = True, index_col = 'Date')
ts2 = pd.read_csv('ts2.csv', parse_dates = True, index_col = 'Date')

ts2_interp = ts2.reindex(ts1.index).interpolate(how = 'linear')

differences = np.abs(ts1 - ts2_interp)

differences.describe()

### Time zones and conversion

df = pd.read_csv('austin_airport_departure_data_2015_july.csv')

df.columns = df.columns.str.strip()

mask = df['Destination Airport'] == 'LAX'

la = df[mask]

times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + 
                                  la['Wheels-off Time'])

times_tz_central = times_tz_none.dt.tz_localize('US/Central')
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

### Plotting time series, date-time indexing

df = pd.read_csv('weather_data_austin_2010.csv')
final_cols = ['Temperature', 'Date']
df2 = df[final_cols]

df2.plot()
plt.show()

df2.Date = pd.to_datetime(df2['Date'])

df2.set_index('Date', inplace = True)

df2.plot()
plt.show()

### Plotting date ranges through partial indexing

df = pd.read_csv('weather_data_austin_2010.csv', parse_dates = True, 
                 index_col = 'Date')

df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()

df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()

### Re-assigning column names 

df = pd.read_csv('NOAA_QCLCD_2011_hourly_13904.txt', delimiter = ',', 
                 header = None)

column_labels = 'Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,dry_bulb_cel,dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,dew_point_faren,dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,relative_humidityFlag,wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,value_for_wind_character,value_for_wind_characterFlag,station_pressure,station_pressureFlag,pressure_tendency,pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag,record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk'

column_labels_list = list(column_labels.split(','))

df.columns = column_labels_list

list_to_drop = 'sky_conditionFlag,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_farenFlag,dry_bulb_celFlag,wet_bulb_farenFlag,wet_bulb_celFlag,dew_point_farenFlag,dew_point_celFlag,relative_humidityFlag,wind_speedFlag,wind_directionFlag,value_for_wind_character,value_for_wind_characterFlag,station_pressureFlag,pressure_tendencyFlag,pressure_tendency,presschange,presschangeFlag,sea_level_pressureFlag,hourly_precip,hourly_precipFlag,altimeter,record_type,altimeterFlag,junk'

list_to_drop2 = list(list_to_drop.split(','))

df_dropped = df.drop(list_to_drop2, axis = 'columns')

df_dropped.head()

### Clean and tidy the df

df_dropped['date'] = df_dropped['date'].astype(str)

df_dropped['Time'] = df_dropped['Time'].apply(lambda x: '{:0>4}'.format(x))

date_string = df_dropped['date'] + df_dropped['Time']

date_times = pd.to_datetime(date_string, format = '%Y%m%d%H%M')

df_clean = df_dropped.set_index(date_times)

df_clean.head()

### Cleaning numeric columns ### Come back to this. Need to get a inverse
### boolean of the string below to capture relevant columns

keepers = 'Wban,date,Time,StationType,sky_condition,visibility,dry_bulb_faren,dry_bulb_cel,wet_bulb_faren,wet_bulb_cel,dew_point_faren,dew_point_cel,relative_humidity,wind_speed,wind_direction,station_pressure,sea_level_pressure'

columns_labels_list2 = list(keepers.split(','))

df = df[columns_labels_list2]

df['date'] = df['date'].astype(str)

df['Time'] = df['Time'].apply(lambda x: '{:0>4}'.format(x))

date_string = df['date'] + df['Time']

date_times = pd.to_datetime(date_string, format = '%Y%m%d%H%M')

df_clean = df.set_index(date_times)

print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 
                   'dry_bulb_faren'])

df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], 
        errors = 'coerce')

df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], 
        errors = 'coerce')

df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'],
        errors = 'coerce')

## Signal min, max, median

df_clean['dry_bulb_faren'].median()

df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median()

df_clean.loc['2011-Jan', 'dry_bulb_faren'].median()

## Signal variance
df_climate = pd.read_csv('weather_data_austin_2010.csv', parse_dates = True, 
                 index_col = 'Date')

daily_mean_2011 = df_clean.resample('D').mean()

daily_temp_2011 = daily_mean_2011.dry_bulb_faren.values

daily_climate = df_climate.resample('D').mean()

daily_temp_climate = daily_climate.reset_index()['Temperature']

difference = daily_temp_2011 - daily_temp_climate 

print(difference.mean())

### Sunny or cloudy

is_sky_clear = df_clean['sky_condition'] == 'CLR'

sunny = df_clean.loc[is_sky_clear]

sunny_daily_max = sunny.resample('D').max()

sunny_daily_max.head()

### Weekly avg temp and visibility, visual EDA

weekly_mean = df_clean[['visibility','dry_bulb_faren']].resample('W').mean()

weekly_mean.corr()

weekly_mean.plot(subplots = True)
plt.show()

### Probability of high temps

august_max = df_climate.loc['2010-08', 'Temperature'].max()

august_2011 = df_clean.loc['2011-08', 'dry_bulb_faren'].resample('D').max()

august_2011_high = august_2011.loc[august_2011 > august_max]

august_2011_high.plot(kind = 'hist', bins = 25, normed = True, 
                      cumulative = True)
plt.show()



