#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:03:35 2020

@author: brett

Data Camp Unit 4

"""

'''an iterable is an object that can return an iterator, while an iterator 
is an object that keeps state and produces the next value when you call next() 
on it'''

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for i in flash:
    
    print(i)

rock = iter(flash)

print(next(rock))
print(next(rock))
print(next(rock))
print(next(rock))

'''Can iter over a range, too'''

rock = iter(range(2,20))

##

mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

mutant_list = list(enumerate(mutants))

print(mutant_list)

for index, value1 in enumerate(mutants):
    print(index, value1)
    
for index, value1 in enumerate(mutants, start = 1):
    print(index, value1)
    
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

mutant_list = list(zip(mutants, aliases, powers))

print(mutant_list)

mutant_zip = zip(mutants, aliases, powers)

for i, j, k in mutant_zip:
    print(i, j, k)
    
###
    
z1 = zip(mutants, powers)

print(*z1)

result1, result2 = zip(*z1)

print(list(result1) == mutants)
print(list(result2) == powers)

##

'''Processing in chunks'''

import pandas as pd
import os

os.getcwd()
os.chdir('/Users/brett/.spyder-py3/sandbox')

counts_dict = {}

for chunk in pd.read_csv('tweets.csv', chunksize = 10):
    
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

print(counts_dict)

###

'''Using a function to chunk out a csv file'''

def count_entries(csv_file, c_size, colname):
    ''''''
    counts_dict = {}
    
    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    
    return counts_dict

result_counts = count_entries('tweets.csv', 10, 'lang')

print(result_counts)

###

''' List comprehension stuff '''

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']    

''' Write a list comprehension statement that prints the first letter of each'''

[i[0] for i in doctor]

'''Using the range of numbers from 0 to 9 as your iterable and i as your 
iterator variable, write a list comprehension that produces a list of numbers 
consisting of the squared values of i'''

[i**2 for i in range(0,10)]

''' make a square matrix: 
    
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
'''

matrix = [[col for col in range(5)] for row in range(5)]

for row in matrix:
    print(row)
    
''' List comprehension with conditionals'''

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 
              'gimli']

reduced = [small for small in fellowship if len(small) >= 7]

print(reduced)

otherreduced = [member if len(member) >= 7 else '' for member in fellowship]

print(otherreduced)

''' dict comprehension '''

sample_dict = {member:len(member) for member in fellowship}

print(sample_dict)

''' generators '''

result = (num for num in range(10))

print(next(result))

for i in result:
    print(i)

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

peeps = (len(yo) for yo in lannister)

for i in peeps:
    print(i)

'''function generator'''
    
def get_lengths(input_list):
    
    for i in input_list:
        yield len(i)
        
for value in get_lengths(lannister):
    print(value)

'''List comprehension for time-stamped data'''

df = pd.read_csv('tweets.csv')

tweet_time = df['created_at']

clock_time = [entry[11:19] for entry in tweet_time]

print(clock_time)

clock_time2 = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

print(clock_time2)

feature_names = ['CountryName', 'CountryCode', 'IndicatorName', 
                 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB', 
            'Adolescent fertility rate (births per 1,000 women ages 15-19)', 
            'SP.ADO.TFRT', '1960', '133.56090740552298']

zipped_lists = zip(feature_names, row_vals)

zipped_dict = dict(zipped_lists)

print(zipped_dict)

def lists2dict(list1, list2):
    
    zipped_lists = zip(list1, list2)
    
    zipped_dict = dict(zipped_lists)
    
    return zipped_dict

result = lists2dict(feature_names, row_vals)
print(result)


row_lists = [['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298'], ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547'], ['Arab World', 'ARB', 'Age dependency ratio, old (% of working-age population)', 'SP.POP.DPND.OL', '1960', '6.634579191565161'], ['Arab World', 'ARB', 'Age dependency ratio, young (% of working-age population)', 'SP.POP.DPND.YG', '1960', '81.02332950839141'], ['Arab World', 'ARB', 'Arms exports (SIPRI trend indicator values)', 'MS.MIL.XPRT.KD', '1960', '3000000.0'], ['Arab World', 'ARB', 'Arms imports (SIPRI trend indicator values)', 'MS.MIL.MPRT.KD', '1960', '538000000.0'], ['Arab World', 'ARB', 'Birth rate, crude (per 1,000 people)', 'SP.DYN.CBRT.IN', '1960', '47.697888095096395'], ['Arab World', 'ARB', 'CO2 emissions (kt)', 'EN.ATM.CO2E.KT', '1960', '59563.9892169935'], ['Arab World', 'ARB', 'CO2 emissions (metric tons per capita)', 'EN.ATM.CO2E.PC', '1960', '0.6439635478877049'], ['Arab World', 'ARB', 'CO2 emissions from gaseous fuel consumption (% of total)', 'EN.ATM.CO2E.GF.ZS', '1960', '5.041291753975099'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (% of total)', 'EN.ATM.CO2E.LF.ZS', '1960', '84.8514729446567'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (kt)', 'EN.ATM.CO2E.LF.KT', '1960', '49541.707291032304'], ['Arab World', 'ARB', 'CO2 emissions from solid fuel consumption (% of total)', 'EN.ATM.CO2E.SF.ZS', '1960', '4.72698138789597'], ['Arab World', 'ARB', 'Death rate, crude (per 1,000 people)', 'SP.DYN.CDRT.IN', '1960', '19.7544519237187'], ['Arab World', 'ARB', 'Fertility rate, total (births per woman)', 'SP.DYN.TFRT.IN', '1960', '6.92402738655897'], ['Arab World', 'ARB', 'Fixed telephone subscriptions', 'IT.MLT.MAIN', '1960', '406833.0'], ['Arab World', 'ARB', 'Fixed telephone subscriptions (per 100 people)', 'IT.MLT.MAIN.P2', '1960', '0.6167005703199'], ['Arab World', 'ARB', 'Hospital beds (per 1,000 people)', 'SH.MED.BEDS.ZS', '1960', '1.9296220724398703'], ['Arab World', 'ARB', 'International migrant stock (% of population)', 'SM.POP.TOTL.ZS', '1960', '2.9906371279862403'], ['Arab World', 'ARB', 'International migrant stock, total', 'SM.POP.TOTL', '1960', '3324685.0']]

print(row_lists[0])
print(row_lists[1])

lists_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
    ## Above turns a list of lists into a list of dictionaries

print(lists_of_dicts[0])
print(lists_of_dicts[1])

df = pd.DataFrame(lists_of_dicts)

print(df.head())

#####

'''generator to read in 1000 line chunks'''

with open('world_ind_pop_data.csv') as file:
    
    file.readline()
    
    counts_dict= {}
    
    for j in range(1000):
        
        line = file.readline().split(',')
        
        first_col = line[0]
        
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
            
print(counts_dict)

'''generator to read lines lazily'''

def read_large_file(file_object):
    
    while True:
        
        data = file_object.readline()
        
        if not data:
            break
        
        yield data
        
with open('world_ind_pop_data.csv') as file:
    
    gen_file = read_large_file(file)
    
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

########
    
counts_dict = {}

with open('world_ind_pop_data.csv') as file:
    
    for line in read_large_file(file):
        
        row = line.split(',')
        first_col = row[0]
        
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
            
print(counts_dict)

######

''' using pandas to load chunks '''

df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize = 10)    

print(next(df_reader))
print(next(df_reader))

####

urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize = 10)

df_urb_pop = next(urb_pop_reader)

print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

pops = zip(df_pop_ceb['TotalPopulation'], 
           df_pop_ceb['Urban population (% of total)'])

pops_list = list(pops)

print(pops_list)
####

