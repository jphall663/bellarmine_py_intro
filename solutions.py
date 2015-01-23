# -*- coding: utf-8 -*-
"""
DISCLAIMER:  
                                                                
THIS INFORMATION IS PROVIDED "AS IS". THERE ARE NO WARRANTIES,
EXPRESSED OR IMPLIED, AS TO MERCHANTABILITY OR FITNESS FOR A
PARTICULAR PURPOSE REGARDING THE ACCURACY OF THE MATERIALS OR CODE
CONTAINED HEREIN.

@author: jpatrickhall@gmail.com

Python exercise SOLUTIONS for Bellarmine Analytics program

1.) Working With Strings
2.) Loops and File I/O
3.) Lists, Dictionaries and Sets
4.) Scraping Data from the Web
5.) Numpy: Kaggle Titanic Competition
6.) IPython: Graphing Results

"""

### EXERCISE 1: WORKING WITH STRINGS ##########################################

### This string represents a user being logged by a web server.
### It contains information such as the user's operating system and browser.

#%%
user_string1 = 'Mozilla/5.0 (Windows NT 6.0; WOW64) App3leWebKit/54.1 (KHTML,\
like Gecko) Version/4.0 Safari/539.1'
print user_string1
#%%

# SLICING
# REFERENCE: https://docs.python.org/2/tutorial/introduction.html#strings

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

#%%
### EXERCISE 1.1: Print only the user's operating system.
print user_string1[user_string1.index('(')+1:user_string1.index(';')]

#%%
### EXERCISE 1.2: Print only the user's browser.
print user_string1[user_string1.rindex(' ')+1:user_string1.rindex('/')]

#%%
# ESCAPE CHARACTERS
# REFERENCE: https://docs.python.org/2/tutorial/introduction.html#strings

### EXERCISE 1.3: Print the user's operating system and browser as a single
# tab-delimited string.
print user_string1[13:27] + '\t' + user_string1[-12:-6]
#%%
### EXERCISE 1.4: Print the user's operating system and browser on separate
# lines using only one python print statement.
print user_string1[13:27] + '\n'+ user_string1[-12:-6]

#%%
### EXERCISE 1.5: What are some other common escape characters?

"""
Other common escape characters include:

\' single quote
\" double quote
\\ backslash
\/ forwardslash
\r carriage return
\b backspace

"""

#%%
# STRING FUNCTIONS
# REFERENCE: https://docs.python.org/2/library/stdtypes.html#string-methods

user_string2 = 'Mozilla/5.0 (Linux; Android 3.2) AppleWebKit/536.4 (KHTML,\
like Gecko) Safari/536.4'
user_string3 = 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/536.4 (KHTML,\
like Gecko) Safari/536.4'
#%%

### EXERCISE 1.5: Convert user_string2 and user_string3 to lowercase and print
# them. Why is this a good idea?

lower2 = user_string2.lower()
print lower2
lower3 = user_string3.lower()
print lower3

"""

This is a good idea because now you can search these strings for terms without
worrying about the many different possible cases of the strings you would like
to find.

"""
#%%

### EXERCISE 1.6: Use a simple string method to decide whether users 2 and 3
# use the same operating system as user 1.

user1_OS = user_string1[13:27].lower() # OS for User 1
print lower2.find(user1_OS) > 0 # Test if User 1 OS in found in User 2
                                # log record
print lower3.find(user1_OS) > 0 # Test if User 1 OS in found in User 3
                                # log record

#%%
### EXERCISE 1.7: Print a tab-separated table of each user's operating system
# and broswer.

line1 = 'user1\t' + user_string1[13:27] + '\t' + user_string1[-12:-6]
line2 = 'user2\t' + user_string2[13:27] + '\t' + user_string2[-12:-6]
line3 = 'user3\t' + user_string3[13:27] + '\t' + user_string3[-12:-6]
print '\n'.join((line1, line2, line3))

### Why does it matter what operating system a user is using?

"""
It is rumored that an online travel agency was able to mark up ticket prices to
users of a certain 'fancy' OS without negatively affecting sales numbers ...
"""

