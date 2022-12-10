import numpy as np

''' 
Función que recibe una matriz jacobiana con las derivadas parciales y un conjunto de valores iniciales X, Y
Retorna una matriz jacobiana habiendo ejecutado esas derivadas con los valores iniciales
'''
def poblar_jacobiano(matriz_jacobiana, X, Y):
    nueva_matriz_jacobiana = list()
    for row_index, row in enumerate(matriz_jacobiana):
        new_row = list()
        for column_index, column in enumerate(row):
            if callable(column):
                new_row.append(column(X, Y))
            else:
                new_row.append(column)
        nueva_matriz_jacobiana.append(new_row)
    return np.array(nueva_matriz_jacobiana)

if __name__ == '__main__':
    # Solución para dirección en X
    matriz_jacobiana_x = list()
    for item in range(39):
        list_of_zeros = list(0 for i in range(39))
        matriz_jacobiana_x.append(list_of_zeros)

    # INGRESO
    matriz_jacobiana_x[0][0] = lambda W,U: (W[1]-1)/2 +4
    matriz_jacobiana_x[0][1] = lambda W,U: W[0]/2 -1
    matriz_jacobiana_x[0][6] = lambda W,U: U[0]/2 -1
    
    matriz_jacobiana_x[1][0] = lambda W,U: (-W[1])/2 -1
    matriz_jacobiana_x[1][1] = lambda W,U: (W[2]-W[0])/2 +4
    matriz_jacobiana_x[1][2] = lambda W,U: (W[1])/2 -1
    matriz_jacobiana_x[1][7] = lambda W,U: (U[1])/2 -1
    
    X0 = np.ones(39)
    Y0 = np.ones(39)
    jacobiano_poblado = poblar_jacobiano(matriz_jacobiana_x, X0, Y0)
    # jacobiano_inverso = np.linalg.inv(jacobiano_poblado)
    print(jacobiano_poblado)

    # Solución para dirección en Y
    matriz_jacobiana_y = list()
    for item in range(39):
        list_of_zeros = list(0 for i in range(39))
        matriz_jacobiana_y.append(list_of_zeros)

    # INGRESO
    matriz_jacobiana_y[0][0] = lambda W,U: (W[1]-1)/2 +4
    matriz_jacobiana_y[0][1] = lambda W,U: W[0]/2 -1
    matriz_jacobiana_y[0][6] = lambda W,U: U[0]/2 -1
    
    matriz_jacobiana_y[1][0] = lambda W,U: (-W[1])/2 -1
    matriz_jacobiana_y[1][1] = lambda W,U: (W[2]-W[0])/2 +4
    matriz_jacobiana_y[1][2] = lambda W,U: (W[1])/2 -1
    matriz_jacobiana_y[1][7] = lambda W,U: (U[1])/2 -1

''' 
fx = lambda x: x**3 + 4*(x**2) - 10
dfx = lambda x: 3*(x**2) + 8*x

x0 = 2 # Punto inicial
tolera = 0.0001

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)
xi = x0
while not(tramo <= tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo = abs(xnuevo - xi) # Error estimado
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ',tramo)
'''