# -*- coding: utf-8 -*-
'''
		   @file: 3-Runge_Kutta.py
		   @date: 9th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import sys
import aux
import numpy as np

def Runge_Kutta(a, b, c, n, f):
	h 		= (b-a)/n 									# The step size
	t 		= a 										# The frist point that we start
	w 		= c											# The y values approx
	k 		= [0, 0, 0, 0]								# Initial condition of K, does not matter the initial value, only that there are 4 numbers on the list
	
	x 		= np.zeros(n+1)
	w		= np.zeros(n+1)
	fs		= np.zeros(n+1)
	k 		= np.zeros(4)

	x[0]	= a
	w[0] 	= c
	fs[0]	= f(t, w[0])
	for i in range(n):
		k[0]	= h*fs[i]
		k[1]	= h*f(t+h/2, w[i]+k[0]/2)
		k[2]	= h*f(t+h/2, w[i]+k[1]/2)
		k[3]	= h*f(t+h, w[i]+k[2])

		w[i+1]	= w[i] + (k[0]+2*k[1]+2*k[2]+k[3])/6
		t		= a + h*(i+1)
		x[i+1]	= t
		fs[i+1] = f(t, w[i+1])
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
	#x, w, fs = Runge_Kutta(a, b, c, n, f)
	# Pegamos os valores dos pontos calculados
	#show()
	# Mostra as informações, caso sejam necessárias
	#img(x, w, fs, y)
	# Mostra na tela os pontos calculados, 