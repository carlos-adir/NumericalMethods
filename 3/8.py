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

def Simpson(x, y):
	# Aqui supomos que len(y) seja impar:
	# len(y) = len(x)
	# len(x) % 2 = 1

	t = sp.symbols('t')

	retorno = []
	n = (len(y)-1)//2 # Indicando que ha n funcoes
	for i in range(n):
		X = np.array([x[2*i], x[2*i+1], x[2*i+2]])
		Y = np.array([y[2*i], y[2*i+1], y[2*i+2]])
		t = sp.symbols('t')
		f = 0
		f += (t-X[0])*(t-X[1])*Y[2]/((X[2]-X[0])*(X[2]-X[1]))
		f += (t-X[1])*(t-X[2])*Y[0]/((X[0]-X[1])*(X[0]-X[2]))
		f += (t-X[2])*(t-X[0])*Y[1]/((X[1]-X[2])*(X[1]-X[0]))
		f = sp.lambdify(t, f, "numpy")
		retorno.append((x[2*i], x[2*i+2], f))

	return aux.Funcao(lambda t: aux.Separavel(retorno, t), "$S(t)$")

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	x, y, f = inp()
	S = Simpson(x, y)
	show()
	img(f, S, x, y)
