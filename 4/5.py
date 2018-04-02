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
	n, h, f = inputs.in5()	# A ordem é quatro
							# Neste exemplo a, b e t sao inuteis pois so serao
							# so utilizados os valores de f nos pontos t e o valor de h

	I1 = f[1]+f[3]			# O valor que sera multiplicado por 32
	I2 = f[2]				# O valor que sera multiplicado por 12
	I3 = 0					# O valor que sera multiplicado por 14
	for i in range(1, n):
		I1 += f[4*i+1]+f[4*i+3]
		I2 += f[4*i+2]
		I3 += f[4*i]
	I = 32*I1 + 12*I2 + 14*I3
	I += 7*(f[0] + f[n])
	I *= (2*h/45)

	print("O valor da integral e: " + str(I))