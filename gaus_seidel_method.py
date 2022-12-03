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
    X = resolver_gaus_seidel(A, B)
    Y = resolver_gaus_seidel(C, D)

    matriz_n = 8 # Filas
    matriz_m = 11 # columnas

    Solucion = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, X[0], X[1], X[2], X[3], X[4], X[5], 0, 0, 0, 0],
        [1, X[6], X[7], X[8], X[9], X[10], X[11], 0, 0, 0, 0],
        [1, X[12], X[13], X[14], X[15], X[16], X[17], X[18], X[19], X[20], 0],
        [1, X[21], X[22], X[23], 0, 0, 0, X[24], X[25], X[26], 0],
        [1, X[27], X[28], X[29], 0, 0, 0, X[30], X[31], X[32], 0],
        [1, X[33], X[34], X[35], 0, 0, 0, X[36], X[37], X[38], 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    #plt.figure()
    plt.imshow(Solucion)
    plt.title( "2-D Heat Map" )
    plt.colorbar()
    plt.show()