#%%
### EXERCISE 2: LOOPS AND FILE I/O ############################################
# In exercises 2 and 3 we will clean up several example dating profiles. Once
# we have the text ready for analysis, we will try to make the best match
# between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/controlflow.html
# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/2/library/stdtypes.html#string-methods

### EXERCISE 2.1: Count the number of lines in the profiles_raw.txt file.
i = 0
with open('profiles_raw.txt', 'r') as f:
    for i, line in enumerate(f):
        pass
print 'The number of lines is:  %d.' % (i+1)

#%%
### EXERCISE 2.2: Remove all non-alphabetic characters from the
# profiles_raw.txt file. Save the new file as profiles_clean.txt.
clean_line = ''
with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for line in in_file:
            for character in line:
                if character.isalpha() or character.isspace():
                    clean_line += character
            out_file.write(clean_line)
            clean_line = ''
#%%
### EXERCISE 2.3: Modify your code from exercise 2.2 to remove all
# non-alphabetic characters from the profiles_raw.txt file and to convert all
# lines of new the 'profiles_clean.txt' file to lowercase.
clean_line = ''
with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for line in in_file:
            for character in line:
                if character.isalpha() or character.isspace():
                    clean_line += character
                clean_line = clean_line.lower()
            out_file.write(clean_line)
            clean_line = ''
#%%
### EXERCISE 2.4: Use the solutions of exercises 2.1 and 2.3 to create a
# progress indicator for our file cleaning code.
i = 0
with open('profiles_raw.txt', 'r') as f:
    for i, line in enumerate(f):
        pass
nlines = i+1

clean_line = ''
with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            for character in line:
                if character.isalpha() or character.isspace():
                    clean_line += character
                clean_line = clean_line.lower()
            out_file.write(clean_line)
            clean_line = ''
            print 'Line %d/%d cleaned ...' % (j+1, i+1)
print 'Done.'

### Why are progress indicator's important?

"""

Progress indicators are important because sometimes jobs take a long time, or
sometimes you might be unsure how long a job will take. Progress indicators
help prevent:

1.) Starting a job, waiting for hours, and finding out it has only
done a small portion of it's work (because you underestimated something).

OR

2.) After waiting for a job to finish for a long time you might get frustrated
and stop it ... just to find out it was almost finished !!!

"""

### BONUS EXERCISE 2.5: Execute the solution_2.py file from the OS command
# prompt.

#%%
### EXERCISE 3: LISTS, DICTIONARIES, AND SETS #################################
# In exercises 2 and 3 we will clean up several example dating profiles. Once
# we have the text ready for analysis, we will try to make the best match
# between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/datastructures.html
# https://docs.python.org/2/library/collections.html

### EXERCISE 3.1: Turn each line into a list to count the number of words in
# the profiles_raw.txt file.
i = 0
with open('profiles_raw.txt', 'r') as f:
    for line in f:
        i += len(line.split())
print 'The number of words is:  %d.' % (i)

#%%
### EXERCISE 3.2: Use list comprehensions to re-write the solution to exercise
# 2.4 in a more "pythonic" fashion.
nlines = sum(1 for line in open('profiles_raw.txt', 'r'))
print 'The number of lines is:  %d.' % (nlines)

with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            out_file.write(' '.join([word.lower() if (word.isalpha() or \
                     word.isspace()) else '' for word in line.split()]) + '\n')
            print 'Line %d/%d cleaned ...' % (j+1, nlines)
print 'Done.'



#%%
### Exercise 3.3: Modify the list comprehension in exercise 3.2 to remove words
# with 3 or less characters in addition to the other cleaning tasks.

nlines = sum(1 for line in open('profiles_raw.txt', 'r'))
print 'The number of lines is:  %d.' % (nlines)

with open('profiles_raw.txt', 'r') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            out_file.write(' '.join([word.lower() if (len(word.strip()) >= 4 \
                and (word.isalpha() or word.isspace())) else '' \
                for word in line.split()]) + '\n')
            print 'Line %d/%d cleaned ...' % (j+1, nlines)
print 'Done.'

# In reality, this list comprehension is waaaaay too long to be understandable.
# This is just for practice.

