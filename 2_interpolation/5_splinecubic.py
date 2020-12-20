# -*- coding: utf-8 -*-
"""
           @file: 5_splinecubic.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Cubic Spline Algorithm
"""


from methods import SplineCubic
import numpy as np
from matplotlib import pyplot as plt


def f1(x):
    return 1 / x


def f2(x):
    return x + 1 / (x + 4)


def f3(x):
    return np.exp(2 * x) * np.cos(3 * x)


def f4(x):
    return np.cos(x)


def f5(x):
    return np.sqrt(1 + x)


def f6(x):
    return np.exp(x)


def f7(x):
    return np.cos(5 * x)


def f8(x):
    return np.cos(5 * x) * np.sin(3 * x)


def get_example(number):
    if number == 1:
        f = f1
        [a, b] = [2, 4]
        n = 4
    elif number == 2:
        f = f2
        [a, b] = [-3, 0]
        n = 4
    elif number == 3:
        f = f3
        [a, b] = [0, 0.6]
        n = 4
    elif number == 4:
        f = f4
        [a, b] = [0, 0.9]
        n = 4
    elif number == 5:
        f = f5
        [a, b] = [0, 0.9]
        n = 4
    elif number == 6:
        f = f6
        [a, b] = [0, 0.9]
        n = 4
    elif number == 7:
        f = f7
        [a, b] = [0, 2]
        n = 4
    elif number == 8:
        f = f8
        [a, b] = [0, 2]
        n = 4
    else:
        raise Exception("Exemple number not found")
    x = np.linspace(a, b, n + 1)
    X = np.linspace(a, b, 3 * n + 1)
    x_plot = np.linspace(a, b, 1024)
    y = f(x)
    Y = f(X)
    y_plot = f(x_plot)
    return (x, y), (X, Y), (x_plot, y_plot)


if __name__ == "__main__":
    number = 1
    (x, y), (X, Y), (x_plot, y_plot) = get_example(number)
    YL = SplineCubic(x, y, X)
    YL_plot = SplineCubic(x, y, x_plot)  # For plotting graph

    plt.plot(x_plot, y_plot, label="Function Real", ls="dotted")
    plt.plot(x_plot, YL_plot, label="Function Interpoled", ls="dashed")
    plt.scatter(X, Y, label="Points Exacts")
    plt.scatter(X, YL, label="Points Interpoled")
    plt.scatter(x, y, label="Points Reference")
    plt.title("Cubic Spline")
    plt.legend()
    plt.show()
