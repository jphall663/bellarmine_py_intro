# -*- coding: utf-8 -*-
"""

Copyright (c) 2015 by Patrick Hall, jpatrickhall@gmail.com
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
   
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

-------------------------------------------------------------------------------

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
