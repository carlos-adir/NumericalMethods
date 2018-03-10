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
	a, b, c, hmax, hmin, f, TOL = inputs.in3() # The principals inputs
									 # The function is defined like f(t, y, y', y'', ...)
	
	# The begin to start the calculations
	h 		= hmax 										# The step size
	t 		= a 										# The frist point that we start
	w 		= c											# The y values approx
	k 		= [0, 0, 0, 0, 0, 0]							# Initial condition of K, does not matter the initial value, only that there are 4 numbers on the list
	
	Kconst 	= [	[1/4,		1/4],
				[3/8,		3/32, 			9/32],
				[12/13,		1932/2197, 		-7200/2197, 7296/2197],
				[1,			439/216,		-8,			3680/513,		-845/4104],
				[1/2, 		-8/27,			2,			-3544/2565,		1859/4104,		-11/40]]

	Rconst	= [1/360, 0, -128/4275, -2197/75240, 1/50, 2/55]

	Wconst  = [25/216, 0, 1408/2565, 2197/4104, -1/5, 0]

	flag = True
	while flag:
		k[0] = h*f(t, 				w)
		k[1] = h*f(t+Kconst[0][0]*h, w+Kconst[0][1]*k[0])
		k[2] = h*f(t+Kconst[1][0]*h, w+Kconst[1][1]*k[0]+Kconst[1][2]*k[1])
		k[3] = h*f(t+Kconst[2][0]*h, w+Kconst[2][1]*k[0]+Kconst[2][2]*k[1]+Kconst[2][3]*k[2])
		k[4] = h*f(t+Kconst[3][0]*h,	w+Kconst[3][1]*k[0]+Kconst[3][2]*k[1]+Kconst[3][3]*k[2]+Kconst[3][4]*k[3])
		k[5] = h*f(t+Kconst[4][0]*h,	w+Kconst[4][1]*k[0]+Kconst[4][2]*k[1]+Kconst[4][3]*k[2]+Kconst[4][4]*k[3]+Kconst[4][5]*k[4])
		# It is possible improve it using matrice multiplication
		R 	 = abs(Rconst[0]*k[0]+Rconst[1]*k[1]+Rconst[2]*k[2]+Rconst[3]*k[3]+Rconst[4]*k[4]+Rconst[5]*k[5])/h
		if R <= TOL:
			t    += h
			w 	 += Wconst[0]*k[0]+Wconst[1]*k[1]+Wconst[2]*k[2]+Wconst[3]*k[3]+Wconst[4]*k[4]+Wconst[5]*k[5] 
			#print(str((t, w)))	
		delta = 0.84*(TOL/R)**(1/4)
		if delta <= 0.1:
			h = 0.1*h
		elif delta >= 4:
			h = 4*h
		else:
			h = delta*h
		if h > hmax:
			h = hmax
		if t >= b:
			flag = False
		elif t + h > b:
			h = b - t
		elif h < hmin:
			flag = False
			print("Minimal h exceeded")

	# The final result
	print("The approximated value: y(" + str(b) + ") = " + str(w))