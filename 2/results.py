# -*- coding: utf-8 -*-
'''
		   @file: results.py
		   @date: 26th March 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Codigo para colocar as funções que mostram os resultados

'''

def show(n, nmax, error, value):
	
	error = abs(error)

	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str(error) + " is:")
	print(value)