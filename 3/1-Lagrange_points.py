'''
		   @file: 1-Lagrange_points.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	x, y, p, f = inputs.in1()

	# The variables
	t 		= sp.symbols('t')

	# The calculations
	n = len(x)
	L = []
	for i in range(n):
		Li = 1
		for j in range(n):
			if i != j:
				Li *= (t-x[j])/(x[i]-x[j])
		L.append(Li)

	g = 0
	for i in range(n):
		g += L[i] * y[i]
	g = sp.simplify(g)

	print("The L functions:")
	for Li in L:
		print(Li)
	print("The final function:")
	print(f)
	print('\n')

	g 		= sp.lambdify(t, g, "numpy") # Transform the function to lambdify

	print("The correct values:")
	print(f(p))
	print("The values calculated by interpolation:")
	print(g(p))