#%%
### Exercise 3.4: Use collections, lists, sets, and dictionaries to create a
# set of frequently (10+) occuring terms in the cleaned profiles and keep only
# them in the profiles. Create a new file called 'profiles_cleaned_freq.txt'.

# Import the collections module.
import collections

# Create a list of every word in the cleaned profiles.
words = []
with open('profiles_clean.txt', 'r') as in_file:
    for line in in_file:
        words += line.split()

# Creates a dictionary of term counts.
term_counts = collections.Counter(words)
print term_counts

# Creates a set that keeps only terms in the dictionary that occured more that
# ten times.
keep_set = set([k for k in term_counts.keys() if term_counts[k] >= 10])

# Keep only these frequently occuring terms.
with open('profiles_clean.txt', 'r') as in_file:
    with open('profiles_clean_freq.txt', 'w') as out_file:
        for line in in_file:
            line_list = line.split()
            freq_list = [word for word in line_list if word in keep_set]
            out_file.write(' '.join(freq_list) + '\n')

#%%
### Exercise 3.5: Use collections and dictionaries to create a dictionary of
# term counts for each profile. Use these dictionaries of term frequencies to
# decide which of the profiles are the best match. Print the term counts to a
# new file called 'profiles_term_counts.txt'.

# Import collections module.
import collections

# Print a dictionary of term counts for each individual cleaned profile
# Which of these profiles looks the most compatible to you?
with open('profiles_clean_freq.txt', 'r') as in_file:
    with open('profiles_term_counts.txt', 'w') as out_file:
        for i, line in enumerate(in_file):
            term_counts = collections.Counter(line.split())
            out_file.write('----------------------------------------\n')
            out_file.write('Profile %d term counts: \n' % (i+1))
            for key in term_counts:
                out_file.write(key + ' ' + str(term_counts[key]) + '\n')

#%%
### EXERCISE 4: SCRAPING DATA FROM THE WEB ####################################

# REFERENCES:
#https://docs.python.org/2/howto/urllib2.html
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://docs.python.org/2/tutorial/controlflow.html#more-on-defining-functions

import urllib2
from bs4 import BeautifulSoup
url = 'http://www.bellarmine.edu/analytics/'

### EXERCISE 4.1: Use urllib2 and BeautifulSoup to scrape information from the
# Bellarmine MSA homepage and print it to the console.
connection = urllib2.urlopen(url)
print BeautifulSoup(connection).prettify()

#%%
### EXERCISE 4.2: Define a function to extract only the text within paragraphs
# from a web page and print that text to the console. Use the Bellarmine MSA
# page to test your function.

# Define the get_pretty_text_from_url function.
def get_pretty_text_from_url(url_):
    """ This is how you document a function.

    This function connects to a url, reads the url, finds blocks of text in
    the read data, and prints them to the console.

    Args:
        url_: The URL to which we will connect.

    """

    # Connect to the url.
    connection_ = urllib2.urlopen(url_)

    # Use the find_all function from BeautifulSoup to locate the paragraphs.
    for block in BeautifulSoup(connection_).find_all('p'):
        # Use the get_text function from BeautifulSoup to extract the text
        # from each paragraph.
        print block.get_text()
        print '\n'

# Execute the function.
get_pretty_text_from_url(url)

#%%
### EXERCISE 4.3: Use the get_pretty_text_from_url function to cycle through
# every link on the Bellarmine MSA page and print the text from every paragraph
# of every link to the console.

# REFERENCE: https://docs.python.org/2/tutorial/errors.html

# Connect to the url
connection = urllib2.urlopen(url)
# Use a for loop and the BeautifulSoup find_all() function to cycle through
# every link on the Bellarmine MSA page.
# find_all('a') will locate hyperlinks.
for link in BeautifulSoup(connection).find_all('a'):
    # get('href') will extract links.
    link = link.get('href')
    # Check that a link was extracted successfully.
    if link:
        # Skip internal links.
        if link.startswith('http://') or link.startswith('https://'):
            # Use a try-catch block to continue to new links in the list even
            # if a given link causes an error.
            try:
                get_pretty_text_from_url(link)
            except:
                print 'Link %s is unavailable.' % link
                continue

