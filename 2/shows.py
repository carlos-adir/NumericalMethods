# -*- coding: utf-8 -*-
'''
		   @file: shows.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import sympy as sp
import numpy as np

def get(algorithm, number):
	if algorithm == 1:
		return show1
	elif algorithm == 2:
		return show2
	elif algorithm == 3:
		return show3
	elif algorithm == 4:
		return show4
	elif algorithm == 5:
		return show5

def show1(n, nmax, error, value):
	error = abs(error)

	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str(error) + " is:")
	print(value)

def show2(n, nmax, error, p, p_):
	error = abs(error)

	if abs(p_) > 1:
		print("The process stoped because g'(p) >= 1")
	else:
		if n == nmax:
			print('The process stoped by the number of iterations')
		else:
			print('The process stoped by the tolerance')
		print("The approximate value with n = " + str(n))
		print("And error " + str(error) + " is:")
		print(p)

def show3(n, nmax, error, value):
	return show1(n, nmax, error, value)

def show4(n, nmax, error, value):
	return show1(n, nmax, error, value)

def show5(n, nmax, error, value):
	return show1(n, nmax, error, value)



