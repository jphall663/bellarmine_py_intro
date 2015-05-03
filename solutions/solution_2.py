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

SOLUTION TO EXERCISE 2

"""

### Count the total number of lines in the file: raw_profiles.txt
i = 0
with open('profiles_raw.txt', 'r') as f:
    for i, line in enumerate(f):
        pass
nlines = i+1

### Clean non-alphabetic characters and convert to lowercase
### with a progress indicator.
### Write results to 'profiles_clean.txt'
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
            print 'Line %i/%i cleaned ...' % (j+1, nlines)
print 'Done.'

