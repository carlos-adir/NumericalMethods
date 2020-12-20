# -*- coding: utf-8 -*-
"""
           @file: methods.py
           @date: 19th Decembre 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Methods for interpolate points
"""

import numpy as np


def Lagrange(x, y, X):
    # The calculations
    n = len(x)
    L = []
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (X - x[j]) / (x[i] - x[j])
        L.append(Li)
    YL = 0
    for i in range(n):
        YL += L[i] * y[i]
    return YL


def Hermite(x, y, y_, X):
    # x, y, y_ are the points that we know
    # X are the positions where we want to evaluate

    n = len(x) - 1
    Q = np.zeros((2 * (n + 1), 2 * (n + 1)))
    Qs = np.zeros(2 * (n + 1))
    z = np.zeros(2 * (n + 1))
    for i in range(n + 1):
        z[2 * i] = x[i]
        z[2 * i + 1] = x[i]
        Q[2 * i][0] = y[i]
        Q[2 * i + 1][0] = y[i]
        Q[2 * i + 1][1] = y_[i]
        if i != 0:
            Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / \
                (z[2 * i] - z[2 * i - 1])
    for i in range(2, 2 * (n + 1)):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])

    for i in range(2 * (n + 1)):
        Qs[i] = Q[i][i]

    multi = 1
    YH = Qs[0]
    for i in range(n):
        multi *= X - x[i]
        YH += Qs[2 * i + 1] * multi
        multi *= X - x[i]
        YH += Qs[2 * i + 2] * multi
    multi *= X - x[-1]
    YH += Qs[2 * n + 1] * multi

    return YH


def SplineLinear(x, y, X):
    """
    Spline Linear is a Spline of degree 1, which for each value of xi,
    the position yi is known, and f(x) is a C-0 class function(continuous).
    The conditions is that:
        * f(x) = fi(x)   for x in [xi, xi+1]
        * fi(x) = ? + ?*x
        * f(x) is continuous (f is C-0 class function)
        * f(xi) = yi
    """
    n = len(x) - 1
    a = np.zeros(n + 1)
    b = np.zeros(n + 1)

    print("x[1:] = " + str(x[1:]))
    print("x[:n] = " + str(x[:n]))
    h = x[1:] - x[:n]
    a[:] = y[:]
    da = a[1:] - a[:n]

    for i in range(n):
        b[i] = da[i] / h[i]

    # return (x, a, b)

    YS = 0
    for i in range(n):
        bol = (x[i] <= X) * (X < x[i + 1])
        dX = X - x[i]
        YSi = a[i]
        YSi += b[i] * dX
        YS += bol * YSi
    if type(X) == np.ndarray:
        if x[-1] == X[-1]:
            YS[-1] = a[-1]
    return YS


def SplineQuad(x, y, X, y__=0):
    """
    Spline Quadratic is a Spline of degree 2, which for each value of xi,
    the position yi is known, and f(x) is a C-1 class function.
    The conditions is that:
        * f(x) = fi(x)   for x in [xi, xi+1]
        * fi(x) = ? + ?*x + ?*x^2
        * f'(x) is continuous (f is C-1 class)
        * f(xi) = yi
    The boundary conditions are:
        y0__ = f''(x0), the second derivate in the frist point
    """
    n = len(x) - 1
    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    c = np.zeros(n)

    h = x[1:] - x[:n]
    a[:] = y[:]
    da = y[1:] - y[:n]

    c[0] = y__
    b[0] = da[0] / h[0] - c[0] * h[0]
    for i in range(n):
        b[i + 1] = 2 * da[i] / h[i] - b[i]
    for i in range(n):
        c[i] = (b[i + 1] / h[i]) - da[i] / (h[i]**2)
    # After here, we have already the values of [a, b, c] calculated
    # return (x, a, b, c)

    YS = 0
    for i in range(n):
        bol = (x[i] <= X) * (X < x[i + 1])
        dX = X - x[i]
        YSi = a[i]
        YSi += b[i] * dX
        YSi += c[i] * dX**2
        YS += bol * YSi
    if type(X) == np.ndarray:
        if x[-1] == X[-1]:
            YS[-1] = a[-1]
    return YS


def SplineCubic(x, y, X, y0__=0, yn__=0):
    """
    Spline Cubic is a Spline of degree 3, which for each value of xi,
    the position yi is known, and f(x) is a C-2 class function.
    The conditions is that:
        * f(x) = fi(x)   for x in [xi, xi+1]
        * fi(x) = ? + ?*x + ?*x^2 + ?*x^3
        * f''(x) is continuous (f is C-2 class function)
        * f(xi) = yi
    The boundary conditions are:
        y0__ = f''(x0), the second derivate in the frist point
        yn__ = f''(xn), the second derivate in the last point
    if y0__ = yn__ = 0, we call that spline as "Natural spline"
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
    al[0] = 3 * ((a[1] - a[0]) / h[0] - y0__)
    al[-1] = 3 * (yn__ - (a[-1] - a[-2]) / h[-2])

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


def SplineHermite(x, y, y_, X):
    """
    Hermite's Spline is a Spline of degree 4, which for each value of xi,
    the position yi and the derivable yi_ is known, and f(x) is a C-2 class
    function.
    The conditions is that:
        * f(x) = fi(x)   for x in [xi, xi+1]
        * fi(x) = ? + ?*x + ?*x^2 + ?*x^3 + ?*x^4
        * f''(x) is continuous (f is C-2 class)
        * f(xi) = yi
        * f'(xi) = yi_
    """
    n = len(x) - 1

    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    c = np.zeros(n + 1)
    d = np.zeros(n + 1)
    e = np.zeros(n + 1)

    h = x[1:] - x[:n]
    a[:] = y[:]
    b[:] = y_[:]

    c[0] = 3 * (a[1] - a[0]) / h[0]**2 - (b[1] + 2 * b[0]) / h[0]
    for i in range(n):
        c[i + 1] = c[i]
        c[i + 1] += 3 * (b[i + 1] + b[i]) / h[i]
        c[i + 1] -= 6 * (a[i + 1] - a[i]) / h[i]**2
    for i in range(n):
        d[i] = 4 * (a[i + 1] - a[i]) / h[i]**3
        d[i] -= (b[i + 1] + 3 * b[i]) / h[i]**2
        d[i] -= 2 * c[i] / h[i]
        e[i] = -3 * (a[i + 1] - a[i]) / h[i]**4
        e[i] += (b[i + 1] + 2 * b[i]) / h[i]**3
        e[i] += c[i] / h[i]**2

    # return (x, a, b, c, d, e)

    YS = 0
    for i in range(n):
        bol = (x[i] <= X) * (X < x[i + 1])
        dX = X - x[i]
        YSi = a[i]
        YSi += b[i] * dX
        YSi += c[i] * dX**2
        YSi += d[i] * dX**3
        YSi += e[i] * dX**4
        YS += bol * YSi
    if type(X) == np.ndarray:
        if x[-1] == X[-1]:
            YS[-1] = a[-1]
    return YS
