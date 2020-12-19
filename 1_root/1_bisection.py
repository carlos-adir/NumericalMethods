# -*- coding: utf-8 -*-
'''
           @file: 1_bisection.py
           @date: 19th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Bissection Method
'''


from methods import Bisection
import numpy as np


def f1(x):
    """
    roots = [-sqrt(3), sqrt(3)]
    """
    return x**2 - 3


def f2(x):
    """
    roots = [1-sqrt(5), 1+sqrt(5)]
    """
    return x**2 - 2 * x - 4


def f3(x):
    """
    Only one real root
    roots = [1.36523]  # approximately
    """
    return x**3 + 4 * x**2 - 10


def f4(x):
    """
    Only one real root
    roots = [-1.8414]  # approximately
    """
    return np.exp(x) - x - 2


def get_example(number):
    if number == 1:
        [a, b] = [1, 2]
        f = f1  # f(x) = x^2 - 3
        tol = 1e-5
        nmax = 10
    elif number == 2:
        [a, b] = [2, 4]
        f = f2  # f(x) = x^2 - 2x - 4
        tol = 1e-5
        nmax = 10
    elif number == 3:
        [a, b] = [1, 2]
        f = f3  # f(x) = x^3 + 4x^2 - 10
        tol = 1e-5
        nmax = 10
    elif number == 4:
        [a, b] = [-2, -1]
        f = f4  # f(x) = e^x - x - 2
        tol = 1e-5
        nmax = 100
    else:
        raise Exception("Exemple number not found")
    return [a, b], f, tol, nmax


if __name__ == "__main__":

    number = 2  # The example number we want to test

    [a, b], f, tol, nmax = get_example(number)
    n, error, r = Bisection(a, b, f, nmax, tol)

    print("root = %.5f" % r)
    print("inter = [%d/%d]" % ((n, nmax)))
    print("error = %.1e" % error)
    print("toler = %.1e" % tol)
    print("error/tol = %.1e" % (error / tol))
