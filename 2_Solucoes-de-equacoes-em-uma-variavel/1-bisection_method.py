'''
		   @file: 1-bisection_method.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
#import roots
import inputs

if __name__ == "__main__":

	a, b, f, tol, nmax = inputs.in1()

	# There at least one root in the interval [a, b]
	# And we show on the screen the root using the sympy algorithms
	# roots.root(a, b, f)

	# The calculations
	n 		= 0 							# Because we are in the frist interaction
	fa		= f(a)							# We calculate the first point, the left
	while n < nmax:							# To never be a infinite loop
		p 	= a + (b-a)/2					# We calculate the midle coordinate
		fp 	= f(p)
		if fp == 0 or (b-a)/2 < tol:		# Verifies if we found the root exaclty on p, or when the size of interval is too small
			break
		n  += 1
		if fa*fp > 0:
			a  = p
			fa = fp
		else:
			b  = p

	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str((b-a)/2) + " is:")
	print(p)