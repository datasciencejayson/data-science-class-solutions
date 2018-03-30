# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:41:01 2018

@author: Jayson Backes
"""

# python crash course excercise solutions.

#Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]

# numpy library

import numpy as np

# create an array of 10 zeros

np.zeros(10)

np.ones(10)

np.ones(10) * 5

np.arange(10,51)

np.arange(10,51,2)

#Create a 3x3 matrix with values ranging from 0 to 8

np.arange(0,9).reshape(3,3)

#Create a 3x3 identity matrix

np.eye(3)

#Use NumPy to generate a random number between 0 and 1

np.random.rand(1)
  
#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

np.random.randn(25)             

norm = np.random.randn(255) 

np.arange(1,101).reshape(10,10) / 100

mat = np.arange(1,26).reshape(5,5)
mat

mat[2:,1:]

mat[3,3]

mat[3:,0:]

mat.sum()

mat.std()

mat.var()

mat.mean()

mat.sum(axis=0)
