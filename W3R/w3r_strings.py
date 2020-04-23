#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:34:09 2020

@author: brett

Strings from w3s:
    
https://www.w3resource.com/python-exercises/string/

"""

'''1. Write a Python program to calculate the length of a string.'''

sam_string = 'Hello there, lil bud.'
print(len(sam_string))

### Or
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))

'''2. Write a Python program to count the number of characters (character 
frequency) in a string.'''

sam_string = 'google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def counter(words):
    
    empty_dict = {}
    
    for i in words:
        if i in empty_dict.keys():
            empty_dict[i] += 1
        else: 
            empty_dict[i] = 1
    return empty_dict

counter(sam_string)

'''3. Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''

def cutter(word):
    
    if len(word) < 2:
        print('Empty String')
    
    elif len(word) == 2:
        return word*2
    
    else:
        return word[:2] + word[-2:]
        
string = '3'

cutter(string)

'''4. Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char 
itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

def money(sent):
    
    char = sent[0]
    
    new_sent = sent.replace(char, '$')
    
    new_sent = char + new_sent[1:]
    
    print(new_sent)

sam = 'pauper'

money(sam)

'''5. Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

def swapper(word1, word2):
    
    new_w1 = word2[0:2] + word1[2:]
    
    new_w2 = word1[0:2] + word2[2:]
    
    print(new_w1, new_w2)
    
w1 = 'abc'
w2 = 'xyz'    

swapper(w1, w2)

'''6. Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). If the given string already ends with 'ing' 
then add 'ly' instead. If the string length of the given string is less than 
3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

def participle(word):
    
    if len(word) < 3:
        
        print(word)
    
    elif word[-3:] == 'ing':
        
        print(word + 'ly')
    
    else: 
        
        print(word + 'ing')
    
sam1 = 'abc'    
sam2 = 'string'
sam3 = 'yo'

participle(sam1)
participle(sam2)
participle(sam3)

'''7. Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace 
the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

def charity(words):
    
    snot = words.find('not')
    spoor = words.find('poor')
    
    if spoor > snot and spoor > 0 and snot > 0:
        
        return words.replace(words[snot:(spoor+4)], 'good')
    
    else:
        return words

sam1 = 'The lyrics is not that poor!'
sam2 = 'The lyrics is poor!'

charity(sam1)

'''8. Write a Python function that takes a list of words and returns the 
length of the longest one.'''

sam1 = 'The lyrics is not that poor!'
sam2 = list(sam1.split())


def maxer(word_list):
    
    empty_dict = {}
    
    for i in word_list:
        
        empty_dict[i] = len(i)
    
    up_key = max(empty_dict, key = empty_dict.get)
    
    return up_key

maxer(sam2)

### Their solution:

def maxer2(word_list):
    
    word_len = []
    
    for i in word_list:
        
        word_len.append((len(i), i))
        
    word_len.sort()
    
    return word_len[-1][1]
    
maxer2(sam2)

'''9. Write a Python program to remove the nth index character from a 
nonempty string.'''

def remover(word, n):
    
    duh = word[n]
    
    duh2 = word.replace(duh,'')
    
    return duh2
    
sam = "Woody"

remover(sam, 3)

### Their solution:

def remover(word, n):
    
    first = word[:n]
    last = word[n+1:]
    
    print(first+last)

remover(sam, 3)

'''10. Write a Python program to change a given string to a new string where 
the first and last chars have been exchanged.'''

def switcher(word):
    
    begin = word[0]
    end = word[-1]
    
    print(end + word[1:-1] + begin)

sam = 'sample'

switcher(sam)

'''11. Write a Python program to remove the characters which have odd index 
values of a given string.'''

def otter(word):
    
    count = (len(word))
    
    elly = list(range(0,count,1))
    
    empty_list = []
    empty_list2 = []
    
    for i in elly:
    
        if i % 2 == 0:
        
            empty_list.append(i)
    
    for j in empty_list:
        
        empty_list2.append(word[j])
    
    return ''.join(empty_list2)
    
###

sam = 'supertastic'

otter(sam)    

### Their solution

def otter(word):
    
    empty = ''
    
    for i in range(len(word)):
        
        if i % 2 == 0:
            
            empty = empty + word[i]

    return empty

otter(sam)

'''12. Write a Python program to count the occurrences of each word in a 
given sentence.'''

def senter(sent_string):
    
    empty_dict = {}
    
    for i in sent_string.split():
        
        if i in empty_dict.keys():
            
            empty_dict[i] += 1
        
        else:
        
            empty_dict[i] = 1
    
    return empty_dict
            
sam = "This is a sentence, a really long sentence, that doesn't make much \
    sense"

senter(sam)

'''13. Write a Python script that takes input from the user and displays 
that input back in upper and lower cases.'''

def changer():
    
    start = input('Enter a string: ')
    
    print(start.upper())
    print(start.lower())

changer()

'''14. Write a Python program that accepts a comma separated sequence of words 
as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red'''

def sorter(words):
    
    new = words.split(',')
    
    new.sort()
    
    print(new)

sam = 'red, white, black, green, orange, yellow'

sorter(sam)

new_sam = sam.split(',')

new_sam.sort()

'''15. Write a Python function to create the HTML string with tags around the 
word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''

def add_tags(lett, word):
    
    print('<'+lett+'>'+word+'<'+lett+'>')

add_tags('i','Python')
add_tags('b', 'Python Tutorial')

'''16. 16. Write a Python function to insert a string in the middle of a 
string. 
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}'''

def do_somethin(word, word2):
    
    new_word = list(word)
    print('%s%s%s%s%s' % (new_word[0], new_word[1], word2, new_word[2], 
                        new_word[3]))



abc = '[[]]'
bcd = 'Python'

do_somethin(abc,bcd)

## Their solution:

def do_somethin(word, word2):
    
    return word[:2] + word2 + word[2:]

do_somethin(abc,bcd)

'''17. Write a Python function to get a string made of 4 copies of the last 
two characters of a specified string (length must be at least 2). 
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses'''

def wierder(word):
    
    return word[-2:]*4

wierder('Python')

'''18. Write a Python function to get a string made of its first three 
characters of a specified string. If the length of the string is less than 3 
then return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

def thrice(word):
    
    if len(word) < 3:
        return word
    else:
        return word[:3]

thrice('python')

'''19. Write a Python program to get the last part of a string before a 
specified character. 
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python'''

def extractor(words, char):
    
    new = words.split(char)
    
    return str(new[0])

extractor('https://www.w3resource.com/python-exercises','-')

'''20. Write a Python function to reverses a string if it's length is a 
multiple of 4.'''

def reverser(word):
    
    if len(word) % 4 == 0:
        
        mt = ''
        
        for i in word:
            mt = i + mt
        
        return mt

reverser('horse')
reverser('hosenose')

## Their solution:

def reverser(word):
    
    if len(word) % 4 == 0:
        
        return ''.join(reversed(word))
    
    return word

'''21. Write a Python function to convert a given string to all uppercase if 
it contains at least 2 uppercase characters in the first 4 characters.'''

def earlyupper(word):
    
    new_sum = 0
    word2 = list(word)
    
    for i in word2[0:5]:
        
        if i.isupper():
            
            new_sum += 1 
    
    if new_sum >= 2:
        
        return word.upper()
    
    else:
        
        return word
    
sample = 'AbCdefg'

earlyupper(sample)

## Their solution:

def earlyupper2(word):
    
    new_sum = 0
    for i in word[:5]:
        if i.upper() == i:
            new_sum += 1
    if new_sum >= 2:
        return word.upper()
    return word

earlyupper2(sample)

'''22.Write a Python program to sort a string lexicographically.'''

def alphabets(word):
    
    word2 = list(word.lower())
    word2.sort()
    word3 = ''.join(word2)
    print(word3)

example = 'Salubrious'

alphabets(example)

## Their solution

def alphabets(word):
    
    return sorted(sorted(word), key=str.upper)

alphabets(example)

'''23. Write a Python program to remove a newline in Python.'''

def lineup(words):
    
    words = words.replace('\n', '')
    print(words)
    
sample = 'This is a really long string\nwith multiple\nlinending chars'

lineup(sample)

## Their example

print(sample.rstrip()) # This only works with end-of-line characters

'''24. Write a Python program to check whether a string starts with 
specified characters.'''

def checker(word, chars):
    
    ex = len(chars)
    print(word[:ex] == chars)

checker('outstanding', 'outie')

# Their solution:

sample = 'outstanding'
print(sample.startswith('out'))

'''25. Write a Python program to create a Caesar encryption.
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, 
the shift cipher, Caesar's code or Caesar shift, is one of the simplest 
and most widely known encryption techniques. It is a type of 
substitution cipher in which each letter in the plaintext is replaced 
by a letter some fixed number of positions down the alphabet. For 
example, with a left shift of 3, D would be replaced by A, E would 
become B, and so on. The method is named after Julius Caesar, who used 
it in his private correspondence.'''

print(chr(97))

#65-90 & 97-122

def caesar(words, shift):
    
    words = [ord(i) for i in words]
    words = [j+shift for j in words]
    words = [chr(k) for k in words]
    return ''.join(words)

sample = "In cryptography, a Caesar cipher, also known as Caesar's"
new_sample = caesar(sample, 2)
caesar(new_sample, -2)

