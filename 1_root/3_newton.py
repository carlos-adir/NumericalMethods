# -*- coding: utf-8 -*-
"""
           @file: 3_newton.py
           @date: 19th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Newtons's Method
"""


from methods import Newton


def f1(x):
    return x**2 - 3


def f1_(x):  # Derivate of f1
    return 2 * x


def f2(x):
    return x**2 - 2 * x - 4


def f2_(x):  # Derivate of f2
    return 2 * x - 2


def f3(x):
    return x**3 + 4 * x**2 - 10


def f3_(x):  # Derivate of f3
    return 3 * x**2 + 8 * x


def get_example(number):
    if number == 1:
        p0 = 1.5
        f = f1    # f(x) = x^2 - 3
        f_ = f1_  # f'(x) = 2x
        tol = 1e-5
        nmax = 10
    elif number == 2:
        p0 = 3
        f = f2    # f(x) = x^2 - 2x - 4
        f_ = f2_  # f'(x) = 2x - 2
        tol = 1e-5
        nmax = 10
    elif number == 3:
        p0 = 1.5
        f = f3    # f(x) = x^3 + 4x^2 - 10
        f_ = f3_  # f_(x) = 3*x^2 + 8x
        tol = 1e-5
        nmax = 10
    else:
        raise Exception("Exemple number not found")
    return p0, f, f_, nmax, tol


if __name__ == "__main__":

    number = 1  # The example number we want to test
    p0, f, f_, nmax, tol = get_example(number)
    n, error, r = Newton(p0, f, f_, nmax, tol)

    print("root = %.5f" % r)
    print("inter = [%d/%d]" % ((n, nmax)))
    print("error = %.1e" % error)
    print("toler = %.1e" % tol)
    print("error/tol = %.1e" % (error / tol))
