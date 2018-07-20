import numpy as np
import sympy as sp
import aux

limites = [	[0, 8],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0, 8]]

def get(algorithm, number):
	if algorithm == 1:
		return lambda : in1(number)
	elif algorithm == 2:
		return lambda : in2(number)
	elif algorithm == 3:
		return lambda : in3(number)
	elif algorithm == 4:
		return lambda : in4(number)
	elif algorithm == 5:
		return lambda : in5(number)
	elif algorithm == 6:
		return lambda : in6(number)
	elif algorithm == 7:
		return lambda : in7(number)
	elif algorithm == 8:
		return lambda : in8(number)
	elif algorithm == 9:
		return lambda : in9(number)
	elif algorithm == 10:
		return lambda : in10(number)

def in1(number):
	# Para o algoritmo 1.py
	# The variables
	limite = limites[1-1] # 1 - 1 porque é o primeiro conjunto de dados,	
						  # mas como nas listas começam em 0, então o primeiro conjutno de dados é 0 
	if number < limite[0]:
		number = limite[0]
	if number > limite[1]:
		number = limite[1]
	if number != 0:
		t	= sp.symbols('t')
		if number == 1:
			f	= 1/t
			x	= np.array((2, 2.75, 4))
		elif number == 2:
			f	= 1/(t+4) + t
			x	= np.array((-3, -1.5, 0))
		elif number == 3:
			f	= sp.exp(2*t)*sp.cos(3*t)
			x	= np.array((0, 0.3, 0.6))
		elif number == 4:
			f	= sp.cos(t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 5:
			f	= sp.sqrt(1+t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 6:
			f	= sp.exp(t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 7:
			f	= sp.cos(5*t)
			x	= np.array((0, 1, 2))
		elif number == 8:
			f	= sp.cos(5*t)*sp.sin(3*t)
			x	= np.array((0, 1, 2))
		feval	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
		flatex	= "$f(t) = " + aux.toLaTeX(f)
		f		= aux.Funcao(feval, flatex)
		y		= f.e(x)
	else:
		x, y = aux.leia_de_arquivo('1.txt')
		f 	 = None
	return x, y, f

'''
def in3():
	# The variables
	t	= sp.symbols('t')
	f	= 1/t
	f_	= sp.diff(f, t)
	f	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	f_	= sp.lambdify(t, f_, "numpy") 			# Transform the function to lambdify

	x	= np.array((2, 3, 4, 5))
	y	= f(x)
	y_	= f_(x)
	p 	= np.array((3.3, 3.7))

	
	return x, y, y_, p, f, f_

def in5():
	t	= sp.symbols('t')
	f	= 1/t
	f	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	
	x	= np.array((2, 3, 4, 5, 6, 7))
	y	= f(x)
	p	= np.array((3.3, 3.7))
	
	return x, y, p, f
	
'''
def in9(number):
	limite = limites[9-1] # 9 - 1 porque é o nono conjunto de dados,	
						  # mas como nas listas começam em 0, então o nono conjutno de dados é 8 
	if number < limite[0]:
		number = limite[0]
	if number > limite[1]:
		number = limite[1]
	if number != 0:
		t	= sp.symbols('t')
		if number == 1:
			f	= 1/t
			x	= np.array((2, 2.75, 4))
		elif number == 2:
			f	= 1/(t+4) + t
			x	= np.array((-3, -1.5, 0))
		elif number == 3:
			f	= sp.exp(2*t)*sp.cos(3*t)
			x	= np.array((0, 0.3, 0.6))
		elif number == 4:
			f	= sp.cos(t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 5:
			f	= sp.sqrt(1+t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 6:
			f	= sp.exp(t)
			x	= np.array((0, 0.6, 0.9))
		elif number == 7:
			f	= sp.cos(5*t)
			x	= np.array((0, 1, 2))
		elif number == 8:
			f	= sp.cos(5*t)*sp.sin(3*t)
			x	= np.array((0, 1, 2))
		feval	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
		flatex	= "$f(t) = " + aux.toLaTeX(f)
		f		= aux.Funcao(feval, flatex)
		y		= f.e(x)
	else:
		x, y = aux.leia_de_arquivo('9.txt')
		f 	 = None
	return x, y, f
