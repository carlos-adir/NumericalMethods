'''
		   @file: 8-Hermite.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs

#from scipy.special import binom
#diff = sp.diff

if __name__ == "__main__":
	x, y, p, f = inputs.in1()




	# The variables
	t	= sp.symbols('t')

	a	= y

	n	= len(x)
	b	= np.zeros(n)
	c	= np.zeros(n)
	d	= np.zeros(n)
	h	= np.zeros(n-1)
	for i in range(n-1):
		h[i] = x[i+1]-x[i]

	k 		= np.zeros(n-1) 			# That means alpha
	for i in range(1,n-1):
		k[i] = 3*((a[i+1]-a[i])/h[i] - (a[i]-a[i-1])/h[i-1])

	# To solve the linear system
	l 		= np.zeros(n)
	u 		= np.zeros(n)
	z 		= np.zeros(n)
	l[0] 	= 1
	for i in range(1, n-1):
		l[i] = 2*(x[i+1]-x[i-1]) - h[i-1]*u[i-1]
		u[i] = h[i]/l[i]
		z[i] = (k[i] - h[i-1]*z[i-1])/l[i]
	l[n-1]	= 1

	for i in range(n-2, -1, -1):
		c[i] = z[i] - u[i]*c[i+1]
		b[i] = (a[i+1] - a[i])/h[i] - h[i]*(c[i+1]+2*c[i])/3
		d[i] = (c[i+1] - c[i])/(3*h[i])


	print("The functions constants value:")
	print(a)
	print(b)
	print(c)
	print(d)

	print("The correct values:")
	print(f(p))
	print("The values calculated by interpolation:")
	#print g(p)
