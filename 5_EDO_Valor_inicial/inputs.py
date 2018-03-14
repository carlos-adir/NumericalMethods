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

These functions are to the methods:
* 2-Taylor

'''

def in3():
	'''
	This function is the Second Taylor
	'''

	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 10										# The number of segments
	f 		= y - t**2 + 1								# The function f(t, y)
	dfdy	= sp.Add(1)
	dfdt	= sp.Add(-2*t)
	
	h = (b-a)/n
	# The begin to start the calculations
	f_		= dfdy*f + dfdt								# The frist derivative
	T2 		= f+(h/2)*f_
	T2 		= sp.lambdify((t, y), T2, "numpy") 			# Transform the function to lambdify
	
	return a, b, c, n, T2


def in4():
	'''
	This function is the Thirth Taylor
	'''

	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 10										# The number of segments
	f 		= y - t**2 + 1								# The function f(t, y)
	dfdy	= sp.Add(1)
	d2fdy2	= sp.Add(0)
	dfdt	= sp.Add(-2*t)
	d2fdt2	= sp.Add(-2)

	h = (b-a)/n
	# The begin to start the calculations
	f_		= dfdy*f + dfdt								# The frist derivative
	f__		= d2fdy2*f + dfdy*f_ + d2fdt2				# The second derivative
	T3 		= f+(h/2)*f_+(h**2/6)*f__
	T3 		= sp.lambdify((t, y), T3, "numpy") 			# Transform the function to lambdify
	
	return a, b, c, n, T3


'''

These functions are to:
* 4-Runge_Kutta_Fehlberg 

'''

def in5():
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