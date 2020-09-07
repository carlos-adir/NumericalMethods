# -*- coding: utf-8 -*-
'''
		   @file: 3-Runge_Kutta.py
		   @date: 9th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import sys
import auxiliar
import numpy as np
from methodes import Runge_Kutta

	


if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Pegando as funcoes base
	a, b, c, n, f, y = inp()
	print('c = ' + str(c))
	print('t = ' + str(type(c)))
	# Pegando o intervalo [a, b] de interesse
	# Pegando c, o valor inicial tal que y(a) = c
	# O valor de n, em que obtemos n intervalos, n+1 pontos
	# E a função f já lambda, tal q ue y'(t) = f(t)
	# E a função y exatamente, caso exista
	x, w, fs = Runge_Kutta(a, b, c, n, f)
	# Pegamos os valores dos pontos calculados
	show()
	# Mostra as informações, caso sejam necessárias
	img(x, w, fs, y)
	# Mostra na tela os pontos calculados, 