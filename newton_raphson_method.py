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
    return nueva_matriz_jacobiana

if __name__ == '__main__':
    X0 = np.zeros(39)
    Y0 = np.zeros(39)

    # INGRESO
    matriz_jacobiana = [
        [lambda X, Y: (X[2]-1)/2 + 4, lambda X, Y: X[1]/2 - 1, 0, 0, 0, 0, lambda X, Y: Y[1]/2 - 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    jacobiano_poblado = poblar_jacobiano(matriz_jacobiana, X0, Y0)
    print(jacobiano_poblado)

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