'''
		   @file: 1-bisection_method.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy
import roots

sympy.init_printing()




# The variables
t 		= sympy.symbols('t')

# Initial conditions
a, b    = 1.0, 2.0						# The interval, it's suppose that a < b
f       = x**3+4*x**2-10 				# The function
tol     = 1e-5 							# The max error acceptable
nmax    = 10 							# Max number iteractions  

coefs 	= [1, 4, 0, -10] 				# To use in numpy, because the function is
										# 1*x**3+4*x**2+0*x**1+(-10)*x**0
										# It is possible to improve it to find the coefficients by itself 

# There at least one root in the interval [a, b]
# And we show on the screen the root using the sympy algorithms
roots.root(a, b, f)

# The calculations
f 		= sympy.lambdify(t, f, "numpy") # Transform the function to lambdify, now we can use like f(0)
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
	print 'The process stoped by the number of iterations'
else:
	print 'The process stoped by the tolerance'

print "The approximate value with n = " + str(n)
print "And error " + str((b-a)/2) + " is:"
print p