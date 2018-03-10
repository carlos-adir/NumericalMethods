# -*- coding: utf-8 -*-
'''
		   @file: 4-Runge_Kutta_Fehlberg.py
		   @date: 10th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	a, b, c, n, f = inputs.in1() # The principals inputs
								 # The function is defined like f(t, y, y', y'', ...)
	# The begin to start the calculations
	h 		= (b-a)/n 									# The step size
	t 		= [a] 										# The frist point that we start
	w 		= [c]										# The y values approx
	k 		= [0, 0, 0, 0]								# Initial condition of K, does not matter the initial value, only that there are 4 numbers on the list

	# The traditional Runge-Kutta 4th order:

	for i in range(3):
		k[0] = h*f(t[i], w[i])
		k[1] = h*f(t[i]+h/2, w[i]+k[0]/2)
		k[2] = h*f(t[i]+h/2, w[i]+k[1]/2)
		k[3] = h*f(t[i]+h, w[i]+k[2])

		w.append(w[i]+(k[0]+2*k[1]+2*k[2]+k[3])/6)
		t.append(a+h*(i+1))

	# Now we do the corrector

	for i in range(3, n):
		T = a+h*(i+1)
		W = w[3]+h*(55*f(t[3], w[3])-59*f(t[2], w[2])+37*f(t[1], w[1])-9*f(t[0], w[0]))/24
		W = w[3]+h*(9*f(T, W)+19*f(t[3], w[3])-5*f(t[2], w[2])+f(t[1], w[1]))/24
		# print(str((T, W)))
		for j in range(3):
			t[j] = t[j+1]
			w[j] = w[j+1]
		t[3] = T
		w[3] = W

	print(t)
	print(w)
