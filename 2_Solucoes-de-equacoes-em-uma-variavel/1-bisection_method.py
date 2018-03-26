'''
		   @file: 1-bisection_method.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: O algoritmo da bissecção faz uso do teorema do valor intermediário que indica
					que se uma função é contínua em um intervalo [a, b], e f(a) e f(b) tem sinais
					opostos, significa que existe pelo menos uma raiz no intervalo [a, b].
					A ideia consiste entao em repartir o intervalo [a, b] na metade, e sucessivamente
					ir escolhendo um intervalo menor em que a raiz está contida.
					Mais informacoes no wiki:
					https://github.com/CarlosAdir/Metodos-Numericos/wiki/2:1:Metodo-da-Bisseccao 

'''

import numpy as np # Nao utilizado, mas um potencial
import sympy as sp
#import roots
import inputs

if __name__ == "__main__":

	a, b, f, tol, nmax = inputs.in1()

	# Existe pelo menos uma raiz no intervalo [a, b]

	# Os calculos
	n 		= 0 							# Porque estamos na primeira interacao
	fa		= f(a)							# Calculamos o primeiro ponto, o da esquerda
	while n < nmax:							# Um loop com uma condição de parada, para fazer as iteracoes.
		p 	= a + (b-a)/2					# Calculamos o ponto médio do intervalo
		fp 	= f(p)							# Calculamos o valor da função nesse ponto médio
		if fp == 0 or (b-a)/2 < tol:		# Verifica se encontramos exatamente a raiz em p, ou quando o tamanho do intervalo é muito pequeno
			break
		n  += 1
		if fa*fp > 0:
			a  = p
			fa = fp
		else:
			b  = p

	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str((b-a)/2) + " is:")
	print(p)