# -*- coding: utf-8 -*-
'''
		   @file: aux.py
		   @date: 
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Funcoes e classes auxiliares

'''

import numpy as np
#import sympy as sp
import inputs
import imgs
import shows

class Funcao(object):
	"""docstring for funcao"""
	def __init__(self, evalu, latex):
		self.e = evalu
		self.l = latex
		
def Separavel(sp, x):
	if type(x) == np.ndarray:
		n = len(x)
		y = np.zeros(n)
		for i in range(n):
			y[i] = Separavel(sp, x[i])
		return y
	else:
		for j in range(len(sp)):
			a, b, f = sp[j]
			if a <= x <= b:
				return f(x)

def toLaTeX(lat):
	cdot	= ' \\cdot '
	return str(lat).replace('**', '^').replace('*', cdot) + '$'

def leia_de_arquivo(nome):
	nome = "input/" + nome
	arq	= open(nome)
	lin	= arq.readlines()
	arq.close()
	n = len(lin)
	x = np.zeros(n)
	y = np.zeros(n)
	for i in range(n):
		lin[i] = lin[i].split('\n')[0].split(' ')
		x[i], y[i] = float(lin[i][0]), float(lin[i][1])
	return x, y


def get_from_args(strings):
	algorit	= int(strings[0].split('.py')[0])
	limite = inputs.limites[algorit-1]
	try:
		number = int(strings[1])
		if number < limite[0]:
			number = limite[0]
			print("Foi digitado um valor menor que " + str(number))
			print("Por isso, será escolhido o valor de " + str(number))
		elif number > limite[1]:
			number = limite[1]
			print("Foi digitado um valor maior que " + str(number))
			print("Por isso, será escolhido o valor de " + str(number))
			print('\n')
	except:
		number = 1
		print("Nao foi informado a entrada selecionada! ")
		print("Por isso, foi escolhido o valor padrão de " + str(number))
		print("Você pode selecionar os valores de " + str(limite[0]) + " a " + str(limite[1]) + ".")
		print('\n')
	return algorit, number

def get_all(argumentos):
	algorit, number = get_from_args(argumentos)
	inp 	= inputs.get(algorit, number)
	img		= imgs.get(algorit, number)
	show	= shows.get(algorit, number) # number é inutilizado aqui, mas serve
	return inp, img, show