### This may take a few minutes to run.

#%%
### EXERCISE 4.4. Scrape the famous Abolone data set from the UCI repository
# and write it to a CSV file.

# Read a bit about the file.
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/\
abalone.names'
get_pretty_text_from_url(url)

# Fetch the data and save it.
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/\
abalone.data'
connection = urllib2.urlopen(url)
# Since the structure of the page is very simple, we can use the
# urllib2 read() function to parse the table.
table = connection.read()
# Open a new CSV file, 'abolone.csv', and write the table to the CSV using a
# for loop.
nfile = open('abalone.csv', 'w')
for line in table.split('\n'):
    line = line.strip()
    if line != '':
        nfile.write(line + '\n')
nfile.close()

#%%

# EXERCISE 4.5: Name some other places on the web to find data.
"""
- https://www.data.gov/
- http://archive.ics.uci.edu/ml/
- http://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public
- APIs: https://developers.facebook.com/, https://dev.twitter.com/
- https://archive.org/web/
- http://www.kaggle.com/
...
"""
#%%
### EXERCISE 5: KAGGLE TITANIC COMPETITION ####################################

### REFERENCES:
# http://www.kaggle.com/c/titanic-gettingStarted
# http://wiki.scipy.org/Tentative_NumPy_Tutorial
# https://docs.python.org/2/library/csv.html
# gendermodel.py - by Kaggle user AstroDave

#%%
### EXERCISE 5.1: Use the csv module to read the titanic training data
# (train.csv) into a numpy array called data.
import csv as csv
import numpy as np

nfile_ref = open('train.csv', 'r')
csv_file = csv.reader(nfile_ref)   # Load the csv file.
header = csv_file.next()           # Skip the first line as it is a header.
data = []                          # Create a variable to hold the data.

for row in csv_file:               # Skip through each row in the csv file,
    data.append(row)               # adding each row to the data variable.
data = np.array(data)              # Then convert from a list to a Numpy array.
nfile_ref.close()

### Numpy also has:
# data = np.genfromtxt('train.csv', delimiter=',', skip_header=1)
# But the data needs to be really clean.

#%%
### EXERCISE 5.2
# A: How many people were on the titanic?
number_passengers = np.size(data[::, 1]) # :: means every element
print number_passengers                  # [::,1] every row in the first column
                                         # Numpy matrices [rows, columns]
# B: How many people survived?
number_survived = np.sum(data[::, 1].astype(np.float))
print number_survived

# C: What proportion of people survived?
proportion_survivors = number_survived / number_passengers
print proportion_survivors

#%%
# EXERCISE 5.3: "WOMEN AND CHILDREN FIRST!"
# What proportion of women survived? What proportion of men survived?

