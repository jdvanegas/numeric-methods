from math import *


def f(x):
    return x**3 - x**2 * 2


def df(x):
    return 3 * x**2 - 2 * x


def newton(f, fprima, p0, tol, n):  # Método de Newton
    i = 1
    while i <= n:
        p = p0 - f(p0) / fprima(p0)
        print("Iter = {0:<2}, p = {1:.8f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return
