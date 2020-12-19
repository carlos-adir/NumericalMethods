
import numpy as np


def Bisection(a, b, f, nmax=30, tol=1e-6):
    """

    """
    n = 0
    fa = f(a)  # We calcule the left point
    fb = f(b)  # We calcule the right point
    if fa * fb > 0:
        msg = "Impossible find root: f(a) and f(b) have the same signal"
        raise Exception(msg)
    while n < nmax:
        p = (a + b) / 2  # The middle point of the interval [a, b]
        fp = f(p)  # The value of f in the middle of the interval [a, b]
        n += 1
        if fp == 0:  # If the root is already in the point p:
            break
        if (b - a) / 2 < tol:  # If the tolerance is satisfazed
            break
        if fa * fp > 0:
            # If fa and fp have the same signal, we get the right interval
            # [a, b] = [p, b]
            a = p
            fa = fp
        else:
            # If fa and fp have the same signal, we get the right interval
            # [a, b] = [a, p]
            b = p
            fb = fp
    error = (b - a) / 2
    return n, error, p


def FixedPoint(p0, g, nmax=20, tol=1e-6, tolmax=1e+6):
    """
    """
    n = 0
    while n < nmax:
        p = g(p0)
        error = np.abs((p - p0) / 2)
        n += 1
        if error > tolmax:
            break
        if error < tol:
            break
        p0 = p
    return n, error, p


def Newton(p0, f, f_, nmax=10, tol=1e-6, tolmax=1e+6):
    """

    """
    n = 0
    while n < nmax:
        fp = f(p0)
        dfp = f_(p0)
        p = p0 - fp / dfp
        n += 1
        if abs(p - p0) < tol or abs(p - p0) > tolmax:
            error = (p - p0) / 2
            break
        p0 = p
    return n, error, p


def Secant(p0, p1, f, nmax=10, tol=1e-6):
    """

    """
    n = 1
    q0 = f(p0)
    q1 = f(p1)
    while n < nmax:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        n += 1
        if abs(p - p1) < tol:
            break
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    error = (p - p1) / 2
    return n, error, p


def FalsePosition(p0, p1, f, nmax=10, tol=1e-6):
    """

    """
    n = 0
    q0 = f(p0)
    q1 = f(p1)
    while n < nmax:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        n += 1
        if abs(p - p1) < tol:
            break

        # Apenas a partir daqui que diferencia do metodo da secante
        q = f(p)
        if q * q1 < 0:
            p1 = p
            q1 = q
    error = (p - p1) / 2
    return n, error, p
