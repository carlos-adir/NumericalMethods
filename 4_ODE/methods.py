# -*- coding: utf-8 -*-
"""
           @file: methods.py
           @date: 20th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Methods for solving Ordinary Differential Equations
"""

import numpy as np


def Euler(a, b, c, n, f):
    """
    # How to use
        x, w, fs = Euler(a, b, c, n, f)
    # Description
        We want to solve a Ordinary Diferential Equation of frist order:
        y'(t) = f(t, y(t))
        with the initial condition y(a) = c
        and interval of interest [a, b]

        And for this we will use the Euler's algorithm
    # Parameters
        float a:    the begin of the interval of interest
        float b:    the end of the interval of interest
        float c:    the initial condition, that is, y(a) = c
        integer n:  the number of intervals, we will get n+1 points, including the 'a' and 'b' points
                    if n = 1, we have only the points 'a' and 'b'
        function f: the function lambda that we will use.
                    We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
    # Return
        numpy.ndarray x:    it's a vector of (n+1) positions, of the positions 't'.
                            x[0] = a
                            x[n] = b
                            x.size = n+1
        numpy.ndarray w:    it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
                            w[0] = y(a) = c
                            w.size = n+1
        numpy.ndarray fs:   it's a vector of (n+1) positions, of the calculated of the function 'f'
                            fs[0] = f(x[0], w[0])
                            fs[i] = f(x[i], w[i])
                            fs[n] = f(x[n], w[n])
                            fs.size = n+1
    # Restrictions
        * a is integer or float
        * b is integer or float
        * c is integer or float
        * n is integer
        * f is a Function
        * b is bigger than a: b > a
        * n is equal or bigger than 1: n >= 1
        * f is a function of 2 arguments
    # Variables locales
        float h:    the step size, the distance between x[i] and x[i+1]
                    in this algorithm the distance will be the same, so, it's a positive constant value
    # Aditional comments
        We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
    """

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)

    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        w[i + 1] = w[i] + h * w_[i]
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_


def Taylor2(a, b, c, n, f, f_):
    """
    # How to use
        x, w, fs = Taylor2(a, b, c, n, f, f_)
    # Description
        We want to solve a Ordinary Diferential Equation of frist order:
        y'(t) = f(t, y(t))
        with the initial condition y(a) = c
        and interval of interest [a, b]

        And for this we will use the Taylors's algorithm or order 2
    # Parameters
        float a:        the begin of the interval of interest
        float b:        the end of the interval of interest
        float c:        the initial condition, that is, y(a) = c
        integer n:      the number of intervals, we will get n+1 points, including the 'a' and 'b' points
                        if n = 1, we have only the points 'a' and 'b'
        function f:     the function lambda that we will use.
                        We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
        function f_:    the function lambda that we will use.
                        f_ = partial f/partial t
    # Return
        numpy.ndarray x:    it's a vector of (n+1) positions, of the positions 't'.
                            x[0] = a
                            x[n] = b
                            x.size = n+1
        numpy.ndarray w:    it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
                            w[0] = y(a) = c
                            w.size = n+1
        numpy.ndarray fs:   it's a vector of (n+1) positions, of the calculated of the function 'f'
                            fs[0] = f(x[0], w[0])
                            fs[i] = f(x[i], w[i])
                            fs[n] = f(x[n], w[n])
                            fs.size = n+1
    # Restrictions
        * a is integer or float
        * b is integer or float
        * c is integer or float
        * n is integer
        * f is a Function
        * ord is integer
        * b is bigger than a: b > a
        * n is equal or bigger than 1: n >= 1
        * f is a function of 2 arguments
        * f_ is a function of 2 arguments
    # Variables locales
        float h:    the step size, the distance between x[i] and x[i+1]
                    in this algorithm the distance will be the same, so, it's a positive constant value
    # Aditional comments
        We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
    """

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)

    def T(x, y):
        return f(x, y) + h * f_(x, y) / 2

    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        Ti = T(x[i], w[i])
        w[i + 1] = w[i] + h * Ti
        w_[i + 1] = f(x[i], w[i])
    return x, w, w_


def Taylor3(a, b, c, n, f, f_, f__):
    """
    # How to use
        x, w, fs = Taylor3(a, b, c, n, f, f_)
    # Description
        We want to solve a Ordinary Diferential Equation of frist order:
        y'(t) = f(t, y(t))
        with the initial condition y(a) = c
        and interval of interest [a, b]

        And for this we will use the Taylors's algorithm or order 2
    # Parameters
        float a:        the begin of the interval of interest
        float b:        the end of the interval of interest
        float c:        the initial condition, that is, y(a) = c
        integer n:      the number of intervals, we will get n+1 points, including the 'a' and 'b' points
                        if n = 1, we have only the points 'a' and 'b'
        function f:     the function lambda that we will use.
                        We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
        function f_:    the function lambda that we will use.
                        f_ = partial f/partial t
        function f__:   the function lambda that we will use.
                        f__ = partial^2 f/partial t^2
    # Return
        numpy.ndarray x:    it's a vector of (n+1) positions, of the positions 't'.
                            x[0] = a
                            x[n] = b
                            x.size = n+1
        numpy.ndarray w:    it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
                            w[0] = y(a) = c
                            w.size = n+1
        numpy.ndarray fs:   it's a vector of (n+1) positions, of the calculated of the function 'f'
                            fs[0] = f(x[0], w[0])
                            fs[i] = f(x[i], w[i])
                            fs[n] = f(x[n], w[n])
                            fs.size = n+1
    # Restrictions
        * a is integer or float
        * b is integer or float
        * c is integer or float
        * n is integer
        * f is a Function
        * ord is integer
        * b is bigger than a: b > a
        * n is equal or bigger than 1: n >= 1
        * f is a function of 2 arguments
        * f_ is a function of 2 arguments
        * f__ is a function of 2 arguments
    # Variables locales
        float h:    the step size, the distance between x[i] and x[i+1]
                    in this algorithm the distance will be the same, so, it's a positive constant value
    # Aditional comments
        We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
    """

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)  # To storage the derivatives

    def T(x, y):
        return f(x, y) + h * f_(x, y) / 2 + h ** 2 * f__(x, y) / 6

    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        Ti = T(x[i], w[i])
        w[i + 1] = w[i] + h * Ti
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_


