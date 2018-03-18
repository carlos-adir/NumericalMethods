'''
		   @file: 4-divided_differences.py
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
	n 		= len(x)
	F		= []
	for i in range(n):
		F.append([y[i]])
		for j in range(1, i+1):
			F[i].append((F[i][j-1] - F[i-1][j-1])/(x[i]-x[i-j]))

	a 		= []
	for i in range(n):
		a.append(F[i][i])

	print("The a values:")
	print(a)

	g 		= a[n-1] 
	for i in range(n-1, 0, -1):
		g  *= (t-x[i-1])
		g  += a[i-1]

	print("The function:")
	print(g)
	g = sp.expand(g)
	print("Expanded:")
	print(g)

	g = sp.lambdify(t, g, "numpy")

	print("The correct values:")
	print(f(p))
	print("The values calculated by interpolation:")
	print(g(p))