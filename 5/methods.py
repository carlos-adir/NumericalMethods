#import types # To verify if there is a lambda function
import types_lib # To verify if there is a lambda function
import numpy as np
import sympy as sp

def Euler(a, b, c, n, f):
	'''
		# How to use
			x, w, fs = Euler(a, b, c, n, f)
		# Description
			We want to solve a Ordinary Diferential Equation of frist order:
			y'(t) = f(t, y(t))
			with the initial condition y(a) = c
			and interval of interest [a, b]
			
			And for this we will use the Euler's algorithm
		# Parameters
			float a:	the begin of the interval of interest
			float b:	the end of the interval of interest
			float c:	the initial condition, that is, y(a) = c
			integer n:	the number of intervals, we will get n+1 points, including the 'a' and 'b' points
						if n = 1, we have only the points 'a' and 'b'
			function f:	the function lambda that we will use.
						We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
		# Return
			numpy.ndarray x:	it's a vector of (n+1) positions, of the positions 't'.
								x[0] = a
								x[n] = b
								x.size = n+1
			numpy.ndarray w:	it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
								w[0] = y(a) = c
								w.size = n+1
			numpy.ndarray fs:	it's a vector of (n+1) positions, of the calculated of the function 'f'
								fs[0] = f(x[0], w[0])
								fs[i] = f(x[i], w[i])
								fs[n] = f(x[n], w[n])
								fs.size = n+1
		# Restrictions
			* a is integer or float
			* b is integer or float
			* c is integer or float
			* n is integer
			* f is a Function
			* b is bigger than a: b > a
			* n is equal or bigger than 1: n >= 1
			* f is a function of 2 arguments
		# Variables locales
			float h:	the step size, the distance between x[i] and x[i+1]
						in this algorithm the distance will be the same, so, it's a positive constant value
		# Aditional comments
			We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
	'''

	
	if True: # Here we do the restriction's tests, put 'False' if you don't want to do the tests
		if not ( type(a) is int or type(a) is float or type(a) is np.float64):
			raise TypeError("A variavel 'a' deve ser um número! " + str(type(a)))
		if not ( type(b) is int or type(b) is float or type(b) is np.float64):
			raise TypeError("A variavel 'b' deve ser um número! " + str(type(b)))
		if not ( type(c) is int or type(c) is float or type(c) is np.float64):
			raise TypeError("A variavel 'c' deve ser um número! O tipo de c: " + str(type(c)))
		if not type(n) is int:
			raise TypeError("A variavel 'n' deve ser um inteiro!")
		if not type(f) is types_lib.Function:
			raise TypeError("A variavel 'f' deve ser uma Function!")
		if not b > a:
			raise ValueError("A variável 'b' nao é maior que a variavel 'a'")
		if not n >= 1:
			raise ValueError("A variavel 'n' deve ser positiva")
		if not f.argcount == 2:
			raise ValueError("A funcao 'f' deve ter 2 parametros!")


	h 		= (b-a)/n 
	
	w		= np.zeros(n+1)
	x 		= np.zeros(n+1)
	fs 		= np.zeros(n+1) 							

	x[0]	= a
	w[0] 	= c
	fs[0]	= f(x[0], w[0])

	for i in range(n):
		w[i+1]		= w[i] + h*fs[i]
		x[i+1] 		= a + h*(i+1)
		fs[i+1]		= f(x[i+1], w[i+1])
		
	return x, w, fs



