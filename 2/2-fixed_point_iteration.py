'''
		   @file: 2-fixed_point_iteration.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs
import results

if __name__ == "__main__":

	p0, g, tol, nmax = inputs.in4()




	# The calculations
	n 		= 0
	while 1:
		p 	= g(p0)
		n  += 1
		if abs(p - p0) < tol or n == nmax:
			break
		p0	= p





	results.show(n, nmax, p-p0, p)