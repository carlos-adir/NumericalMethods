# -*- coding: utf-8 -*-
"""
           @file: 4_secant.py
           @date: 19th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Secant Method
"""


from methods import Secant


def f1(x):
    return x**2 - 3


def f2(x):
    return x**2 - 2 * x - 4


def f3(x):
    return x**3 + 4 * x**2 - 10


def get_example(number):
    if number == 1:
        p0, p1 = 1, 2  # The interval, it's suppose
        f = f1  # f(x) = x^2 - 3
        tol = 1e-5
        nmax = 10
    elif number == 2:
        p0, p1 = 2, 4
        f = f2  # f(x) = x^2 - 2x - 4
        tol = 1e-5
        nmax = 10
    elif number == 3:
        p0, p1 = 1, 2
        f = f3  # f(x) = x^3 + 4x^2 - 10
        tol = 1e-5
        nmax = 10
    else:
        raise Exception("Exemple number not found")
    return p0, p1, f, nmax, tol


if __name__ == "__main__":

    number = 1  # The example number we want to test
    p0, p1, f, nmax, tol = get_example(number)
    n, error, r = Secant(p0, p1, f, nmax, tol)

    print("root = %.5f" % r)
    print("inter = [%d/%d]" % ((n, nmax)))
    print("error = %.1e" % error)
    print("toler = %.1e" % tol)
    print("error/tol = %.1e" % (error / tol))
