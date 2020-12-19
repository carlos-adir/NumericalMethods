# -*- coding: utf-8 -*-
"""
           @file: 1_retangular.py
           @date: 19th Decembre 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
          @title: Retangular integration - Constant
"""


from methods import Retangular
import numpy as np


def f1(x):
    return 1 / x


def f2(x):
    return 1 / (x + 4) + x


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


def f9(x):
    return np.sin(2 * x)


def get_example(number):
    if number == 1:
        f = f1  # f(x) = 1/x
        n = 10
        a, b = 2, 4
        # I = ln(b) - ln(a) = ln(b/a)
        # I0 = ln(2) = 0.693147181
    elif number == 2:
        f = f2  # f(x) = x + 1/(x+4)
        n = 10
        a, b = -3, 0
        # I = (b^2 - a^2)/2 + ln(b + 4) - ln(a+4)
        # I0 = ln(4) - 9/2 = -3.11370564
    elif number == 3:
        f = f3  # f(x) = e^(2x) * cos(3x)
        n = 10
        a, b = 0, 0.6
        # I = (e^(2b)*(3sin(3b)+2cos(3b))-e^(2a)*(3sin(3a)+2cos(3a)))/13
        # I0 = (1/13)*(e^1.2 * (3sin(1.8)+2cos(1.8)) -2)
        #    = 0.476245304568719
    elif number == 4:
        f = f4  # f(x) = cos(x)
        n = 10
        a, b = 0, 0.9
        # I = sin(b) - sin(a)
        # I0 = sin(0.9) = 0.78332690962748
    elif number == 5:
        f = f5  # f(x) = sqrt(1+x)
        n = 10
        a, b = 0, 0.9
        # I = (2/3)*( (1+b)^(3/2) - (1+a)^(3/2) )
        # I0 = (2/3)*( 1.9^1.5 - 1) = 1.0793128419314
    elif number == 6:
        f = f6  # f(x) = e^x
        n = 10
        a, b = 0, 0.9
        # I = e^b - e^a
        # I0 = e^0.9 - 1 = 1.4596031111569499
    elif number == 7:
        f = f7  # f(x) = cos(5x)
        n = 10
        a, b = 1, 2
        # I = (sin(5b)-sin(5a))/5
        # I0 = (sin(10)-sin(5))/5 = 0.08298063275475373
    elif number == 8:
        f = f8  # f(x) = cos(5x) sin(3x)
        n = 10
        a, b = 1, 2
        # I = (8cos^2(b) - cos(8b) - 8cos^2(a) + cos(8a))/16
        # I0 = -0.00861423067194423
    elif number == 9:
        f = f9  # f(x) = sin(2x)
        n = 10
        a, b = 0, 8
        # I = (cos(2a)-cos(2b))/2
        # I0 = 0.9788297401616923
    else:
        raise Exception("Exemple number not found")
    return f, a, b, n


if __name__ == "__main__":
    number = 7
    f, a, b, n = get_example(number)
    x, y, I = Retangular(f, a, b, n)

    print("Example Number %d" % number)
    print("n = " + str(n))
    print("I = " + str(I))
