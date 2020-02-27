def f(x):
    return x**3 - x**2 + 2


def secanteMod(xi, delta, tol):
    n = 1
    error = 1
    print("Esto es metodo de la secante modificado")
    while error >= tol:
        df = (f(xi + delta * xi) - f(xi)) / (delta * xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi) / df
            xNew = xi - h
            error = abs(xNew - xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, xNew, f(xNew), error))
            xi = xNew
            n += 1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi


xi = -20
delta = .1
tol = 1e-4
secanteMod(xi, delta, tol)