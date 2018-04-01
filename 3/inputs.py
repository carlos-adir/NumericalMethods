import numpy as np
import sympy as sp

def in1():
	# The variables
	t	= sp.symbols('t')
	f	= 1/t
	f	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	
	x	= np.array((2, 2.75, 4))
	y	= f(x)
	p	= np.array((3, 2.9))
	
	return x, y, p, f

def in3():
	# The variables
	t	= sp.symbols('t')
	f	= 1/t
	f_	= sp.diff(f, t)
	f	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	f_	= sp.lambdify(t, f_, "numpy") 			# Transform the function to lambdify

	x	= np.array((2, 3, 4, 5))
	y	= f(x)
	y_	= f_(x)
	p 	= np.array((3.3, 3.7))

	
	return x, y, y_, p, f, f_

def in5():
	t	= sp.symbols('t')
	f	= 1/t
	f	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	
	x	= np.array((2, 3, 4, 5, 6, 7))
	y	= f(x)
	p	= np.array((3.3, 3.7))
	
	return x, y, p, f
	