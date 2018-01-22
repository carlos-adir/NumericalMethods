import numpy as np
import sympy


def root(a, b, f):
	# sympy.re(complex) to get the real number
	# sympy.im(complex) to get the imag number
	# There is a root in the interval [a, b]
	x 			= sympy.symbols('x')
	x1 			= a if a < b else b
	x2 			= b if a < b else a
	a, b 		= x1, x2
	sympyroots 	= sympy.solve(f, x)
	back 		= []
	for sympyroot in sympyroots:
		if a <= sympy.re(sympyroot) <= b and sympy.im(sympyroot) == 0:
			back.append(sympyroot)

	print "Using the sympy, the f roots in [" + str(a) + ", " + str(b) + "] are:"
	print back
	print "The approximate value using sympy is:"
	for i in xrange(len(back)):
		back[i] = back[i].evalf()
	print back
	print '\n'