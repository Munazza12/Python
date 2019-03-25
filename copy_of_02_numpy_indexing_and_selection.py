# -*- coding: utf-8 -*-
"""Copy of 02-Numpy Indexing and Selection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hfDFPRMlLVfeuQWAKfZqwhHPrxUAez3w

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

## Using NumPy

To import NumPy in Colaboratory simply type the following:
"""

import numpy as np

"""# NumPy Indexing and Selection

In this section we will discuss how to select elements or groups of elements from an array.
"""

import numpy as np

arr = np.arange(0,11)

arr

"""## Bracket Indexing and Selection
The simplest way to pick one or some elements of an array looks very similar to python lists:
"""

arr[8]      #Get a value at an index

arr[1:5]      #Get values in a range

arr[0:5]      #Get values in a range

"""**Exercise 2.1:**

Create an array **arr** from 10 to 25 using **arange** function. Print the numbers from index 8 to 12.
"""

### START CODE HERE ###
arr=np.arange(10,25)
arr[8:12]
  
### END CODE HERE ###

"""**Expected Output:**

array([18, 19, 20, 21])

## Broadcasting

Numpy arrays differ from a normal Python list because of their ability to broadcast:
"""

arr[0:5]=100      #Setting a value with index range (Broadcasting)

arr

# Reset array 
arr = np.arange(0,11)

arr

slice_of_arr = arr[0:6]

slice_of_arr

slice_of_arr[:]=99

slice_of_arr

"""**Note:** The changes also occur in the original array."""

arr

"""Data is not copied, it's a view of the original array. This avoids memory problems.

To get a copy of the array we can simply use the **copy** function.
"""

arr_copy = arr.copy()

arr_copy

"""**Exercise 2.2:**

Create an array **arr** from 5 to 15. Create a copy **arr2** of the same array and replace first 5 values with 100.
"""

### START CODE HERE ###
arr=np.arange(5,15)
arr2=arr.copy()
slice_of_arr = arr[0:6]
slice_of_arr[:]=100
slice_of_arr
arr  
### END CODE HERE ###

"""**Expected output:**

array([100, 100, 100, 100,   9,  10,  11,  12,  13,  14])

## Indexing a 2D array (matrices)

The general format is **arr_2d[row][col]** or **arr_2d[row,col]**.
"""

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

arr_2d

arr_2d[1]      #Indexing row

# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
arr_2d[1][0]

# Getting individual element value
arr_2d[1,0]

# 2D array slicing

#Shape (2,2) from top right corner
arr_2d[:2,1:]

#Shape bottom row
arr_2d[2]

#Shape bottom row
arr_2d[2,:]

"""**Exercise 2.3:**

Using the given array **arr_2d** print (2, 2) matrix of the bottom right elements.
"""

### START CODE HERE ###
arr_2d      #don't forget to run the previous cells first
arr_2d[:2,1:]
  
### END CODE HERE ###

"""**Expected Output:**

array([[25, 30],

       [40, 45]])

### Fancy Indexing

Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:
"""

#Set up matrix
arr2d = np.zeros((10,10))

#Length of array
arr_length = arr2d.shape[1]

#Set up array

for i in range(arr_length):
    arr2d[i] = i
    
arr2d

"""Fancy indexing allows the following"""

arr2d[[2,4,6,8]]

#Allows in any order
arr2d[[6,4,2,7]]

"""## Selection

Let's briefly go over how to use brackets for selection based off of comparison operators.
"""

arr = np.arange(1,11)
arr

arr > 4

bool_arr = arr>4

bool_arr

arr[bool_arr]

arr[arr>2]

x = 2
arr[arr>x]

"""**Exercise 2.4:**

Create and array **odd** of odd numbers between 20 to 30 and print the array containing numbers greater than 25.
"""

### START CODE HERE ###
arr = np.arange(21,30,2)
arr[arr>25]

### END CODE HERE ###

"""**Expected Output: **

array([27, 29])

# Great Job!
"""