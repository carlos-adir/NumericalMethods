# -*- coding: utf-8 -*-
'''
		   @file: 3-Runge_Kutta.py
		   @date: 9th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import numpy as np
import sympy as sp

if __name__ == "__main__":
	a, b, c, n, f = inputs.in1() # The principals inputs
								 # The function is defined like f(t, y, y', y'', ...)
	
	# The begin to start the calculations
	h 		= (b-a)/n 									# The step size
	t 		= a 										# The frist point that we start
	w 		= c											# The y values approx
	k 		= [0, 0, 0, 0]								# Initial condition of K, does not matter the initial value, only that there are 4 numbers on the list
	
	for i in range(n):
		k[0] = h*f(t, w)
		k[1] = h*f(t+h/2, w+k[0]/2)
		k[2] = h*f(t+h/2, w+k[1]/2)
		k[3] = h*f(t+h, w+k[2])

		w 	+= (k[0]+2*k[1]+2*k[2]+k[3])/6
		t    = a + h*(i+1)

		#print(str((t, w)))	

	# The final result
	print("The approximated value: y(" + str(b) + ") = " + str(w))