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

import numpy as np # Nao utilizado, mas um potencial
import sympy as sp
import matplotlib.pyplot as plt
import inputs
import results

def show(n, nmax, error, value):
	error = abs(error)

	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str(error) + " is:")
	print(value)

def img(a, b, funcoes, raiz):
	X = np.linspace(a, b, 1024)
	Y = f.e(X)

	# Para alterar o range do eixo X
	axes = plt.gca()
	axes.set_xlim([a - (b-a)/5, b + (b-a)/5])
	
	plt.grid(True, which='both')
	plt.plot(X, Y, label = f.l)

	plt.annotate(str(raiz),
				ha = 'center', va = 'bottom',
				xytext = (raiz - (b-a)/5, f.e(raiz)), 
				xy = (raiz, f.e(raiz)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(raiz, f.e(raiz), c = 'k', s = 25.)

	plt.annotate("a",
				ha = 'center', va = 'bottom',
				xytext = (a+(b-a)/5, f.e(a)), 
				xy = (a, f.e(a)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(a, f.e(a), c = 'k', s = 25.)
	plt.annotate("b",
				ha = 'center', va = 'bottom',
				xytext = (b-(b-a)/5, f.e(b)), 
				xy = (b, f.e(b)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(b, f.e(b), c = 'k', s = 25.)


	X = np.linspace(a - (b-a)/2, b + (b-a)/2, 10)
	plt.legend()
	plt.plot(X, np.zeros(len(X)), linewidth = 2., c = 'k')

	plt.title("Grafico das funções")
	plt.xlabel('Eixo $t$')
	plt.ylabel('Eixo $y$')

	plt.show()

def Bissection(a, b, f, tol, nmax):
	# Os calculos
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

	a, b, f, tol, nmax = inputs.in1(1)
	n, error, p = Bissection(a, b, f.e, tol, nmax)
	
	show(n, nmax, error, p)
	img(a, b, [f], p)