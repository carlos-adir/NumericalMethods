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
	y 		= sp.symbols('y')
 
	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 5 										# The number of segments
	f 		= y - t**2 + 1								# The function f(t, y)
	
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
	return a, b, c, n, f

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

'''

These functions are to:
* 4-Runge_Kutta_Fehlberg 

'''

def in3():
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	hmax	= 0.2 										# The max step size that we want
	hmin 	= 0.002										# The minimal value of step size
	f 		= y - t**2 + 1								# The function f(t, y)
	TOL		= 1e-4
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
	return a, b, c, hmax, hmin, f, TOL	