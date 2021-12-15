import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# METODOS ABIERTOS
# Metodo de la biseccion

def f(x, pol):
    return eval(pol)

def graficar_funcion(pol, xr):
    x = np.linspace(-10, 10, 100)
    y = []
    for i in x:
        y.append(f(i, pol))
    
    plt.title("Función")
    plt.plot(x, y)
    plt.plot(xr, 0, marker='o', color='r')
    plt.show()


def biseccion(a, b, tol, pol):
    iter = [1]  # Lista para guardar los iteraciones
    cota_inf = [a] # Lista para guardar la cota inferior
    cota_sup = [b] # Lista para guardar la cota superior
    x = [] # Lista para guardar los valores de x
    fx = [] # Lista para guardar los valores de f(x)
    err = [] # Lista para guardar los errores en %

    x.append(a)
    fx.append(f(a, pol))
    x.append(b)
    fx.append(f(b, pol))
    e = abs((b - a) / 2)
    err.append(e*100)


    while e > tol:
        c = (a + b) / 2
        x.append(c)
        fx.append(f(c, pol))
        if f(a, pol) * f(c, pol) < 0:
            b = c
        else:
            a = c

        cota_sup.append(b)
        cota_inf.append(a)
        e = abs((b - a) / 2)
        err.append(e*100)
        iter.append(iter[-1] + 1)
    return iter, cota_inf, cota_sup, x, fx, err




funcion = 'x**10 -1'
bis = biseccion(0, 1.4, 0.001, funcion)
print(bis[3][-1])
graficar_funcion(funcion, bis[3][-1])
for b in bis:
    print(b)
    print("\n")
