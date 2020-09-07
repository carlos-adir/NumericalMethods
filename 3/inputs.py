import numpy as np
import sympy as sp
import auxiliar

limites = [	[0, 8],\
			[0, 8],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0, 9],\
			[0, 9],\
			[0, 9],\
			[0, 9]]

def get(algorithm, number):
	limite = limites[algorithm-1]
	if number < limite[0]:
		number = limite[0]
	if number > limite[1]:
		number = limite[1]

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

def master(number):
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
	elif number == 9:
		f 	= sp.cos(5*t)*sp.sin(3*t)
		n 	= 17
		a, b = 0, 2
		x   = np.linspace(a, b, n)
	return f, t, x

def in1(number):
	f, t, x = master(number)
	feval	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	flatex	= "$f(t) = " + aux.toLaTeX(f)
	f		= aux.Funcao(feval, flatex)
	y		= f.e(x)
	return x, y, f 	# x e y são arrays, que indicam os pontos

def in2(number):
	f, t, x = master(number)
	f_		= sp.diff(f, t)
	feval	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	flatex	= "$f(t) = " + aux.toLaTeX(f)
	f_eval	= sp.lambdify(t, f_, "numpy") 			# Transform the function to lambdify
	f_latex	= "$f'(t) = " + aux.toLaTeX(f_)
	f		= aux.Funcao(feval, flatex)
	f_		= aux.Funcao(f_eval, f_latex)
	y		= f.e(x)
	y_		= f_.e(x)
	return x, y, y_, f, f_

def in7(number):
	return in1(number)

def in8(number):
	return in1(number)

def in9(number):
	return in1(number)

def in10(number):
	f, t, x = master(number)
	f_ 		= sp.diff(f, t)
	f_ 		= sp.lambdify(t, f_, "numpy")
	FP		= np.array((f_(x[0]), f_(x[-1])))

	feval	= sp.lambdify(t, f, "numpy") 			# Transform the function to lambdify
	flatex	= "$f(t) = " + aux.toLaTeX(f)
	f		= aux.Funcao(feval, flatex)
	y		= f.e(x)
	return x, y, f, FP
