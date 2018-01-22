'''
		   @file: 1-Eulers_method.py
		   @date: 28th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy

if __name__ == "__main__":
	# The variables

	# Initial conditions
	a, b, c	= 0.0, 2.0, 0.5	# The interval and initial value
	n 		= 5 			# The number of segments
	f 		= y - t**2 + 1	# The function f(t, y)

	# Calculating the exactly DOE 
	t		= sympy.symbols('t')
	y 		= sympy.symbols('y', cls = sympy.Function)
	f 		= y(t) - t**2 + 1
	difeq	= sympy.Eq(y(t).diff(t), f)
	ics 	= {y(0):0.5}
	y 		= sympy.dsolve(difeq, y(t), ics = ics)
	print y	

	# The begin to start the calculations
	f 		= sympy.lambdify((t, y), f, "numpy") 					# Transform the function to lambdify
	h 		= (b-a)/n
	t 		= a
	w 		= [c]

	for i in xrange(n):
		w.append(w[i] + f(t, w[i]))
		t 	= a + h*(i+1)

	# The final result
	print '   The "exactly" value: ' + str()
	print 'The approximated value: ' + str(w[n])

	y 		= sympy.symbols('y', cls = sympy.Function)

	#x, dx	= np.linspace(Dh[0][0], Dh[0][1], n+1, retstep = True)	# Here we divide the domin in n subparts
	#y, dy	= np.linspace(Dh[1][0], Dh[1][1], n+1, retstep = True)	# Here we divide the domin in n subparts