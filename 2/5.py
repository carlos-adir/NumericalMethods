'''
		   @file: 5-False_position_method.py
   		   @date: 17th July 2017
		 @author: Carlos Adir (carlos.adir.leite@gmail.com)
	@description: 	Este algoritmo descreve o método da falsa posição.
					Esse metodo consiste em pegar diferentes cordas e traçar e ver a todo momento a intersecção.
					O metodo é muito semelhante ao método da secante.

'''

import numpy as np # Nao utilizado, mas um potencial
import sympy as sp
import matplotlib.pyplot as plt
import inputs
import results


def show(n, nmax, error, p):
	error = abs(error)
	if n == nmax:
		print('The process stoped by the number of iterations')
	else:
		print('The process stoped by the tolerance')

	print("The approximate value with n = " + str(n))
	print("And error " + str(error) + " is:")
	print(p)

def img(funcoes, raiz, p0, p1): # Para mostrar na tela a imagem
	a, b = p0, p1
	if a > b:
		a, b = b,a
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
	plt.annotate("$p_1$",
				ha = 'center', va = 'bottom',
				xytext = (p1 - (b-a)/5, funcoes[0].e(p1)), 
				xy = (p1, funcoes[0].e(p1)),
				bbox=dict(boxstyle="round4", fc="w"),
				arrowprops = dict(arrowstyle="->"))
	plt.scatter(p1, funcoes[0].e(p1), c = 'k', s = 25.)

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

def Secant(p0, p1, f, tol, nmax):
	# Os calculos
	n 		= 0
	q0 		= f(p0)
	q1 		= f(p1)
	while 1:
		p 	= p1 - q1*(p1-p0)/(q1-q0)
		n  += 1
		if abs(p - p1) < tol or n == nmax:
			error = (p-p1)/2
			return n, error, p
		# Apenas a partir daqui que diferencia do metodo da secante
		q	= f(p)
		if q*q1 < 0:
			p1 = p
			q1 = q

if __name__ == "__main__":
	p0, p1, f, tol, nmax = inputs.in4(3)
	n, error, p = Secant(p0, p1, f.e, tol, nmax)
	
	show(n, nmax, error, p)
	img([f], p, p0, p1)

