# -*- coding: utf-8 -*-
'''
		   @file: 1-Eulers_method.py
		   @date: 10th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Para os algoritmos que utilizam os métodos de taylor, além de ter necessariamente
				  a função f(t, y), é necessário saber também as derivadas de f(t, y) em relação a 
				  t e em relação a y

'''

import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	a, b, c, n, T = inputs.in3() # The principals inputs
								 # The function is defined like f(t, y, y', y'', ...)

	h = (b-a)/n
	t = a
	w = c
	for i in range(n):
		w += h*T(t, w)
		t = a + (i+1)*h
		print(w)

	print(w)


