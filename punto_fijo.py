import numpy as np
# metodo de punto fijo
def punto_fijo(xo, tol, pol):

    f = lambda x: eval(pol)
    g = lambda x: eval(str(pol) + "+x")

    tol = int(tol)
    x = [xo]
    gx = [g(xo)]
    fx = [f(xo)]
    err = [100]

    while err[-1] > 10**(-1*tol):
        x.append(round(gx[-1], tol+1))
        gx.append(round(g(x[-1]), tol+1))
        fx.append(round(f(x[-1]), tol+1))
        err.append(round(abs((x[-1]-x[-2])/x[-1]), tol+1))

    return x, gx, fx, err

pf = punto_fijo(1, 4, "np.exp(-x)-x")
print(pf)
print(pf[0][-1])