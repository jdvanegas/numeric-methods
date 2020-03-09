#Primer parcial metodos numericos

from math import cos, log, e, sin, tan, sqrt


# Definición de la función 'bisección' por iteración
#Metodo de Bisección
def biseccion(f, a, b, t):
    #Validar cambio de signo
    if f(a) * f(b) >= 0:
        print('Intervalo invalido')
        return 0
    a_n, b_n, c_n, n = a, b, (a + b) / 2, 1
    #Iteración hasta hallar la solución correcta o aproximada
    while abs(b_n - a_n) / 2 > t:
        if f(c_n) == 0:
            print('la solución exacta es: ', c_n, 'con ', n, 'iteraciones')
        elif f(a_n) * f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n
        c_n = (a_n + b_n) / 2
        print('Iter {0:.8f}, el valor de c_n es: {1:.8f}'.format(n, c_n))
        n += 1

    print('la solución aproximada es: {0:8f}, con {1} iteraciones'.format(
        c_n, n))
    return c_n


## Ejercicio 01.


# Definición de la función
def f_1(x):
    return x - cos(x)


print("Ejercicio 1 f(x) es: {0:.8f}".format(biseccion(f_1, 0.5, 1, 1e-10)))
print('\n')

## Ejercicio 02.


# Definición de la función 1
def f_2(x):
    return pow((x - 1), 4.5) - 5 * (x - 1) - 0.1


# Definición de la función 2
def g_2(x):
    return (x * log((x + 1))) - 2


print("La solución para f(x) es: {0:.16f}\n\n".format(
    biseccion(f_2, 1, 3, 1e-6)))
print("La solución para g(x) es: {0:.16f}".format(biseccion(g_2, 0, 2, 1e-6)))
print('\n')

## Ejercicio 03.


# Definición del método de Newton-Raphson
def newton(f, fprima, p0, tol, n=100):  # Método de Newton
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


# Definición de la función
def f_3(x):
    return pow(e, -x) - sin(x)


# Definición de la derivada
def df_3(x):
    return pow(e, -x) - cos(x)


newton(f_3, df_3, 2, 1e-3)

## Ejecicio 04.

print('\n')


# Definición del método de la secante
def secante(f, x_old, xi, tol):
    n = 1
    error = 1
    print("Esto es metodo de la secante")
    while error >= tol:
        df = (f(x_old) - f(xi)) / (x_old - xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi) / df
            # x(i+1) = x(i) - f(x) / f'(x)
            x_new = xi - h
            error = abs(x_new - xi)
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(
                n, x_new, f(x_new), error))
            xi = x_new
            n += 1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi


# Definición de la función
def f_4(x):
    return x - (0.5 * tan(x))


print("La solución para f(x) es: {0:.16f}".format(secante(f_4, 1, 3.5, 1e-4)))
print('\n')

# Ejercicio 5

#Definir metodo de punto fijo


def puntofijo(f, p0, tol, n=100):  # Método del punto fijo
    i = 1
    while i <= n:
        p = (f(p0))
        print("Iter = {0:<2}, p = {1:.8f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return


def f_5(x):
    return sqrt(10 / (x + 4))


print("La solución para f(x) es: {0:.16f}".format(puntofijo(f_5, 1, 1e-4)))
