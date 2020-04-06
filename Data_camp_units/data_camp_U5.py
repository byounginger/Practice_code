#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:55:08 2020

@author: brett

From DataCamp Unit 5:
    Introduction to Importing Data in Python

Uses the following datasets:

Chinook (SQLite)
LIGO (HDF5)
Battledeath (XLSX)
Extent of infectious diseases (DTA)
Gene expressions (MATLAB)
MNIST
Sales (SAS7BDAT)
Seaslugs
Titanic

"""

import os

os.getcwd()
os.chdir('/Users/brett/.spyder-py3/sandbox')

## Examine working directory:
! ls

### Open a txt file

file = open('seaslug.txt', mode = 'r')

print(file.read())
print(file.closed)
file.close()
print(file.closed)

#### Opening a file with context manager (with statement)

with open('seaslug.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Note that after you call the context manager, the file doesn't remain open...
    
### Using numpy to import flat files:
    
!ls

import numpy as np
from matplotlib import pyplot as plt

file = 'mnist_kaggle_some_rows.csv'

gaps = np.loadtxt(file, delimiter = ',')

print(type(gaps))

# Select and reshape a row
im = gaps[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

### Customizing numpy imports

file = 'mnist_kaggle_some_rows.csv'

gaps = np.loadtxt(file, delimiter = ',', skiprows=1, usecols=[0,2])

print(gaps)

### Tab-delim with strings

file = 'seaslug.txt'

data = np.loadtxt(file, delimiter = '\t', dtype = str)

print(data[0])

# Re-load and skip the header, importing as floats

data = np.loadtxt(file, delimiter = '\t', skiprows=0, dtype=float)

print(data[9])

# Plot it

plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

# The above doesn't work since I have a different seaslug.txt file

### Moving beyond np.loadtxt since it only handles one datatype per file...

file = 'titanic_sub.csv'
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)

print(data['Survived'])

### Using np.recfromcsv since its dtype is 'None' by default
file = 'titanic_sub.csv'

data = np.recfromcsv(file)

print(data[:3])

### Flat files with pandas

import pandas as pd

file = 'titanic_sub.csv'

data = pd.read_csv(file)

print(data.head())

### More flat files with pandas

file = 'mnist_kaggle_some_rows.csv'

df = pd.read_csv(file, nrows=5, header=None)

df_array = df.values

print(type(df_array))

### Opening a pickle file which is just a funny way of calling a file
### that has dictionaries or lists, but is flat

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

### Importing spreadsheets and referring to sheets 

file = 'battledeath.xlsx'

xls = pd.ExcelFile(file)

print(xls.sheet_names)

### Parse specific sheets

df1 = xls.parse('2004')

print(df1.head())

df2 = xls.parse(0)

print(df2.head())

### Parsing and changing column headers

df1 = xls.parse(0, skiprows=[1], names=['Country', 'AAM due to war (2002)'])

print(df1.head())

df2 = xls.parse(1, usecols=[0], skiprows=1, names=['Country'])

print(df2.head())

### SAS Files

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

# Don't have sas7bdat imported, so will skip above for now

### Stata files with pandas

df = pd.read_stata('disarea.dta')

print(df.head())

pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

### HDF5 Files

import h5py

h5py_file = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'

h5py_data = h5py.File(h5py_file, 'r')

print(type(h5py_data))

print(h5py_data.keys())

# Or:

for key in h5py_data.keys():
    print(key)

# Extract data from the file
    
group = h5py_data['strain']

for key in group.keys():
    print(key)

strain = h5py_data['strain']['Strain'].value

# Sampling timepoints
num_samples = 10000

# Make a time vector
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

### Importing MATLAB files

import scipy.io

file = 'ja_data2.mat'

mat = scipy.io.loadmat(file)

print(type(mat))

print(mat.keys())

print(type(mat['CYratioCyt']))

print(np.shape(mat['CYratioCyt']))

data = mat['CYratioCyt'][25, 5:]

fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()


### Creating SQL database engines

from sqlalchemy import create_engine

engine = create_engine('sqlite:///Chinook.sqlite')

table_names = engine.table_names()

print(table_names)

# Open a table connection

con = engine.connect()

rs = con.execute('SELECT * FROM Artist')

df = pd.DataFrame(rs.fetchall())

con.close()

print(df.head())

### Open engine with a context manager

with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()
    
print(len(df))
print(df.head())

### Filtering with conditionals in sql

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeID >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    
print(df.head())

### Ordering your query:

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    
print(df.head())

### Using pandas to streamline query code

df = pd.read_sql_query('SELECT * FROM Album', engine)

print(df.head())

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Album')
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

print(df.equals(df1))

### Increased query complexity

df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate', engine)

print(df.head())

### Using INNER JOIN

with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())

### Filtering INNER JOIN

df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackID WHERE Milliseconds < 250000', engine)

print(df.head())

### DONE!



