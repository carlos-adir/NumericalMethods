'''
		   @file: 1-linear.py
		   @date: 16th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This program calculates the curve length when the functions x(t), y(t), z(t)
				  are given in a closed interval [a, b]. The program calculates using the
				  linear approximation: we break the curve in n points and we add up every
				  distance between the connected points.

				  For instance, we can calculate the curve length of (sin(t), cos(t), 0) when
				  t is the between the values [0, pi].

'''


import numpy as np
import sympy


def length(x, y, z):
	summ	= 0 
	n 		= len(x) - 1
	for ti in xrange(n):
		dx = x[ti+1] - x[ti]
		dy = y[ti+1] - y[ti]
		dz = z[ti+1] - z[ti]
		summ += np.sqrt(dx**2 + dy**2 + dz**2)
	return summ;


# The variables
t 		= sympy.symbols('t')

# Initial conditions
#a, b, n = 0, 1, 3						# You use it if you want 
#x, y, z = 3+t-2*t**3, 4-t+t**2, 0		# This too
a, b, n = 0, np.pi, 100 
x, y, z = sympy.sin(t), sympy.cos(t), 0

# The begin to start the calculations
x 		= sympy.lambdify(t, x, "numpy") # Transform the function to lambdify
y 		= sympy.lambdify(t, y, "numpy")
z 		= sympy.lambdify(t, z, "numpy")
t 		= np.linspace(a, b, n+1) 		# Create a array with n+1 elements. There are n+1 poins, n segments
x, y, z	= x(t), y(t), z(t)				# The values of x and y to calculate

print length(x, y, z)