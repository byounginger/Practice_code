#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:56:46 2020

@author: brett

Practice cleaning and visualizing datasets downloaded from the web:

https://www.dataquest.io/blog/free-datasets-for-projects/
https://paulvanderlaken.com/2017/10/20/datasets/

Also, check this out at the bottom! 
    https://data36.com/data-science-career-question-1/

Will use a G&T dataset downloaded from the web
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir('/Users/brett/.spyder-py3/sandbox')

gt_data = pd.read_csv('G_N_T_responses.csv')

'''Things to accomplish
1. Loading and viewing
2. Summary stats
3. Visualize variables with histograms and scatterplots
4. Reshaping the data with melt and pivot (if applicable)
5. Splitting and concatenating columns and rows
6. Data frame merging
7. Converting data types
8. Cleaning data with functions
9. Dropping duplicates and filling in missing data
10. Tests with assert statements
'''

print(gt_data.columns)
print(gt_data.shape)
print(gt_data.describe())

# Looks like the district is coded as a float. Will need to change to categorical

print(gt_data.info())
print(gt_data['Entering Grade Level'].describe())
print(gt_data['Entering Grade Level'])
print(gt_data['Overall Score'].value_counts())

# Should recode the column headers so no spaces

cols1 = list(gt_data.columns)

cols2 = [x.replace(' ', '_') for x in cols1]
cols2 = [x.replace('?', '') for x in cols2]

gt_data.columns = cols2

## Plot some summary stats

gt_data['Overall_Score'].plot(kind = 'hist')
plt.show()

gt_data['OLSAT_Verbal_Score'].value_counts(dropna=False)
gt_data['OLSAT_Verbal_Score'].info()

gt_data['OLSAT_Verbal_Score'] = pd.to_numeric(gt_data['OLSAT_Verbal_Score'], 
       errors = 'coerce')

gt_data['OLSAT_Verbal_Score'].plot(kind = 'hist')
    # Some values close to 100 whereas the rest are ~20

# Fill in some missing values with the mean in the last column (should do median)
    
gt_med = gt_data.OLSAT_Verbal_Score.median()

gt_data['OLSAT_Verbal_Score'] = gt_data.OLSAT_Verbal_Score.fillna(gt_med)

assert gt_data.OLSAT_Verbal_Score.notnull().all().all()
assert gt_data.Overall_Score.notnull().all()

gt_data['OLSAT_Verbal_Score'].describe()
gt_data['OLSAT_Verbal_Score'].median()





    









