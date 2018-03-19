# -*- coding: utf-8 -*-
'''
		   @file: input.py
		   @date: 09th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This code is to be the inputs of the codes, only for don't repeat the same part of code
					in all the files

'''

import sympy as sp
import numpy as np

'''

These functions are to the methods:


'''
def in1():
	
	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	a, b    = 1, 2							# The interval, it's suppose that a < b
	f       = t**2 - 3						# The function
	tol     = 1e-5 							# The max error acceptable
	nmax    = 10 							# Max number iteractions  

	# The begin to start the calculations
	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify, now we can use like f(0)
	return a, b, f, tol, nmax

def in2():
	
	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	a, b    = 2, 4							# The interval, it's suppose that a < b
	f       = t**2-2*t-4	 				# The function
	tol     = 1e-5 							# The max error acceptable
	nmax    = 10 							# Max number iteractions  

	# The begin to start the calculations
	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify, now we can use like f(0)
	return a, b, f, tol, nmax

def in3():
	
	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	a, b    = 1, 2							# The interval, it's suppose that a < b
	f       = t**3+4*t**2-10 				# The function
	tol     = 1e-5							# The max error acceptable
	nmax    = 10							# Max number iteractions  

	# The begin to start the calculations
	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify, now we can use like f(0)
	return a, b, f, tol, nmax