# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 16:57:22 2014

@author: jpatrickhall@gmail.com

SOLUTION TO EXERCISE 5
"""

### IMPORTS
import csv
import numpy as np

### EXERCISE 5.1: Use the csv module to read the titanic training data
# (train.csv) into a numpy array called data.
nfile_ref = open('train.csv', 'r')
csv_file = csv.reader(nfile_ref)
header = csv_file.next()
data = []
for row in csv_file:
    data.append(row)
data = np.array(data)
nfile_ref.close()

# EXERCISE 5.2
print np.size(data[::, 1].astype(np.float))
print np.sum(data[::, 1].astype(np.float))
print np.sum(data[::, 1].astype(np.float))/np.size(data[::, 1])

# EXERCISE 5.3
women_only_stats = data[0::, 4] == "female"
women_onboard = data[women_only_stats, 1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
print 'Proportion of women who survived is %s' % proportion_women_survived

men_only_stats = data[0::, 4] != "female"
men_onboard = data[men_only_stats, 1].astype(np.float)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print 'Proportion of men who survived is %s' % proportion_men_survived

# EXERCISE 5.4

number_passengers = np.size(data[::, 1])
training_target = data[::, 1].astype(np.float)
training_predictions = np.array([1 if data[i, 4] == 'female' else 0 for i in\
                                 range(0, number_passengers)], dtype='float64')
training_correct_classification_rate =\
    1-(np.sum(np.abs(training_target-training_predictions))/number_passengers)
print 'Training correct classification rate is %s'\
    % training_correct_classification_rate

# EXERCISE 5.5

# Read in test.csv, skipping first row
test_file_ref = open('test.csv', 'r')
test_file = csv.reader(test_file_ref)
skip_header = test_file.next()

# Write predictions file

# Write the column headers.
# For each row in the test file,
# if it a female, then
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
