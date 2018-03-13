'''
		   @file: 6-False_position_method.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy
import roots
sqrt 	= sympy.sqrt

sympy.init_printing()


# The variables
x 		= sympy.symbols('x')

# Initial conditions
p0, p1	= 1.0, 2.0								# The initial aproximations
f       = x**3+4*x**2-10 						# The function that we want to calculate the roots
tol     = 1e-5 									# The max error acceptable
nmax    = 10 									# Max number iteractions

coefs 	= [1, 4, 0, -10] 						# To use in numpy to calculate the f roots

# There at least one root in the interval [a, b]
roots.root(p0, p1, f)

# The calculations
f 		= sympy.lambdify(x, f, "numpy") # Transform the function to lambdify
n 		= 1
q0 		= f(p0)
q1 		= f(p1)
while 1:
	p 	= p1 - q1*(p1-p0)/(q1-q0)
	n  += 1
	if abs(p - p1) < tol or n == nmax:
		break
	q 	= f(p)
	if q * q1 < 0:
		p0 = p1
		q0 = q1
	p1 = p
	q1 = q

if n == nmax:
	print "The process stoped by the number of iterations"
else:
	print "The process stoped by the tolerance"
print "The approximate value with n = " + str(n)
print "And error " + str(abs(p-p1)) + " is:"
print p
