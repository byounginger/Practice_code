#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:47:30 2020

@author: brett

Lists from w3s:
    
https://www.w3resource.com/python-exercises/list/

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

def sordid(lstolst):
    
    return sorted(sample_list, key = lambda sample_list: sample_list[1])
    

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sordid(sample_list)

'''7. Write a Python program to remove duplicates from a list.'''

def duped(lst):
    
    return list(set(lst))

sample_list = [1,2,4,3,2,3,4,6,5,4,5,4,3,2, 'ab', 'abc', 'ab']
duped(sample_list)

'''8. Write a Python program to check if a list is empty or not.'''

def emptee(lst):
    
    if len(lst) == 0:
        print('The list is empty')
        
    else:
        return lst

empty_list = []
sample_list = [1,2,4,3,2,3,4,6,5,4,5,4,3,2]

emptee(empty_list)
emptee(sample_list)

'''9. Write a Python program to clone or copy a list.'''

def drone(lst):
    
    print(lst,lst)
    
sample_list = [1,2,4,3,2,3,4,6,5,4,5,4,3,2]

drone(sample_list)

'''10. Write a Python program to find the list of words that are longer than n from a given list of words.'''

def verbose(lst, n):
    
    '''Finds a list of words that are longer than n'''
    
    empty_list = []
    
    for i in lst:
        
        if len(i) > n:
            
            empty_list.append(i) # Don't forget append method for list of strings
            
    return empty_list

sample_list = ['apples', 'origins', 'oranges', 'plums', 'san', 'red']

verbose(sample_list, 3)

'''11. Write a Python function that takes two lists and returns True if they have at least one common member.'''

def comparerer(lst1, lst2):
    
    '''takes two lists and returns True if they have at least one common member'''
    
    result = False
    
    for i in lst1:
        
        for j in lst2:

            if i == j:
                
                result = True
                
                return result
            

sample1 = ['Hey', 'oh', 'we', 'got', 'big', 'Gretch']
sample2 = ['That', 'woman', 'from', 'Michigan', 'Gretchen']

comparerer(sample1, sample2)

'''12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.'''

sample_list=['Hey', 'oh', 'we', 'got', 'big', 'Gretch', 'That', 'woman', 'from', 'Michigan', 'Gretchen']

def remover(lst):
    
    lst.pop(5)
    lst.pop(4)
    lst.pop(0)    
    
    return lst

remover(sample_list)

# Their solution:

sample_list=['Hey', 'oh', 'we', 'got', 'big', 'Gretch', 'That', 'woman', 'from', 'Michigan', 'Gretchen']

sample_list=[x for (i,x) in enumerate(sample_list) if i not in (0,4,5)]
sample_list    

'''13. Write a Python program to generate a 3*4*6 3D array whose each element is *.'''

some_array = [[['*' for i in range(3)] for j in range(4)] for k in range(6)]

some_array

