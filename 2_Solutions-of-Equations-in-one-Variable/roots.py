#import numpy as np
import sympy as sp


def root(a, b, f):
	# sympy.re(complex) to get the real number
	# sympy.im(complex) to get the imag number
	# There is a root in the interval [a, b]
	x 			= sympy.symbols('x')
	x1 			= a if a < b else b
	x2 			= b if a < b else a
	a, b 		= x1, x2
	sympy_roots	= sympy.solve(f, x)
	back 		= []
	for sympy_root in sympy_roots:
		if a <= sympy.re(sympy_root) <= b and sympy.im(sympy_root) == 0:
			back.append(sympy_root)

	print "Using the sympy, the f roots in [" + str(a) + ", " + str(b) + "] are:"
	print back
	print "The approximate value using sympy is:"
	for i in xrange(len(back)):
		back[i] = back[i].evalf() # This function is from numpy, it calculates using numpy library 
	print back
	print '\n'