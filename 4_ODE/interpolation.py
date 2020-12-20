# -*- coding: utf-8 -*-
"""
           @file: interpolation.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Interpolation Method for use after find EDO solutions
"""


import numpy as np


def SplineCubic(x, y, X, y0_=0, yn_=0):
    """
    Spline Cubic is a Spline of degree 3, which for each value of xi,
    the position yi is known, and f(x) is a C-2 class function.
    The conditions is that:
        * f(x) = fi(x)   for x in [xi, xi+1]
        * fi(x) = ? + ?*x + ?*x^2 + ?*x^3
        * f''(x) is continuous (f is C-2 class function)
        * f(xi) = yi
    The boundary conditions are:
        y0_ = f'(x0), the second derivate in the frist point
        yn_ = f'(xn), the second derivate in the last point
    if y0_ = yn_ = 0, we call that spline as "Natural spline"
    """
    n = len(x) - 1
    h = x[1:] - x[:n]
    al = np.zeros(n + 1)  # alpha
    l = np.zeros(n + 1)  # diagonal terms
    mu = np.zeros(n + 1)
    z = np.zeros(n + 1)

    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    c = np.zeros(n + 1)
    d = np.zeros(n + 1)

    a[:] = y[:]

    for i in range(1, n):
        al[i] = (3 / h[i]) * (a[i + 1] - a[i]) - \
            (3 / h[i - 1]) * (a[i] - a[i - 1])
    al[0] = 3 * ((a[1] - a[0]) / h[0] - y0_)
    al[-1] = 3 * (yn_ - (a[-1] - a[-2]) / h[-2])

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = al[0] / l[0]

    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (al[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = h[n - 1] * (2 - mu[n - 1])
    z[n] = (al[n] - h[n - 1] * z[n - 1]) / l[n]
    c[n] = z[n]

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j]
        b[j] -= h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # return (x, a, b, c, d)

    YS = 0
    for i in range(n):
        bol = (x[i] <= X) * (X < x[i + 1])
        dX = X - x[i]
        YSi = a[i]
        YSi += b[i] * dX
        YSi += c[i] * dX**2
        YSi += d[i] * dX**3
        YS += bol * YSi
    if type(X) == np.ndarray:
        if x[-1] == X[-1]:
            YS[-1] = a[-1]
    return YS
