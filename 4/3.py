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


def Simpson(a, b, n, f):
	h 	= (b-a)/(2*n)
	x 	= np.linspace(a, b, 2*n+1)
	y 	= f(x)
	I0	= y[0]+y[-1]
	I1	= 0				# Soma de f(x_{2i-1})
	I2	= 0				# Soma de f(x_{2i})
	for i in range(1, 2*n-1):
		if i % 2 == 1: # Se i for impar, ou if i is even
			print(i)
			I1 += y[i]
		else:
			I2 += y[i]
	I = h*(I0 + 2*I2 + 4*I1)/3
	return x, y, I




if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	a, b, n, f = inp()
	x, y, I = Simpson(a, b, n, f.e)
	show(I)
	img(a, b, n, f, x, y)

