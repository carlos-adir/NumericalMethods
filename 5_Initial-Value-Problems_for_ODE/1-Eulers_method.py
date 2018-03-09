# -*- coding: utf-8 -*-
'''
		   @file: 1-Eulers_method.py
		   @date: 28th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	a, b, c, n, f = inputs.in1() # The principals inputs
								 # The function is defined like f(t, y, y', y'', ...)
	
	# The begin to start the calculations
	h 		= (b-a)/n 									# The step size
	t 		= a 										# The frist point that we start
	w 		= c											# The y values approx

	for i in range(n):
		w  += h*f(t, w)
		t   = a + h*(i+1)

		#print(str((t, w)))

	# The final result
	print("The approximated value: y(" + str(b) + ") = " + str(w))

	