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

'''14. Write a Python program to print the numbers of a specified list after removing even numbers from it.'''

def even_remover(lst):
    
    empty_list = []
    
    for i in lst:
        
        if i % 2 != 0:
            
            empty_list.append(i)
            
    return empty_list

sample_list = [1,2,3,4,5,6,7,8,9]

even_remover(sample_list)

## List comprehension method:

print([i for i in sample_list if i%2 != 0])

'''15. Write a Python program to shuffle and print a specified list.'''

import random

## Or from random import shuffle

random.shuffle(sample_list)

print(sample_list)

'''16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)'''

def sq_bear(lst):
    
    '''generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30'''
    
    matcher = [x**2 for x in range(30)]
    
    new_list = []
    
    for i in lst[0:5]:
        
        if i in matcher:
        
            new_list.append(i)
        
    for j in lst[-5:]:
        
        if j in matcher:
        
            new_list.append(j)
        
    return new_list
        
sample_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]       
    
sq_bear(sample_list)

'''17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).'''

def even_stranger(lst):
    
    print([i**2 for i in lst[5:]])

sample_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even_stranger(sample_list)

'''18. Write a Python program to generate all permutations of a list in Python.'''

def permuter(lst):
    
    empty_list = []
    
    for i in range(len(lst)):
        
        m = lst[i]
        
        p = lst[:i] + lst[i+1:]
        
        empty_list.append([m] + p)
    
    return empty_list
  
sample_list = [1,2,3,4,5]

permuter(sample_list)

# Their solution:

import itertools

print(list(itertools.permutations([1,2,3,4,5])))

# Different solutions and results!
    # Itertools version actually has all permutations since the order
        # of the permuted list is what matters

'''19. Write a Python program to get the difference between the two lists.'''

def differ(lst1, lst2):
    
    empty_list = []
    
    for i in range(len(lst1)):
        
        diff = lst1[i] - lst2[i]
        
        empty_list.append(diff)
    
    return empty_list

samA = [3,5,4,6,3,4,5]
samB = [5,4,3,5,6,7,6,15,17,43]

differ(samA, samB)

# Not what I expected for difference in lists in their solution! 

def differ(lst1, lst2):
     
    diff_a_b = list(set(lst1) - set(lst2))
    diff_b_a = list(set(lst2) - set(lst1))
    
    new_list = diff_a_b + diff_b_a
    
    return new_list

differ(samA, samB)

'''20. Write a Python program access the index of a list.'''

def dexer(lst, num):
    
    for i in lst:
        
        if i == num:
            
            print(lst.index(i))


dexer(samB, 15)

# Their solution (enumerate the list)

def dexer(lst):
    
    for i, j in enumerate(lst):
        
        print(i, j)
        
dexer(samB)

'''21. Write a Python program to convert a list of characters into a string.'''

def strips(lst):
    
    return "".join(lst)

samA = ['t','h','i','s','l','i','s','t','a','c','t','u','a','l','l','y','m','e','a','n','s','s','o','m','e','t','h','i','n','g']

strips(samA)

'''22. Write a Python program to find the index of an item in a specified list.'''

# This is what I originally wrote for #20, I think

def dexer(lst, let):
    
    print(lst.index(let))
            
dexer(samA, 'i')



