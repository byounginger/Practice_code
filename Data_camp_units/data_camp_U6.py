#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:36:53 2020

@author: brett

Data Camp Unit 6 - Intermediate Importing Data in Python

"""

'''Importing flat files from the web with urlretrieve'''

from urllib.request import urlretrieve

import pandas as pd

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

urlretrieve(url, 'winequality-red.csv')

df = pd.read_csv('winequality-red.csv', sep = ';')
print(df.head())

'''opening and reading flat files from the web'''

import matplotlib.pyplot as plt

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

df = pd.read_csv('winequality-red.csv', sep = ';')

print(df.head())

pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

'''importing non-flat files'''

url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

xls = pd.read_excel(url, sheet_name = None)

print(xls.keys())

print(xls['1700'].head())

'''Performing URL requests with urllib'''

from urllib.request import urlopen, Request

url = "http://www.datacamp.com/teach/documentation"

## Get familiar with the request package!!

request = Request("http://www.datacamp.com/teach/documentation")

response = urlopen(request)

print(type(response))

response.close()

'''Printing HTTP requests with urllib'''

from urllib.request import urlopen, Request

url = "http://www.datacamp.com/teach/documentation"

request = Request(url)

response = urlopen(request)

html = response.read()

print(html)

response.close()

'''HTTP requests with the requests package'''

import requests

url = "http://www.datacamp.com/teach/documentation"

r = requests.get(url)

text = r.text

print(text)

'''Parsing HTML with BeautifulSoup'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

pretty_soup = soup.prettify()

print(pretty_soup)

'''Turning a webpage into data with BeautifulSoup'''

import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)

'''Getting the hyperlinks'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

print(soup.title)

a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))

''' Loading and exploring a JSON'''

## Note: Don't have access to the file below, so just pasting in code ##

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
    
''' Further JSON exploration '''

import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

print(json_data['Title'])

print(json_data['Year'])

''' API Requests '''

import requests

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

r = requests.get(url)

print(r.text)

'''JSON from the web '''

import requests

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

r = requests.get(url)

json_data = r.json()

for k in json_data.keys():
    print(k + ':', json_data[k])

'''Wikipedia API'''

import requests

url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

r = requests.get(url)

json_data = r.json()

pizza_extract = json_data['query']['pages']['24768']['extract']

print(pizza_extract)

'''API Authentication'''

conda install -c conda-forge tweepy

import tweepy

access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

## Set the def MyStreamListener:
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

l = MyStreamListener()

stream = tweepy.Stream(auth, l)

stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])

import json

tweets_data_path = '/Users/brett/.spyder-py3/sandbox/tweets3.txt'

tweets_data = []

tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

tweets_file.close()

print(tweets_data[0].keys())

'''Convert the twitter data to a df'''

import pandas as pd

df = pd.DataFrame(tweets_data, columns = ['text','lang'])

print(df.head())

'''Twitter text analysis'''

## word_in_text function:
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    cruz += word_in_text('cruz', row['text'])
    sanders += word_in_text('sanders', row['text'])
    trump += word_in_text('trump', row['text'])
    
'''Plotting the results'''

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)

cd = ['clinton', 'trump', 'sanders', 'cruz']

ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()

## Done!!
