# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:56:34 2014

@author: jpatrickhall@gmail.com

Python exercise SOLUTIONS for Bellarmine Analytics program

1.) Working With Strings
2.) Loops and File I/O 
3.) Lists, Dictionarys and Sets
4.) Scraping Data From the Web 
5.) Numpy and Scipy 
6.) Kaggle Titanic Competition 
7.) Graphing Results

"""

### EXERCISE 1: WORKING WITH STRINGS ##########################################

### This string represents a user being logged by a web server
### It contains information such as the user's operating system and browser

#%%
user_string1= 'Mozilla/5.0 (Windows NT 6.1; WOW64) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Safari/533.1'
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
print user_string1[13:27]

#%%
### EXERCISE 1.2: Print only the user's browser.  
print user_string1[-12:-6]

#%%
# ESCAPE CHARACTERS 
# REFERENCE: https://docs.python.org/2/tutorial/introduction.html#strings

### EXERCISE 1.3: Print the user's operating system and browser as a single tab-delimited string
print user_string1[13:27] + '\t' + user_string1[-12:-6]
#%%
### EXERCISE 1.4: Print the user's operating system and browser on separate lines using only one python print statement. 
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

user_string2= 'Mozilla/5.0 (Linux; Android 2.2) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Mobile Safari/536.5'
user_string3= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5'
#%%

### EXERCISE 1.5: Convert user_string2 and user_string3 to lowercase and print them. Why is this a good idea?

lower2= user_string2.lower()
print lower2
lower3= user_string3.lower()
print lower3

""" 

This is a good idea because now you can search these strings for terms without
worrying about the many different possible cases of the strings you would like to 
find.

