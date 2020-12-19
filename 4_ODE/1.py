# -*- coding: utf-8 -*-
'''
		   @file: 1-Eulers_method.py
		   @date: 28th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: This algorithm returns the final value

'''

import sys
import auxiliar

from methodes import Euler




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