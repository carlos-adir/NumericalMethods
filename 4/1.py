# -*- coding: utf-8 -*-
'''
		   @file: 
   		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Algoritmo de integração numerica atraves 

'''

import numpy as np
import auxiliar
import sys

def Const(a, b, n, f):
	I = 0
	h = (b-a)/n
	x = np.linspace(a, b, n)
	y = f(x)
	for i in range(n-1):
		I += y[i]
	I *= h
	return x, y, I


if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	a, b, n, f = inp()
	x, y, I = Const(a, b, n, f.e)
	show(I)
	img(a, b, n, f, x, y)
