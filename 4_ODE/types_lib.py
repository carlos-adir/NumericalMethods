import sympy as sp
import numpy as np 

class Function:
	def __init__(self, param, f):
		self.__param = param
		self.__f = f
		self.__lambda = None
	def __create_lambda(self):
		self.__lambda = sp.lambdify(self.param, self.symb, "numpy")
	def __lambda_function(self, *argv):
		if self.__lambda == None:
			self.__create_lambda()
		return self.__lambda(*argv)

	@property
	def t(self):
		if type(self.__param) is tuple:
			return self.__param[0]
		else:
			return self.__param
	@property
	def y_(self):
		return sp.diff(self.y, self.t)
	@property
	def y(self):
		if not type(self.param) is tuple:
			raise ValueError("Nao existe a variavel y!") 
		return self.__param[1]
	@property
	def param(self):
		return self.__param
	@property
	def symb(self):
		return self.__f
	@property
	def argcount(self):
		if self.__lambda == None:
			self.__create_lambda()
		return self.__lambda.__code__.co_argcount

	def simplify(self):
		self.__f = sp.simplify(self.__f)
	def __call__(self, *argv):
		return self.__lambda_function(*argv)
	def __str__(self):
		return str(self.__f)
	def __add__(self, element):
		if type(element) != Function:
			return Function(self.param, element + self.symb)
		else:
			if element.param != self.param:
				raise ValueError("Nao foi possivel somar, os paramentros das duas funcoes sao diferentes")
			else:
				return Function(self.param, self.symb + element.symb)
	def __radd__(self, other):
		return self.__add__(other)
	def __sub__(self, element):
		if type(element) != Function:
			return Function(self.param, element - self.symb)
		else:
			if element.param != self.param:
				raise ValueError("Nao foi possivel somar, os paramentros das duas funcoes sao diferentes")
			else:
				return Function(self.param, element.symb - self.symb)
	def __rsub__(self, element):
		if type(element) != Function:
			return Function(self.param, - self.symb + element )
		else:
			if element.param != self.param:
				raise ValueError("Nao foi possivel somar, os paramentros das duas funcoes sao diferentes")
			else:
				return Function(self.param, - self.symb + element.symb)
	def __mul__(self, element):
		if type(element) != Function:
			return Function(self.param, element * self.symb)
		else:
			if element.param != self.param:
				raise ValueError("Nao foi possivel multiplicar, os paramentros das duas funcoes sao diferentes")
			else:
				return Function(self.param, self.symb * element.symb)
	def __rmul__(self, other):
		return self.__mul__(other)


if __name__ == "__main__":
	t = sp.symbols('t')
	y = sp.symbols('y', cls = sp.Function)(t) 
	f = t**2 + 1 + 2*y

	k = Func()