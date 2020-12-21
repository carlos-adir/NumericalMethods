# -*- coding: utf-8 -*-
'''
           @file: input.py
           @date:
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
    @description:

'''

import sympy as sp
import numpy as np

limites = [[1, 9],
           [1, 9]]


def get_example(number):
    if number == 1:
        A = [[1, 1, 0, 3],
             [2, 1, -1, 1],
             [3, -1, -1, 2],
             [-1, 2, 3, -1]]
        b = [4, 1, -3, 4]
        # x = [-1, 2, 0, 1]
    elif number == 2:
        A = [[1, -1, 2, -1],
             [2, -2, 3, -3],
             [1, 1, 1, 0],
             [1, -1, 4, 3]]
        b = [-8, -20, -2, 4]
        # x = [-7, 3, 2, 2]
    elif number == 3:
        A = [[1, 1, 1],
             [2, 2, 1],
             [1, 1, 2]]
        b = [4, 6, 6]
        # x = doesn't exist
    elif number == 4:
        A = [[1, 1, 1],
             [2, 2, 1],
             [1, 1, 2]]
        b = [4, 4, 6]
        # x = doesn't exist
    elif number == 5:
        A = [[4, -1, 1],
             [2, 5, 2],
             [1, 2, 4]]
        b = [8, 3, 11]
        # x = [1, -1, 3]
    elif number == 6:
        A = [[4, 1, 2],
             [2, 4, -1],
             [1, 1, -3]]
        b = [9, -5, -9]
        # x = [1, -1, 3]
    elif number == 7:
        A = [[0.003, 59.14],
             [5.291, -6.13]]
        b = [59.17, 46.78]
        # x = [10, 1]
    elif number == 8:
        A = [[30, 591400],
             [5.291, -6.13]]
        b = [591700, 46.78]
        # x = [10, 1]
    elif number == 9:
        A = [[2.11, -4.21, 0.921],
             [4.01, 10.2, -1.12],
             [1.09, 0.987, 0.832]]
        b = [2.01, -3.09, 4.21]
        # x = [-0.436, 0.430, 5.12]
    else:
        raise Exception("Exemple number not found: Number = " + str(number))
    return np.array(A), np.array(b)


def exact_solution(number):
    if number == 1:
        x = [-1, 2, 0, 1]
    elif number == 2:
        x = [-7, 3, 2, 2]
    elif number == 3:
        x = None  # doesn't have solution
    elif number == 4:
        x = None  # doesn't have solution
    elif number == 5:
        x = [1, -1, 3]
    elif number == 6:
        x = [1, -1, 3]
    elif number == 7:
        x = [10, 1]
    elif number == 8:
        x = [10, 1]
    elif number == 9:
        x = [-0.436, 0.430, 5.12]
    return np.array(x)
