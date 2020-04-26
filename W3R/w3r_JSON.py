#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:11:58 2020

@author: brett

JSON Practice

https://www.w3resource.com/python-exercises/python-json-index.php

"""

'''1. Write a Python program to convert JSON data to Python object.'''

import json

json_var = '{"Name":"Burt", "Class":"K", "Age":6}'

py_var = json.loads(json_var)

print("\nName: ", py_var["Name"])
print("Class: ", py_var["Class"])
print("Age: ", py_var["Age"])

''' 2. Write a Python program to convert Python object to JSON data'''

json_var2 = json.dumps(py_var)
print(type(py_var))
print(type(json_var2))
print(json_var2)


'''3. Write a Python program to convert Python objects into JSON strings. 
Print all the values.'''



'''4. Write a Python program to convert Python dictionary object (sort by key) 
to JSON data. Print the object members with indent level 4.'''


'''5. Write a Python program to convert JSON encoded data into Python objects
'''





 



