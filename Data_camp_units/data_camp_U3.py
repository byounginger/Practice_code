#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:26:23 2020

@author: brett

Code for DataCamp Unit 3 on Functions and Scope Control
"""

''' Looking at different types of operators '''

object1 = 'data' + 'analysis' + 'visualization'
object2 = 1 * 3
object3 = '1' * 3

print(object1)
print(object2)
print(object3)


x = 1.02
y1 = str(x)
y2 = print(x)

type(x)
type(y1)
type(y2)

''' Defining functions '''

def shout():
    '''print a string with three exclamation points'''
    shout_word = 'congratulations' + '!!!'
    
    print(shout_word)
    
shout()    


def rando_practice():
    '''trying my hand at another function'''
    middle_finger = 'fuck off' * 3 + '!!!'
    
    print(middle_finger)
    
rando_practice()    

'''Function with a return, because print results in a NoneType function
and return will return a value of an actual type'''

def shout(word):
    '''return any word typed with three exclamation points'''
    shout_word = word + '!!!'
    
    return shout_word

yell = shout('hello')
print(yell)

######

def shout(word1, word2):
    ''''''
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'

    new_shout = shout1 + shout2

    return new_shout

yell = shout('congratulations', 'you')   
print(yell) 

'''Tuples, baby!!!'''

nums = (3, 4, 6)    
num1, num2, num3 = nums    
print(num1)

'''Function with tuples returned'''

def shout(word1, word2):
    ''''''
    shout_word1 = word1 + '!!!'
    shout_word2 = word2 + '!!!'
    
    new_shout = (shout_word1, shout_word2)
    
    return new_shout

yell1, yell2 = shout('congratulations', 'you')

print(yell1)
print(yell2)

''' Bringing it together '''
  
import pandas as pd

df = pd.read_csv('/Users/brett/.spyder-py3/sandbox/tweets.csv')

langs_count = {}

col = df['lang']

for i in col:
    
    if i in langs_count.keys():
        
        langs_count[i] += 1
        
    else:
        
        langs_count[i] = 1
        
print(langs_count)

''' Part II '''

tweets_df = pd.read_csv('/Users/brett/.spyder-py3/sandbox/tweets.csv')

def count_entries(df, col_name):
    '''return a dictionary with counts of entries for the value of each key'''
    
    langs_count = {}
    
    col = df[col_name]
    
    for entry in col:
        
        if entry in langs_count.keys():
            
            langs_count[entry] += 1
            
        else:
            
            langs_count[entry] = 1
            
    return langs_count

result = count_entries(tweets_df, 'lang')

print(result)

'''Scope'''

num = 5

def func():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)

print(func2())

''' Messing with scope '''

team = 'teen titans'

def change_team():
    
    global team
    
    team = 'justice league'
    
print(team)

change_team()

print(team)

import builtins

dir(builtins)

''' Nested functions '''

def three_shouts(word1, word2, word3):
    
    def inner(word):
        
        return word + '!!!'
    
    return (inner(word1), inner(word2), inner(word3))

print(three_shouts('a', 'b', 'c'))

''' Closure '''

def echo(n):
    
    def inner_echo(word1):
        
        echo_word = word1 * n
        
        return echo_word
    
    return inner_echo

once = echo(1)
twice = echo(2)
thrice = echo(3)

print(once('hello'), twice('hello'), thrice('hello'))

'''using nonlocal'''

def echo_shout(word):

    echo_word = word * 2

    print(echo_word)
    
    def shout():
        
        nonlocal echo_word
        
        echo_word = echo_word + '!!!' 
        
    shout()
    
    print(echo_word)
    
echo_shout('hello')

''' Default arguments '''

def shout_echo(word1, echo = 1):
    ''''''
    
    echo_word = word1 * echo
    
    shout_word = echo_word + '!!!' 
    
    return shout_word

no_echo = shout_echo('hey')
with_echo = shout_echo('hey', echo = 5)

print(no_echo)
print(with_echo)

''' More arguments with a boolean '''

def shout_echo(word1, echo = 1, intense = False):
    
    echo_word = word1 * echo
    
    if intense is True:
        
        echo_word_new = echo_word.upper() + '!!!' 
        
    else: 
        
        echo_word_new = echo_word + '!!!' 
        
    return echo_word_new

with_big_echo = shout_echo('hey', echo = 5, intense = True)

big_no_echo = shout_echo('hey', intense = True)

print(with_big_echo)
print(big_no_echo)

''' *args '''

def gibberish(*args):
    
    hodgepodge = ''
    
    for word in args:
        
        hodgepodge += word
        
    return hodgepodge

one_name = gibberish('luke')
many_words = gibberish('luke', 'luck', 'likes', 'lakes')

print(one_name)
print(many_words)

''' *kwargs'''

def report_status(**kwargs):
    
    print('\nBegin: Report\n')
    
    for keys, values in kwargs.items():
        
        print(keys, ":", values)
        
    print('\nEnd Report')

report_status(name = "luke", affiliation = "jedi", status = "missing")

report_status(name = "luke", affiliation = "jedi", status = "missing", likes = 'walks on the beach')

''' Bringing it all together...again'''

def count_entries(df, col_name = 'lang'):
    
    cols_count = {}
    
    col = df[col_name]
    
    for entry in col:
        
        if entry in cols_count.keys():
            
            cols_count[entry] += 1
        
        else:
            
            cols_count[entry] = 1
            
    return cols_count

result1 = count_entries(tweets_df) 
result2 = count_entries(tweets_df, col_name = 'source')

print(result1)
print(result2)           

''' One more time '''

def count_entries(df, *args):

    cols_count = {}
    
    for col_name in args:
        
        col = df[col_name]
        
        for entry in col:
            
            if entry in cols_count.keys():
                
                cols_count[entry] += 1
            
            else:
                
                cols_count[entry] = 1
                
    return cols_count

result1 = count_entries(tweets_df, 'lang') 
result2 = count_entries(tweets_df, 'source', 'lang')

print(result1)
print(result2) 

'''Unit 3.3 - Error messages and lambda functions'''

add_bangs = (lambda word: word + '!!!')
 
print(add_bangs('hello'))

###

echo = (lambda word, echo: word * echo)

echo('hello', 5)

###

spells = ["protego", "accio", "expecto patronum", "legilimens"]

shout_spells = map(lambda word: word + '!!!', spells)

shout = list(shout_spells)

print(shout)

###

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 
              'legolas', 'gimli', 'gandalf']

result = filter(lambda people: len(people) > 6, fellowship)        

out = list(result)        

print(out)

###

from functools import reduce

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce(lambda word1, word2: word1 + word2, stark)

print(result)

###

def shout_echo(word1, echo = 1):
    ''''''
    echo_word = ''
    shout_words = ''
    
    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except:
        print('word1 is a string and echo is an integer')
    return(shout_words)
    
print(shout_echo('fiddlesticks', echo = 5))

###

'''Using the raise Value Error'''

def shout_echo(word1, echo = 1):
    ''''''
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')
    
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    
    return shout_word

print(shout_echo('jeepers', 5))

###

import pandas as pd

df = pd.read_csv('/Users/brett/.spyder-py3/sandbox/tweets.csv')

result = filter(lambda x: x[0:2] == 'RT', df['text'])

res_list = list(result)

print(res_list)

###

def lang_count(df, col_name = 'lang'):
    
    cols_count = {}
    
    try:
    
        col = df[col_name]
        
        for entry in col:
        
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1

        return cols_count
    
    except:
        print('The data frame does not have a(n) ' + col_name + ' column.')
        
result1 = lang_count(df, 'lang')

print(result1)

###

def count_entries(df, col_name = 'lang'):
    
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a(n) ' + col_name + 
        ' column.')
    
    cols_count = {}
    
    col = df[col_name]
    
    for entry in col:
        
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    
    return cols_count

result = count_entries(df, col_name = 'lang')

print(result)

            


