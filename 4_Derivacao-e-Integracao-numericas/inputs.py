# -*- coding: utf-8 -*-
'''
		   @file: inputs.py
		   @date: 09th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This code is to be the inputs of the codes, only for don't repeat the same part of code
					in all the files

'''

import sympy as sp
import numpy as np

'''

These functions are to the methods:
* 1-Constant
* 3-Runge_Kutta

'''
def in1():
	
	# The variables
	t		= sp.symbols('t')
	
	# Initial conditions
	a, b	= 0, np.pi									# The interval and initial value
	n 		= 5 										# The number of segments
	f 		= sp.sin(t)									# The function f(t, y)
	
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
	t 		= np.linspace(a, b, n+1) 		# Create a array with n+1 elements. There are n+1 poins, n segment
	y		= f(t)
	return a, b, n, t, y

