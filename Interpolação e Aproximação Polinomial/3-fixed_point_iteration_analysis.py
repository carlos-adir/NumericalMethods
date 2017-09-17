'''
		   @file: 3-fixed_point_analysis.py
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
p0 		= 1.5 									# The initial aproximation
f       = x**3+4*x**2-10 						# The function that we want to calculate the roots
tol     = 1e-5 									# The max error acceptable
nmax    = 10 									# Max number iteractions
# The fixed point functions, using f(x) = 0 we can get the functions:
#g 		= x - x**3 - 4*x**2 + 10				# It doesn't converg
#g 		= sqrt(4*x - 10/x)						# It doesn't converg
g 		= sqrt(10-x**3)/2						# It converges
#g 		= sqrt(10/(4+x))						# It converges quite well
#g 		= x - (x**3+4*x**2-10)/(3*x**2 + 8*x)	# It converges very well, we will see this funcion in the Newton's method

dg 		= sympy.diff(g, x)						# The function g' derivative of g

coefs 	= [1, 4, 0, -10] 						# To use in numpy to calculate the f roots

# There at least one root in the interval [a, b]
a, b 	= 1, 2									# We don't need it to use the Fixed point iteration
roots.root(a, b, f)


# The calculations
g 		= sympy.lambdify(x, g, "numpy") # Transform the function to lambdify
dg 		= sympy.lambdify(x, dg, "numpy")
dp 		= dg(p0)
n 		= 0
print "n = " + str(n) + " and p = " + str(p0) + " then |g'(p)| = " + str(abs(dp))
while 1:
	p 	= g(p0)
	dp 	= dg(p)
	n  += 1
	print "n = " + str(n) + " and p = " + str(p) + " then |g'(p)| = " + str(abs(dp))
	if abs(p - p0) < tol or n == nmax or abs(dp) >= 1:
		break
	p0	= p


if abs(dp) >= 1:
	print "The process stoped with no sucess because |g'(p)| >= 1"
else:
	if n == nmax:
		print "The process stoped by the number of iterations"
	else:
		print "The process stoped by the tolerance"
	print "The approximate value with n = " + str(n)
	print "And error " + str(abs(p-p0)) + " is:"
	print p
