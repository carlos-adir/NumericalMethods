# -*- coding: utf-8 -*-
"""
           @file: 4_LU.py
           @date: 21th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
    @description: LU decomposition solution
"""


from methods import LUFactorization, solvewithLU
from inputs import get_example, exact_solution


if __name__ == "__main__":
    number = 1
    A, b = get_example(number)
    print("A = ")
    print(A)
    print("b = ")
    print(b)
    L, U = LUFactorization(A)
    x_numer = solvewithLU(L, U, b)
    x_exact = exact_solution(number)

    print("x_numer = " + str(x_numer))
    print("x_exact = " + str(x_exact))
