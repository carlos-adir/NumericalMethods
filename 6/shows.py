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
	elif algorithm == 6:
		return show6
	elif algorithm == 7:
		return show7
	elif algorithm == 8:
		return show8

def show1(x):
	print(x)
def show2(x):
	return show1(x)
def show3():
	return show1(x)
