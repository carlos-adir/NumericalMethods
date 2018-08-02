import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt
import interpolacao


def get(algorit, number):
	# lambda a, b, funcoes, raiz: img1(a, b, funcoes, raiz, algorit, number)
	if algorit == 1:
		img = lambda a, b, n, f, x, y: img1(a, b, n, f, x, y, algorit, number)
	elif algorit == 2:
		img = lambda a, b, n, f, x, y: img2(a, b, n, f, x, y, algorit, number)
	elif algorit == 3:
		img = lambda a, b, n, f, x, y: img3(a, b, n, f, x, y, algorit, number)
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
		img = img9
	elif algorit == 10:
		img = img10
	
	return img

def img1(a, b, n, f, x, y, algorit, number):
	# Para organizar os termos
	for i in range(n-1):
		for j in range(i+1, n):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
				y[i], y[j] = y[j], y[i]
	
	# Definindo os intervalos e obtendo os valores das funções
	X = np.linspace(a - (b-a)/5, b + (b-a)/5, 1024)
	
	if f != None:
		Yf = f.e(X)
		plt.plot(X, Yf, label = f.l, c = 'b')
	
	if algorit == 1:
		L = interpolacao.Const(x, y)
	elif algorit == 2:
		L = interpolacao.Linear(x, y)
	elif algorit == 3:
		L = interpolacao.Simpson(x, y)

	XL = np.linspace(a, b, 1024)
	YL = L.e(XL)
	plt.plot(XL, YL, label = L.l, c = 'r')

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

def img2(a, b, n, f, x, y, algorit, number):
	return img1(a, b, n, f, x, y, algorit, number)


def img3(a, b, n, f, x, y, algorit, number):
	return img1(a, b, n, f, x, y, algorit, number)
