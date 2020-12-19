# -*- coding: utf-8 -*-
'''
		   @file: 1.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Metodo de Taylor de ordem maior

'''

import sys
import auxiliar
import numpy as np
from methodes import Taylor



if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Pegando as funcoes base
	a, b, c, n, f, y = inp()
	# Pegando o intervalo [a, b] de interesse
	# Pegando c, o valor inicial tal que y(a) = c
	# O valor de n, em que obtemos n intervalos, n+1 pontos
	# E a função f já lambda, tal q ue y'(t) = f(t)
	# E a função y exatamente, caso exista
	x, w, Ts = Taylor(a, b, c, n, f, order = 4)
	# Pegamos os valores dos pontos calculados
	show()
	# Mostra as informações, caso sejam necessárias
	img(x, w, Ts, y)
	# Mostra na tela os pontos calculados, 

