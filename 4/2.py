# -*- coding: utf-8 -*-
'''
		   @file: 
   		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np
import sympy as sp
import inputs

if __name__ == "__main__":
	n, h, f = inputs.in2()	# A ordem é zero
							# Neste exemplo a, b e t sao inuteis pois so serao
							# so utilizados os valores de f nos pontos t e o valor de h

	I = 0 								# O valor da soma total
	for i in range(1, n):
		I += f[i]
	I *= 2
	I += f[0] + f[n]
	I *= (h/2)

	print("O valor da integral e: " + str(I))