'''


Como usar

Este é um algoritmo para calcular as funcoes interpoladoras para o geogebra
Se eu quero o 1_1.ggb, então eu coloco o = 0
Se eu quero o 2_1.ggb, então eu coloco o = 1
...
Se eu quero o 5_1.ggb, então eu coloco o = 4

'''

n = 3
a = 0
b = 1
o = 4
oldo = o
#f = sqrt(1+cos(x)^2)

if not o > 0:
	o = 1

print("n = " + str(n))
print("a = " + str(a))
print("b = " + str(b))
print("o = " + str(o))
print("h = (b-a)/(" + str(o) + "*n)")
print("f = Function[sqrt(0.25+cos(" + str(2**oldo) + "*x)^2)-exp(-x)/2, a, b]")

for i in range(o*n+1):
	print("t_{" + str(i) + "} = a + h*" + str(i))
	print("T_{" + str(i) + "} = (t_{" + str(i) + "}, 0)")
	print("F_{" + str(i) + "} = (t_{" + str(i) + "}, f(t_{" + str(i) + "}))" )
for i in range(n):
	message = "f_{" + str(i) + "} = Function["
	fun = ""
	for j in range(oldo+1):
		fun += "y(F_{" + str(o*i+j) + "})*(1*"
		for k in range(oldo+1):
			if k != j:
				fun += "(x-t_{" + str(k+o*i) + "})*"
		fun += "1)/(1*"
		for k in range(oldo+1):
			if k != j:
				fun += "(t_{" + str(j+o*i) + "}-t_{" + str(k+o*i) + "})*"
		fun += "1) + "
	fun += "0"
	final   = ", t_{" + str(o*i) + "}, t_{" + str(o*(i+1)) + "}]"
	print(message + fun + final)
for i in range(n):
	print("Integral[f_{" + str(i) + "}, t_{" + str(i*o) + "}, t_{" + str(o*(i+1)) + "}]")
	print("Segment[ T_{" + str(i*o) + "}, F_{"+ str(i*o) +"}]")

