#---------------------------------------------------------------------------
# Solución aproximada para f(x)=0 entre [a, b] por el metodo de la biseccion
# --------------------------------------------------------------------------

from math import log


#Funcion a calcular raiz
def f(x):
    return log(x**2)


#Metodo de Regla falsa
def falsa(a, b, t):
    #Validar cambio de signo
    if f(a) * f(b) >= 0:
        print('Intervalo invalido')
        return
    a_n, b_n, c_n, n, delta = a, b, (a + b) / 2, 1, 1
    #Iteración hasta hallar la solución correcta o aproximada
    while delta > t:
        c_n = b_n - (f(b_n) * (b_n - a_n) / (f(b_n) - f(a_n)))
        if f(c_n) == 0:
            print('la solución exacta es: ', c_n, 'con ', n, 'iteraciones')
        elif f(a_n) * f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n

        c_n_new = b_n - (f(b_n) * (b_n - a_n) / (f(b_n) - f(a_n)))
        delta = (c_n_new - c_n)
        print(
            'el valor de a_n es: {0:8f}, el valor de b_n es: {1:8f}, el valor de c_n es: {2:8f}'
            .format(a_n, b_n, c_n))
        n += 1

    print('la solución aproximada es: {0:8f}, con {1} iteraciones'.format(
        c_n, n))


falsa(0.5, 2, 1e-5)
