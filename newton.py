from math import *


def f(x):
    return x**3 - x**2 * 2


def df(x):
    return 3 * x**2 - 2 * x


def newton(x):
    error, n = 1, 1
    while error >= tol:
        if (df(x) == 0):
            print('Derivada nula')
            return
        else:
            h = f(x) / df(x)
            x_new = x - f(x) / df(x)
