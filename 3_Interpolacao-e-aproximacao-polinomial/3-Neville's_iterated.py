'''
		   @file: 3-Neville's_iterated.py
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
	Q		= []
	for i in range(n):
		Q.append([y[i]])
		for j in range(1, i+1):
			Q[i].append(sp.simplify(((t-x[i-j])*Q[i][j-1] - (t-x[i])*Q[i-1][j-1])/(x[i]-x[i-j])))

	q 		= []
	for i in range(n):
		q.append(sp.simplify(Q[i][i]))
		q[i] = sp.lambdify(t, q[i], "numpy")

	print("The Q functions:")
	for i in Q:
		print(i)


	print("The correct values:")
	print(f(p))
	print("The values calculated by interpolation:")
	for i in range(n):
		print("q[" + str(i) + "] = " + str(q[i](p)))