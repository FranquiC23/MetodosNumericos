# Metodo de la secante

def secante(x0, x1, tol, pol):

    f = lambda x: eval(pol)

    tol = int(tol)
    x = [x0]
    x.append(x1)

    fx = [round(f(x[-2]), tol+1)]
    fx.append(round(f(x[-1]), tol+1))
    err = [100]

    
    while err[-1] > 10**(-1*tol):
        x0 = x[-1] - (fx[-1] * (x[-2] - x[-1])) / (fx[-2] - fx[-1])
        x.append(round(x0, tol+1))
        fx.append(round(f(x0), tol+1))
        err.append(round(abs((x[-1]-x[-2])/x[-1])*100, tol+1))
    return x, fx, err

s = secante(-1, 0, 4, "x**5 + x**3 + 3")
print(s)
print(s[0][-1])