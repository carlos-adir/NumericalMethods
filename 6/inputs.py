# -*- coding: utf-8 -*-
'''
		   @file: input.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import sympy as sp
import numpy as np

limites = [	[1, 9],\
			[1, 9]]


def get(algorithm, number):
	if algorithm == 1:
		return lambda : in1(number)
	elif algorithm == 2:
		return lambda : in2(number)
	elif algorithm == 3:
		return lambda : in3(number)
	elif algorithm == 4:
		return lambda : in4(number)
	elif algorithm == 5:
		return lambda : in5(number)
	elif algorithm == 6:
		return lambda : in6(number)
	elif algorithm == 7:
		return lambda : in7(number)
	elif algorithm == 8:
		return lambda : in8(number)
	elif algorithm == 9:
		return lambda : in9(number)
	elif algorithm == 10:
		return lambda : in10(number)

def master(number):
	if number == 1:
		n = 4
		A = [[1, 1, 0, 3], \
			 [2, 1, -1, 1], \
			 [3, -1, -1, 2], \
			 [-1, 2, 3, -1]]
		b = [4, 1, -3, 4]
		# x = [-1, 2, 0, 1]
	elif number == 2:
		n = 4
		A = [[1, -1, 2, -1], \
			 [2, -2, 3, -3], \
			 [1, 1, 1, 0], \
			 [1, -1, 4, 3]]
		b = [-8, -20, -2, 4]
		# x = [-7, 3, 2, 2]
	elif number == 3:
		n = 3
		A = [[1, 1, 1], \
			 [2, 2, 1], \
			 [1, 1, 2]]
		b = [4, 6, 6]
		# x = nao existe
	elif number == 4:
		n = 3
		A = [[1, 1, 1], \
			 [2, 2, 1], \
			 [1, 1, 2]]
		b = [4, 4, 6]
		# x = nao existe
	elif number == 5:
		n = 3
		A = [[4 ,-1 , 1], \
			 [2, 5, 2], \
			 [1, 2, 4]]
		b = [8, 3, 11]
		# x = [1, -1, 3]
	elif number == 6:
		n = 3
		A = [[4, 1, 2], \
			 [2, 4, -1], \
			 [1, 1, -3]]
		b = [9, -5, -9]
		# x = [1, -1, 3]
	elif number == 7:
		n = 2
		A = [[0.003, 59.14], \
			 [5.291, -6.13]]
		b = [59.17, 46.78]
		# x = [10, 1]
	elif number == 8:
		n = 2
		A = [[30, 591400], \
			 [5.291, -6.13]]
		b = [591700, 46.78]
		# x = [10, 1]
	elif number == 9:
		n = 3
		A = [[2.11, -4.21, 0.921], \
			 [4.01, 10.2, -1.12], \
			 [1.09, 0.987, 0.832]]
		b = [2.01, -3.09, 4.21]
		# x = [-0.436, 0.430, 5.12]
	return A, b, n


def in1(number):
	A, b, n = master(number)

	#X = np.linalg.solve(A,b)
	#print('X = ' + str(X))
	A = np.array(A)
	M = np.zeros((n, n+1))
	for i in range(n):
		for j in range(n):
			M[i][j] = A[i][j]
		M[i][-1] = b[i]
	return M

def in2(number):
	return in1(number)

def in3(number):
	return in1(number)