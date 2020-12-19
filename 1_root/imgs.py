import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt

def get(algorit, number):
	if algorit == 1:
		img = lambda a, b, funcoes, raiz: img1(a, b, funcoes, raiz, algorit, number)
	elif algorit == 2:
		img = lambda a, b, funcoes, raiz, p0: img2(a, b, funcoes, raiz, p0, algorit, number)
	elif algorit == 3:
		img = lambda funcoes, raiz, p0: img3(funcoes, raiz, p0, algorit, number)
	elif algorit == 4:
		img = lambda funcoes, raiz, p0, p1: img4(funcoes, raiz, p0, p1, algorit, number)
	elif algorit == 5:
		img = lambda funcoes, raiz, p0, p1: img5(funcoes, raiz, p0, p1, algorit, number)
	return img

def img1(a, b, funcoes, raiz, algorit, number):
	'''
	Informações ainda a colocar
	'''
	f = funcoes[0]
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

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

def img2(a, b, funcoes, raiz, p0, algorit, number):
	'''
	Informações ainda a colocar
	'''
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

def img3(funcoes, raiz, p0, algorit, number): # Para mostrar na tela a imagem
	'''
	Informações ainda a colocar
	'''
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

	plt.savefig("img/" + str(algorit) + "_" + str(number) + '.png')

	plt.show()

def img4(funcoes, raiz, p0, p1, algorit, number): # Para mostrar na tela a imagem
	'''
	Informações ainda a colocar
	'''
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
	'''
	Informações ainda a colocar
	'''
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


