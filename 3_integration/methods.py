# -*- coding: utf-8 -*-
"""
           @file: methods.py
           @date: 19th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Methods of Numerical Integration
"""


import numpy as np


def Retangular(f, a, b, n):
    Integral = 0
    h = (b - a) / n
    x = np.linspace(a, b, n)
    y = f(x)
    for i in range(n - 1):
        Integral += y[i]
    Integral *= h
    return x, y, Integral


def Trapezoidal(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    y = f(x)
    I0 = y[0] + y[-1]
    I1 = 0
    for i in range(1, n - 1):
        I1 += y[i]
    Integral = h * (2 * I1 + I0) / 2
    return x, y, Integral


def Simpson(f, a, b, n):
    h = (b - a) / (2 * n)
    x = np.linspace(a, b, 2 * n + 1)
    y = f(x)
    I0 = y[0] + y[-1]
    I1 = 0  # sum of f(x_{2i-1})
    I2 = 0  # sum of f(x_{2i})
    for i in range(1, n):
        I1 += y[2 * i - 1]
        I2 += y[2 * i]
    Integral = h * (I0 + 4 * I1 + 2 * I2) / 3
    return x, y, Integral


def Simpson38(f, a, b, n):
    h = (b - a) / (3 * n)
    x = np.linspace(a, b, 3 * n + 1)
    y = f(x)
    I0 = y[0] + y[-1]
    I1 = 0  # sum of f(x_{3i-2})
    I2 = 0  # sum of f(x_{3i-1})
    I3 = 0  # sum of f(x_{3i})
    for i in range(1, n):
        I1 += y[3 * i - 2]
        I2 += y[3 * i - 1]
        I3 += y[3 * i]
    Integral = 3 * h * (I0 + 3 * I1 + 3 * I2 + 2 * I3) / 8
    return x, y, Integral
