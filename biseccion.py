#---------------------------------------------------------------------------
# Solución aproximada para f(x)=0 entre [a, b] por el metodo de la biseccion
# --------------------------------------------------------------------------

from math import *

#Funcion a calcular raiz
def f(x):
    return x**3 + x - 1

#Metodo de Bisección
def biseccion(a, b, t):
    #Validar cambio de signo
    if f(a)*f(b) >= 0:
        print('Intervalo invalido')
        return    
    a_n,b_n,c_n,n = a, b, (a+b)/2,1
    #Iteración hasta hallar la solución correcta o aproximada
    while abs(b_n - a_n)/2 > t:        
        if f(c_n) == 0: print('la solución exacta es: ',c_n,'con ', n, 'iteraciones')
        elif f(a_n)*f(c_n) < 0: b_n = c_n
        else: a_n = c_n
        c_n = (a_n+b_n)/2
        n+=1

    print('la solución aproximada es: {0:16f}, con {1} iteraciones'.format(c_n, n))

biseccion(0, 1, 1e-9)

