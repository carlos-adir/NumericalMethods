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
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5		# The interval and initial value
	n 		= 5 			# The number of segments
	f 		= y - t**2 + 1	# The function f(t, y)
	
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
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

	print("The final value is: y(" + str(b) + ") = " + str(w))