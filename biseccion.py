# Metodo de la biseccion
def biseccion(a, b, tol, pol):
    f = lambda x: eval(pol)
    lim_inf = [a]
    lim_sup = [b]
    x = [a]
    fx = [f(a)]
    err = [100]
    tol = int(tol)
    while err[-1] > 10**(-1*tol):
        c = (a + b) / 2
        x.append(round(c, tol+1))
        fx.append(round(f(c), tol+1))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        lim_inf.append(round(a, tol+1))
        lim_sup.append(round(b, tol+1))
        err.append(round(abs((b - a) / 2), tol+1))
    return x, fx, lim_inf, lim_sup, err