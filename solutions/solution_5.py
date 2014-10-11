# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 16:57:22 2014

@author: jpatrickhall@gmail.com

SOLUTION TO EXERCISE 5
"""

### IMPORTS 
import csv as csv
import numpy as np

### EXERCISE 5.1: Use the csv module to read the titanic training data 
# (train.csv) into a numpy array called data.   
o= open('train.csv', 'rb')
csv_file= csv.reader(o)                                
header= csv_file.next()                                
data= []                                               
for row in csv_file:                                  
    data.append(row[0:])                               
data= np.array(data)                                  
o.close()


### EXERCISE 5.2
print np.size(data[::,1].astype(np.float))  
print np.sum(data[::,1].astype(np.float))
print np.sum(data[::,1].astype(np.float))/np.size(data[::,1].astype(np.float))                             
          
# EXERCISE 5.3: "
women_only_stats= data[0::,4] == "female" 	              
women_onboard= data[women_only_stats,1].astype(np.float) 
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
print 'Proportion of women who survived is %s' % proportion_women_survived

men_only_stats= data[0::,4] != "female" 	             
men_onboard= data[men_only_stats,1].astype(np.float)     
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print 'Proportion of men who survived is %s' % proportion_men_survived

# EXERCISE 5.4: Use the results of this analysis to make predictions about the 
# the passengers in the test set.

# Read in test.csv, skipping first row
o= open('test.csv', 'r')
test_file= csv.reader(o)
skip_header= test_file.next()

# Write predictions file
p= open('gendermodel.csv', 'w')
predictions_file= csv.writer(p)
predictions_file.writerow(["PassengerId", "Survived"]) # Write the column headers.
for row in test_file:                                  # For each row in the test file,
    if (row[3] == 'female'):                           # fs it a female, then
        predictions_file.writerow([row[0], "1"])       # write the PassengerId, and predict 1.
    else:                                              # Otherwise the passenger is male,
        predictions_file.writerow([row[0], "0"])       # write the PassengerId, and predict 0.

o.close()
p.close()
