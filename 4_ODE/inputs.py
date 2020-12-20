# -*- coding: utf-8 -*-
'''
           @file: input.py
           @date: 20th December
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Inputs for use in the ODE problems examples

'''

import numpy as np
from scipy.special import erf


def f1(t, y):
    return y - t**2 + 1


def y1(t):
    return -0.5 * np.exp(t) + t**2 + 2 * t + 1


def f2(t, y):
    return y * np.tan(t) + t - 3


def y2(t):
    return -3 / np.cos(t) + t * np.tan(t) - 3 * np.tan(t) + 1


def f3(t, y):
    return y - t


def y3(t):
    return -0.5 * np.exp(t) + t + 1


def f4(t, y):
    return 2 * y / t + t**2 * np.exp(t)


def y4(t):
    return t**2 * (np.exp(t) - np.exp(1))


def f5(t, y):
    return t * np.exp(3 * t) - 2 * y


def f6(t, y):
    return 1 + (1 - y)**2


def f7(t, y):
    return 1 + y / t


def f8(t, y):
    return (1 + t) / (1 + y)


def f9(t, y):
    return np.exp(- t**2) / np.sqrt(np.pi)


def y9(t):
    # y =
    # The exact solution is something like that
    return (erf(t) + 1) / 2


def get_example(number):
    if number == 1:
        a, b, c = 0, 2, 0.5  # The interval and initial value
        n = 10  # The number of segments
        f = f1  # The function f(t, y)
    elif number == 2:
        a, b, c = 0, 1, -2
        n = 5
        f = f2
    elif number == 3:
        a, b, c = 0, 2, 0.5
        n = 5
        f = f3
    elif number == 4:
        a, b, c = 1, 2, 0
        n = 10
        f = f4
    elif number == 5:
        a, b, c = 0, 1, 0
        n = 20
        f = f5
    elif number == 6:
        a, b, c = 2, 3, 1
        n = 20
        f = f6
    elif number == 7:
        a, b, c = 1, 2, 2
        n = 40
        f = f7
    elif number == 8:
        a, b, c = 1, 2, 2
        n = 20
        f = f8
    elif number == 9:
        a, b, c = -5, 5, 0
        n = 10
        f = f9
    else:
        raise Exception("Exemple number not found: Number = " + str(number))
    return a, b, c, n, f


def exact_solution(number):
    if number == 1:
        y = y1
    elif number == 2:
        y = y2
    elif number == 3:
        y = y3
    elif number == 4:
        y = y4
    elif number == 9:
        y = y9
    else:
        y = None
    return y
