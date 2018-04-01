'''
		   @file: 4-Newton's_method.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy
import roots
sqrt 	= sympy.sqrt 
diff 	= sympy.diff

sympy.init_printing()


# The variables
x 		= sympy.symbols('x')

# Initial conditions
p0 		= 1.5 									# The initial aproximation
f       = x**3+4*x**2-10 						# The function that we want to calculate the roots
df 		= diff(f, x)							# The function f' derivative of f
tol     = 1e-5 									# The max error acceptable
nmax    = 10 									# Max number iteractions

coefs 	= [1, 4, 0, -10] 						# To use in numpy to calculate the f roots

# There at least one root in the interval [a, b]
a, b 	= 1, 2									# We don't need it to use the Newton's method
roots.root(a, b, f)


# The calculations
g 		= x - f/df
g 		= sympy.lambdify(x, g, "numpy") # Transform the function to lambdify
n 		= 0
while 1:
	p 	= g(p0)
	n  += 1
	if abs(p - p0) < tol or n == nmax:
		break
	p0	= p

if n == nmax:
	print "The process stoped by the number of iterations"
else:
	print "The process stoped by the tolerance"
print "The approximate value with n = " + str(n)
print "And error " + str(abs(p-p0)) + " is:"
print p
