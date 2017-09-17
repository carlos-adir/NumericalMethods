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
x 		= sympy.symbols('x')

# Initial conditions
a, b    = 1.0, 2.0						# The interval
f       = x**3+4*x**2-10 				# The function
tol     = 1e-5 							# The max error acceptable
nmax    = 10 							# Max number iteractions  

coefs 	= [1, 4, 0, -10] 				# To use in numpy

# There at least one root in the interval [a, b]
roots.root(a, b, f)

# The calculations
f 		= sympy.lambdify(x, f, "numpy") # Transform the function to lambdify
n 		= 0
fa		= f(a)
while n < nmax:
	p 	= a + (b-a)/2
	fp 	= f(p)
	if fp == 0 or (b-a)/2 < tol:
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