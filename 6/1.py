# -*- coding: utf-8 -*-
'''
		   @file: 1.py
   		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Algoritmo de eliminação gaussiana 

'''

import numpy as np
import aux
import sys

def Gauss(A):
	n = len(A)
	m = np.zeros((n, n+1))
	x = np.zeros(n)
	for i in range(n-1):
		p = i
		while p < n-1 and A[p][i] == 0:
			p += 1
		if p != i:
			# A[i], A[p] = A[p], A[i] # Essa troca nao acontece
			for j in range(i, n+1):
				A[i][j], A[p][j] = A[p][j], A[i][j] # Troca linha
		if p == n-1:
			print('Nao existe solucao - 1')
			return None
		for j in range(i+1, n):
			m[j][i] = A[j][i]/A[i][i]
			A[j] = A[j] - m[j][i]*A[i]
			#print(A)
	if A[-1][-1] == 0:
		print('Nao existe solucao - 2') 
		return None
	x[-1] = A[-1][-1]/A[-1][-2]
	for i in range(n-2, -1, -1):
		soma = 0
		for j in range(i+1, n):
			soma += A[i][j]*x[j]
		x[i] = (A[i][-1]-soma)/A[i][i]
	return x

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	M = inp()
	x = Gauss(M)
	print(x)
	#show()
	#img(x, y, f)