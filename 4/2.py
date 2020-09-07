# -*- coding: utf-8 -*-
'''
		   @file: 
   		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import auxiliar
import sys
import numpy as np

def Trapezoidal(a, b, n, f):
	I = 0
	h = (b-a)/n
	x = np.linspace(a, b, n)
	y = f(x)
	for i in range(1, n-1):
		I += y[i]
	I += (1/2)*(y[0]+y[-1]) # O -1 indica que é o ultimo termo
	I *= h
	return x, y, I


if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	a, b, n, f = inp()
	x, y, I = Trapezoidal(a, b, n, f.e)
	show(I)
	img(a, b, n, f, x, y)

