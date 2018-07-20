# -*- coding: utf-8 -*-
'''
		   @file: 2.py
   		   @date: 17th July 2018
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: Método Iterativo do Ponto Fixo
					Esse algoritmo é a implementação do algoritmo de ponto fixo.
					Ele mostra o resultado final, bem como o gráfico da curva ao redor do ponto de interesse

'''

import sys
import aux


def FixedPoint(p0, g, g_, tol, nmax): # Este algoritmo não é muito robusto, caso g' fique 1 ou maior, ele diverge
	n 		= 0
	while 1:
		p 	= g(p0)
		error = (p-p0)/2.
		p_	= g_(p0)
		n  += 1
		if abs(error) < tol or n == nmax or (not abs(p_) < 1):
			return n, error, p, p_
		p0	= p

def getAB(p0, f): # Para retornar os valores de a e de b para poder imprimir o valor na tela.
				  # É utilizado o metodo da bissecção
	a, b = -2*p0, 3*p0
	nmax = 20
	tol  = 10**(-6)

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
	size_interval = abs(p-p0)
	a	= p - 3*size_interval
	b	= p + 3*size_interval 
	return a, b
		

if __name__ == "__main__":
	inp, img, show = aux.get_all(sys.argv)
	# Aqui pega as funções base a partir dos argumentos digitados no terminal
	p0, f, g, g_, tol, nmax = inp()
	# Pega os valores de entrada, com base nos argumentos digitados no terminal
	a, b  = getAB(p0, f.e)
	# Aqui pegamos uma estimativa do intervalo [a, b] para se plotar o gráfico.
	# Isso porque diferentemente do método da bissecção, em que é dado um intervalo já para se plotar o gráfico
	# Esse metodo iterativo não fornece o intervalo, apenas valores
	n, error, r, p_ = FixedPoint(p0, g.e, g_.e, tol, nmax)
	# Fazemos os calculos, e obtemos então 4 valores que são respectivamente
	# O numero de iterações feitas
	# O valor do erro estimado, sempre maior que o real
	# O valor r da raiz
	# O valor de p' na iteração n. Esse valor é pego apenas para saber se o processo foi interrompido porque |g'(p)| >= 1
	show(n, nmax, error, r, p_)
	# Mostramos os resultados na tela, sabendo o numero de iterações e o maximo
	# O valor do erro
	# O valor da raiz, caso o processo tenha sido um sucesso(não foi interrompido por |p_| >= 1)
	# E o valor de p_ para saber se foi interrompido por |g'(p)| >= 1 ou não
	img(a, b, [f, g, g_], r, p0)
	# e plotamos os gráficos das funções [f, g, g_] no intervalo [a, b]
	# Bem como mostramos o ponto da raiz r e a estimativa inicial p0