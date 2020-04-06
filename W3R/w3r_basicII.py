#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:17:11 2020

@author: brett

The basics II from w3s
https://www.w3resource.com/python-exercises/basic/

"""

'''1. Write a Python function that takes a sequence of numbers and determines 
whether all the numbers are different from each other.'''

def differ(*num):
    
    if len(num) == len(set(num)):
        return True
    else:
        return False

differ(2,4,6,8)
differ(2,2,4,6,8)

'''2. Write a Python program to create all possible strings by using 'a', 
'e', 'i', 'o', 'u'. Use the characters exactly once.'''

import random

char_list = ['a','e','i','o','u']

random.shuffle(char_list)

print(''.join(char_list))

'''3. Write a Python program to remove and print every third number from a 
list of numbers until the list becomes empty.'''

def remover(num):
    
    shrink_list = len(num)
    
    position = 2
    
    ren = 0    
    
    while shrink_list > 0:
           ren = (position + ren) % shrink_list           
           shrink_list -= 1
           print(num.pop(ren))

sample = [1,2,3,4,5,6,7,7,7,6,5,4,5,6,8]
remover(sample)

position = 2
ren = 0
shrink_list = len(sample)
print((position+ren)%shrink_list)
len(sample)

'''4. Write a Python program to find unique triplets whose three elements 
gives the sum of zero from an array of n integers.'''

def three_sums(num):
    
    result = []
    
    num.sort()
    
    for i in range(len(num) - 2): # maybe add the -2 here
        if i > 0 and num[i] == num[i - 1]:
            continue
        l, r = i + 1, len(num)-1
        while l < r:
            s = num[i] + num[l] + num[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                result.append((num[i], num[l], num[r]))
                
                while l < r and num[l] == num[l + 1]:
                    l += 1
                    while l < r and num[r] == num[r - 1]:
                        r -= 1
                        l += 1
                        r -= 1
                    return result

x = [-1,-2,-3,3,4,3,2,1,-3,-2,0,4,3,2,1,-3,-2,-1,0]

three_sums(x)

'''5. Write a Python program to create the combinations of 3 digit combo.'''

# This is poorly worded and confusing. Will move on...

'''6. Write a Python program to print a long text, convert the string to a 
list and print all the words and their frequencies.'''

def word_counter(words):
    
    print(words)
    
    new = list(words.split())
    
    empty_dict = {}
    
    for i in new:
        if i in empty_dict.keys():
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    
    return empty_dict
    

samp = 'This is a sample string string string sample sample sample'

word_counter(samp)

## Yeah!

## Their answer:

string_words = 'This is a sample string string string sample sample sample'

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))

## I think my solution is better

'''7. Write a Python program to count the number of each character of a given 
text of a text file.'''


def char_count(w):
    
    w = w.lower()
    
    new = list(w.strip())
    
    empty_dict = {}
    
    for i in new:
        if i in empty_dict.keys():
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    
    empty_dict.pop(' ', None)
    
    return empty_dict

char_count(samp)

'''8. Write a Python program to get the top stories from Google news.'''

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
client = urlopen(news_url)
xml_page = client.read()
client.close()

soup_page = soup(xml_page, 'xml')
news_list = soup_page.find_all('item') # May be findAll
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print('-' * 60)

## Will work with url requests some more if needed

'''9. Write a Python program to get a list of locally installed Python 
modules.'''

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)

'''10. Write a Python program to display some information about the OS 
where the script is running.'''

import platform as pl

os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(pl, key):
    print(key +  ": " + str(getattr(pl, key)()))

'''11. Write a Python program to check the sum of three elements (each from 
an array) from three arrays is equal to a target value. Print all those 
three-element combinations.'''

#import numpy as py
#
#def arsumer(ar1, ar2, ar3):
#    
#    target = input('Enter a target value:')
#    
#    for i in ar1:
#        for j in ar2:
#            for k in ar3:
#                if (i + j + k) == target:
#                    print(i, j, k)
#
#a = [3,2,1,4,5,6,7,5,4,3]
#b = [7,6,5,4,5,6,8,9,4,3]
#c = [1,2,3,2,1,2,3,1,2,3]
#a = py.array(a)
#b = py.array(b)
#c = py.array(c)
#
#arsumer(a, b, c)

### Not sure about that one. Here's their answer:

#import itertools
#from functools import partial
#target = 8
#
#def arsumer(N, *ar):
#    if sum(x for x in ar) == N:
#        return (True, ar)
#    else: 
#        return (False, nums)
#
#arsumer(8, a, b, c)
  
import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
  if sum(x for x in nums) == N:
    return (True, nums)
  else:
      return (False, nums)
  
pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
      result.add(s[1])
      print(result)   
    
'''
12. Write a Python program to create all possible permutations from a 
given collection of distinct numbers'''

#import random
#
#def mixer(nums):
#    
#    empty_dict = {}
#    empty_keys = 0
#    nums = list(nums)
#    
#    for i in nums:
#        random.shuffle(nums)
#        if nums in empty_dict:
#            pass
#        else: 
#            empty_dict.keys(empty_keys).index(nums)
#            empty_keys += 1
#
#sample = (1,2,3,4,5,6,7,8)
#
#mixer(sample)

## Their answer:

def mixer(nums):
    
    result_perms = [[]]        
    for n in nums:   
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
                
    return result_perms                

sample_nums = [1,2,3,4,5,6]
mixer(sample_nums)

# Practice recoding this again tomorrow on my own! 


        
        
        
        