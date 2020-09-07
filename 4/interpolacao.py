# -*- coding: utf-8 -*-
'''
		   @file: input.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''


import sys
import auxiliar
import numpy as np
import sympy as sp

def Separavel(sp, x):
	if type(x) == np.ndarray:
		n = len(x)
		y = np.zeros(n)
		for i in range(n):
			y[i] = Separavel(sp, x[i])
		return y
	else:
		for j in range(len(sp)):
			a, b, f = sp[j]
			if a <= x <= b:
				#print('[a, b] = [' + str(a) + ', ' + str(b) + ']')
				#print(f(x))
				return f(x)

def Spline_cubico(x, y):
	# A funcao ja retorna no modo lambdify

	n	= len(x)-1
	h	= np.zeros(n+1)
	al	= np.zeros(n+1) # alpha
	l 	= np.zeros(n+1)
	mu	= np.zeros(n+1)
	z	= np.zeros(n+1)

	a 	= y
	b	= np.zeros(n+1)
	c	= np.zeros(n+1)
	d	= np.zeros(n+1)

	for i in range(n):
		h[i] = x[i+1]-x[i]
	for i in range(1, n):
		al[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])

	l[0]	= 1
	mu[0]	= 0
	z[0]	= 0

	for i in range(1, n):
		l[i]	= 2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
		mu[i]	= h[i]/l[i]
		z[i]	= (al[i]-h[i-1]*z[i-1])/l[i]

	l[n]	= 1
	mu[n]	= 0
	z[n]	= 0

	for j in range(n-1, -1, -1):
		c[j]	= z[j]-mu[j]*c[j+1]
		b[j]	= (a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
		d[j]	= (c[j+1]-c[j])/(3*h[j])

	#return a, b, c, d

	t	= sp.symbols('t')
	retorno = []
	for j in range(n):
		f = a[j]+b[j]*(t-x[j]) + c[j]*(t-x[j])**2 + d[j]*(t-x[j])**3
		f = sp.lambdify(t, f, "numpy")
		retorno.append((x[j], x[j+1], f))

	return aux.Funcao(lambda t: Separavel(retorno, t), "$S(t)$")

def Lagrange(x, y):
	# The variables
	t 		= sp.symbols('t')

	# The calculations
	n = len(x)
	L = []
	for i in range(n):
		Li = 1
		for j in range(n):
			if i != j:
				Li *= (t-x[j])/(x[i]-x[j])
		L.append(Li)
	g = 0
	for i in range(n):
		g += L[i] * y[i]
	g = sp.simplify(g)
	L = aux.Funcao(sp.lambdify(t, g, "numpy"), '$L(t) = ' + aux.toLaTeX(g))
	return L



# Agora composicoes 
def Const(x, y):
	n 	= len(x)-1

	a 	= y
	#print('n = ' + str(n))
	t	= sp.symbols('t') # Nao é utilizado, mas é colocado para que funcione com Separavel
	retorno = []
	for j in range(n):
		f = a[j]-t*10**(-6)
		
		f = a[j]+(t-1)**2-t**2+2*t-1
		f = sp.lambdify(t, f, "numpy")
		retorno.append((x[j], x[j+1], f))
		#print('[a, b] = [' + str(x[j]) + ', ' + str(x[j+1]) + ']')
		#print(f(1))
	for i in range(n):
		a, b, f = retorno[i]
		print(f(1))
	return aux.Funcao(lambda t: Separavel(retorno, t), "$S(t)$")


def Linear(x, y):
	# A funcao ja retorna no modo lambdify
	
	n	= len(x)-1
	
	a 	= y
	b	= np.zeros(n+1)
	h	= np.zeros(n+1)

	for i in range(n):
		h[i] = x[i+1]-x[i]
	for i in range(n):
		b[i] = (a[i+1]-a[i])/(x[i+1]-x[i])

	#return a, b

	t	= sp.symbols('t')
	retorno = []
	for j in range(n):
		f = a[j]+b[j]*(t-x[j])
		f = sp.lambdify(t, f, "numpy")
		retorno.append((x[j], x[j+1], f))

	return aux.Funcao(lambda t: Separavel(retorno, t), "$S(t)$")
	


def Simpson(x, y):
	# Aqui supomos que len(y) seja impar:
	# len(y) = len(x)
	# len(x) % 2 = 1

	t = sp.symbols('t')

	retorno = []
	#print('len(y) = ' + str(len(y)))
	n = (len(y)-1)//2 # Indicando que ha n funcoes
	#print('n = ' + str(n))
	for i in range(n):
		X = np.array([x[2*i], x[2*i+1], x[2*i+2]])
		Y = np.array([y[2*i], y[2*i+1], y[2*i+2]])
		f = Lagrange(X, Y)
		#print(type(f.e))
		#print(type(f(x[2*i])))
		#print(f(x[2*i]))
		#print('122')
		retorno.append((x[2*i], x[2*i+2], f.e))

	return aux.Funcao(lambda t: Separavel(retorno, t), "$S(t)$")


