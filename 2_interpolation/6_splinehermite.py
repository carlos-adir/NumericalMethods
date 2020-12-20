# -*- coding: utf-8 -*-
"""
           @file: 6_splinehermite.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Hermite's Spline Algorithm
    @description: Hermite's Spline is a Spline of degree 4, which for each
                  value of xi, the position yi and the derivable yi_ is known.
                  The conditions is that:
                    * f(x) = fi(x)   for x in [xi, xi+1]
                    * fi(x) = ? + ?*x + ?*x^2 + ?*x^3 + ?*x^4
                    * f''(x) is continuous (f is C-2 class)
                    * f(xi) = yi
                    * f'(xi) = yi_
"""


from methods import SplineHermite
import numpy as np
from matplotlib import pyplot as plt


def f1(x):
    return 1 / x


def f1_(x):
    return -1 / x**2


def f2(x):
    return x + 1 / (x + 4)


def f2_(x):
    return 1 - 1 / (x + 4)**2


def f3(x):
    return np.exp(2 * x) * np.cos(3 * x)


def f3_(x):
    return np.exp(2 * x) * (2 * np.cos(3 * x) - 3 * np.sin(3 * x))


def f4(x):
    return np.cos(x)


def f4_(x):
    return -np.sin(x)


def f5(x):
    return np.sqrt(1 + x)


def f5_(x):
    return 1 / (2 * np.sqrt(1 + x))


def f6(x):
    return np.exp(x)


def f6_(x):
    return np.exp(x)


def f7(x):
    return np.cos(5 * x)


def f7_(x):
    return -5 * np.sin(5 * x)


def f8(x):
    return np.cos(5 * x) * np.sin(3 * x)


def f8_(x):
    return -5 * np.sin(5 * x) * np.sin(3 * x) + 3 * np.cos(5 * x) * np.cos(3 * x)


def get_example(number):
    if number == 1:
        f = f1
        f_ = f1_
        [a, b] = [2, 4]
        n = 4
    elif number == 2:
        f = f2
        f_ = f2_
        [a, b] = [-3, 0]
        n = 4
    elif number == 3:
        f = f3
        f_ = f3_
        [a, b] = [0, 0.6]
        n = 4
    elif number == 4:
        f = f4
        f_ = f4_
        [a, b] = [0, 0.9]
        n = 4
    elif number == 5:
        f = f5
        f_ = f5_
        [a, b] = [0, 0.9]
        n = 4
    elif number == 6:
        f = f6
        f_ = f6_
        [a, b] = [0, 0.9]
        n = 4
    elif number == 7:
        f = f7
        f_ = f7_
        [a, b] = [0, 2]
        n = 4
    elif number == 8:
        f = f8
        f_ = f8_
        [a, b] = [0, 2]
        n = 4
    else:
        raise Exception("Exemple number not found")
    x = np.linspace(a, b, n + 1)
    X = np.linspace(a, b, 3 * n + 1)
    x_plot = np.linspace(a, b, 1024)
    y = f(x)
    y_ = f_(x)
    Y = f(X)
    y_plot = f(x_plot)
    return (x, y, y_), (X, Y), (x_plot, y_plot)


if __name__ == "__main__":
    number = 8
    (x, y, y_), (X, Y), (x_plot, y_plot) = get_example(number)
    YL = SplineHermite(x, y, y_, X)
    YL_plot = SplineHermite(x, y, y_, x_plot)  # For plotting graph

    plt.plot(x_plot, y_plot, label="Function Real", ls="dotted")
    plt.plot(x_plot, YL_plot, label="Function Interpoled", ls="dashed")
    plt.scatter(X, Y, label="Points Exacts")
    plt.scatter(X, YL, label="Points Interpoled")
    plt.scatter(x, y, label="Points Reference")
    plt.title("Hermite's Spline")
    plt.legend()
    plt.show()