""" 
#%%

### EXERCISE 1.6: Use a simple string method to decide whether users 2 and 3 use the same operating system as user 1.

user1_OS= user_string1[13:27].lower() # OS for User 1
print lower2.find(user1_OS) > 0 # Test if User 1 OS in found in User 2 log record 
print lower3.find(user1_OS) > 0 # Test if User 1 OS in found in User 3 log record 

#%%
### EXERCISE 1.7: Print a tab-separated table of each user's operating system and broswer.

line1= 'user1\t' + user_string1[13:27] + '\t' + user_string1[-12:-6]
line2= 'user2\t' + user_string2[13:27] + '\t' + user_string2[-12:-6]
line3= 'user3\t' + user_string3[13:27] + '\t' + user_string3[-12:-6]
print '\n'.join((line1, line2, line3))

#%%
### EXERCISE 2: LOOPS AND FILE I/O ############################################ 
### In exercises 2 and 3 we will clean up several example dating profiles. Once we have 
### the text ready for analysis, we will try to make the best match between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/controlflow.html
# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/2/library/stdtypes.html#string-methods

### EXERCISE 2.1: Count the number of lines in the profiles_raw.txt file.
i= 0
with open('profiles_raw.txt') as f:
    for i, line in enumerate(f): 
        pass
print 'The number of lines is:  %i.' % (i+1)

#%%
### EXERCISE 2.2: Remove all non-alphabetic characters from the profiles_raw.txt file.
### Save the new file as profiles_clean.txt.                   
clean_line= ''
with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for line in in_file:
            for character in line:
                if (character.isalpha() or character.isspace()):
                    clean_line+= character
            out_file.write(clean_line)

#%%
### EXERCISE 2.3: Modify your code from exercise 2.2 to remove all non-alphabetic 
# characters from the profiles_raw.txt file and to convert all lines of new the 
# 'profiles_clean.txt' file to lowercase.   
clean_line= ''
with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for line in in_file:
            for character in line:
                if (character.isalpha() or character.isspace()):
                    clean_line+= character
                clean_line= clean_line.lower()
            out_file.write(clean_line)
  
#%%          
### EXERCISE 2.4: Use the solutions of exercises 2.1 and 2.3 to create a progress indicator 
# for our file cleaning code.               
i= 0
with open('profiles_raw.txt') as f:
    for i, line in enumerate(f): 
        pass
nlines= i+1

clean_line= ''
with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            for character in line:
                if (character.isalpha() or character.isspace()):
                    clean_line+= character
                clean_line= clean_line.lower()
            out_file.write(clean_line)
            print 'Line %i/%i cleaned ...' % (j+1, i+1)
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

#%%         
### EXERCISE 3: LISTS, DICTIONARIES, AND SETS ################################# 
### In exercises 2 and 3 we will clean up several example dating profiles. Once we have 
### the text ready for analysis, we will try to make the best match between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/datastructures.html
# https://docs.python.org/2/library/collections.html

### EXERCISE 3.1: Turn each line into a list to count the number of words in 
# the profiles_raw.txt file.
i= 0
with open('profiles_raw.txt') as f:
    for line in f:
        i+= len(line.split())
print 'The number of words is:  %i.' % (i)

#%%
### EXERCISE 3.2: Use list comprehensions to re-write the solution to exercise 2.4
# in a more pythonic fashion.
nlines= sum(1 for line in open('profiles_raw.txt'))
print 'The number of lines is:  %i.' % (nlines)

with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            out_file.write(' '.join([word.lower() if (word.isalpha() or word.isspace()) else '' for word in line.split()]) + '\n')        
            print 'Line %i/%i cleaned ...' % (j+1, nlines)
print 'Done.'

#%%
### Exercise 3.3: Modify the list comprehension in exercise 3.2 to remove words 
# with 3 or less characters in addition to the other cleaning tasks. 

nlines= sum(1 for line in open('profiles_raw.txt'))
print 'The number of lines is:  %i.' % (nlines)

with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            out_file.write(' '.join([word.lower() if (len(word.strip()) >= 4 and (word.isalpha() or word.isspace())) else '' for word in line.split()]) + '\n')        
            print 'Line %i/%i cleaned ...' % (j+1, nlines)
print 'Done.'

#%%
### Exercise 3.4: Use collections, lists, sets, and dictionaries to create a set of frequently (10+)
# occuring terms in the cleaned profiles and keep only them in the profiles. Create 
# a new file called 'profiles_cleaned_freq.txt'.

# Import the collections module 
import collections

# Create a list of every word in the cleaned profiles
words= []
with open('profiles_clean.txt') as in_file:
    for line in in_file:
        words+= line.split()

# Creates a dictionary of term counts               
term_counts= collections.Counter(words) 
print term_counts

# Creates a set that keeps only terms in the dictionary that occured more that ten times        
keep_set= set([k for k in term_counts.keys() if term_counts[k] >= 10]) 

# Keep only these frequently occuring terms 
with open('profiles_clean.txt') as in_file:
    with open ('profiles_clean_freq.txt', 'w') as out_file:  
        for line in in_file:
            line_list= line.split()
            freq_list= [word for word in line_list if word in keep_set]
            out_file.write(' '.join(freq_list) + '\n')

#%%            
### Exercise 3.5: Use collections and dictionaries to create a dictionary of term counts 
# for each profile. Use these dictionaries of term frequencies to decide which 
# of the profiles are the best match. Print the term counts to a new file called 
# 'profiles_term_counts.txt'.

# Import collections module
import collections

# Print a dictionary of term counts for each individual cleaned profile
# Which of these profiles looks the most compatible to you?            
with open('profiles_clean_freq.txt') as in_file:
    with open('profiles_term_counts.txt', 'w') as out_file:
        for i, line in enumerate(in_file): 
             term_counts= collections.Counter(line.split())
             out_file.write('----------------------------------------\n')
             out_file.write('Profile %i term counts: \n' % (i+1))
             for key in term_counts:
                 out_file.write(key + ' ' + str(term_counts[key]) + '\n')
             
#%%



