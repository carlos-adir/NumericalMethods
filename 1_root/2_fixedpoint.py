# -*- coding: utf-8 -*-
"""
           @file: 2_fixedpoint.py
           @date: 19th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Fixed Point Method
"""


from methods import FixedPoint
import numpy as np


def f1(x):
    return x**3 + 4 * x**2 - 10


def g1(x):
    return x - f1(x)


def f2(x):
    return x**3 + 4 * x**2 - 10


def g2(x):
    return np.sqrt(4 * x - 10 / x)


def f3(x):
    return x**3 + 4 * x**2 - 10


def g3(x):
    return np.sqrt(10 - x**3) / 2


def f4(x):
    return x**3 + 4 * x**2 - 10


def g4(x):
    return np.sqrt(10 / (4 + x))


def f5(x):
    return x**3 + 4 * x**2 - 10


def g5(x):
    return 2 * (x**3 + 2 * x**2 + 5) / (3 * x**2 + 8 * x)


def get_example(number):
    if number == 1:
        p0 = 1.5
        f = f1  # f(x) = x^3 + 4x^2 - 10
        g = g1  # g(x) = x - f(x)
        tol = 1e-5
        nmax = 10
    elif number == 2:
        p0 = 1.5
        f = f2  # f(x) = x^3 + 4x^2 - 10
        g = g2  # g(x) = sqrt(4*t - 10/t)
        tol = 1e-5
        nmax = 10
    elif number == 3:
        p0 = 1.5
        f = f3  # f(x) = x^3 + 4x^2 - 10
        g = g3  # g(x) = sqrt(10-t**3)/2
        tol = 1e-5
        nmax = 10
    elif number == 4:
        p0 = 1.5
        f = f4  # f(x) = x^3 + 4x^2 - 10
        g = g4  # g(x) = sqrt(10/(4+t))
        tol = 1e-5
        nmax = 10
    elif number == 5:
        p0 = 1.5
        f = f5  # f(x) = x^3 + 4x^2 - 10
        g = g5  # g(x) = 2(t^3 + 2t^2 + 5)/(3t^2 + 8t)
        tol = 1e-5
        nmax = 10
    else:
        raise Exception("Exemple number not found")
    return p0, g, nmax, tol


if __name__ == "__main__":

    number = 1  # The example number we want to test
    p0, g, nmax, tol = get_example(number)
    n, error, r = FixedPoint(p0, g, nmax, tol)

    print("root = %.5f" % r)
    print("inter = [%d/%d]" % ((n, nmax)))
    print("error = %.1e" % error)
    print("toler = %.1e" % tol)
    print("error/tol = %.1e" % (error / tol))
