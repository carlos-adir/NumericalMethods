# -*- coding: utf-8 -*-
'''
		   @file: 9.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Algoritmo Quadratico

'''

import sys
import auxiliar
import numpy as np
import sympy as sp

def Linear(x, y):
	# A funcao ja retorna no modo lambdify
	
	n	= len(x)-1
	
	a 	= y
	b	= np.zeros(n+1)
	h	= np.zeros(n+1)

	for i in range(n):
		h[i] = x[i+1]-x[i]
		b[i] = (a[i+1]-a[i])/h[i]

	#return a, b

	t	= sp.symbols('t')
	retorno = []
	for j in range(n):
		f = a[j]+b[j]*(t-x[j])
		f = sp.lambdify(t, f, "numpy")
		retorno.append((x[j], x[j+1], f))

	return aux.Funcao(lambda t: aux.Separavel(retorno, t), "$S(t)$")

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	x, y, f = inp()
	S = Linear(x, y)
	show()
	img(f, S, x, y)