def Taylor(a, b, c, n, f, order):
	'''
		# How to use
			x, w, fs = Taylor(a, b, c, n, f, order)
		# Description
			We want to solve a Ordinary Diferential Equation of frist order:
			y'(t) = f(t, y(t))
			with the initial condition y(a) = c
			and interval of interest [a, b]
			
			And for this we will use the Taylors's algorithm
		# Parameters
			float a:		the begin of the interval of interest
			float b:		the end of the interval of interest
			float c:		the initial condition, that is, y(a) = c
			integer n:		the number of intervals, we will get n+1 points, including the 'a' and 'b' points
							if n = 1, we have only the points 'a' and 'b'
			function f:		the function lambda that we will use.
							We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
			integer order:	the order of the Taylor's algorithm
							if ord = 1, we have teh Euler's methode
		# Return
			numpy.ndarray x:	it's a vector of (n+1) positions, of the positions 't'.
								x[0] = a
								x[n] = b
								x.size = n+1
			numpy.ndarray w:	it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
								w[0] = y(a) = c
								w.size = n+1
			numpy.ndarray fs:	it's a vector of (n+1) positions, of the calculated of the function 'f'
								fs[0] = f(x[0], w[0])
								fs[i] = f(x[i], w[i])
								fs[n] = f(x[n], w[n])
								fs.size = n+1
		# Restrictions
			* a is integer or float
			* b is integer or float
			* c is integer or float
			* n is integer
			* f is a Function
			* ord is integer
			* b is bigger than a: b > a
			* n is equal or bigger than 1: n >= 1
			* f is a function of 2 arguments
			* order is equal or bigger than 1: ord >= 1
		# Variables locales
			float h:	the step size, the distance between x[i] and x[i+1]
						in this algorithm the distance will be the same, so, it's a positive constant value
		# Aditional comments
			We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
	'''


	if True: # Here we do the restriction's tests, put 'False' if you don't want to do the tests
		if not ( type(a) is int or type(a) is float or type(a) is np.float64):
			raise TypeError("A variavel 'a' deve ser um número! " + str(type(a)))
		if not ( type(b) is int or type(b) is float or type(b) is np.float64):
			raise TypeError("A variavel 'b' deve ser um número! " + str(type(b)))
		if not ( type(c) is int or type(c) is float or type(c) is np.float64):
			raise TypeError("A variavel 'c' deve ser um número! O tipo de c: " + str(type(c)))
		if not type(n) is int:
			raise TypeError("A variavel 'n' deve ser um inteiro!")
		if not type(f) is types_lib.Function:
			raise TypeError("A variavel 'f' deve ser uma Function!")
		if not type(order) is int:
			raise TypeError("A variavel 'order' deve ser um inteiro!")
		if not b > a:
			raise ValueError("A variável 'b' nao é maior que a variavel 'a'")
		if not n >= 1:
			raise ValueError("A variavel 'n' deve ser positiva")
		if not f.argcount == 2:
			raise ValueError("A funcao 'f' deve ter 2 parametros!")
		if not order >= 1:
			raise ValueError("A variavel 'order' deve ser pelo menos 1")

		


	h 		= (b-a)/n 									
	
	T 		= 0

	termo	= 1
	df 		= types_lib.Function(f.param, f.symb)
	T 	    = T + df*termo
	for i in range(2, order+1):
		print('df = ' + str(df))
		df = types_lib.Function(f.param, sp.diff(df.symb, df.t).replace(df.y_, f))
		print('df = ' + str(df))
		#df = sp.diff(df, t) + sp.diff(df, y)*f  # Para obtermos a derivada
		termo  *= h/i 							# Para obtermos o fatorial
		print("T = " + str(T))
		T 	    = T + termo*df
		T.simplify()
		print('i = ' + str(i))
	w		= np.zeros(n+1)
	x 		= np.zeros(n+1)
	Ts 		= np.zeros(n+1) 							# Não é necessário, mas se quisermos fazer a interpolação de Hermite, é possível

	x[0]	= a
	w[0] 	= c
	Ts[0]	= T(x[0], w[0])
	for i in range(n):
		w[i+1]		= w[i] + h*Ts[i]
		x[i+1] 		= a + h*(i+1)
		Ts[i+1]		= T(x[i+1], w[i+1])
	return x, w, Ts


def modified_Euler(a, b, c, n, f):
	pass

