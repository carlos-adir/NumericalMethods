
from sympy import *

'''
V, I = symbols("V I", cls=Function)
RC, t, C, Vs, L, R1, V0, I0 = symbols("RC t C Vs L R1 V0 I0")
system = [Eq(V(t).diff(t), -1/RC*V(t) + I(t)/C), \
		  Eq(I(t).diff(t), -R1/L*I(t) - 1/L*V(t) + Vs/L)]
print system
ics = {V(0): V0, I(0): I0}
print ics
print V(t)
k = dsolve(system, (V(t), I(t)))
print(k)
'''

y 	= symbols("f", cls = Function)
t 	= symbols("t")
f 	= y(t) - t**2 + 1
eq 	= Eq(y(t).diff(t), f)
cle = {y(1): 1}
sol = dsolve(eq, y(t), cls = cle)
print sol

'''
import numpy as np
from sympy import *
from IPython.display import *
import matplotlib.pyplot as plt
init_printing(use_latex=True)
var('a b t k C1')
u = Function("u")(t)
de = Eq(u+u.diff(t) * k)
des = dsolve(de,u).subs(C1,1)
print des
'''