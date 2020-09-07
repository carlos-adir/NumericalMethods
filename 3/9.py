# -*- coding: utf-8 -*-
'''
		   @file: 9.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Algoritmo de Spline Cubico

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

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	x, y, f = inp()
	S = Spline_cubico(x, y)
	show()
	img(f, S, x, y)
