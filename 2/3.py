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

def img(funcoes, raiz, p0): # Para mostrar na tela a imagem
	a = raiz - 3*abs(raiz-p0)
	b = raiz + 3*abs(raiz-p0)
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

	p0, f, f_, tol, nmax = inputs.in3(1)
	n, error, p = Newton(p0, f.e, f_.e, tol, nmax)
	
	show(n, nmax, error, p)
	img([f, f_], p, p0)