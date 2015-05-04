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

SOLUTION TO EXERCISE 6

"""

# Imports
import matplotlib.pyplot as plt
import csv
import numpy as np

# Import the training data.
nfile_ref = open('train.csv', 'r')
csv_file = csv.reader(nfile_ref)   # Load the csv file.
header = csv_file.next()           # Skip the first line as it is a header.
data = []                          # Create a variable to hold the data.

for row in csv_file:               # Skip through each row in the csv file,
    data.append(row[0:])           # adding each row to the data variable.
data = np.array(data)              # Then convert from a list to a Numpy array.
nfile_ref.close()

# Make some magic numbers for the plot ... like:
# The location along the x-axis where the bars will sit.
# And the width of the bars.
bottom_locs = np.array([1., 2.])
width = 0.3

# Define the actual quanities to plot:
# The numbers of men who died and who survived.
# The numbers of women who died and who survived.
men_only_stats = data[0::, 4] != "female"
men_onboard = data[men_only_stats, 1].astype(np.float)
men = (np.size(men_onboard) - np.sum(men_onboard), np.sum(men_onboard))

women_only_stats = data[0::, 4] == "female"
women_onboard = data[women_only_stats, 1].astype(np.float)
women = (np.size(women_onboard)-np.sum(women_onboard), np.sum(women_onboard))

# Add the values to the plot.
plt.bar(bottom_locs, men, label='Male', width=width)
plt.bar(bottom_locs, women, color='m', label='Female', width=width,\
        bottom=men)

# Decorate the plot.
plt.ylabel('Count')
plt.title("Who Survived the Titanic?")
plt.legend(loc='best')
plt.xticks(bottom_locs+width/2., ('Died', 'Survived'))
plt.show()
