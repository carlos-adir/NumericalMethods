import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt
import interpolacao

def get(algorit, number):
	if algorit == 1:
		img = lambda x, w, fs, y: img1(x, w, fs, y, algorit, number) # Done
	elif algorit == 2:
		img = lambda x, w, Ts, y: img3(x, w, Ts, y, algorit, number) # Done
	elif algorit == 3:
		img = lambda x, w, fs, y: img3(x, w, fs, y, algorit, number) # Done
	elif algorit == 4:
		img = lambda funcoes, raiz, p0, p1: img4(funcoes, raiz, p0, p1, algorit, number)
	elif algorit == 5:
		img = lambda funcoes, raiz, p0, p1: img5(funcoes, raiz, p0, p1, algorit, number)
	return img
	

def img1(x, w, fs, y, algorit, number):
	a = x[0]
	b = x[-1]
	X = np.linspace(a, b, 1024)
	
	# Para alterar o range do eixo X

	if y != None:
		Y = y(X)
		plt.plot(X, Y, label = "Exato", c = 'b')
	fw = interpolacao.Spline_cubico(x, w)
	Yw = fw.e(X)
	plt.plot(X, Yw, label = "Numericamente", c = 'r')
	
	plt.scatter(x, w, c = 'k', s = 25.)

	axes = plt.gca()
	axes.set_xlim([a - (b-a)/5, b + (b-a)/5])
	plt.grid(True, which='both')
	plt.legend()
	plt.title("Grafico das funções")
	plt.xlabel('Eixo $t$')
	plt.ylabel('Eixo $y$')

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

'''
def img2(a, b, funcoes, raiz, p0, algorit, number):
	
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

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

'''
def img3(x, w, fs, y, algorit, number): # Para mostrar na tela a imagem
	return img1(x, w, fs, y, algorit, number)

def img4(funcoes, raiz, p0, p1, algorit, number): # Para mostrar na tela a imagem
	
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

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

def img5(funcoes, raiz, p0, p1, algorit, number): # Para mostrar na tela a imagem
	
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

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

