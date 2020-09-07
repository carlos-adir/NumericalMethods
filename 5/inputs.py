# -*- coding: utf-8 -*-
'''
		   @file: input.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import sympy as sp
import numpy as np
from types_lib import Function

limites = [	[1, 9],\
			[1, 9],\
			[1, 9]]


def get(algorithm, number):
	limite = limites[algorithm-1]
	if number < limite[0]:
		number = limite[0]
	if number > limite[1]:
		number = limite[1]

	if algorithm == 1:
		return lambda : in1(number)
	elif algorithm == 2:
		return lambda : in2(number)
	elif algorithm == 3:
		return lambda : in3(number)
	elif algorithm == 4:
		return lambda : in4(number)
	elif algorithm == 5:
		return lambda : in5(number)
	elif algorithm == 6:
		return lambda : in6(number)
	elif algorithm == 7:
		return lambda : in7(number)
	elif algorithm == 8:
		return lambda : in8(number)
	elif algorithm == 9:
		return lambda : in9(number)
	elif algorithm == 10:
		return lambda : in10(number)

def all(number):
	t		= sp.symbols('t')
	y 		= sp.symbols('y', cls = sp.Function)(t)
	if number < 5:
		if number == 1:
			a, b, c	= 0, 2, 0.5									# The interval and initial value
			n 		= 10 										# The number of segments
			f 		= y - t**2 + 1								# The function f(t, y)
		elif number == 2:
			a, b, c = 0, 1, -2
			n 		= 5
			f 		= y * sp.tan(t) + t - 3
		elif number == 3:
			a, b, c	= 0, 2, 0.5									# The interval and initial value
			n 		= 5 										# The number of segments
			f 		= y - t										# The function f(t, y)
		elif number == 4:
			a, b, c = 1, 2, np.cos(2)*np.sin(10)
			n 		= 10
			f 		= 10*y*(sp.cos(10*t)/sp.sin(10*t)) - 2*y**2*sp.sin(2*t)/(sp.sin(10*t)*((sp.cos(2*t))**2))
	else:
		if number == 5:
			a, b, c = 0, 1, 0
			n 		= 20
			f 		= t*sp.exp(3*t) - 2*y
		elif number == 6:
			a, b, c = 2, 3, 1
			n 		= 20
			f 		= 1 + (1-y)**2
		elif number == 7:
			a, b, c = 1, 2, 2
			n 		= 40
			f 		= 1+y/t
		elif number == 8:
			a, b, c = 1, 2, 2
			n 		= 40
			f 		= (1+t)/(1+y)
		elif number == 9:										# A função do Peniel
			a, b, c	= -5, 5, 0									# The interval and initial value
			n 		= 20										# The number of segments
			f 		= sp.exp(- t**2 + 1)						# The function f(t, y)
			#y 		= (sp.E*sp.sqrt(sp.pi)/2*(sp.erf(t)-sp.erf(-5))	# É alguma coisa com o erf, a funcao exata
	f = Function((t, y), f)
	return a, b, c, n, f

def exact(number):
	t		= sp.symbols('t')
	if number == 1:
		y	= -0.5 * sp.exp(t)+t**2+2*t+1
	elif number == 2:
		y	= -3/(sp.cos(t))+t*sp.tan(t)- 3 *sp.tan(t) + 1
	elif number == 3:
		y	= -0.5*sp.exp(t)+t+1
	elif number == 4:
		y	= sp.cos(2*t)*sp.sin(10*t)
	y 		= Function(t, y)
	return y


def in1(number):
	a, b, c, n, f = all(number)
	if number < 5:
		y	= exact(number)
	else:
		y	= None
	return a, b, c, n, f, y

def in2(number):

	# Mudando o valor de ordem se obtém diferentes ordens para o método de Taylor

	# The variables
	a, b, c, n, f = all(number)
	

	if number < 5:
		y	= exact(number)
	else:
		y	= None	
	return a, b, c, n, f, y


def in3(number):
	return in1(number)
	
def in4(number):
	return in1(number)
'''
def in3(number):
	#This function is the Second Taylor
	
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 10										# The number of segments
	f 		= y - t**2 + 1								# The function f(t, y)
	dfdy	= sp.Add(1)
	dfdt	= sp.Add(-2*t)
	
	h = (b-a)/n
	# The begin to start the calculations
	f_		= dfdy*f + dfdt								# The frist derivative
	T2 		= f+(h/2)*f_
	T2 		= sp.lambdify((t, y), T2, "numpy") 			# Transform the function to lambdify
	
	return a, b, c, n, T2
'''

def in4(number):
	'''
	#This function is the Thirth Taylor
	'''

	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	n 		= 10										# The number of segments
	f 		= y - t**2 + 1								# The function f(t, y)
	dfdy	= sp.Add(1)
	d2fdy2	= sp.Add(0)
	dfdt	= sp.Add(-2*t)
	d2fdt2	= sp.Add(-2)

	h = (b-a)/n
	# The begin to start the calculations
	f_		= dfdy*f + dfdt								# The frist derivative
	f__		= d2fdy2*f + dfdy*f_ + d2fdt2				# The second derivative
	T3 		= f+(h/2)*f_+(h**2/6)*f__
	T3 		= sp.lambdify((t, y), T3, "numpy") 			# Transform the function to lambdify
	
	return a, b, c, n, T3


'''

These functions are to:
* 4-Runge_Kutta_Fehlberg 

'''

def in5(number):
	# The variables
	t		= sp.symbols('t')
	y 		= sp.symbols('y')

	# Initial conditions
	a, b, c	= 0, 2, 0.5									# The interval and initial value
	hmax	= 0.2 										# The max step size that we want
	hmin 	= 0.002										# The minimal value of step size
	f 		= y - t**2 + 1								# The function f(t, y)
	TOL		= 1e-4
	# The begin to start the calculations
	f 		= sp.lambdify((t, y), f, "numpy") 			# Transform the function to lambdify
	return a, b, c, hmax, hmin, f, TOL	
