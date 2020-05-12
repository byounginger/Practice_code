#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:47:30 2020

@author: brett

Lists from w3s:
    
https://www.w3resource.com/python-exercises/string/

"""

'''1. Write a Python program to sum all the items in a list.'''

sample = [2,3,3,4,5,6,7,8]

print(sum(sample))

'''2. Write a Python program to multiplies all the items in a list.'''

def multer(lst):
    
    grand = 1
    
    for i in lst:
        
        grand *= i
    
    return grand

multer(sample)

'''3. Write a Python program to get the largest number from a list.'''

max(sample)

'''4. Write a Python program to get the smallest number from a list.'''

min(sample)        

'''
5. Write a Python program to count the number of strings where the 
string length is 2 or more and the first and last character are same 
from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

def weird(lststr):
    
    empty_count = 0
    
    for i in lststr:
        
        if len(i) > 2:
            
            if i[0] == i[-1]:
                
              empty_count += 1
    
    return empty_count

sample_list = ['abc', 'xyz', 'aba', '1221', 'aa', '1222221']

weird(sample_list)

'''6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''


