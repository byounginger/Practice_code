#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:08:51 2020

@author: brett
"""

import pandas as pd
import re

mapper = '/Users/brett/Documents/Temporal_turnover/Informatics/map_file14.txt'

mapper2 = pd.read_csv(mapper, sep = '\t', header = 0)

print(mapper2.head())

keepers = ['BY-6-3-4', 'BY-15-3-4', 'BY-1-2-4', 'BY-19-1-4', 'BY-6-4-4', 
           'BY-16-4-4', 'BY-5-2-4', 'BY-5-4-4', 'BY-5-3-4', 'BY-1-3-4']

mapper3 = mapper2[mapper2.SampleID.str.contains('|'.join(keepers))]

print(mapper3)

mapper3.to_csv('/Users/brett/Documents/Temporal_turnover/Informatics/map_file15.txt', 
               header = True, sep = '\t', index = False)

''' Solution to the problem solved on line 21 and found here:
https://kanoki.org/2019/03/27/pandas-select-rows-by-condition-and-string-operations/
'''

'''Comparing the OTU table and map file to identify missing labels'''

IDs = '/Users/brett/Documents/Temporal_turnover/Informatics/OTU_output/Changed_headers/ID_matches.txt'

IDs = pd.read_csv(IDs, sep = '\t', header = 0)

print(IDs.head())

#IDs.sort_values(by='MAP_IDs')

empty_list = []

for i in IDs['MAP_IDs']:
    if i not in IDs['OTU_IDs']:
        empty_list += i

missing = [x for x in IDs['MAP_IDs'] if x not in IDs['OTU_IDs']]

print(missing)

# pd.unique(IDs['MAP_IDs'], IDs['OTU_IDs'])

MAPs = IDs['MAP_IDs']

MAPs = list(MAPs)

OTUs = list(IDs['OTU_IDs'])

print(MAPs)
print(OTUs)

MAPs = [x for x in MAPs if str(x) != 'nan']

newIDs = [x for x in MAPs if x not in OTUs]

print(newIDs)

newIDs = IDs[IDs.MAP_IDs.str.contains('|'.join(MAPs))]





