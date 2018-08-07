import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt
#import interpolacao

def get(algorit, number):
	if algorit == 1:
		img = lambda x, w, fs, y: img1(x, w, fs, y, algorit, number) # Done
	elif algorit == 2:
		img = lambda x, w, fs, y: img2(x, w, fs, y, algorit, number) # Done
	elif algorit == 3:
		img = lambda x, w, fs, y: img3(x, w, fs, y, algorit, number) # Done
	return img
	
def img1():
	pass

def img2(a, b, funcoes, raiz, p0, algorit, number):
	return img1(x, w, fs, y, algorit, number)

def img3(x, w, fs, y, algorit, number): # Para mostrar na tela a imagem
	return img1(x, w, fs, y, algorit, number)
