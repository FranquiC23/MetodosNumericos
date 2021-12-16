import numpy as np
from scipy.misc import derivative

# metodo de newton raphson 
def newton_raphson(x0, tol, pol):

    f = lambda x: eval(pol)

    x = [x0]
    fx = [f(x0)]
    dx = [derivative(f, x0, 0.0001)]
    err = [100]

    while err[-1] > 10**(-1*tol):
        x.append(round(x[-1] - (fx[-1] / dx[-1]), tol+1))
        fx.append(round(f(x[-1]), tol+1))
        dx.append(round(derivative(f, x[-1], 0.0001), tol+1))
        err.append(round(abs((x[-1]-x[-2])/x[-1]), tol+1))
    return x, fx, dx, err

nr = newton_raphson(0, 5, "x**3 - 2*x**2 + x - 3")
print(nr)
print(nr[0][-1])