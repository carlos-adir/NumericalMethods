# -*- coding: utf-8 -*-
'''
		   @file: 1.py
   		   @date: 17th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Método da Bissecção
					O algoritmo da bissecção faz uso do teorema do valor intermediário que indica
					que se uma função é contínua em um intervalo [a, b], e f(a) e f(b) tem sinais
					opostos, significa que existe pelo menos uma raiz no intervalo [a, b].
					A ideia consiste entao em repartir o intervalo [a, b] na metade, e sucessivamente
					ir escolhendo um intervalo menor em que a raiz está contida.
					Mais informacoes no wiki:
					https://github.com/CarlosAdir/Metodos-Numericos/wiki/2:1:Metodo-da-Bisseccao 

'''

import sys
import auxiliar

def Bissection(a, b, f, tol, nmax):
	# Os calculos
	if type(f) != type(Bissection): 		# Para ver se f é uma função já ou se é uma classe. Pois queremos uma função
		f 		= f.e
	n 		= 0 							# Porque estamos na primeira interacao
	fa		= f(a)							# Calculamos o primeiro ponto, o da esquerda
	while n < nmax:							# Um loop com uma condição de parada, para fazer as iteracoes.
		p 	= a + (b-a)/2					# Calculamos o ponto médio do intervalo
		fp 	= f(p)							# Calculamos o valor da função nesse ponto médio
		n  += 1
		if fp == 0 or (b-a)/2 < tol:		# Verifica se encontramos exatamente a raiz em p, ou quando o tamanho do intervalo é muito pequeno
			break
		if fa*fp > 0:
			a  = p
			fa = fp
		else:
			b  = p
	error = (b-a)/2
	return n, error, p

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	a, b, f, tol, nmax = inp()
	# Pega os valores de entrada, com base nos argumentos digitados no terminal
	n, error, r = Bissection(a, b, f, tol, nmax)
	# Aqui fazemos o metodo da Bissecção
	# Aqui obtemos o valor de n, que é a quantidade de iterações que ja foram feitas
	# O valor de error, que é o erro estimado da raiz. Esse erro é sempre maior que o erro real
	# E também o valor estimado da raiz, que chamamos de r
	show(n, nmax, error, r)
	# Essa funcao informa os resultados obtidos com n, com nmax, erro e o valor da raiz
	img(a, b, [f], r)
	# Aqui plota o gráfico da curva, com o ponto em que a raiz se encontra