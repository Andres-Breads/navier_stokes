import numpy as np
import matplotlib.pyplot as plt

"""
A es una matriz cuadrada de NxN con la diagonal principal dominante
B es un vector con los coeficientes independientes en el sistema de ecuaciones de tamaño N
tolera es un valor de tolerancia de la función y sirve como condición de parada 
"""
def conjugate_gradient(A, b, tolera = 1e-5, iteramax = 20):
    iter = 0
    n = A.shape[0]
    x = np.zeros(n)
    r = b - np.dot(A, x) # El gradiente negativo
    d = r # Dirección conjugada
    while np.linalg.norm(r) > tolera and iter <= iteramax:
        # Alpha controla la velocidad de convergencia
        alpha = np.divide(np.dot(np.transpose(r), r), np.dot(np.dot(np.transpose(d), A), d))
        x = x + np.dot(alpha, d)
        r_new = r - np.dot(np.dot(alpha, A), d)
        beta = np.divide(np.dot(np.transpose(r_new), r_new), np.dot(np.transpose(r), r))
        d = r_new + np.dot(beta, d)
        r = r_new
        iter = iter + 1
    return (x, iter)

if __name__ == "__main__":
    # INGRESO
    A = np.loadtxt('matriz_X_A.txt', skiprows=0)
    B = np.loadtxt('matriz_X_B.txt', skiprows=0)
    C = np.loadtxt('matriz_Y_A.txt', skiprows=0)
    D = np.loadtxt('matriz_Y_B.txt', skiprows=0)
    X, itera_x = conjugate_gradient(A, B)
    Y, itera_y = conjugate_gradient(C, D)

    print(X, itera_x)
    print(Y, itera_y)
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