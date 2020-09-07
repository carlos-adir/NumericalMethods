# -*- coding: utf-8 -*-
'''
		   @file: 3.py
   		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Algoritmo de eliminação parcial

'''

import numpy as np
import auxiliar
import sys


def Scaled(A):
	n = len(A)
	m = np.zeros((n, n+1))
	x = np.zeros(n)
	nrow = np.zeros(n, dtype = type(int))

	# Adicao em relacao ao outro algoritmo
	s = np.zeros(n)
	for i in range(n):
		for j in range(n):
			if s[i] < np.abs(A[i][j]):
				s[i] = np.abs(A[i][j])
		if s[i] == 0:
			return None
	# Ate aqui

	for i in range(n):		
		nrow[i] = i
	for i in range(n-1):
		maximo = 0
		p = i
		for j in range(i, n):
			if np.abs(A[nrow[j]][i])/s[nrow[j]] > maximo: # Alteracao desse
				maximo = np.abs(A[nrow[j]][i])/s[nrow[j]] # E desse
				p = j

		if A[nrow[p]][i] == 0:
			print('Nao existe solucao - 1')
			return None
		if nrow[i] != nrow[p]:
			nrow[i], nrow[p] = nrow[p], nrow[i] # A troca de linhas
		for j in range(i+1, n):
			m[nrow[j]][i] = A[nrow[j]][i]/A[nrow[i]][i]
			A[nrow[j]] = A[nrow[j]] - m[nrow[j]][i]*A[nrow[i]]
			#print(A)
	if A[nrow[-1]][n] == 0:
		print('Nao existe solucao - 2') 
		return None
	x[-1] = A[nrow[-1]][-1]/A[nrow[-1]][-2]
	for i in range(n-2, -1, -1):
		soma = 0
		for j in range(i+1, n):
			soma += A[nrow[i]][j]*x[j]
		x[i] = (A[nrow[i]][-1]-soma)/A[nrow[i]][i]
	return x


if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	M = inp()
	x = Scaled(M)
	show(x)
	#img(x, y, f)