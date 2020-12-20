# -*- coding: utf-8 -*-
"""
           @file: 3_taylor3.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Taylor's method order 3
"""


from methods import Taylor3
from interpolation import SplineCubic
import numpy as np
import matplotlib.pyplot as plt


def f1(t, y):
    return y - t**2 + 1


def f1_(t, y):
    return f1(t, y) - 2 * t


def f1__(t, y):
    return f1_(t, y) - 2


def y1(t):
    return -0.5 * np.exp(t) + t**2 + 2 * t + 1


def get_example(number):
    if number == 1:
        f = f1
        f_ = f1_
        f__ = f1__
        a, b, c = 0, 2, 0.5  # The interval and initial value
        n = 10  # The number of segments
    else:
        raise Exception("Exemple number not found: Number = " + str(number))
    return a, b, c, n, f, f_, f__


def exact_solution(number):
    if number == 1:
        y = y1
    else:
        raise Exception("Exemple number not found: Number = " + str(number))
    return y


if __name__ == "__main__":
    number = 1
    a, b, c, n, f, f_, f__ = get_example(number)
    x, w, w_ = Taylor3(a, b, c, n, f, f_, f__)
    y = exact_solution(number)

    print("w_ = " + str(w_))

    x_plot = np.linspace(a, b, 1024)
    # w_plot = SplineQuad(x, w, x_plot)
    w_plot = SplineCubic(x, w, x_plot, y0_=w_[0], yn_=w_[-1])

    if y is not None:
        plt.plot(x_plot, y(x_plot), label="exact solution",
                 color="g", ls="dotted")
    plt.scatter(x, w, label="numerical solution", color="b", marker=".")
    plt.plot(x_plot, w_plot, label="numerical solution interpoled",
             color="b", ls="dashed")
    plt.legend()
    plt.title("Taylor's Method order 3")
    plt.show()
