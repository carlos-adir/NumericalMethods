# -*- coding: utf-8 -*-
'''
		   @file: 1-Eulers_method.py
		   @date: 28th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp

if __name__ == "__main__":
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0		# The interval and initial value
	n 		= 5 			# The number of segments
	f 		= y - t**2 + 1	# The function f(t, y)
	
	# The begin to start the calculations
	f 		= sp.lambdify((y, t), f, "numpy") 			# Transform the function to lambdify
	h 		= (b-a)/n 									# The step size
	t 		= a 										# The frist point that we start
	w 		= [c]										# The y values approx

	for i in range(n):
		w.append(w[i] + f(w[i], t))
		t 	= a + h*(i+1)

	# The final result
	print("The approximated value: y(" + str(b) + ") = " + str(w[n]))

	