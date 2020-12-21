# -*- coding: utf-8 -*-
"""
           @file: methods.py
           @date: 21th December 2020
         @author: Carlos Adir (carlos.adir.leite@gmail.com)
    @description: Methods for solving linear systems
"""

import numpy as np
from numpy import linalg as la


def Gauss(A, b):
    """
    Gaussian Elimination with Backward Substitution
    """
    lines, columns = A.shape
    n = lines

    M = np.zeros((n, n + 1))
    M[:, :-1] = A
    M[:, -1] = b

    x = np.zeros(n)
    for i in range(n - 1):
        p = i
        while p < n - 1 and M[p][i] == 0:
            p += 1
        if p != i:
            M[i], M[p] = M[p], M[i]  # swap lines
        if p == n - 1:
            # print("Solution doesn't exist - 1")
            return None
        for j in range(i + 1, n):
            m = M[j][i] / M[i][i]
            M[j] = M[j] - m * M[i]
            # print(M)
    if M[n - 1][n - 1] == 0:
        # print("Solution doesn't exist - 2")
        return None
    x[-1] = M[-1][-1] / M[-1][-2]
    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += M[i][j] * x[j]
        x[i] = (M[i][-1] - soma) / M[i][i]
    return x


def Partial(A, b):
    """
    Gaussian Elimination with Partial Pivoting
    """
    lines, columns = A.shape
    n = lines

    M = np.zeros((n, n + 1))
    M[:, :-1] = A
    M[:, -1] = b

    x = np.zeros(n)
    nrow = np.zeros(n, dtype=type(int))
    for i in range(n):
        nrow[i] = i
    for i in range(n - 1):
        maxim = 0
        p = i
        for j in range(i, n):
            if np.abs(M[nrow[j]][i]) > maxim:
                maxim = np.abs(M[nrow[j]][i])
                p = j
        if M[nrow[p]][i] == 0:
            # print("Solution doesn't exist - 1")
            return None
        if nrow[i] != nrow[p]:
            nrow[i], nrow[p] = nrow[p], nrow[i]  # M troca de linhas
        for j in range(i + 1, n):
            m = M[nrow[j]][i] / M[nrow[i]][i]
            M[nrow[j]] = M[nrow[j]] - m * M[nrow[i]]
            # print(M)
    if M[nrow[-1]][n] == 0:
        # print("Solution doesn't exist - 2")
        return None
    x[-1] = M[nrow[-1]][-1] / M[nrow[-1]][-2]
    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += M[nrow[i]][j] * x[j]
        x[i] = (M[nrow[i]][-1] - soma) / M[nrow[i]][i]
    return x


def Scaled(A, b):
    """
    Gaussian Elimination with Scaled Partial Pivoting
    """
    lines, columns = A.shape
    n = lines

    M = np.zeros((n, n + 1))
    M[:, :-1] = A
    M[:, -1] = b

    x = np.zeros(n)
    nrow = np.zeros(n, dtype=type(int))

    # Only this difference between this algorithm and the precedent
    s = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if s[i] < np.abs(M[i][j]):
                s[i] = np.abs(M[i][j])
        if s[i] == 0:
            return None
    # Until here

    for i in range(n):
        nrow[i] = i
    for i in range(n - 1):
        maximo = 0
        p = i
        for j in range(i, n):
            if np.abs(M[nrow[j]][i]) / s[nrow[j]] > maximo:  # Alteracao desse
                maximo = np.abs(M[nrow[j]][i]) / s[nrow[j]]  # E desse
                p = j

        if M[nrow[p]][i] == 0:
            # print("Solution doesn't exist - 1")
            return None
        if nrow[i] != nrow[p]:
            nrow[i], nrow[p] = nrow[p], nrow[i]  # M troca de linhas
        for j in range(i + 1, n):
            m = M[nrow[j]][i] / M[nrow[i]][i]
            M[nrow[j]] = M[nrow[j]] - m * M[nrow[i]]
            # print(M)
    if M[nrow[-1]][n] == 0:
        # print("Solution doesn't exist - 2")
        return None
    x[-1] = M[nrow[-1]][-1] / M[nrow[-1]][-2]
    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += M[nrow[i]][j] * x[j]
        x[i] = (M[nrow[i]][-1] - soma) / M[nrow[i]][i]
    return x


def LUFactorization(A):
    """
    LU Factorization
    This algorithm is good if you have always the same matrix A, and with different configurations of b.

    """
    lines, columns = A.shape
    n = lines

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    if A[0, 0] == 0:
        # Impossible factorization
        return None, None
    L[0, 0] = A[0, 0]

    U[0] = A[0] / L[0, 0]
    L[:, 0] = A[:, 0] / U[0, 0]

    for i in range(1, n - 1):
        soma = 0
        for k in range(i):
            soma += L[i, k] * U[k, i]
        L[i, i] = A[i, i] - soma
        U[i, i] = 1
        if L[i, i] == 0:
            # Impossible factorization
            return None, None

        for j in range(i + 1, n):
            soma = 0
            for k in range(i):
                soma += L[i, k] * U[k, j]
            U[i, j] = (A[i, j] - soma) / L[i, i]
            soma = 0
            for k in range(i):
                soma += L[j, k] * U[k, i]
            L[j, i] = (A[j, i] - soma) / U[i, i]
    soma = 0
    for k in range(n - 1):
        soma += L[-1, k] * U[k, -1]
    L[-1, -1] = (A[-1, -1] - soma)
    U[-1, -1] = 1
    if L[-1, -1] == 0:
        # Impossible, matrix A is singular
        return None, None
    return L, U

def solvewithLU(L, U, b):

    # Now that A * x = b
    # and A = L * U
    # So, L*U*x = b is equal to
    #   L*y = b
    #   U*x = y
    # So, we find frist y and after that x
    # Now, it's solve using
    if L is None:  # If it couldn't decompose A in LU method
        return None
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        soma = 0
        for j in range(i):
            soma += L[i, j] * y[j]
        y[i] = (b[i] - soma) / L[i, i]

    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]
        x[i] = (y[i] - soma) / U[i, i]

    return x
