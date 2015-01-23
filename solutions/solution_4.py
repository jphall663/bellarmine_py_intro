# -*- coding: utf-8 -*-
"""
DISCLAIMER:  
                                                                
THIS INFORMATION IS PROVIDED "AS IS". THERE ARE NO WARRANTIES,
EXPRESSED OR IMPLIED, AS TO MERCHANTABILITY OR FITNESS FOR A
PARTICULAR PURPOSE REGARDING THE ACCURACY OF THE MATERIALS OR CODE
CONTAINED HEREIN.

@author: jpatrickhall@gmail.com

SOLUTION TO EXERCISE 4
"""

import urllib2
from bs4 import BeautifulSoup

# Define the get_pretty_text_from_url function.
def get_pretty_text_from_url(url_):
    """ Connects to a url, reads it, prints block of text to console

    Args:
        url_: The URL to which to connect

    """

    connection_ = urllib2.urlopen(url_)
    for block in BeautifulSoup(connection_).find_all('p'):
        print block.get_text()
        print '\n'

# Execute the function.
url = 'http://www.bellarmine.edu/analytics/'
get_pretty_text_from_url(url)

### Cycle through every link on the Bellarmine MSA page and print the text from
# every paragraph of every link to the console.

# Connect to the url
connection = urllib2.urlopen(url)
for link in BeautifulSoup(connection).find_all('a'):
    link = link.get('href')
    try:
        if link.startswith('http://') or link.startswith('https://'):
            get_pretty_text_from_url(link)
    except:
        print 'Link %s is unavailable.' % link
        continue

### Scrape the famous Abolone data set from the UCI repository and
# write it to a CSV file.

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/\
abalone.data'
connection = urllib2.urlopen(url)
table = connection.read()
ofile_ref = open('abalone.csv', 'w')
for line in table.split('\n'):
    line = line.strip()
    if line != '':
        ofile_ref.write(line + '\n')
ofile_ref.close()
print table
