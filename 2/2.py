'''
		   @file: 2-fixed_point_iteration.py
   		   @date: 17th September 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 

'''

import numpy as np # Nao utilizado, mas um potencial
import sympy as sp
import matplotlib.pyplot as plt
import inputs
import results


def show(n, nmax, error, p, p_):
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

def img(a, b, funcoes, raiz, p0):
	X = np.linspace(a, b, 1024)
	
	# Para alterar o range do eixo X
	axes = plt.gca()
	axes.set_xlim([a - (b-a)/5, b + (b-a)/5])
	
	# Adicionar  a malha
	plt.grid(True, which='both')

	# Adicionar a raiz
	plt.annotate(str(raiz),
				ha = 'center', va = 'bottom',
				xytext = (raiz - (b-a)/5, funcoes[0].e(raiz)), 
				xy = (raiz, funcoes[0].e(raiz)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(raiz, funcoes[0].e(raiz), c = 'k', s = 25.)

	plt.annotate("$p_0$",
				ha = 'center', va = 'bottom',
				xytext = (p0 - (b-a)/5, funcoes[0].e(p0)), 
				xy = (p0, funcoes[0].e(p0)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(p0, funcoes[0].e(p0), c = 'k', s = 25.)

	for f in funcoes:
		Y = f.e(X)		
		plt.plot(X, Y, label = f.l)


	# Para plotar o eixo t, ou seja y = 0
	X = np.linspace(a - (b-a)/2, b + (b-a)/2, 10)
	plt.legend()
	plt.plot(X, np.zeros(len(X)), linewidth = 2., c = 'k')

	plt.title("Grafico das funções")
	plt.xlabel('Eixo $t$')
	plt.ylabel('Eixo $y$')

	plt.show()

def FixedPoint(p0, g, g_, tol, nmax): # Este algoritmo não é muito robusto, caso g' fique 1 ou maior, ele diverge
	n 		= 0
	while 1:
		p 	= g(p0)
		p_	= g_(p0)
		if abs(p - p0) < tol or n == nmax or (not abs(p_) < 1):
			error = (p-p0)/2.
			break
		n  += 1
		p0	= p
	return n, error, p, p_

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
		if fp == 0 or (b-a)/2 < tol:		# Verifica se encontramos exatamente a raiz em p, ou quando o tamanho do intervalo é muito pequeno
			break
		n  += 1
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
	p0, f, g, g_, tol, nmax = inputs.in2(2)
	a, b  = getAB(p0, f.e)
	n, error, p, p_ = FixedPoint(p0, g.e, g_.e, tol, nmax)

	show(n, nmax, (p-p0)/2, p, p_)
	img(a, b, [f, g, g_], p, p0)