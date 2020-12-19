import numpy as np
import sympy as sp
import auxiliar

limites = [	[1, 9],\
			[1, 9],\
			[1, 9],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0,0],\
			[0, 0]]

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
		f		= 1/t
		n		= 10
		a, b	= 2, 4
	elif number == 2:
		f		= 1/(t+4) + t
		n		= 10
		a, b 	= -3, 0 
	elif number == 3:
		f		= sp.exp(2*t)*sp.cos(3*t)
		n		= 10
		a, b	= 0, 0.6
	elif number == 4:
		f		= sp.cos(t)
		n		= 10
		a, b	= 0, 0.9 
	elif number == 5:
		f		= sp.sqrt(1+t)
		n		= 10
		a, b	= 0, 0.9
	elif number == 6:
		f		= sp.exp(t)
		n		= 10
		a, b	= 0, 0.9
	elif number == 7:
		f		= sp.cos(5*t)
		n		= 10
		a, b	= 1, 2
	elif number == 8:
		f		= sp.cos(5*t)*sp.sin(3*t)
		n		= 10
		a, b	= 1, 2
	elif number == 9:
		f 		= sp.sin(2*t)
		n		= 10
		a, b	= 0, 8
	return f, t, a, b, n


def in1(number):
	f, t, a, b, n = master(number)
	feval	= sp.lambdify(t, f, "numpy")
	flatex	= "$f(t) = " + aux.toLaTeX(f)
	f		= aux.Funcao(feval, flatex)
	return a, b, n, f

def in2(number):
	a, b, n, f = in1(number)
	return a, b, int(n/1.5), f

def in3(number):
	a, b, n, f = in1(number)
	return a, b, n//2, f

