def f(x):
    return x * 3 - x * 2 + 2


def secanteMod(xi, delta, tol):
    n = 1
    error = 1.0
    print("Esto es metodo de la secante modificado")
    while error >= tol:
        df = (f(xi + delta * xi) - f(xi)) / (delta * xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return
        else:
            print(xi)
            print(f(xi))
            print(df)
            # x(i+1) = x(i) - f(x) / f'(x)
            x_new = xi - f(xi) / df
            error = abs(x_new - xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, x_new, f(x_new), error))
            xi = x_new
            n += 1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi


xi = -20
tol = 1e-4
delta = .1
secanteMod(xi, delta, tol)
