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
* 1-Euler_method
* 3-Runge_Kutta

'''
def in1():
	
	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	a, b    = 1.0, 2.0						# The interval, it's suppose that a < b
	f       = t**3+4*t**2-10 				# The function
	tol     = 1e-5 							# The max error acceptable
	nmax    = 10 							# Max number iteractions  

	#coefs 	= [1, 4, 0, -10] 				# To use in numpy, because the function is
											# 1*t**3+4*t**2+0*t**1+(-10)*t**0
											# It is possible to improve it to find the coefficients by itself
	
	# The begin to start the calculations
	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify, now we can use like f(0)
	return a, b, f, tol, nmax, 

def in2():
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 5 										# The number of segments
	f 		= y - t + 1									# The function f(t, y)
	
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
	return a, b, c, n, f
