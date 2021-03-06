# -*- coding: utf-8 -*-
"""Copy of 01-NumPy Arrays.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QdhliV0NkU0TrIPepfCXMXb0ekYXwv0s

#Introduction to NumPy 

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/1200px-NumPy_logo.svg.png)

NumPy (or Numpy) is a Linear Algebra Library for Python. NumPy is a Python package. It stands for 'Numerical Python'. It is a library consisting of multidimensional array objects and a collection of routines for processing of array.

Numpy is also incredibly fast, as it has bindings to C libraries.

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.


**In this notebook you will learn -**
* Numpy arrays
* Numpy Selecting and Indexing
* Numpy Operations

## Importing NumPy

To import NumPy in Colaboratory under the name **np** type the following:
"""

import numpy as np

"""Numpy has many built-in functions and capabilities. We won't cover them all but instead we will focus on some of the most important aspects of Numpy: vectors, arrays, matrices, and number generation. Let's start with arrays.

# Numpy Arrays

NumPy arrays are the main way we will use Numpy throughout the course. Numpy arrays essentially come in two flavors: vectors and matrices. Vectors are strictly 1-d arrays and matrices are 2-d.

**Note:** A matrix can still have only one row or one column.


## Creating NumPy Arrays

### From a Python List

We can create an array by directly converting a list or list of lists:
"""

my_list = [1,2,3]
my_list

np.array(my_list)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]      # list of lists
my_matrix

np.array(my_matrix)      # 3x3 matrix

"""**Exercise 1.1:**

Create a list named **odd_list** containing all odd numbers from 0 to 10 and print it.
"""

### START CODE HERE ### (2 lines of code)

odd_list=[1,3,5,7,9]
odd_list
### END CODE HERE ###

"""**Expected Output:**

[1, 3, 5, 7, 9]

**Exercise 1.2:**

Create a 2x2 matrix of all even numbers from 1 to 9.
"""

### START CODE HERE ###
 
m=([2,4],[6,8])                   #create list of 2 lists
m                                 #print the list
np.array(m)                       #convert the list into array
  
### END CODE HERE ###

"""**Expected Output:**

array[[2, 4],

     [6,8]]

#Built-in Methods

There are lots of built-in ways to generate Arrays.

### arange

Return evenly spaced values within a given interval.
"""

np.arange(0,10)     #creates an array from 0 to 9

"""**Note:** 
The first parameter is the starting value and second parameter (excluding) is the ending value.
"""

np.arange(0,11,2)

"""**Note:** 
The third parameter is the step value.

**Exercise 1.3:**

Create an array of odd numbers between 30 to 40 using **arange** function.
"""

### START CODE HERE ###
np.arange(31,40,2)

### END CODE HERE ###

"""**Expected Output:**

[31, 33, 35, 37, 39]

### zeros and ones

Generate arrays of zeros or ones
"""

np.zeros(3)      #creates an array of 3 zeros

np.zeros((5,5))      #creates a 5x5 matrix of zeros

np.ones(3)      #creates an array of 3 ones

np.ones((3,3))      #creates a 5x5 matrix of ones

"""### Linspace

 Returns number spaces evenly w.r.t interval. Similiar to arange but instead of step it uses sample number.

numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None,axis = 0)
 
 Parameters :

* start  : [optional] start of interval range. By default start = 0

* stop   : end of interval range, unless endpoint is set to False.In that case, the sequence consists of all but the last.

* num    : [int, optional] No. of samples to generate.Default is 50. Must be non-negative.

* endpoint   :  [bool, optional] If True, stop is the last sample. Otherwise, it is not included. Default is True.

* restep :  [bool, optional] If True, return (samples, step,)where step is the spacing between samples. By deflut restep = False.

* dtype  : [dtype, optional] The type of the output array. If dtype is not given, infer the data type from the other input arguments.

*axis  :  [int, optional] The axis in the result to store the samples. Relevant only if start or stop are array-like. By default (0), the samples will be along a new axis inserted at the beginning. Use -1 to get an axis at the end.
"""

np.linspace(0,10,5)                 #5 intervals generated between 0 and 10

np.linspace(0,10,50)                #50 intervals generated between 0 and 10

"""### eye

Creates an identity matrix
"""

np.eye(4)

"""###Random 

Numpy also has lots of ways to create random number arrays:

### rand
Create an array of the given shape and populate it with
random samples from a uniform distribution
over ``[0, 1]``.
"""

np.random.rand(2)

np.random.rand(5,5)

"""### randn

Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:
"""

np.random.randn(2)

np.random.randn(5,5)

"""### randint
Return random integers from `low` (inclusive) to `high` (exclusive).
"""

np.random.randint(1,100)

np.random.randint(1,100,10)      #print 10 values between 1 to 100

"""**Note:**
The third parameter indicates the number of values to be printed.

# Array Attributes and Methods

Let's discuss some useful attributes and methods or an array:
"""

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

arr

ranarr

"""### Reshape
Returns an array containing the same data with a new shape.
"""

arr.reshape(5,5)

"""### max, min, argmax, argmin

These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
"""

ranarr

ranarr.max()      #prints the maximum value in the array

ranarr.argmax()      #prints the index of the max value

ranarr.min()      #prints the minimum value in the array

ranarr.argmin()      #prints the index of the max value

"""### Shape

Shape is an attribute that arrays have (not a method). It gives you the shape if the array(M x N).
"""

# Vector
arr.shape

# Notice the two sets of brackets
arr.reshape(1,25)

arr.reshape(1,25).shape

arr.reshape(25,1)

arr.reshape(25,1).shape

"""### dtype

You can also grab the data type of the object in the array:
"""

arr.dtype

"""**Exercise 1.4:**

Create a random array of 15 numbers from 10 to 40. Reshape the same array to 3x5 matrix. Also print the min and max numbers from that array list.
"""

### START CODE HERE ###   
arr = np.random.randint(10,40,15)      #create random array
arr                                    #print the array
arr.reshape(3,5)                       #reshape the array

a = arr.min()                          #get the minimum value
a

b = arr.max()                         #get the maximum value
b
### END CODE HERE ###

"""# Great Job!"""