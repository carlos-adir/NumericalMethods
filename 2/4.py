# -*- coding: utf-8 -*-
'''
		   @file: 4-Secant_method.py
   		   @date: 17th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Método da Secante
					Este algoritmo descreve o método da secante.
					Esee metodo da secante consiste em uma adaptação do método de Newton mas que aproxima a derivada
					f'(t) pela a inclinação da reta entre dois pontos extremos.

'''

import sys
import aux

def Secant(p0, p1, f, tol, nmax):
	# Os calculos
	n 		= 1
	q0 		= f(p0)
	q1 		= f(p1)
	while 1:
		p 	= p1 - q1*(p1-p0)/(q1-q0)
		n  += 1
		if abs(p - p1) < tol or n == nmax:
			error = (p-p1)/2
			return n, error, p
		p0	= p1
		q0 	= q1
		p1 	= p
		q1 	= f(p)

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	p0, p1, f, tol, nmax = inp()
	# Aqui pegamos duas estimativas, p0 e p1
	# A função f já lambda, que queremos achar a raiz
	# A tolerancia tol para limitar o erro
	# e nmax que limita a quantidade de iterações e não deixar entrar em loops infinitos
	n, error, p = Secant(p0, p1, f.e, tol, nmax)
	# Calculamos a quantidade de iterações realizadas, o erro e a estimativa da raiz
	show(n, nmax, error, p)
	# Mostramos os resultados com a quantidade de iterações, o valor do erro e a estimativa para raiz
	img([f], p, p0, p1)
	# Plotamos o gŕafico da função f.
	# Obtemos o intervlao [a, b] para plotar o gráfico através das estimativas iniciais p0 e p1
	# E mostramos a raiz estimada chamada p
