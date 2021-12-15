import numpy as np

# METODO DE ELIMINACION DE GAUSS

#Eliminacion hacia adelante
def eliminacion_adelante(A,B):
    a = np.copy(A)
    b = np.copy(B)
    m, n = a.shape
    for k in range(0,m-1):
        print(f'f{k+1}-f{k}')
        for i in range(1+k,m):
            factor = a[i,k]/a[k,k]
            print(f'{a[i,k]}/{a[k,k]}')

            for j in range(0,n):
                a[i,j] = a[i,j] - factor*a[k,j]
                print(a)
            b[i,0] = b[i,0] - factor*b[k,0]
    return a,b

A = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
B = np.array([7.85,-19.3,71.4]).reshape((3,1))

print(A)
print(B)

eliminacion_adelante(A,B)

