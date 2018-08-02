import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt

def get(algorit, number):
	# lambda a, b, funcoes, raiz: img1(a, b, funcoes, raiz, algorit, number)
	if algorit == 1:
		img = lambda f, L, x, y: img1(f, L, x, y, algorit, number)
	elif algorit == 2:
		img = img2
	elif algorit == 3:
		img = img3
	elif algorit == 4:
		img = img4
	elif algorit == 5:
		img = img5
	elif algorit == 6:
		img = img6
	elif algorit == 7:
		img = img7
	elif algorit == 8:
		img = img8
	elif algorit == 9:
		img = lambda f, S, x, y: img9(f, S, x, y, algorit, number)
	elif algorit == 10:
		img = lambda f, S, x, y, FP: img10(f, S, x, y, FP, algorit, number)
	
	return img

def img1(f, L, x, y, algorit, number):
	# Para organizar os termos
	n = len(x)
	for i in range(n-1):
		for j in range(i+1, n):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
				y[i], y[j] = y[j], y[i]
	
	# Definindo os intervalos e obtendo os valores das funções
	a, b = x[0], x[-1]
	X = np.linspace(a - (b-a)/5, b + (b-a)/5, 1024)
	
	if f != None:
		Yf = f.e(X)
		plt.plot(X, Yf, label = f.l, c = 'b')
	
	YL = L.e(X)
	plt.plot(X, YL, label = L.l, c = 'r')

	plt.scatter(x, y, c = 'k', s = 25.)
	
	# Definindo o range e a grade
	axes = plt.gca()
	axes.set_xlim([a - (b-a)/5, b + (b-a)/5])
	plt.grid(True, which='both')

	plt.legend()
	plt.title("Grafico das funções")
	plt.xlabel('Eixo $t$')
	plt.ylabel('Eixo $y$')

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

def img9(f, S, x, y, algorit, number):
	# Definindo os intervalos e obtendo os valores das funções
	a, b = x[0], x[-1]
	X = np.linspace(a - (b-a)/5, b + (b-a)/5, 1024)
	

	if f != None:
		Yf = f.e(X)
		plt.plot(X, Yf, label = f.l, c = 'b')
	

	YS = S.e(X)
	plt.plot(X, YS, label = S.l, c = 'r')

	# Começando a plotar
	plt.scatter(x, y, c = 'k', s = 25.)
	


	# Definindo o range e a grade
	axes = plt.gca()
	axes.set_xlim([a - (b-a)/5, b + (b-a)/5])
	plt.grid(True, which='both')

	plt.legend()
	plt.title("Grafico das funções")
	plt.xlabel('Eixo $t$')
	plt.ylabel('Eixo $y$')

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

def img10(f, S, x, y, FP, algorit, number):
	# Definindo os intervalos e obtendo os valores das funções
	return img9(f, S, x, y, algorit, number)