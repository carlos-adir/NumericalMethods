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
	n, h, f = inputs.in4()	# A ordem é terceira
							# Neste exemplo a, b e t sao inuteis pois so serao
							# so utilizados os valores de f nos pontos t e o valor de h

	I1 = f[1]+f[2]			# O valor que sera multiplicado por 3
	I2 = 0					# O valor que sera multiplicado por 2
	for i in range(1, n):
		I1 += f[3*i+1]+f[3*i+2]
		I2 += f[3*i]
	I = 3*I1 + 2*I2
	I += f[0] + f[n]
	I *= (3*h/8)

	print("O valor da integral e: " + str(I))