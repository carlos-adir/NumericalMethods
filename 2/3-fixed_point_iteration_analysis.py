'''
		   @file: 3-fixed_point_analysis.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs
import results


if __name__ == "__main__":

	p0, g, g_, tol, nmax = inputs.in5()


	# The calculations
	p_ 		= g_(p0)
	n 		= 0
	print("n = " + str(n) + " and p = " + str(p0) + " then |g'(p)| = " + str(abs(p_)))
	while 1:
		p 	= g(p0)
		p_ 	= g_(p)
		n  += 1
		print("n = " + str(n) + " and p = " + str(p) + " then |g'(p)| = " + str(abs(p_)))
		if abs(p - p0) < tol or n == nmax or (not abs(p_) < 1):
			break
		p0	= p


	if not abs(p_) < 1:
		print("The process stoped with no sucess because |g'(p)| >= 1")
	else:
		results.show(n, nmax, p-p0, p)