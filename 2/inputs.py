# -*- coding: utf-8 -*-
'''
		   @file: input.py
		   @date: 09th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This code is to be the inputs of the codes, only for don't repeat the same part of code
					in all the files

'''

import sympy as sp
import numpy as np

class Funcao(object):
	"""docstring for funcao"""
	def __init__(self, evalu, latex):
		self.e = evalu
		self.l = latex
		

def toLaTeX(lat):
	cdot	= ' \\cdot '
	return str(lat).replace('**', '^').replace('*', cdot) + '$'

def in1(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 1.py
	'''
	# The variables
	t		= sp.symbols('t')
	limites = [1, 3]





	if number < limites[0]:
		number = limites[0]
	if number > limites[1]:
		number = limites[1]
	# Initial conditions
	if number == 1:
		a, b    = 1, 2							# The interval, it's suppose that a < b
		f       = t**2 - 3						# The function
		tol     = 1e-5 							# The max error acceptable
		nmax    = 10 							# Max number iteractions  
	elif number == 2:
		a, b    = 2, 4							# The interval, it's suppose that a < b
		f       = t**2-2*t-4	 				# The function
		tol     = 1e-5 							# The max error acceptable
		nmax    = 10 							# Max number iteractions
	elif number == 3:
		a, b    = 1, 2							# The interval, it's suppose that a < b
		f       = t**3+4*t**2-10 				# The function
		tol     = 1e-5							# The max error acceptable
		nmax    = 10							# Max number iteractions



	# The begin to start the calculations
	feval 	= sp.lambdify(t, f, "numpy")
	flatex	= "$f(t) = " + toLaTeX(f)
	f		= Funcao(feval, flatex)
	return a, b, f, tol, nmax

def in2(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 2.py
	'''
	# The variables
	t		= sp.symbols('t')
	limites = [1, 5]




	if number < limites[0]:
		number = limites[0]
	if number > limites[1]:
		number = limites[1]
	# Initial conditions
	if 1 <= number <= 5:
		p0 		= 1.5 							# The initial aproximation
		f       = t**3+4*t**2-10 				# The function that we want to calculate the roots
		tol     = 1e-5 							# The max error acceptable
		nmax    = 10 							# Max number iteractions
		if number == 1:
			g 		= t - t**3 - 4*t**2 + 10				# It doesn't converg
		elif number == 2:
			g 		= sp.sqrt(4*t - 10/t)						# It doesn't converg
		elif number == 3:
			g 		= sp.sqrt(10-t**3)/2					# The fixed point function, using f(x) = 0 we can get x = sqrt(10-x**3)/2
		elif number == 4:
			g 		= sp.sqrt(10/(4+t))						# It converges quite well
		elif number == 5:
			g 		= t - (t**3+4*t**2-10)/(3*t**2 + 8*t)	# It converges very well, we will see this funcion in the Newton's method


	g_ 		= sp.diff(g, t)						# The function g' derivative of g
	
	feval 	= sp.lambdify(t, f, "numpy")
	flatex	= "$f(t) = " + toLaTeX(f)
	f		= Funcao(feval, flatex)

	geval 	= sp.lambdify(t, g, "numpy")
	glatex	= "$g(t) = " + toLaTeX(g)
	g		= Funcao(geval, glatex)

	g_eval 	= sp.lambdify(t, g_, "numpy")
	g_latex	= "$g'(t) = " + toLaTeX(g_)
	g_		= Funcao(g_eval, g_latex)

	

	return p0, f, g, g_, tol, nmax

def in3(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 1.py
	'''
	# The variables
	t		= sp.symbols('t')
	limites = [1, 3]





	if number < limites[0]:
		number = limites[0]
	if number > limites[1]:
		number = limites[1]
	# Initial conditions
	if number == 1:
		p0		= 1.5							# The interval, it's suppose that a < b
		f       = t**2 - 3						# The function
		tol     = 1e-5 							# The max error acceptable
		nmax    = 10 							# Max number iteractions  
	elif number == 2:
		p0 		= 3								# The interval, it's suppose that a < b
		f       = t**2-2*t-4	 				# The function
		tol     = 1e-5 							# The max error acceptable
		nmax    = 10 							# Max number iteractions
	elif number == 3:
		p0 		= 1.5							# The interval, it's suppose that a < b
		f       = t**3+4*t**2-10 				# The function
		tol     = 1e-5							# The max error acceptable
		nmax    = 10							# Max number iteractions


	f_ 		= sp.diff(f, t)						# The function f' derivative of f

	# The begin to start the calculations
	feval 	= sp.lambdify(t, f, "numpy")
	flatex	= "$f(t) = " + toLaTeX(f)
	f		= Funcao(feval, flatex)

	f_eval 	= sp.lambdify(t, f_, "numpy")
	f_latex	= "$f'(t) = " + toLaTeX(f_)
	f_		= Funcao(f_eval, f_latex)

	return p0, f, f_, tol, nmax
