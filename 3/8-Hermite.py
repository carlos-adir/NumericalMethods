'''
		   @file: 8-Hermite.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

#import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	x, y, y_, p, f, f_ = inputs.in3()

	# The variables
	t	= sp.symbols('t')

	# The calculations
	n	= len(x)
	Q	= []
	z	= []
	for i in range(n):
		z.append(x[i])
		z.append(x[i])
		Q.append([y[i]])
		Q.append([y[i]])
		Q[2*i+1].append(y_[i])
		if i != 0:
			Q[2*i].append((Q[2*i][0] - Q[2*i-1][0])/(z[2*i]-z[2*i-1]))

	for i in range(2, 2*n):
		for j in range(2, i+1):
				Q[i].append((Q[i][j-1] - Q[i-1][j-1])/(z[i] - z[i-j]))

	a	= []
	for i in range(2*n):
		a.append(Q[i][i])

	print("The a values:")
	print(a)

	g	= a[2*n-1]*(t-x[n-1])
	for i in range(n-1, 0, -1):
		g  += a[2*i]
		g  *= t-x[i-1]
		g  += a[2*i-1]
		g  *= t-x[i-1]
	g   += a[0]



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
