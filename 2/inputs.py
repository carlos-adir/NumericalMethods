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

def in4():

	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	p0 		= 1.5 							# The initial aproximation
	f       = t**3+4*t**2-10 				# The function that we want to calculate the roots
	tol     = 1e-5 							# The max error acceptable
	nmax    = 10 							# Max number iteractions
	
	# The fixed point functions, using f(x) = 0 we can get the functions:
	#g 		= t - t**3 - 4*t**2 + 10				# It doesn't converg
	#g 		= sqrt(4*t - 10/t)						# It doesn't converg
	g 		= sp.sqrt(10-t**3)/2				# The fixed point function, using f(x) = 0 we can get x = sqrt(10-x**3)/2
	#g 		= sqrt(10/(4+t))						# It converges quite well
	#g 		= t - (t**3+4*t**2-10)/(3*t**2 + 8*t)	# It converges very well, we will see this funcion in the Newton's method

	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify
	g 		= sp.lambdify(t, g, "numpy") # Transform the function to lambdify

	return p0, g, tol, nmax

def in5():

	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	p0 		= 1.5 							# The initial aproximation
	f       = t**3+4*t**2-10 				# The function that we want to calculate the roots
	tol     = 1e-5 							# The max error acceptable
	nmax    = 10 							# Max number iteractions
	
	# The fixed point functions, using f(x) = 0 we can get the functions:
	#g 		= t - t**3 - 4*t**2 + 10				# It doesn't converg
	#g 		= sp.sqrt(4*t - 10/t)						# It doesn't converg
	g 		= sp.sqrt(10-t**3)/2					# It converges 
	#g 		= sp.sqrt(10/(4+t))						# It converges quite well
	#g 		= t - (t**3+4*t**2-10)/(3*t**2 + 8*t)	# It converges very well, we will see this funcion in the Newton's method

	g_ 		= sp.diff(g, t)							# The function g' derivative of g

	f 		= sp.lambdify(t, f, "numpy") # Transform the function to lambdify
	g 		= sp.lambdify(t, g, "numpy") # Transform the function to lambdify
	g_ 		= sp.lambdify(t, g_, "numpy") # Transform the function to lambdify

	return p0, g, g_, tol, nmax