# This finds where all the women are in the data set.
# 1st column of data (survived= 0,1), but only women.
women_only_stats = data[0::, 4] == "female"
women_onboard = data[women_only_stats, 1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
print 'Proportion of women who survived is %s' % proportion_women_survived

# This finds all the men.
# 1st column of data (survived = 0,1), but only men.
men_only_stats = data[0::, 4] != "female"
men_onboard = data[men_only_stats, 1].astype(np.float)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print 'Proportion of men who survived is %s' % proportion_men_survived

#%%
# EXERCISE 5.4: Let's see how accurate our model is on the training data.
# For every person in the training data, predict that men will die and
# women will survive. What percentage of the time are we correct? Is this
# more accurate than predicting everyone dies?

training_target = data[::, 1].astype(np.float)
training_predictions = np.array([1 if data[i, 4] == 'female' else 0 for i in\
    range(0, number_passengers)], dtype='float64')
training_correct_classification_rate =\
    1-(np.sum(np.abs(training_target-training_predictions))/number_passengers)
print 'Training correct classification rate is %s'\
    % training_correct_classification_rate

# Is this more accurate than predicting everyone dies? YES
# The correct classification rate for predicting everyone dies is:
# 1-proportion_survivors = 0.616161616162

#%%
# EXERCISE 5.5: Use the results of this analysis to make predictions about
# the passengers in the test set. Basically, if the passenger was a male, we
# predict he will die. If she was female, we predict she will survive.
#
# Make a CSV file containing only two columns:
# First column: the passenger IDs from the test.csv file.
# Second column: a 0 if the passender was male; a 1 if the passenger was female.
# The first row (header) should read: "PassengerId", "Survived"

# Read in test.csv, skipping first row
test_file_ref = open('test.csv', 'r')
test_file = csv.reader(test_file_ref)
skip_header = test_file.next()

# Write predictions file

# Write the column headers.
# For each row in the test file,
# if it is a female, then
# write the PassengerId, and predict 1.
# Otherwise the passenger is male,
# write the PassengerId, and predict 0.
pred_file_ref = open('gendermodel.csv', 'w')
predictions_file = csv.writer(pred_file_ref)
predictions_file.writerow(["PassengerId", "Survived"])
for row in test_file:
    if row[3] == 'female':
        predictions_file.writerow([row[0], "1"])
    else:
        predictions_file.writerow([row[0], "0"])

test_file_ref.close()
pred_file_ref.close()

#%%
# BONUS EXERCISE 5.6: Submit your model to the Kaggle competition. What was
# your score? What does this number mean?

"""
0.76555

This is the proportion of correct predictions in the test set. So about 77% of
our predictions are correct in the test data - this is pretty good for real
data.

"""
#%%
### EXERCISE 6: IPYTHON: PLOTTING RESULTS #####################################

### REFERENCES:
# http://ipython.org/
# http://matplotlib.org/
# http://nbviewer.ipython.org/github/jphall663/bellarmine_py_intro/blob/master/Titanic.ipynb

### To start an Ipython session:
# 1.) Open a command prompt and change directories to the class working
#     directory.
# 2.) Start an Ipython session by typing something like:
#     C:\Anaconda\ipython.exe notebook
# 2.) Open a browser and navigate to the given url,
#     probably something like: http://localhost:8888/
# 3.) Press 'New Notebook' in the upper righthand corner.
# 4.) Enter the python statements in this exercise into the notebook prompt.

# We are going to construct a simple stacked bar chart ...

# Import the training data.
import csv as csv
import numpy as np

nfile_ref = open('train.csv', 'r')
csv_file = csv.reader(nfile_ref)   # Load the csv file.
header = csv_file.next()           # Skip the first line as it is a header.
data = []                          # Create a variable to hold the data.

for row in csv_file:               # Skip through each row in the csv file,
    data.append(row[0:])           # adding each row to the data variable.
data = np.array(data)              # Then convert from a list to a Numpy array.
nfile_ref.close()

# Import matplotlib and allow it to plot in the notebook.
import matplotlib.pyplot as plt
%matplotlib inline

# Import Numpy
import numpy as np


# Make some magic numbers for the plot ... like:
# The location along the x-axis where the bars will sit.
# And the width of the bars.
bottom_locs = np.array([1., 2.])
width = 0.3

# Define the actual quanities to plot:
# The numbers of men who died and who survived.
# The numbers of women who died and who survived.

# This finds all the men.
# 1st column of data (survived = 0,1), but only men.
men_only_stats = data[0::, 4] != "female"
men_onboard = data[men_only_stats, 1].astype(np.float)
men = (np.size(men_onboard)-np.sum(men_onboard), np.sum(men_onboard))

# This finds all the women.
# 1st column of data (survived = 0,1), but only women.
women_only_stats = data[0::, 4] == "female"
women_onboard = data[women_only_stats, 1].astype(np.float)
women = (np.size(women_onboard)-np.sum(women_onboard), np.sum(women_onboard))

# Add the values to the plot.
plt.bar(bottom_locs, men, label='Male', width=width)
plt.bar(bottom_locs, women, color='m', label='Female', width=width, bottom=men)

# Decorate the plot.
plt.ylabel('Count')
plt.title('Who Survived the Titanic?')
plt.legend(loc='best')
plt.xticks(bottom_locs+width/2., ('Died', 'Survived'))
