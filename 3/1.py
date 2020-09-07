# -*- coding: utf-8 -*-
'''
		   @file: 1.py
   		   @date: 20th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Metodo de Lagrange

'''

import sys
import sympy as sp
import auxiliar

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

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	x, y, f = inp()
	L = Lagrange(x, y) # Pega a função e já deixa no lambdify
	show(L)
	img(f, L, x, y)
	