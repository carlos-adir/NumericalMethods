# -*- coding: utf-8 -*-
'''
		   @file: 3.py
   		   @date: 17th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 	Método de Newton
					Este algoritmo é a representação do algoritmo de Newton para achar raizes
					Uma das grandes vantagens de utilizar esse método é a sua rapida convergência
					Contudo, um dos problemas é que caso a derivaa se anule ao redor da raiz,
					o algoritmo provavelmente dará problema

'''

import sys
import auxiliar

def Newton(p0, f, f_, tol, nmax):
	# Os calculos
	tolmax	= 10**6
	n 		= 0 							# Porque estamos na primeira interacao
	while n < nmax:
		fp = f(p0)
		dfp = f_(p0)
		p = p0 - fp/dfp
		n += 1
		if abs(p - p0) < tol or abs(p - p0) > tolmax:
			error = (p-p0)/2
			return n, error, p
		p0 = p

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	p0, f, f_, tol, nmax = inp()
	# Pega os valores de entrada, com base nos argumentos digitados no terminal
	# Neles estão a estimativa inicial.
	# A função f(já lambidificada) que queremos achar a raiz e sua derivada f_(também já lambd)
	# A tolerância para o erro
	# E a quantidade máxima de iterações que o método pode fazer. Frenquentemente utilizado para não divergir
	n, error, p = Newton(p0, f.e, f_.e, tol, nmax)
	# Aqui temos a quantidade de iterações feitas, o valor do erro, e a estimativa da raiz
	show(n, nmax, error, p)
	# Mostramos os resultados com a quantidade de iterações, o valor do erro e a estimativa para raiz
	img([f, f_], p, p0) 
	# Plotamos o gŕafico das funções [f, f'].
	# Diferentemente do método do ponto fixo, não precisamos dos valores de [a, b] porque eles são obtidos dentro da função
	# img através dos valores de p e p0