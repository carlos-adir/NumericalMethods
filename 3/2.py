# -*- coding: utf-8 -*-
'''
		   @file: 1.py
   		   @date: 20th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Interpolação de Hermite

'''

import sys
import sympy as sp
import aux
import numpy as np

def Hermite(x, y, y_):
	# The variables
	t 		= sp.symbols('t')

	# The calculations
	n = len(x)-1
	Q = np.zeros((2*(n+1), 2*(n+1))) 
	Qs = np.zeros(2*(n+1))
	z = np.zeros(2*(n+1))
	for i in range(n+1):
		z[2*i]		= x[i]
		z[2*i+1]	= x[i]
		Q[2*i][0]	= y[i]
		Q[2*i+1][0]	= y[i]
		Q[2*i+1][1]	= y_[i]
		if i != 0:
			Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0])/(z[2*i]-z[2*i-1])
		#L.append(Li)
	for i in range(2, 2*(n+1)):
		for j in range(2, i+1):
			Q[i][j] = (Q[i][j-1] - Q[i-1][j-1])/(z[i]-z[i-j])

	for i in range(2*(n+1)):
		Qs[i] = Q[i][i]

	multi = 1
	f = Qs[0]
	for i in range(n):
		multi *= t-x[i]
		f += Qs[2*i+1]*multi
		multi *= t-x[i]
		f += Qs[2*i+2]*multi
	multi *= t-x[-1]
	f += Qs[2*n+1]*multi

	f = sp.simplify(f)

	L = aux.Funcao(sp.lambdify(t, f, "numpy"), '$L(t) = ')# + aux.toLaTeX(f))
	return L

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	x, y, y_, f, f_ = inp()
	L = Hermite(x, y, y_) # Pega a função e já deixa no lambdify
	show(L)
	img(f, L, x, y)
	