def ModifiedEuler(a, b, c, n, f):
    """
    w0 = c
    k1 = h*f(ti, wi)
    k2 = h*f(ti + h, wi + k1)
    wi+1 = wi + (k1+k2)/2
    """
    h = (b - a) / n  # The step size
    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)

    x[0] = a
    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        k1 = h * w_[i]
        k2 = h * f(x[i] + h, w[i] + k1)
        w[i + 1] = w[i] + (k1 + k2) / 2
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_


def Midpoint(a, b, c, n, f):
    """
    Runge Kutta Order 2
    w0 = c
    k1 = h * f(ti, wi)
    k2 = h * f(ti+h/2, wi + k1/2)
    wi+1 = wi + k2
    """
    h = (b - a) / n  # The step size
    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)

    x[0] = a
    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        k1 = h * w_[i]
        k2 = h * f(x[i] + h / 2, w[i] + k1 / 2)

        w[i + 1] = w[i] + k2
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_


def Heun(a, b, c, n, f):
    """
    Runge Kutta order 3
    w0 = c
    k1 = h * f(ti, wi)
    k2 = h * f(ti +   h/3, wi +   k1/3)
    k3 = h * f(ti + 2*h/3, wi + 2*k2/3)
    wi+1 = wi + (k1 + 3*k3)/4
    """
    h = (b - a) / n  # The step size
    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)

    x[0] = a
    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        k1 = h * w_[i]
        k2 = h * f(x[i] + h / 3, w[i] + k1 / 3)
        k3 = h * f(x[i] + 2 * h / 3, w[i] + 2 * k2 / 3)

        w[i + 1] = w[i] + (k1 + 3 * k3) / 4
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_


def RungeKutta(a, b, c, n, f):
    """
    # How to use
        x, w, fs = Runge_Kutta(a, b, c, n, f)
    # Description
        We want to solve a Ordinary Diferential Equation of frist order:
        y'(t) = f(t, y(t))
        with the initial condition y(a) = c
        and interval of interest [a, b]

        And for this we will use the Runge Kutta's algorithm of order 4
    # Parameters
        float a:    the begin of the interval of interest
        float b:    the end of the interval of interest
        float c:    the initial condition, that is, y(a) = c
        integer n:  the number of intervals, we will get n+1 points, including the 'a' and 'b' points
                    if n = 1, we have only the points 'a' and 'b'
        function f: the function lambda that we will use.
                    We will call it as 'f(t, y)', and it will return a float value if 't' and 'y' are float
    # Return
        numpy.ndarray x:    it's a vector of (n+1) positions, of the positions 't'.
                            x[0] = a
                            x[n] = b
                            x.size = n+1
        numpy.ndarray w:    it's a vector of (n+1) positions, of approximated value for the solution of the ODE.
                            w[0] = y(a) = c
                            w.size = n+1
        numpy.ndarray fs:   it's a vector of (n+1) positions, of the calculated of the function 'f'
                            fs[0] = f(x[0], w[0])
                            fs[i] = f(x[i], w[i])
                            fs[n] = f(x[n], w[n])
                            fs.size = n+1
    # Restrictions
        * a is integer or float
        * b is integer or float
        * c is integer or float
        * n is integer
        * f is a function lambda
        * b is bigger than a: b > a
        * n is equal or bigger than 1: n >= 1
        * f is a function of 2 arguments
    # Variables locales
        float h:    the step size, the distance between x[i] and x[i+1]
                    in this algorithm the distance will be the same, so, it's a positive constant value
    # Aditional comments
        We could not return the value of 'fs', but if someone wants to do a Hermite's interpolation, it's necessary.
    """

    h = (b - a) / n                                   # The step size
    k = np.zeros(4)

    x = np.linspace(a, b, n + 1)
    w = np.zeros(n + 1)
    w_ = np.zeros(n + 1)
    k = np.zeros(4)

    x[0] = a
    w[0] = c
    w_[0] = f(x[0], w[0])
    for i in range(n):
        k1 = h * w_[i]
        k2 = h * f(x[i] + h / 2, w[i] + h * k1 / 2)
        k3 = h * f(x[i] + h / 2, w[i] + h * k2 / 2)
        k4 = h * f(x[i] + h, w[i] + h * k3)

        w[i + 1] = w[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        w_[i + 1] = f(x[i + 1], w[i + 1])
    return x, w, w_
