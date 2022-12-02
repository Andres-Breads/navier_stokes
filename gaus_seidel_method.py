import numpy as np
import matplotlib.pyplot as plt

'''
A = np.array([
    [3., -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
])
B = np.array([7.85, -19.3, 71.4])
'''

"""
A es una matriz cuadrada de NxN con la diagonal principal dominante
B es un vector con las igualdades en el sistema de ecuaciones de tamaño N
"""
def resolver_gaus_seidel(A, B, iteramax = 20):
    tolera = 0.0001

    # PROCEDIMIENTO
    # Gaus-Seidel
    tamano = np.shape(A)
    n = tamano[0] # número de filas
    m = tamano[1] # número de columnas

    X0 = np.zeros(n, dtype = float)
    # valores iniciales
    X = np.copy(X0)
    diferencia = np.ones(n, dtype = float)
    errado = 2*tolera

    i = 0
    itera = 0

    while not(errado <= tolera or itera > iteramax):
        for i in range(0, n, 1):
            suma = 0
            for j in range(0, m, 1):
                if (j != i):
                    suma = suma + A[i,j]*X[j]

            nuevo = (B[i] - suma)/A[i,i] # Esta sería la forma de obtener el nuevo valor de X[i]
            diferencia[i] = np.abs(nuevo - X[i]) # Es para calcular el error
            X[i] = nuevo

        print(f'Iteración {itera}')
        print(X)
        test = np.dot(A, X)
        print(test)
        errado = np.max(diferencia)
        itera = itera + 1

    # revisa convergencia
    if (itera > iteramax):
        X = 0

    return X

if __name__ == "__main__":
    # INGRESO
    A = np.loadtxt('matriz_X_A.txt', skiprows=0)
    B = np.loadtxt('matriz_X_B.txt', skiprows=0)
    C = np.loadtxt('matriz_Y_A.txt', skiprows=0)
    D = np.loadtxt('matriz_Y_B.txt', skiprows=0)
    solucionX = resolver_gaus_seidel(A, B)
    solucionY = resolver_gaus_seidel(C, D)
    ''' solucion = np.meshgrid(solucionX, solucionY)
    print(solucion)
    plt.imshow( solucion , origin='lower' )
    plt.title( "2-D Heat Map" )
    plt.show() '''