# -*- coding: utf-8 -*-
"""
           @file: 1_gauss.py
           @date: 21th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
    @description: Gaussian Elimination with Backward Substitution
"""


from methods import Gauss
from inputs import get_example, exact_solution


if __name__ == "__main__":
    number = 7
    A, b = get_example(number)
    print("A = ")
    print(A)
    print("b = ")
    print(b)
    x_numer = Gauss(A, b)
    x_exact = exact_solution(number)

    print("x_numer = " + str(x_numer))
    print("x_exact = " + str(x_exact))
