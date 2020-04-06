#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:22:13 2020

@author: brett

w3resource practice problems: functions
https://www.w3resource.com/python-exercises/python-functions-exercises.php

"""

'''1. Write a Python function to find the Max of three numbers. '''

def maxer(num1, num2, num3):
    ''''''
    top = max(num1, num2, num3)
    
    return top

maxer(6,2,4)

'''2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

def summer(*args):
    ''''''
    somethin = sum(args)
    
    return somethin

summer(1,3,4,6,7,8,2)

'''3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''

def multer(*args):
    ''''''
    total = 1
    for i in args:
        
        total *= i
    
    return total

multer(8,2,3,-1,7)

'''4. Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''

def reverser(numlet):
    ''''''
    revlet = str(numlet[::-1])
    
    return revlet

reverser('1234abcd')

'''5. Write a Python function to calculate the factorial of a number 
(a non-negative integer). The function accepts the number as an argument. 
'''

def factorial(n):
    ''''''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))

'''6. Write a Python function to check whether a number is in a given range.
'''

def ranger(n, upper, lower):
    
    if n >= lower and n <= upper:
        
        return True
    
    else:
        
        return False

ranger(15, 25, 10)
ranger(10, 15, 25)

'''7. Write a Python function that accepts a string and calculate the number 
of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

def uplow(word):
    ''''''
    d = {'upper':0, 'lower':0}
    
    for i in word:
        if i.isupper():
            d['upper'] += 1
        elif i.islower():
            d['lower'] += 1
        else:
            pass
    
    print("No. of Upper case characters :" + str(d['upper']))
    print("No. of Lower case characters :" + str(d['lower']))

uplow('The quick Brown Fox')

'''8. Write a Python function that takes a list and returns a new 
list with unique elements of the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def uniqer(l):
    ''''''
    unique_list = []
    
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

sample_list = [1,2,3,3,3,3,4,5]
uniqer(sample_list)

'''9. Write a Python function that takes a number as a parameter and check 
the number is prime or not. Go to the editor
Note : A prime number (or a prime) is a natural number greater than 1 and 
that has no positive divisors other than 1 and itself.'''

def primer(n):
    ''''''
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        for y in range(2,n):
            if(n % y == 0):
                return False
        return True
        
primer(3)
primer(4)
primer(9)
primer(11) 

'''10. Write a Python program to print the even numbers from a given list. 
Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]    '''

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_printer(n):
    
    Empty_list = []
    
    for i in Sample_List:
        
        if i % 2 == 0:
            Empty_list.append(i)
            
    return Empty_list

even_printer(Sample_List)

'''11. Write a Python function to check whether a number is perfect or not. 
Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive 
integer that is equal to the sum of its proper positive divisors, that is, 
the sum of its positive divisors excluding the number itself (also known as 
its aliquot sum). Equivalently, a perfect number is a number that is half the 
sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper 
positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to 
half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next 
perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect 
numbers 496 and 8128.'''

def perfecto(n):
    ''''''
    
    summer = 0
    for i in range(1,n):
        if n % i == 0:
            summer += i
    return n == summer

print(perfecto(496))

'''12. Write a Python function that checks whether a passed string is 
palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward 
as forward, e.g., madam or nurses run.'''

def drome(word):
    
    new_word = word[::-1]
    
    if new_word == word:
        return True
    else:
        return False

drome('badass')
drome('madam')    
drome('aza')

def drome2(word):
    
    leftie = 0
    rightie = len(word) - 1
    
    while rightie >= leftie:
        if not word[rightie] == word[leftie]:
            return False
        leftie += 1
        rightie -= 1
    return True

drome2('badass')
drome2('madam')
drome2('aza')
drome2('nurses run')


'''13. Write a Python function that prints out the first n rows of Pascal's 
triangle. Go to the editor
Note : Pascal's triangle is an arithmetic and geometric figure first imagined 
by Blaise Pascal.'''

''' Not sure I understand the code behind this one:'''

def pascal_triangle(n):
   
   trow = [1]
   y = [0]
   
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   
   return n>=1

pascal_triangle(6) 

'''14. Write a Python function to check whether a string is a pangram or not. 
Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet 
at least once.
For example : "The quick brown fox jumps over the lazy dog"'''

def panny(word):
    
    empty_list = []
    
    empty_list2 = []
    
    word2 = ''.join(word.split())
    
    for i in range(97,123):
        empty_list.append(chr(i))
    
    for j in word2:
        
        k = j.lower()
        
        if k not in empty_list2:
            empty_list2.append(k)
        else: 
            pass
    
    empty_list2.sort()
    
    print(empty_list)
    print(empty_list2)
    return empty_list == empty_list2

panny('The quick brown fox jumps over the lazy dog')  
panny('n')

''' Their version:'''
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

ispangram('The quick brown fox jumps over the lazy dog')
ispangram('n')

'''15. Write a Python program that accepts a hyphen-separated sequence of 
words as input and prints the words in a hyphen-separated sequence after 
sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

Sample_Items = 'green-red-yellow-black-white'

def color_sorter(word):
    ''''''
    word2 = word.split('-')
    word2.sort()
    word3 = '-'.join(word2)
    
    return word3

color_sorter(Sample_Items)

'''16. Write a Python function to create and print a list where the values 
are square of numbers between 1 and 30 (both included).'''

def square_bear():
    ''''''
    empty_list = []
    for n in range(1,31):
        empty_list.append(n**2)
    print(empty_list)

square_bear()

'''17. Write a Python program to make a chain of function decorators (bold, 
italic, underline etc.) in Python.'''

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped


def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"

print(make_bold(hello()))

'''Not following this above. Doesn't seem too important. Will move on'''

'''18. Write a Python program to execute a string containing Python code.'''

code1 = 'print("hello")'

code2 = '''

def multy(x,y):
    return x * y
    
print('The product of X and Y is: ', multy(2,3))

'''


code3 = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""

exec(code1)
exec(code2)
exec(code3)

'''Okay, will keep exec function in mind'''

help(exec)

'''19. Write a Python program to access a function inside a function.'''

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b
    return add

func = test(4)

print(func(6))

''' try this again on my own...'''

'''20. Write a Python program to detect the number of local variables 
declared in a function.'''

def sample_func():
    x = 1
    y = 2
    z = 'string'
    return 'yay!'

print(sample_func.__code__.co_nlocals)










