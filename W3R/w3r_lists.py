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

        