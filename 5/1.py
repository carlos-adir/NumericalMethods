# -*- coding: utf-8 -*-
'''
		   @file: 1-Eulers_method.py
		   @date: 28th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import sys
import aux
import numpy as np

def Euler(a, b, c, n, f):
	# O intervalo [a, b]
	# Condição inicial y(a) = c
	# n é o numero de intervalos, obtendo assim n+1 pontos
	# E f é a função já lambda, tal que y'(t) = f(t)
	h 		= (b-a)/n 									# The step size
	t 		= a 										# The frist point that we start
	
	w		= np.zeros(n+1)
	x 		= np.zeros(n+1)
	fs 		= np.zeros(n+1) 							# Não é necessário, mas se quisermos fazer a interpolação de Hermite, é possível

	x[0]	= a
	w[0] 	= c
	fs[0]	= f(t, w[0])
	for i in range(n):
		w[i+1]		= w[i] + h*fs[i]
		t   		= a + h*(i+1)
		x[i+1] 		= t
		fs[i+1]		= f(t, w[i+1])
	return x, w, fs


if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Pegando as funcoes base
	a, b, c, n, f, y = inp()
	# Pegando o intervalo [a, b] de interesse
	# Pegando c, o valor inicial tal que y(a) = c
	# O valor de n, em que obtemos n intervalos, n+1 pontos
	# E a função f já lambda, tal q ue y'(t) = f(t)
	# E a função y exatamente, caso exista
	x, w, fs = Euler(a, b, c, n, f)
	# Pegamos os valores dos pontos calculados
	show()
	# Mostra as informações, caso sejam necessárias
	img(x, w, fs, y)
	# Mostra na tela os pontos calculados, 