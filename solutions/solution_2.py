# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 16:57:22 2014

@author: jpatrickhall@gmail.com

SOLUTION TO EXERCISE 2
"""

### Count the total number of lines in the file: raw_profiles.txt
i= 0
with open('profiles_raw.txt') as f:
    for i, line in enumerate(f): 
        pass
nlines= i+1

### Clean non-alphabetic characters and convert to lowercase 
### with a progress indicator.
### Write results to 'profiles_clean.txt' 
clean_line= ''
with open('profiles_raw.txt') as in_file:
    with open('profiles_clean.txt', 'w') as out_file:
        for j, line in enumerate(in_file):
            for character in line:
                if (character.isalpha() or character.isspace()):
                    clean_line+= character
                clean_line= clean_line.lower()
            out_file.write(clean_line)
            print 'Line %i/%i cleaned ...' % (j+1, nlines)
print 'Done.'

