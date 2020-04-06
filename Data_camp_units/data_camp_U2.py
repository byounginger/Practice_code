#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:29:05 2020

@author: brett
"""
## Code for Unit 2: Intermediate Python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gapminder = pd.read_csv('/Users/brett/.spyder-py3/sandbox/gapminder.csv')

gdp_cap = gapminder['gdp_cap']
life_exp = gapminder['life_exp']
pop = gapminder['population']


plt.plot(gdp_cap, life_exp)
plt.show()

""" 
Replot it to show a scatterplot with the x-axis on a log scale:
"""
plt.scatter(gdp_cap, life_exp)

plt.xscale('log')

plt.show()

plt.scatter(pop, life_exp)

plt.show()

plt.hist(life_exp, bins = 10)
plt.show()
plt.clf()

plt.hist(life_exp, bins = 5)
plt.show()

""" Plot customization """

plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

xlab = "GDP in bagillions"
ylab = "Life expectancy (years)"
title = "World development in 2007"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

#plt.show()

tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

plt.xticks(tick_val, tick_lab)

plt.show()

""" Dictionaries """

countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany')

print(capitals[ind_ger])

europe = { 'spain':'madrid', "france":"paris","germany":"berlin",
          "norway":"oslo"}

print(europe)

print(europe['france'])

print(europe.keys())

europe['italy'] = 'rome'

print('italy' in europe)
print('rome' in europe)

europe['poland'] = 'warsaw'

print(europe)

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe['france']['population'])

data = {'capital':'rome', 'population':24.20}

europe['italy'] = data

print(europe)

""" Dictionaries to dataframes """

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country':names, 'drives_right':dr, 'cars_per_capita':cpc}

print(my_dict)

cars = pd.DataFrame(my_dict)

print(cars)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels

print(cars)

cars = pd.read_csv('cars.csv', index_col = 0)

print(cars[['country','drives_right']]) # Make sure you use the double brackets! 

print(cars[3:8])

print(cars.loc['JAP'])
print(cars.iloc[2])

print(cars.loc[['MOR','EG']])
print(cars.iloc[[-2,-1]])

print(cars.loc['MOR','drives_right'])
print(cars.loc[['IN','JAP'],['cars_per_cap','drives_right']])

print(cars.loc[:,'drives_right'])
print(cars.iloc[:,[2]])
print(cars.iloc[:,[0,2]])

""" Boolean operators """

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(np.logical_or(my_house > 18, my_house < 10))
print(np.logical_and(my_house < 11, your_house < 11))

# Extract a column as a series based on a Boolean of True

dr = cars['drives_right']

sel = cars[dr]

print(sel)

## Instead, can do this as a one-liner:

sel = cars[cars['drives_right']]

print(sel)

cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

print(car_maniac)

cpc = cars.iloc[:,0]
many_cars = cpc > 70

car_maniacs = cars[many_cars]

print(car_maniacs)

between = np.logical_and(cpc < 700, cpc > 70)

medium = cars[between]

print(medium)

''' Make sure you review the np.nditer function!'''

### While statements

x = 2 
while x < 10:
    print(x)
    x = x + 1

### Offset example
    
offset = -6 
while offset != 0:
    print('correcting')
    offset = offset - 1
    print(offset)

while offset != 0:
    print('correcting')
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
    
### Use enumerate to provide the index of lists in for loops:
    
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for index, a in enumerate(areas):
    print('row ' + str(index) + ': ' + str(a))
    
#####
    
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

'''Write a for loop that goes through each sublist of house and prints out 
the x is y sqm, where x is the name of the room and y is the area of the room.
'''

for i,j in house:
    print(i + ' is ' + str(j) + ' sqm')

#### Looping over a dictionary, you need the items() function ####
    
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
    
    
'''Write a for loop that goes through each key:value pair of europe. On each 
iteration, "the capital of x is y" should be printed out, where x is the key 
and y is the value of the pair.'''

for i, j in europe.items():
    print('the capital of ' + i.upper() + ' is ' + j.capitalize())

'''np.nditer commands to iterate over multidimensional arrays
Write a for loop that iterates over all elements in np_height 
and prints out "x inches" for each element, where x is the value in the array.
Write a for loop that visits every element of the np_baseball array and prints 
it out.'''

heights_in = pd.read_csv('/Users/brett/Documents/sandbox/heights_weights.csv', 
                         index_col = "Name")

'''Need to figure out how to convert this import out of a series and into an
 array'''

#heights_in.to_numpy()
#
heights = heights_in.iloc[:,2]
#heights = heights.to_numpy()
#weights = heights_in.iloc[:,3]
#weights = weights.to_numpy()
#
#heights = heights.astype(float)
#
#full = np.concatenate(heights, weights)

bball = heights_in.iloc(2,3)

print(heights)

for x in heights:
    print(str(x) + ' inches')
    
cars = pd.read_csv('/Users/brett/Documents/sandbox/cars.csv', index_col = 0)

for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
for lab, row in cars.iterrows():
    print(lab + ': ' + str(row[0]))

for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row['country'].upper()

print(cars.iloc[:,3])

for lab, row in cars.iterrows():
    cars['COUNTRY'] = cars['country'].apply(str.upper)

print(cars.iloc[:,3])

print(cars)

'''Random number generators and such'''

np.random.seed(777)

np.random.rand()

print(np.random.randint(1,7))
print(np.random.randint(1,7))

'''The dice-steps game'''

step = 50

dice = np.random.randint(1,7)

if dice <= 2:
    step = step - 1
elif dice <= 5: 
    step = step + 1
else:
    step = step + np.random.randint(1,7)

print(dice)
print(step)

'''The random walk'''

random_walk = [0]

for x in range(100):
    
    step = random_walk[-1]
    
    dice = np.random.randint(1,7)
    
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5: 
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    
    random_walk.append(step)
    
print(random_walk)

plt.plot(random_walk)
plt.show()

'''Repeat of above with 10 iterations'''

all_walks = []

for i in range(500):
    
    random_walk = [0]
    
    for x in range(100):
    
        step = random_walk[-1]
    
        dice = np.random.randint(1,7)
    
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5: 
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        if np.random.rand() <= 0.001:
            step = 0
        
        random_walk.append(step)
        
    all_walks.append(random_walk)

print(all_walks)

np_walks = np.array(all_walks)

#plt.plot(np_walks)
#plt.show()
#plt.clf()

np_t = np.transpose(np_walks)
plt.plot(np_t)
plt.show()

ends = np_t[100,:]
plt.hist(ends)
plt.show()

np.mean(ends >= 60)