def midpoint_methode(a, b, c, n, f):
	# It's the same as Runge_Kutta methode of order 2.
	pass

def Runge_Kutta(a, b, c, n, f):
	'''
		# How to use
			x, w, fs = Runge_Kutta(a, b, c, n, f)
		# Description
			We want to solve a Ordinary Diferential Equation of frist order:
			y'(t) = f(t, y(t))
			with the initial condition y(a) = c
			and interval of interest [a, b]
			
			And for this we will use the Runge Kutta's algorithm of order 4
		# Parameters
			float a:	the begin of the interval of interest
			float b:	the end of the interval of interest
			float c:	the initial condition, that is, y(a) = c
			integer n:	the number of intervals, we will get n+1 points, including the 'a' and 'b' points
						if n = 1, we have only the points 'a' and 'b'
			function f:	the function lambda that we will use.
						We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
		# Return
			numpy.ndarray x:	it's a vector of (n+1) positions, of the positions 't'.
								x[0] = a
								x[n] = b
								x.size = n+1
			numpy.ndarray w:	it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
								w[0] = y(a) = c
								w.size = n+1
			numpy.ndarray fs:	it's a vector of (n+1) positions, of the calculated of the function 'f'
								fs[0] = f(x[0], w[0])
								fs[i] = f(x[i], w[i])
								fs[n] = f(x[n], w[n])
								fs.size = n+1
		# Restrictions
			* a is integer or float
			* b is integer or float
			* c is integer or float
			* n is integer
			* f is a function lambda
			* b is bigger than a: b > a
			* n is equal or bigger than 1: n >= 1
			* f is a function of 2 arguments
		# Variables locales
			float h:	the step size, the distance between x[i] and x[i+1]
						in this algorithm the distance will be the same, so, it's a positive constant value
		# Aditional comments
			We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
	'''

	if True: # Here we do the restriction's tests, put 'False' if you don't want to do the tests
		if not ( type(a) is int or type(a) is float or type(a) is np.float64):
			raise TypeError("A variavel 'a' deve ser um número! " + str(type(a)))
		if not ( type(b) is int or type(b) is float or type(b) is np.float64):
			raise TypeError("A variavel 'b' deve ser um número! " + str(type(b)))
		if not ( type(c) is int or type(c) is float or type(c) is np.float64):
			raise TypeError("A variavel 'c' deve ser um número! O tipo de c: " + str(type(c)))
		if not type(n) is int:
			raise TypeError("A variavel 'n' deve ser um inteiro!")
		if not type(f) is types_lib.Function:
			raise TypeError("A variavel 'f' deve ser uma Function!")
		if not b > a:
			raise ValueError("A variável 'b' nao é maior que a variavel 'a'")
		if not n >= 1:
			raise ValueError("A variavel 'n' deve ser positiva")
		if not f.argcount == 2:
			raise ValueError("A funcao 'f' deve ter 2 parametros!")
		

	h 		= (b-a)/n 									# The step size
	w 		= c											# The y values approx
	k 		= np.zeros(4)								# Initial condition of K, does not matter the initial value, only that there are 4 numbers on the list
	
	x 		= np.zeros(n+1)
	w		= np.zeros(n+1)
	fs		= np.zeros(n+1)
	k 		= np.zeros(4)

	x[0]	= a
	w[0] 	= c
	fs[0]	= f(x[0], w[0])
	for i in range(n):
		k[0]	= h*fs[i]
		k[1]	= h*f(x[i]+h/2, w[i]+k[0]/2)
		k[2]	= h*f(x[i]+h/2, w[i]+k[1]/2)
		k[3]	= h*f(x[i]+h, w[i]+k[2])

		w[i+1]	= w[i] + (k[0]+2*k[1]+2*k[2]+k[3])/6
		x[i+1]	= a + h*(i+1)
		fs[i+1] = f(x[i+1], w[i+1])
	return x, w, fs