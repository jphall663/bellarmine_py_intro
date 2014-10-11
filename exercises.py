# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:56:34 2014

@author: jpatrickhall@gmail.com

Python exercises for Bellarmine Analytics program

1.) Working With Strings
2.) Loops and File I/O 
3.) Lists, Dictionarys and Sets
4.) Scraping Data From the Web 
5.) Numpy: Kaggle Titanic Competition 
6.) Ipython: Graphing Results

"""

### PREFACE ###################################################################

### A quick note about comments ..
### Lines like this are called comments - they are not executed.
#%% 
# Comments like this create separate cells in the Spyder IDE.
#%%
"""
You can have multi-line comments by using triple quotes ...
like this.
"""

### A quick note about working directories ...
# All the exercises below assume you have set your working directory
# to the directory you downloaded for the class. Use the working directory 
# dialog in the upper right hand corner of the Spyder IDE to set your working 
# directory. 

### EXERCISE 1: WORKING WITH STRINGS ##########################################

### This string represents a user being logged by a web server.
### It contains information such as the user's operating system and browser.
user_string1= 'Mozilla/5.0 (Windows NT 6.0; WOW64) App3leWebKit/54.1 (KHTML, like Gecko) Version/4.0 Safari/539.1'
print user_string1

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

user_string2= 'Mozilla/5.0 (Linux; Android 3.2) AppleWebKit/536.4 (KHTML, like Gecko) Safari/536.4'
user_string3= 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/536.4 (KHTML, like Gecko) Safari/536.4'
### EXERCISE 1.5: Convert user_string2 and user_string3 to lowercase and print them. Why is this a good idea?

### EXERCISE 1.6: Use a simple string method to decide whether users 2 and 3 use the same operating system as user 1.

### EXERCISE 1.7: Print a tab-separated table of each user's operating system and broswer.

### Why does it matter what operating system a user is using?

### EXERCISE 2: LOOPS AND FILE I/O ############################################ 
### In exercises 2 and 3 we will clean up several example dating profiles. Once we have 
### the text ready for analysis, we will try to make the best match between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/controlflow.html
# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/2/library/stdtypes.html#string-methods

### EXERCISE 2.1: Count the number of lines in the profiles_raw.txt file using a for loop.

### EXERCISE 2.2: Remove all non-alphabetic characters from the profiles_raw.txt file.
### Save the new file as profiles_clean.txt.                   

### EXERCISE 2.3: Modify your code from exercise 2.2 (remove all non-alphabetic 
# characters from the profiles_raw.txt file) AND to convert all lines of new the 
# 'profiles_clean.txt' file to lowercase.   
  
### EXERCISE 2.4: Use the solutions of exercises 2.1 (counting the number of lines in
# profiles_raw.txt) and 2.3 (removing all non-alphabetic character and converting 
# to lowercase) to add a progress indicator to our file cleaning code. The 
# progress indicator should tell you which line of the file your program is 
# working on.   
  
### Why do you think progress indicator's are important? 
  
### BONUS EXERCISE 2.5: Execute the solution_2.py file from the OS command prompt. 
        
### EXERCISE 3: LISTS, DICTIONARIES, AND SETS ################################# 
### In exercises 2 and 3 we will clean up several example dating profiles. Once we have 
### the text ready for analysis, we will try to make the best match between profiles in exercise 3.

# REFERENCES:
# https://docs.python.org/2/tutorial/datastructures.html
# https://docs.python.org/2/library/collections.html

### EXERCISE 3.1: Turn each line into a list to count the number of words in 
# the profiles_raw.txt file.

### EXERCISE 3.2: Use list comprehensions to re-write the solution to exercise 2.4
# (remove all non-alphabetic characters from the profiles_raw.txt and convert
# to lowercase) in a more pythonic fashion.

### Exercise 3.3: Modify the list comprehension in exercise 3.2 (remove all 
# non-alphabetic characters from the profiles_raw.txt and convert to lowercase) 
# to also remove words with 3 or less characters in addition to the other cleaning tasks. 

### Exercise 3.4: Use collections, lists, sets, and dictionaries to create a set of frequently (10+)
# occuring terms in the cleaned profiles and keep only them in the profiles. Create 
# a new file called 'profiles_cleaned_freq.txt'.

# (HINT) Import the collections module. 

# (HINT) Create a list of every word in the cleaned profiles.

# (HINT) Create a dictionary of term counts using the Counter collection.              

# (HINT) Create a set that keeps only terms in the dictionary that occured more than ten times.       

# (HINT) Compare a list of the words in a line to the set of frequent terms to 
# keep only the frequently occuring terms.
     
### Exercise 3.5: Use collections and dictionaries to create a dictionary of term counts 
# for each profile. Use these dictionaries of term frequencies to decide which 
# of the profiles are the best match. Print the term counts to a new file called 
# 'profiles_term_counts.txt'.

# (HINT) Import collections module.

# (HINT) Print a dictionary of term counts for each individual cleaned profile.

# Which of these profiles looks the most compatible to you? 
# (HINT) Compare the term counts of important words.           

### EXERCISE 4: SCRAPING DATA FROM THE WEB ####################################

# REFERENCE: https://docs.python.org/2/howto/urllib2.html
# REFERENCE: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# REFERENCE: https://docs.python.org/2/tutorial/controlflow.html#more-on-defining-functions

url= 'http://www.bellarmine.edu/analytics/'

### EXERCISE 4.1: Use urllib2 and BeautifulSoup to scrape information from the 
# Bellarmine MSA homepage and print it to the console.  

### EXERCISE 4.2: Define a function to extract only the text within paragraphs 
# from a web page and print that text to the console. Use the Bellarmine MSA 
# page to test your function.  

# (HINT) Define the get_pretty_text_from_url function by ... 
# (HINT) Connecting to the url.
# (HINT) Using the find_all function from BeautifulSoup to locate the paragraphs.
# (HINT) find_all('p')
# (HINT) Using the get_text function from BeautifulSoup to extract the text from 
# from each paragraph.
# (HINT) Execute the function - don't forget!

### EXERCISE 4.3: Use the get_pretty_text_from_url function to cycle through 
# every link on the Bellarmine MSA page and print the text from every paragraph 
# of every link to the console.  

# REFERENCE: https://docs.python.org/2/tutorial/errors.html

# (HINT) Connect to the url
# (HINT) Use a for loop and the BeautifulSoup find_all() function to cycle through
# every link on the Bellarmine MSA page.
# (HINT) find_all('a') will locate hyperlinks.
# (HINT) get('href') will extract links.
# (HINT) Check that a link was extracted successfully.
# (HINT) We can skip internal links.
# (HINT) Use a try-catch block to continue to new links even if a given link 
# causes an error.
# (HINT) This may take a few minutes to run.
          
### EXERCISE 4.4. Scrape the famous Abolone data set from the UCI repository and
# write it to a CSV file.          

# (HINT) Read a bit about the file.
url= 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.names'
url= 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

# (HINT) Since the structure of the page is very simple, we can use the 
# urllib2 read() function to parse the table. We don't need BeautifulSoup.
# (HINT) Open a new CSV file, 'abolone.csv', and write the table to the CSV using a 
# for loop.  

# EXERCISE 4.5: Name some other places on the web to find data.

### EXERCISE 5: KAGGLE TITANIC COMPETITION ####################################

### REFERENCES: 
# http://www.kaggle.com/c/titanic-gettingStarted
# http://wiki.scipy.org/Tentative_NumPy_Tutorial
# https://docs.python.org/2/library/csv.html
# gendermodel.py - by Kaggle user AstroDave

### EXERCISE 5.1: Use the csv module to read the titanic training data 
# (train.csv) into a numpy array called data.   

### EXERCISE 5.2
# A: How many people were on the titanic?
# B: How many people survived?
# C: What proportion of people survived?

# EXERCISE 5.3: "WOMEN AND CHILDREN FIRST!" 
# What proportion of women survived? What proportion of men survived?

# EXERCISE 5.4: Use the results of this analysis to make predictions about the 
# the passengers in the test set. Basically, if the passenger was a male, we
# predict he will die. If she was female, we predict she will survive. 
#
# Make a CSV file containing only two columns:
# First column: the passenger IDs from the test.csv file.
# Second column: a 0 if the passender was male; a 1 if the passenger was female. 
# The first row (header) should read: "PassengerId", "Survived"

# (HINT) First, read in test.csv, skipping the first row.
# (HINT) Then, write the predictions file ...
# (HINT) Write the column headers. Then, for each row in the test file, if it 
# is a female, then write the PassengerId, and predict 1. Otherwise the 
# passenger is male, and write the PassengerId, and predict 0.

# BONUS EXERCISE 5.5: Submit your model to the Kaggle competition. What was 
# your score? What does this number mean?

### EXERCISE 6: IPYTHON: PLOTTING RESULTS #####################################

### REFERENCES:
# http://ipython.org/
# http://matplotlib.org/
# http://nbviewer.ipython.org/github/jphall663/bellarmine_py_intro/blob/master/Titanic.ipynb

### To start an Ipython session:
# 1.) Open a command prompt and change directories to the class working directory.
# 2.) Start an Ipython session by typing something like:
#     C:\Anaconda\ipython.exe notebook
# 2.) Open a browser and navigate to the given url, 
#     probably something like: http://localhost:8888/
# 3.) Press 'New Notebook' in the upper righthand corner.
# 4.) Enter the python statements in this exercise into the notebook prompt 
# one-by-one. 

# We are going to construct a simple stacked bar chart ... 

# Import the training data. 
import csv as csv
import numpy as np

o= open('train.csv', 'r')
csv_file= csv.reader(o)                                # Load the csv file.
header= csv_file.next()                                # Skip the first line as it is a header.
data= []                                               # Create a variable to hold the data.

for row in csv_file:                                   # Skip through each row in the csv file,
    data.append(row[0:])                               # adding each row to the data variable.
data= np.array(data)                                   # Then convert from a list to a Numpy array.
o.close()

# Import matplotlib and allow it to plot in the notebook.
import matplotlib.pyplot as plt
%matplotlib inline                                     

# Import Numpy
import numpy as np

# Make some magic numbers for the plot ... like:
# The location along the x-axis where the bars will sit.
# And the width of the bars.
bottom_locs= np.array([1.,2.])
width= 0.3                     

# Define the actual quanities to plot:
# The numbers of men who died and who survived.
# The numbers of women who died and who survived.
men_only_stats= data[0::,4] != "female"                   # This finds all the men. 
men_onboard= data[men_only_stats,1].astype(np.float)      # 1st column of data (survived= 0,1), but only men.
men= (np.size(men_onboard)-np.sum(men_onboard), np.sum(men_onboard))

women_only_stats= data[0::,4] == "female"                 # This finds all the women. 
women_onboard= data[women_only_stats,1].astype(np.float)  # 1st column of data (survived= 0,1), but only women. 
women= (np.size(women_onboard)-np.sum(women_onboard), np.sum(women_onboard))

# Add the values to the plot.
plt.bar(bottom_locs, men, label= 'Male', width= width)
plt.bar(bottom_locs, women, color= 'm', label= 'Female', width= width, bottom= men)

# Decorate the plot.
plt.ylabel('Count')
plt.title('Who Survived the Titanic?')
plt.legend(loc='best')
plt.xticks(bottom_locs+width/2., ('Died', 'Survived'))