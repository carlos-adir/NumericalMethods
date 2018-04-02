# -*- coding: utf-8 -*-
'''
		   @file: inputs.py
		   @date: 09th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This code is to be the inputs of the codes, only for don't repeat the same part of code
					in all the files

'''

import sympy as sp
import numpy as np

def master(number):
	'''
	Essa funcao retorna apenas o intervalo, o numero de n e a funcao ja na forma lambda
	'''
	t		= sp.symbols('t')
	

	if number == 1:
		a, b	= 0, 1										# The interval and initial value
		n 		= 5 										# The number of segments
		f 		= sp.sqrt(1+sp.cos(t)**2)					# The function f(t, y)
	elif number == 2:
		a, b	= 0, 0.5
		n 		= 5 	
		f 		= 1/(t-4)
	elif number == 3:
		a, b	= 0, 0.5									# The interval and initial value
		n 		= 5 										# The number of segments
		f 		= t**2*sp.ln(t)								# The function f(t, y)


	f 		= sp.lambdify(t, f, "numpy") 					# Transform the function to lambdify
	return a, b, n, f

def in1(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 1.py
	'''
	a, b, n, f = master(number)
	t, h	= np.linspace(a, b, n+1, endpoint = True, retstep = True) # n+1 pois sao n+1 pontos
	f		= f(t)
	return n, h, f

def in2(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 2.py
	Retorna in1 pois é a mesma entrada do algoritmo de 1
	'''
	return in1(number)

def in3(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 3.py
	'''
	a, b, n, f = master(number)
	t, h	= np.linspace(a, b, 2*n+1, endpoint = True, retstep = True) # n+1 pois sao n+1 pontos
	f		= f(t)
	return n, h, f

def in4(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 4.py
	'''
	a, b, n, f = master(number)
	t, h	= np.linspace(a, b, 3*n+1, endpoint = True, retstep = True) # n+1 pois sao n+1 pontos
	f		= f(t)
	return n, h, f

def in5(number = 1):
	'''
	Esta funcao é apenas para o algoritmo 5.py
	'''
	a, b, n, f = master(number)
	t, h	= np.linspace(a, b, 4*n+1, endpoint = True, retstep = True) # n+1 pois sao n+1 pontos
	f		= f(t)
	return n, h, f