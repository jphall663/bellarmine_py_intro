
# coding: utf-8

# # Python Tricks
# ***

# # License
# 
# Copyright (c) 2017 by Patrick Hall, jpatrickhall@gmail.com
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#    
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# ***

# ## Explicit integer division

# In[1]:

type(4/2) # float


# In[2]:

type(4//2) # int, double slash performs integer division


# ## Helpful numeric formats

# In[3]:

# printf-like syntax
# """ allows printed statements in multiple lines

print("""
Compact decimal notation: %g 
Compact scientific notation: %e
Percent sign: %.2f%%
""" % (1234.5678, 1234.5678, 1234.5678))


# In[4]:

# format string syntax

print("""
Compact decimal notation: {dec_:g}
Compact scientific notation: {exp_:e}
Percent sign: {per_:.2f}%
""".format(dec_=1234.5678, exp_=1234.5678, per_=1234.5678))


# ## Symbolic math with `sympy`

# In[5]:

from sympy import (
    symbols,    # define symbols
    diff,       # derivatives
    integrate,  # integrals
    lambdify,   # symbolic expression -> python function
    latex,      # create latex expressions
    sin         # symbolic sine function
)

x = symbols('x')
y = sin(x)


# In[6]:

dydx = diff(y, x)
dydx


# In[7]:

integrate(dydx)


# In[8]:

f = lambdify(x, y)


# In[9]:

from math import pi
f(pi/2)


# In[10]:

y.series(x, 0, 6)


# In[11]:

print(latex(y.series(x, 0, 6)))


# In[12]:

from IPython.display import display, Math
display(Math(latex(y.series(x, 0, 6))))


# ## Viewing doc strings with `__doc__`
# * Also using zip() for multiple list processing 

# In[13]:

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3, 4, 5]

def f(list1, list2):
    
    """ Uses zip to process 2 lists in parallel.
    
    Args:
        list1: first list.
        list2: second list.
    
    """
    
    for i, j in zip(list1, list2):
        print(i, j)
    


# In[14]:

print(f.__doc__)


# In[15]:

f(list1, list2)


# ## Profiling code snippet performance with `timeit `
# * Notice performance increase when list is pre-initialized

# In[16]:

import timeit
n = 10000000
list3 = [0]*n
list4 = []
print(timeit.timeit('for i in range(0, n): list3[i] = i', number=1, setup='from __main__ import n, list3'))
print(timeit.timeit('for i in range(0, n): list4.append(i)', number=1, setup='from __main__ import n, list4'))


# ## Profiling memory usage with `memory_profiler`

# In[17]:

# '!' executes OS commands 
# installs memory profiler package 
# stores a short script to a file, biglist.py
# executes biglist.py with the memory_profiler module ... slow!
get_ipython().system(' pip install memory_profiler ')
get_ipython().system(' printf "@profile\\ndef biglist():\\n list_ = []\\n for i in range(0, 1000000):\\n  list_.append(i)\\n return list_\\nbiglist()" > biglist.py')
get_ipython().system(" python -m memory_profiler 'biglist.py'")


# ## Passing a variable number of function arguments with **kwargs

# In[18]:

# use the **kwargs variable to pass in any number of 
# keyword arguments to a function
def f(**kwargs):
    
    # kwargs is a dict
    if kwargs is not None:
        for key, val in sorted(kwargs.items()):
            print('%s = %s' %(key, val))
            
    print('----------')
        
f(a='hello')
f(a='hello', b='world')
f(a='goodbye', b='cruel', c='world')


# ## Function passing

# In[19]:

# import numeric sine function
from math import sin
print(sin(0))

# simple function for numerical derivative of f at x
def num_dfdx(f, x, h):
    
    return (f(x + h) - f(x))/float(h)

print(num_dfdx(sin, 0, 0.01))
print(num_dfdx(sin, 0, 1e-6))


# ## In-line `if`/`then` statements

# In[20]:

# value1 if condition else value2
def magnitude(x):
    
    # value1 if condition else value2
    return 'small' if 1 >= x >= -1 else 'big'

print(magnitude(0.5))
print(magnitude(-10))


# ## Anonymous `lambda` functions
# * Define simple functions in one line of code

# In[21]:

num_dfdx(lambda x: x**2, 1, 1e-6)


# In[22]:

magnitude = lambda x: 'small' if 1 >= x >= -1 else 'big'
print(magnitude(0.5))


# In[23]:

# map and lamba used often to apply a simple function
# to all elements in a list
list(map(lambda x: x**2, range(0,10)))


# ## Dynamic programming with `eval()` and `exec()`

# #### `eval()` is used to evaluate simple expressions and returns the object the expression generates

# In[24]:

operator = input('Please type an arithmatic operator: +, -, *, /. ') # read input from command line
print('1 ' + operator + ' 2')                                        # this is a string
print(eval('1 ' + operator + ' 2'))                                  # this evaluates the string as a code expression
print(type(eval('1 ' + operator + ' 2')))                            # this returns the type of the evaluated code expression


# #### `exec()` executes arbitrary strings as code blocks without returning anything

# In[25]:

operator = input('Please type an arithmatic operator: +, -, *, /. ') # read input from command line

# define a function - more complex than a simple expression - as string with substitution 
code = """                                                           
def combine():
    x = 1 %s 2
    return x
""" % (operator)
print(code)             # this is a string                                                                         
print(type(exec(code))) # this interprets the function and prints its type, i.e. None
print(combine())        # print output of interpreted function 

