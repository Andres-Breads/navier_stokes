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

    matriz_jacobiana_x[2][1] = lambda W,U: (-W[2])/2 -1
    matriz_jacobiana_x[2][2] = lambda W,U: (W[3]-W[1])/2 +4
    matriz_jacobiana_x[2][3] = lambda W,U: (W[2])/2 -1
    matriz_jacobiana_x[2][8] = lambda W,U: (U[2])/2 -1

    matriz_jacobiana_x[3][2] = lambda W,U: (-W[3])/2 -1
    matriz_jacobiana_x[3][3] = lambda W,U: (W[4]-W[2])/2 +4
    matriz_jacobiana_x[3][4] = lambda W,U: (W[3])/2 -1
    matriz_jacobiana_x[3][9] = lambda W,U: (U[3])/2 -1

    matriz_jacobiana_x[4][3] = lambda W,U: (-W[4])/2 -1
    matriz_jacobiana_x[4][4] = lambda W,U: (W[5]-W[3])/2 +4
    matriz_jacobiana_x[4][5] = lambda W,U: (W[4])/2 -1
    matriz_jacobiana_x[4][10] = lambda W,U: (U[4])/2 -1

    matriz_jacobiana_x[5][4] = lambda W,U: (-W[5])/2 -1
    matriz_jacobiana_x[5][5] = lambda W,U: (-W[4])/2 +4
    matriz_jacobiana_x[5][11] = lambda W,U: (U[5])/2 -1

    matriz_jacobiana_x[6][0] = lambda W,U: (-W[6])/2 -1
    matriz_jacobiana_x[6][6] = lambda W,U: (W[7]-1)/2 +4
    matriz_jacobiana_x[6][7] = lambda W,U: (W[6])/2 -1
    matriz_jacobiana_x[6][12] = lambda W,U: (U[6])/2 -1

    matriz_jacobiana_x[7][1] = lambda W,U: (-U[7])/2 -1
    matriz_jacobiana_x[7][6] = lambda W,U: (-W[7])/2 -1
    matriz_jacobiana_x[7][7] = lambda W,U: (W[8]-W[6])/2 +4
    matriz_jacobiana_x[7][8] = lambda W,U: (W[7])/2 -1
    matriz_jacobiana_x[7][13] = lambda W,U: (U[7])/2 -1

    matriz_jacobiana_x[8][2] = lambda W,U: (-U[8])/2 -1
    matriz_jacobiana_x[8][7] = lambda W,U: (-W[8])/2 -1
    matriz_jacobiana_x[8][8] = lambda W,U: (W[9]-W[7])/2 +4
    matriz_jacobiana_x[8][9] = lambda W,U: (W[8])/2 -1
    matriz_jacobiana_x[8][14] = lambda W,U: (U[8])/2 -1

    matriz_jacobiana_x[9][3] = lambda W,U: (-U[9])/2 -1
    matriz_jacobiana_x[9][8] = lambda W,U: (-W[9])/2 -1
    matriz_jacobiana_x[9][9] = lambda W,U: (W[10]-W[8])/2 +4
    matriz_jacobiana_x[9][10] = lambda W,U: (W[9])/2 -1
    matriz_jacobiana_x[9][15] = lambda W,U: (U[9])/2 -1

    matriz_jacobiana_x[10][4] = lambda W,U: (-U[10])/2 -1
    matriz_jacobiana_x[10][9] = lambda W,U: (-W[10])/2 -1
    matriz_jacobiana_x[10][10] = lambda W,U: (W[11]-W[9])/2 +4
    matriz_jacobiana_x[10][11] = lambda W,U: (W[10])/2 -1
    matriz_jacobiana_x[10][16] = lambda W,U: (U[10])/2 -1

    matriz_jacobiana_x[11][5] = lambda W,U: (-U[11])/2 -1
    matriz_jacobiana_x[11][10] = lambda W,U: (-W[11])/2 -1
    matriz_jacobiana_x[11][11] = lambda W,U: (-W[10])/2 +4
    matriz_jacobiana_x[11][17] = lambda W,U: (U[11])/2 -1

    matriz_jacobiana_x[12][6] = lambda W,U: (-U[12])/2 -1
    matriz_jacobiana_x[12][12] = lambda W,U: (W[13]-1)/2 +4
    matriz_jacobiana_x[12][13] = lambda W,U: (W[12])/2 -1
    matriz_jacobiana_x[12][21] = lambda W,U: (U[12])/2 -1

    matriz_jacobiana_x[13][7] = lambda W,U: (-U[13])/2 -1
    matriz_jacobiana_x[13][12] = lambda W,U: (-W[13])/2 -1
    matriz_jacobiana_x[13][13] = lambda W,U: (W[14]-W[12])/2 +4
    matriz_jacobiana_x[13][14] = lambda W,U: (W[13])/2 -1
    matriz_jacobiana_x[13][22] = lambda W,U: (U[13])/2 -1

    matriz_jacobiana_x[14][8] = lambda W,U: (-U[14])/2 -1
    matriz_jacobiana_x[14][13] = lambda W,U: (-W[14])/2 -1
    matriz_jacobiana_x[14][14] = lambda W,U: (W[15]-W[13])/2 +4
    matriz_jacobiana_x[14][15] = lambda W,U: (W[14])/2 -1
    matriz_jacobiana_x[14][23] = lambda W,U: (U[14])/2 -1

    matriz_jacobiana_x[15][9] = lambda W,U: (-U[15])/2 -1
    matriz_jacobiana_x[15][14] = lambda W,U: (-W[15])/2 -1
    matriz_jacobiana_x[15][15] = lambda W,U: (W[16]-W[14])/2 +4
    matriz_jacobiana_x[15][16] = lambda W,U: (W[15])/2 -1

    matriz_jacobiana_x[16][10] = lambda W,U: (-U[16])/2 -1
    matriz_jacobiana_x[16][15] = lambda W,U: (-W[16])/2 -1
    matriz_jacobiana_x[16][16] = lambda W,U: (W[17]-W[15])/2 +4
    matriz_jacobiana_x[16][17] = lambda W,U: (W[16])/2 -1

    matriz_jacobiana_x[17][11] = lambda W,U: (-U[17])/2 -1
    matriz_jacobiana_x[17][16] = lambda W,U: (-W[17])/2 -1
    matriz_jacobiana_x[17][17] = lambda W,U: (W[18]-W[16])/2 +4
    matriz_jacobiana_x[17][18] = lambda W,U: (W[17])/2 -1

    matriz_jacobiana_x[18][17] = lambda W,U: (-W[18])/2 -1
    matriz_jacobiana_x[18][18] = lambda W,U: (W[19]-W[17])/2 +4
    matriz_jacobiana_x[18][19] = lambda W,U: (W[18])/2 -1
    matriz_jacobiana_x[18][24] = lambda W,U: (U[18])/2 -1

    matriz_jacobiana_x[19][18] = lambda W,U: (-W[19])/2 -1
    matriz_jacobiana_x[19][19] = lambda W,U: (W[20]-W[18])/2 +4
    matriz_jacobiana_x[19][20] = lambda W,U: (W[19])/2 -1
    matriz_jacobiana_x[19][25] = lambda W,U: (U[19])/2 -1

    matriz_jacobiana_x[20][19] = lambda W,U: (-W[20])/2 -1
    matriz_jacobiana_x[20][20] = lambda W,U: (-W[19])/2 +4
    matriz_jacobiana_x[20][26] = lambda W,U: (U[20])/2 -1

    matriz_jacobiana_x[21][12] = lambda W,U: (-U[21])/2 -1
    matriz_jacobiana_x[21][21] = lambda W,U: (W[22]-1)/2 +4
    matriz_jacobiana_x[21][22] = lambda W,U: (W[21])/2 -1
    matriz_jacobiana_x[21][27] = lambda W,U: (U[21])/2 -1

    matriz_jacobiana_x[22][13] = lambda W,U: (-U[22])/2 -1
    matriz_jacobiana_x[22][21] = lambda W,U: (-W[22])/2 -1
    matriz_jacobiana_x[22][22] = lambda W,U: (W[23]-W[21])/2 +4
    matriz_jacobiana_x[22][23] = lambda W,U: (W[22])/2 -1
    matriz_jacobiana_x[22][28] = lambda W,U: (U[22])/2 -1

    matriz_jacobiana_x[23][14] = lambda W,U: (-U[23])/2 -1
    matriz_jacobiana_x[23][22] = lambda W,U: (-W[23])/2 -1
    matriz_jacobiana_x[23][23] = lambda W,U: (-W[22])/2 +4
    matriz_jacobiana_x[23][29] = lambda W,U: (U[23])/2 -1

    matriz_jacobiana_x[24][18] = lambda W,U: (-U[24])/2 -1
    matriz_jacobiana_x[24][24] = lambda W,U: (W[25])/2 +4
    matriz_jacobiana_x[24][25] = lambda W,U: (W[24])/2 -1
    matriz_jacobiana_x[24][30] = lambda W,U: (U[24])/2 -1

    matriz_jacobiana_x[25][19] = lambda W,U: (-U[25])/2 -1
    matriz_jacobiana_x[25][24] = lambda W,U: (-W[25])/2 -1
    matriz_jacobiana_x[25][25] = lambda W,U: (W[26]-W[24])/2 +4
    matriz_jacobiana_x[25][26] = lambda W,U: (W[25])/2 -1
    matriz_jacobiana_x[25][31] = lambda W,U: (U[25])/2 -1

    matriz_jacobiana_x[26][20] = lambda W,U: (-U[26])/2 -1
    matriz_jacobiana_x[26][25] = lambda W,U: (-W[26])/2 -1
    matriz_jacobiana_x[26][26] = lambda W,U: (-W[25])/2 +4
    matriz_jacobiana_x[26][32] = lambda W,U: (U[26])/2 -1

    matriz_jacobiana_x[27][21] = lambda W,U: (-U[27])/2 -1
    matriz_jacobiana_x[27][27] = lambda W,U: (W[28]-1)/2 +4
    matriz_jacobiana_x[27][28] = lambda W,U: (W[27])/2 -1
    matriz_jacobiana_x[27][33] = lambda W,U: (U[27])/2 -1

    matriz_jacobiana_x[28][22] = lambda W,U: (-U[28])/2 -1
    matriz_jacobiana_x[28][27] = lambda W,U: (-W[28])/2 -1
    matriz_jacobiana_x[28][28] = lambda W,U: (W[29]-W[27])/2 +4
    matriz_jacobiana_x[28][29] = lambda W,U: (W[28])/2 -1
    matriz_jacobiana_x[28][34] = lambda W,U: (U[28])/2 -1

    matriz_jacobiana_x[29][23] = lambda W,U: (-U[29])/2 -1
    matriz_jacobiana_x[29][28] = lambda W,U: (-W[29])/2 -1
    matriz_jacobiana_x[29][29] = lambda W,U: (-W[28])/2 +4
    matriz_jacobiana_x[29][35] = lambda W,U: (U[29])/2 -1

    matriz_jacobiana_x[30][24] = lambda W,U: (-U[30])/2 -1
    matriz_jacobiana_x[30][30] = lambda W,U: (W[31])/2 +4
    matriz_jacobiana_x[30][31] = lambda W,U: (W[30])/2 -1
    matriz_jacobiana_x[30][36] = lambda W,U: (U[30])/2 -1

    matriz_jacobiana_x[31][25] = lambda W,U: (-U[31])/2 -1
    matriz_jacobiana_x[31][30] = lambda W,U: (-W[31])/2 -1
    matriz_jacobiana_x[31][31] = lambda W,U: (W[32]-W[30])/2 +4
    matriz_jacobiana_x[31][32] = lambda W,U: (W[31])/2 -1
    matriz_jacobiana_x[31][37] = lambda W,U: (U[31])/2 -1

    matriz_jacobiana_x[32][26] = lambda W,U: (-U[32])/2 -1
    matriz_jacobiana_x[32][31] = lambda W,U: (-W[32])/2 -1
    matriz_jacobiana_x[32][32] = lambda W,U: (-W[31])/2 +4
    matriz_jacobiana_x[32][38] = lambda W,U: (U[32])/2 -1

    matriz_jacobiana_x[33][27] = lambda W,U: (-U[33])/2 -1
    matriz_jacobiana_x[33][33] = lambda W,U: (W[34]-1)/2 +4
    matriz_jacobiana_x[33][34] = lambda W,U: (W[33])/2 -1

    matriz_jacobiana_x[34][28] = lambda W,U: (-U[34])/2 -1
    matriz_jacobiana_x[34][33] = lambda W,U: (-W[34])/2 -1
    matriz_jacobiana_x[34][34] = lambda W,U: (W[35]-W[33])/2 +4
    matriz_jacobiana_x[34][35] = lambda W,U: (W[34])/2 -1

    matriz_jacobiana_x[35][29] = lambda W,U: (-U[35])/2 -1
    matriz_jacobiana_x[35][34] = lambda W,U: (-W[35])/2 -1
    matriz_jacobiana_x[35][35] = lambda W,U: (-W[34])/2 +4

    matriz_jacobiana_x[36][30] = lambda W,U: (-U[36])/2 -1
    matriz_jacobiana_x[36][36] = lambda W,U: (W[37])/2 +4
    matriz_jacobiana_x[36][37] = lambda W,U: (W[36])/2 -1

    matriz_jacobiana_x[37][31] = lambda W,U: (-U[37])/2 -1
    matriz_jacobiana_x[37][36] = lambda W,U: (-W[37])/2 -1
    matriz_jacobiana_x[37][37] = lambda W,U: (W[38]-W[36])/2 +4
    matriz_jacobiana_x[37][38] = lambda W,U: (W[37])/2 -1

    matriz_jacobiana_x[38][32] = lambda W,U: (-U[38])/2 -1
    matriz_jacobiana_x[38][37] = lambda W,U: (-W[38])/2 -1
    matriz_jacobiana_x[38][38] = lambda W,U: (-W[37])/2 +4
    
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