# -*- coding: utf-8 -*-
"""
           @file: 6_heun.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Heun's Method, or Runge Kutta order 3
"""


from methods import Heun
from interpolation import SplineCubic
from inputs import get_example, exact_solution
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    number = 1
    a, b, c, n, f = get_example(number)
    x, w, w_ = Heun(a, b, c, n, f)
    y = exact_solution(number)

    x_plot = np.linspace(a, b, 1024)
    w_plot = SplineCubic(x, w, x_plot, y0_=w_[0], yn_=w_[-1])

    if y is not None:
        plt.plot(x_plot, y(x_plot), label="exact solution",
                 color="g", ls="dotted")
    plt.scatter(x, w, label="numerical solution", color="b", marker=".")
    plt.plot(x_plot, w_plot, label="numerical solution interpoled",
             color="b", ls="dashed")
    plt.legend()
    plt.title("Heun's method")
    plt.show()
