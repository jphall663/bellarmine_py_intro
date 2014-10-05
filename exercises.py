# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:56:34 2014

@author: patrickh

Python exercises for Bellarmine Analytics program

1.) Strings
2.) File I/O 
3.) Lists, Dictionarys and Sets
4.) Retrieving Data From the Web 
5.) Numpy/Scipy 
6.) Kaggle Titanic competition 
7.) Graphing Results

"""

### EXERCISE 1: WORKING WITH STRINGS ##########################################

### This string represents a user being logged by a web server
### It contains information such as the user's operating system and browser
user_string= 'Mozilla/5.0 (Windows NT 6.1; WOW64) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Safari/533.1'
print user_string

# SLICING
# REFERENCE: https://docs.python.org/2/tutorial/introduction.html#strings

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

### EXERCISE 1.1: Print only the user's operating system. 

### EXERCISE 1.2: Print only the user's browser.  
 
# ESCAPE CHARACTERS 
# REFERENCE: https://docs.python.org/2/tutorial/introduction.html#strings

### EXERCISE 1.3: Print the user's operating system and browser as a single tab-delimited string.

### EXERCISE 1.4: Print the user's operating system and browser on separate lines using only one python print statement. 

### EXERCISE 1.5: What are some other common escape characters?

# STRING FUNCTIONS
# REFERENCE: https://docs.python.org/2/library/stdtypes.html#string-methods

user_string2= 'Mozilla/5.0 (Linux; Android 2.2) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Mobile Safari/536.5'
user_string3= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5'

### EXERCISE 1.5: Convert user_string2 and user_string3 to lower case and print them. Why is this a good idea?

### EXERCISE 1.6: Use a simple string method to decide whether users 2 and 3 use the same operating system as user 1.

### EXERCISE 1.7: Print a tab-separated table of each user's operating system and broswer.

