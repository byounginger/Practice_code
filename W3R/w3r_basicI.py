#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:57:50 2020

@author: brett

The basics from w3s
https://www.w3resource.com/python-exercises/python-basic-exercises.php

"""

'''1. Write a Python program to print the following string in a specific 
format (see the output). Go to the editor


Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''
    
print('Twinke, twinkle\n\tHow I wonder\n\t\tUp above the world so high!')

'''
2. Write a Python program to get the Python version you are using.'''

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

'''3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''

from datetime import datetime

now = datetime.now()
print('Current date and time :\n' + str(now))


'''4. Write a Python program which accepts the radius of a circle from the 
user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

import numpy as py

r = 1.1

print(py.pi * r**2)

'''5. Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them.'''


first = input('Enter your first name: ')
last = input('Enter your last name: ')
print('Hello ' + last + ', ' + first + ', you dog-faced pony soldier')

'''
6. Write a Python program which accepts a sequence of comma-separated numbers 
from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

one = input('Enter a number:')
two = input('Enter another number:')
three = input('Enter a third number:')
four = input('For the last freaking time, enter a number:')

print(list(one + two + three + four))
#print(tuple(one, two, three, four))

values = input('Enter some comma-separated values:')

ellisto = list(values.split(','))
tupperware = tuple(ellisto)

print('List: ', ellisto)
print('Tuple: ', tupperware)

'''
7. Write a Python program to accept a filename from the user and print the 
extension of that. Go to the editor
Sample filename : abc.java
Output : java
'''

filename = input('Type a filename:')

heyo = list(filename.split('.'))
print(heyo[1])

'''
8. Write a Python program to display the first and last colors from the 
following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]

print('%s %s' %(color_list[0], color_list[-1]))

'''
9. Write a Python program to display the examination schedule. (extract the 
date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

exam_st_date = (11, 12, 2014)

exam = list(exam_st_date)

print('The exam will start on: %i / %i / %i'%(exam[0], exam[1], exam[2]))

### They said:
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
### Don't even need to index since it unpacks the tuple automatically

'''10. Write a Python program that accepts an integer (n) and computes the 
value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''

somenum = int(input('Type a number budee:'))

n1 = int('%s' % somenum)
n2 = int('%s%s' % (somenum, somenum))
n3 = int('%s%s%s' % (somenum, somenum, somenum))

print(n1 + n2 + n3)

'''11. Write a Python program to print the documents (syntax, description etc.) 
of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.'''

a = input('Enter a function: ')

print(help(a))

### OR ###

print(abs.__doc__)

'''12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.'''

import calendar as cd 

y = int(input('Enter the year: '))
m = int(input('Enter the month: '))

print(cd.month(y,m))

'''
13. Write a Python program to print the following here document. Go to the 
editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example'''

## Um...

print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')


'''14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date

d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)

delta = d2 - d1
print(delta.days)
 # OR
print(d2 - d1)

'''15. Write a Python program to get the volume of a sphere with radius 6.'''

import numpy as py

sphere = (4/3*py.pi*6**3)

print(sphere)

'''16. Write a Python program to get the difference between a given number 
and 17, if the number is greater than 17 return double the absolute 
difference.'''

num = int(input('Enter an integer: '))

if num > 17:
    print((py.abs(17 - num))*2)

else:
    print(17 - num)

# They did the above as a function

'''17. Write a Python program to test whether a number is within 100 of 
1000 or 2000.'''

def ranger(num):
    
    diff1 = py.abs(1000 - num)
    diff2 = py.abs(2000 - num)
    
    if diff1 <= 100:
        return True
    elif diff2 <= 100:
        return True
    else:
        return False

ranger(2020)

## They wrote it more elegantly:

def ranger(num):
    return((abs(2000 - num)) <= 100 or abs(1000 - num) <= 100)
    
ranger(1010)    
ranger(1500)    
    
'''18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum.'''

def summer(a, b, c):
    if a == b == c:
        return(3 * (a + b + c))
    else:
        return(a + b + c)

summer(3,6,9)
summer(2,2,3)

'''19. Write a Python program to get a new string from a given string where 
"Is" has been added to the front. If the given string already begins with "Is" 
then return the string unchanged.'''

def adder(word):
    
    if word[:2] == 'Is':
        return word
    else: 
        return 'Is_' + word

adder('shebang')
adder('Ishebang')

'''20. Write a Python program to get a string which is n (non-negative 
integer) copies of a given string.'''

def multer(word, num):
    
    result = ''
    for i in range(num):
        result = result + word
    return result

multer('abc', 3)

'''21. Write a Python program to find whether a given number (accept from 
the user) is even or odd, print out an appropriate message to the user.'''

num = int(input('Enter any fucking number: '))

if num % 2 == 0:
    print('That number is even')
else:
    print('That number is odd')

'''22. Write a Python program to count the number 4 in a given list.'''

def countin(num):

    count_list = 0
    
    for i in num:
        if i == 4:
            count_list += 1
        
    return count_list

countin([2,3,4,5,6,7,5,4,5,6,4,5,3,4,5])
countin([2,3,4,4,4,4,4,4,4,4,4,4,5,6,7])

'''23. Write a Python program to get the n (non-negative integer) copies of 
the first 2 characters of a given string. Return the n copies of the whole 
string if the length is less than 2.'''

def counter(word, num):
    
    if len(word) < 2:
        return word * num
    
    else:
        somethin = word[0:2]
        return somethin * num

counter('h', 3)

'''24. Write a Python program to test whether a passed letter is a vowel 
or not.'''

def letter(word):
    
    vowel_list = ['a','e','i','o','u']
    
    if word in vowel_list:
        print('It\'s a friggin\' vowel')
    else:
        print('It\'s a consonant')

letter('b')
letter('e')

## OR...

def letter(word):
    
    vowels = 'aeiou'
    
    return word in vowels

letter('b')
letter('e')

'''25. Write a Python program to check whether a specified value is 
contained in a group of values.'''

def val(word):
    
    sample = 'abcdefg' 
    broken = list(sample.strip())
    
    return word in broken

val('h')
val('c')
val('dag') ## This one doesn't work

## Their answer

def val(word, let):
    
    for i in word:
        if let == i:
            return True
    return False

val([3,4,5,6,7,8], 2)
val([3,4,5,6,7,8], 6)

'''26. Write a Python program to create a histogram from a given list of 
integers.'''

import matplotlib.pyplot as plt

def upright(vals):
    
    ellisto = list(vals)
    
    plt.hist(ellisto, bins = 5)
    plt.show()

upright('2,3,4,5,6,5,4,5,4,3,2,3,4')

'''27. Write a Python program to concatenate all elements in a list into 
a string and return it.'''

def catlover(lst):
    
    empty_string = ''
    
    for i in lst:
    
        empty_string += str(i)
    
    return empty_string

catlover([2,4,'d',3,3.3,18])

'''28. Write a Python program to print all even numbers from a given numbers 
list in the same order and stop the printing if any numbers that come after 
237 in the sequence.'''

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]

for i in numbers:
    
    if i == 237:
        print(i)
        break;
    elif i % 2 == 0:
        print(i)
        
'''29. Write a Python program to print out a set containing all the colors 
from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

## Oooh, the difference method. I likey!

'''30. Write a Python program that will accept the base and height of a 
triangle and compute the area.'''

h = int(input('Enter the height of a triangle: '))
b = int(input('Enter the base of a triangle: '))

area = ((h*b)/2)

print('area: ', area)

'''31. Write a Python program to compute the greatest common divisor (GCD) 
of two positive integers.'''

def divisor(num1, num2):

    gcd = 1
    
    if num1 % num2 == 0:
        return num2
    
    else:
        for k in range(int(num2), 0, -1):
            if num1 % k == 0 and num2 % k == 0:
                gcd = k
                break
    return gcd

divisor(2,3)
divisor(5,15)
divisor(24,100)
divisor(12,96)

'''32. Write a Python program to get the least common multiple (LCM) of two 
positive integers.'''

def lcm(x,y):

    if x > y:
        z = x
    else:
        z = y
        
    while(True):
        if((z % x == 0)) and ((z % y == 0)):
            lowest = z
            break
        z += 1
    return lowest

lcm(9,15)

## Practice the above again

'''33. Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero.'''

def sunny(x,y,z):
    
    if (x == y) or (x == z) or (y == z):
        return 0
    else:
        return(int(x) + int(y) + int(z))

sunny(10,3,4)

'''34. Write a Python program to sum of two given integers. However, if the 
sum is between 15 to 20 it will return 20.'''

def sunny(x,y):
    
    up = int(x) + int(y)
    
    if up in range(15,20):
        return 20
    else:
        return up

sunny(15,3)

'''35. Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.'''

def strange(x,y):
    
    if x == y or (int(x) + int(y) == 5) or (abs(int(x) - int(y)) == 5):
        return True
    else:
        return False

strange(3,8)

'''36. Write a Python program to add two objects if both objects are an 
integer type.'''

def strange(x,y):
    
    if not (isinstance(x, int)) and (isinstance(y, int)):
        return TypeError('x and y must be type int')
    return x + y

strange('3',4)
strange(3,4)

'''37. Write a Python program to display your details like name, age, 
address in three different lines.'''

def personal():
    
    name = 'Appleseed, Johnny'
    address = '666 Mockingbird Ln\nHellsville, WI 99999'
    
    print('Name: %s \nAddress: %s' %(name, address))

personal()

'''38. Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''
    
def solver(x,y):
    print((x + y) * (x + y))
    
solver(4,3)

'''39. Write a Python program to compute the future value of a specified 
principal amount, rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''

def interest(x,y,z):
    
    future = (float(x) * float(1 + y/100) ** float(z))
    print(round(future, 2))
    
interest(10000,3.5,7)

'''40. Write a Python program to compute the distance between the points 
(x1, y1) and (x2, y2).'''

import math

point_a = (2,3)
point_b = (4,5)

x1, y1 = point_a
x2, y2 = point_b

run = x2 - x1
rise = y2 - y1

distance1 = (run**2) + (rise**2)
distance2 = math.sqrt(distance1)

print(distance2)

'''41. Write a Python program to check whether a file exists.'''

import os

os.getcwd()
! ls
os.chdir('/Users/brett/.spyder-py3/sandbox')

print(os.path.isfile('cars.csv'))

'''42. Write a Python program to determine if a Python shell is executing in 
32bit or 64bit mode on OS.'''

import struct
print(struct.calcsize("P") * 8)

##### Note that the rest are system-specific commands and are probably not that 
##### useful. Will wrap it up with these last three and then move on

'''48. Write a Python program to parse a string to Float or Integer.'''

anystring = '12345678.12345'

anyfloat = round(float(anystring), 3) 
print(anyfloat)

mediate = anystring.split('.')

anyint = int(mediate[0])

'''58. Write a python program to find the sum of the first n positive 
integers.'''

def increase(*numlist, n):
    
    new = list(numlist)
    new2 = new[0:n]
    return sum(new2)

increase(1,2,3,5,5,5,6,7,8,3)
# Work on this one...Need to figure out how to get the *args and then 
# an additional argument

## They answered like this:

n = int(input('Enter a number: '))
num_sum = (n * (n + 1))/2
print(num_sum)


'''59. Write a Python program to convert height (in feet and inches) 
to centimeters.'''

def converter():
    
    feet = input('Enter the length in feet: ')
    inches = input('Enter the length in inches: ')
    
    if not isinstance(feet, int) and isinstance(inches, int):
        return TypeError('Feet and inches must be type int')
    if int(inches) > 12:
        return TypeError('There are only 12 inches in one foot')
    
    incher = feet * 12
    
    return str(float(incher + inches) * 2.54) + ' cm'

converter()

### Check it out

'''60. Write a Python program to calculate the hypotenuse of a right 
angled triangle.'''

## Already did this one...

'''61. Write a Python program to convert the distance (in feet) to inches, 
yards, and miles.'''

def feeter():
    feet = float(input('Enter a distance in feet: '))
    
    incher = feet*3
    yards = feet/3
    miles = feet/5000
    
    print('Inches = %.2f' % incher)
    print('Yards = %.2f' % yards)
    print('Miles = %.3f' % miles)

feeter()

'''68. Write a Python program to calculate the sum of the digits in 
an integer.'''

def gerint(num):
    
    num2 = str(num)
    
    empty = []
    
    for i in num2:
        
        empty += i
    
    new = [int(j) for j in empty]
    
    return sum(new)

gerint(555)    

'''69. Write a Python program to sort three integers without using conditional 
statements and loops.'''

def sorter(x,y,z):
    
    high = max(x,y,z)
    low = min(x,y,z)
    middle = (x + y + z) - (low + high)
    print('Highest = %i' % high)
    print('Middle = %i' % middle)
    print('Lowest = %i' % low)

sorter(40,3,7)

'''Look into module names'''

import sys

print(sys.builtin_module_names)

'''83. Write a Python program to test whether all numbers of a list is 
greater than a certain number.'''

sample_list = [10,11,12,14,15,17]
given_num = 3

for i in sample_list:
    if i <= given_num:
        return False
    else:
        return True



'''147. Write a Python function to check whether a number is divisible by 
another number. Accept two integers values form the user. Go to the editor
Click me to see the sample solution'''

def div(x,y):
    if x % y == 0:
        return True
    return False

div(20,5)

'''148. Write a Python function to find the maximum and minimum numbers from 
a sequence of numbers. Go to the editor
Note: Do not use built-in functions.
Click me to see the sample solution'''

## Wowza

def getit(*nums):
    l = nums[0]
    s = nums[0]
    
    for i in nums:
        if i > l:
            l = i
        elif i < s:
            s = i
    return l, s
            
getit(3,4,5,6,5,4,-9,14,15,16,19,10001,2)

'''149. Write a Python function that takes a positive integer and returns 
the sum of the cube of all the positive integers smaller than the specified 
number. Go to the editor
Click me to see the sample solution'''


def cuber(num):
    
    sample = range(num, 0, -1)
    
    total = 0
    
    for i in sample:
        total += i**3
    
    return total

cuber(3)

'''150. Write a Python function to find a distinct pair of numbers whose 
product is odd from a sequence of integer values.'''

def producto(*num):
    
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                product = num[i] * num[j]
                
                if product & 1:
                    return True
                    return False

producto(1,4,5,6,8)    
            
## Don't understand this one^




        
        
        
        









