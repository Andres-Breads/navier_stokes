import numpy as np

''' 
Función que recibe una matriz jacobiana con las derivadas parciales y un conjunto de valores iniciales X, Y
Retorna una matriz jacobiana habiendo ejecutado esas derivadas con los valores iniciales
'''
def poblar_funciones(matriz_funciones, X, Y):
    nueva_matriz_funciones = list()
    for index, item in enumerate(matriz_funciones):
        nueva_matriz_funciones.append(item(X, Y))
    return np.array(nueva_matriz_funciones)

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
    matriz_funciones_x = list()
    matriz_funciones_x.append( lambda W,U: W[0]*((W[1]-1)/2)+U[0]*((W[6])/2)-W[1]-1-W[6]+4*W[0] )
    matriz_funciones_x.append( lambda W,U: W[1]*((W[2]-W[0])/2)+U[1]*((W[7])/2)-W[2]-W[0]-W[7]+4*W[1] )
    matriz_funciones_x.append( lambda W,U: W[2]*((W[3]-W[1])/2)+U[2]*((W[8])/2)-W[3]-W[1]-W[8]+4*W[2] )
    matriz_funciones_x.append( lambda W,U: W[3]*((W[4]-W[2])/2)+U[3]*((W[9])/2)-W[4]-W[2]-W[9]+4*W[3] )
    matriz_funciones_x.append( lambda W,U: W[4]*((W[5]-W[3])/2)+U[4]*((W[10])/2)-W[5]-W[3]-W[10]+4*W[4] )
    matriz_funciones_x.append( lambda W,U: W[5]*((-W[4])/2)+U[5]*((W[11])/2)-W[4]-W[11]+4*W[5] )
    matriz_funciones_x.append( lambda W,U: W[6]*((W[7]-1)/2)+U[6]*((W[12]-W[0])/2)-W[7]-1-W[12]-W[0]+4*W[6] )
    matriz_funciones_x.append( lambda W,U: W[7]*((W[8]-W[6])/2)+U[7]*((W[13]-W[1])/2)-W[8]-W[6]-W[13]-W[1]+4*W[7] )
    matriz_funciones_x.append( lambda W,U: W[8]*((W[9]-W[7])/2)+U[8]*((W[14]-W[2])/2)-W[9]-W[7]-W[14]-W[2]+4*W[8] )
    matriz_funciones_x.append( lambda W,U: W[9]*((W[10]-W[8])/2)+U[9]*((W[15]-W[3])/2)-W[10]-W[8]-W[15]-W[3]+4*W[9] )
    matriz_funciones_x.append( lambda W,U: W[10]*((W[11]-W[9])/2)+U[10]*((W[16]-W[4])/2)-W[11]-W[9]-W[16]-W[4]+4*W[10] )
    matriz_funciones_x.append( lambda W,U: W[11]*((-W[10])/2)+U[11]*((W[17]-W[5])/2)-W[10]-W[17]-W[5]+4*W[11] )
    matriz_funciones_x.append( lambda W,U: W[12]*((W[13]-1)/2)+U[12]*((W[21]-W[6])/2)-W[13]-1-W[21]-W[6]+4*W[12] )
    matriz_funciones_x.append( lambda W,U: W[13]*((W[14]-W[12])/2)+U[13]*((W[22]-W[7])/2)-W[14]-W[12]-W[22]-W[7]+4*W[13] )
    matriz_funciones_x.append( lambda W,U: W[14]*((W[15]-W[13])/2)+U[14]*((W[23]-W[8])/2)-W[15]-W[13]-W[23]-W[8]+4*W[14] )
    matriz_funciones_x.append( lambda W,U: W[15]*((W[16]-W[14])/2)+U[15]*((-W[9])/2)-W[16]-W[14]-W[9]+4*W[15] )
    matriz_funciones_x.append( lambda W,U: W[16]*((W[17]-W[15])/2)+U[16]*((-W[10])/2)-W[17]-W[15]-W[10]+4*W[16] )
    matriz_funciones_x.append( lambda W,U: W[17]*((W[18]-W[16])/2)+U[17]*((-W[11])/2)-W[18]-W[16]-W[11]+4*W[17] )
    matriz_funciones_x.append( lambda W,U: W[18]*((W[19]-W[17])/2)+U[18]*((W[24])/2)-W[19]-W[17]-W[24]+4*W[18] )
    matriz_funciones_x.append( lambda W,U: W[19]*((W[20]-W[18])/2)+U[19]*((W[25])/2)-W[20]-W[18]-W[25]+4*W[19] )
    matriz_funciones_x.append( lambda W,U: W[20]*((-W[19])/2)+U[20]*((W[26])/2)-W[19]-W[26]+4*W[20] )
    matriz_funciones_x.append( lambda W,U: W[21]*((W[22]-1)/2)+U[21]*((W[27]-W[12])/2)-W[22]-1-W[27]-W[12]+4*W[21] )
    matriz_funciones_x.append( lambda W,U: W[22]*((W[23]-W[21])/2)+U[22]*((W[28]-W[13])/2)-W[23]-W[21]-W[28]-W[13]+4*W[22] )
    matriz_funciones_x.append( lambda W,U: W[23]*((-W[22])/2)+U[23]*((W[29]-W[14])/2)-W[22]-W[29]-W[14]+4*W[23] )
    matriz_funciones_x.append( lambda W,U: W[24]*((W[25])/2)+U[24]*((W[30]-W[20])/2)-W[25]-W[30]-W[20]+4*W[24] )
    matriz_funciones_x.append( lambda W,U: W[25]*((W[26]-W[24])/2)+U[25]*((W[31]-W[19])/2)-W[26]-W[24]-W[31]-W[19]+4*W[25] )
    matriz_funciones_x.append( lambda W,U: W[26]*((-W[25])/2)+U[26]*((W[32]-W[20])/2)-W[25]-W[32]-W[20]+4*W[26] )
    matriz_funciones_x.append( lambda W,U: W[27]*((W[28]-1)/2)+U[27]*((W[33]-W[21])/2)-W[28]-1-W[33]-W[21]+4*W[27] )
    matriz_funciones_x.append( lambda W,U: W[28]*((W[29]-W[27])/2)+U[28]*((W[34]-W[22])/2)-W[29]-W[27]-W[34]-W[22]+4*W[28] )
    matriz_funciones_x.append( lambda W,U: W[29]*((-W[28])/2)+U[29]*((W[35]-W[23])/2)-W[28]-W[35]-W[23]+4*W[29] )
    matriz_funciones_x.append( lambda W,U: W[30]*((W[31])/2)+U[30]*((W[36]-W[24])/2)-W[31]-W[36]-W[24]+4*W[30] )
    matriz_funciones_x.append( lambda W,U: W[31]*((W[32]-W[30])/2)+U[31]*((W[37]-W[25])/2)-W[32]-W[30]-W[37]-W[25]+4*W[31] )
    matriz_funciones_x.append( lambda W,U: W[32]*((-W[31])/2)+U[32]*((W[38]-W[26])/2)-W[31]-W[38]-W[26]+4*W[32] )
    matriz_funciones_x.append( lambda W,U: W[33]*((W[34]-1)/2)+U[33]*((-W[27])/2)-W[34]-1-W[27]+4*W[33] )
    matriz_funciones_x.append( lambda W,U: W[34]*((W[35]-W[33])/2)+U[34]*((-W[28])/2)-W[35]-W[33]-W[28]+4*W[34] )
    matriz_funciones_x.append( lambda W,U: W[35]*((-W[34])/2)+U[35]*((-W[29])/2)-W[34]-W[29]+4*W[35] )
    matriz_funciones_x.append( lambda W,U: W[36]*((W[37])/2)+U[36]*((-W[30])/2)-W[37]-W[30]+4*W[36] )
    matriz_funciones_x.append( lambda W,U: W[37]*((W[38]-W[36])/2)+U[37]*((-W[31])/2)-W[38]-W[36]-W[31]+4*W[37] )
    matriz_funciones_x.append( lambda W,U: W[38]*((-W[37])/2)+U[38]*((-W[32])/2)-W[37]-W[32]+4*W[38] )

    matriz_funciones_y = list()
    matriz_funciones_y.append( lambda W,U: W[0]*((U[1])/2)+U[0]*((U[6])/2)-U[1]-U[6]+4*U[0] )
    matriz_funciones_y.append( lambda W,U: W[1]*((U[2]-U[0])/2)+U[1]*((U[7])/2)-U[2]-U[0]-U[7]+4*U[1] )
    matriz_funciones_y.append( lambda W,U: W[2]*((U[3]-U[1])/2)+U[2]*((U[8])/2)-U[3]-U[1]-U[8]+4*U[2] )
    matriz_funciones_y.append( lambda W,U: W[3]*((U[4]-U[2])/2)+U[3]*((U[9])/2)-U[4]-U[2]-U[9]+4*U[3] )
    matriz_funciones_y.append( lambda W,U: W[4]*((U[5]-U[3])/2)+U[4]*((U[10])/2)-U[5]-U[3]-U[10]+4*U[4] )
    matriz_funciones_y.append( lambda W,U: W[5]*((-U[4])/2)+U[5]*((U[11])/2)-U[4]-U[11]+4*U[5] )
    matriz_funciones_y.append( lambda W,U: W[6]*((U[7])/2)+U[6]*((U[12]-U[0])/2)-U[7]-U[12]-U[0]+4*U[6] )
    matriz_funciones_y.append( lambda W,U: W[7]*((U[8]-U[6])/2)+U[7]*((U[13]-U[1])/2)-U[8]-U[6]-U[13]-U[1]+4*U[7] )
    matriz_funciones_y.append( lambda W,U: W[8]*((U[9]-U[7])/2)+U[8]*((U[14]-U[2])/2)-U[9]-U[7]-U[14]-U[2]+4*U[8] )
    matriz_funciones_y.append( lambda W,U: W[9]*((U[10]-U[8])/2)+U[9]*((U[15]-U[3])/2)-U[10]-U[8]-U[15]-U[3]+4*U[9] )
    matriz_funciones_y.append( lambda W,U: W[10]*((U[11]-U[9])/2)+U[10]*((U[16]-U[4])/2)-U[11]-U[9]-U[16]-U[4]+4*U[10] )
    matriz_funciones_y.append( lambda W,U: W[11]*((-U[10])/2)+U[11]*((U[17]-U[5])/2)-U[10]-U[17]-U[5]+4*U[11] )
    matriz_funciones_y.append( lambda W,U: W[12]*((U[13])/2)+U[12]*((U[21]-U[6])/2)-U[13]-U[21]-U[6]+4*U[12] )
    matriz_funciones_y.append( lambda W,U: W[13]*((U[14]-U[12])/2)+U[13]*((U[22]-U[7])/2)-U[14]-U[12]-U[22]-U[7]+4*U[13] )
    matriz_funciones_y.append( lambda W,U: W[14]*((U[15]-U[13])/2)+U[14]*((U[23]-U[8])/2)-U[15]-U[13]-U[23]-U[8]+4*U[14] )
    matriz_funciones_y.append( lambda W,U: W[15]*((U[16]-U[14])/2)+U[15]*((-U[9])/2)-U[16]-U[14]-U[9]+4*U[15] )
    matriz_funciones_y.append( lambda W,U: W[16]*((U[17]-U[15])/2)+U[16]*((-U[10])/2)-U[17]-U[15]-U[10]+4*U[16] )
    matriz_funciones_y.append( lambda W,U: W[17]*((U[18]-U[16])/2)+U[17]*((-U[11])/2)-U[18]-U[16]-U[11]+4*U[17] )
    matriz_funciones_y.append( lambda W,U: W[18]*((U[19]-U[17])/2)+U[18]*((U[24])/2)-U[19]-U[17]-U[24]+4*U[18] )
    matriz_funciones_y.append( lambda W,U: W[19]*((U[20]-U[18])/2)+U[19]*((U[25])/2)-U[20]-U[18]-U[25]+4*U[19] )
    matriz_funciones_y.append( lambda W,U: W[20]*((-U[19])/2)+U[20]*((U[26])/2)-U[19]-U[26]+4*U[20] )
    matriz_funciones_y.append( lambda W,U: W[21]*((U[22])/2)+U[21]*((U[27]-U[12])/2)-U[22]-U[27]-U[12]+4*U[21] )
    matriz_funciones_y.append( lambda W,U: W[22]*((U[23]-U[21])/2)+U[22]*((U[28]-U[13])/2)-U[23]-U[21]-U[28]-U[13]+4*U[22] )
    matriz_funciones_y.append( lambda W,U: W[23]*((-U[22])/2)+U[23]*((U[29]-U[14])/2)-U[22]-U[29]-U[14]+4*U[23] )
    matriz_funciones_y.append( lambda W,U: W[24]*((U[25])/2)+U[24]*((U[30]-U[20])/2)-U[25]-U[30]-U[20]+4*U[24] )
    matriz_funciones_y.append( lambda W,U: W[25]*((U[26]-U[24])/2)+U[25]*((U[31]-U[19])/2)-U[26]-U[24]-U[31]-U[19]+4*U[25] )
    matriz_funciones_y.append( lambda W,U: W[26]*((-U[25])/2)+U[26]*((U[32]-U[20])/2)-U[25]-U[32]-U[20]+4*U[26] )
    matriz_funciones_y.append( lambda W,U: W[27]*((U[28])/2)+U[27]*((U[33]-U[21])/2)-U[28]-U[33]-U[21]+4*U[27] )
    matriz_funciones_y.append( lambda W,U: W[28]*((U[29]-U[27])/2)+U[28]*((U[34]-U[22])/2)-U[29]-U[27]-U[34]-U[22]+4*U[28] )
    matriz_funciones_y.append( lambda W,U: W[29]*((-U[28])/2)+U[29]*((U[35]-U[23])/2)-U[28]-U[35]-U[23]+4*U[29] )
    matriz_funciones_y.append( lambda W,U: W[30]*((U[31])/2)+U[30]*((U[36]-U[24])/2)-U[31]-U[36]-U[24]+4*U[30] )
    matriz_funciones_y.append( lambda W,U: W[31]*((U[32]-U[30])/2)+U[31]*((U[37]-U[25])/2)-U[32]-U[30]-U[37]-U[25]+4*U[31] )
    matriz_funciones_y.append( lambda W,U: W[32]*((-U[31])/2)+U[32]*((U[38]-U[26])/2)-U[31]-U[38]-U[26]+4*U[32] )
    matriz_funciones_y.append( lambda W,U: W[33]*((U[34])/2)+U[33]*((-U[27])/2)-U[34]-U[27]+4*U[33] )
    matriz_funciones_y.append( lambda W,U: W[34]*((U[35]-U[33])/2)+U[34]*((-U[28])/2)-U[35]-U[33]-U[28]+4*U[34] )
    matriz_funciones_y.append( lambda W,U: W[35]*((-U[34])/2)+U[35]*((-U[29])/2)-U[34]-U[29]+4*U[35] )
    matriz_funciones_y.append( lambda W,U: W[36]*((U[37])/2)+U[36]*((-U[30])/2)-U[37]-U[30]+4*U[36] )
    matriz_funciones_y.append( lambda W,U: W[37]*((U[38]-U[36])/2)+U[37]*((-U[31])/2)-U[38]-U[36]-U[31]+4*U[37] )
    matriz_funciones_y.append( lambda W,U: W[38]*((-U[37])/2)+U[38]*((-U[32])/2)-U[37]-U[32]+4*U[38] )

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
    
    # Solución para dirección en Y
    matriz_jacobiana_y = list()
    for item in range(39):
        list_of_zeros = list(0 for i in range(39))
        matriz_jacobiana_y.append(list_of_zeros)

    # INGRESO
    matriz_jacobiana_y[0][0] = lambda W,U: (U[6])/2 +4
    matriz_jacobiana_y[0][1] = lambda W,U: (W[0])/2 -1
    matriz_jacobiana_y[0][6] = lambda W,U: (U[0])/2 -1
    
    matriz_jacobiana_y[1][0] = lambda W,U: (-W[1])/2 -1
    matriz_jacobiana_y[1][1] = lambda W,U: (U[7])/2 +4
    matriz_jacobiana_y[1][2] = lambda W,U: (W[1])/2 -1
    matriz_jacobiana_y[1][7] = lambda W,U: (U[1])/2 -1

    matriz_jacobiana_y[2][1] = lambda W,U: (-W[2])/2 -1
    matriz_jacobiana_y[2][2] = lambda W,U: (U[8])/2 +4
    matriz_jacobiana_y[2][3] = lambda W,U: (W[2])/2 -1
    matriz_jacobiana_y[2][8] = lambda W,U: (U[2])/2 -1

    matriz_jacobiana_y[3][2] = lambda W,U: (-W[3])/2 -1
    matriz_jacobiana_y[3][3] = lambda W,U: (U[9])/2 +4
    matriz_jacobiana_y[3][4] = lambda W,U: (W[3])/2 -1
    matriz_jacobiana_y[3][9] = lambda W,U: (U[3])/2 -1

    matriz_jacobiana_y[4][3] = lambda W,U: (-W[4])/2 -1
    matriz_jacobiana_y[4][4] = lambda W,U: (U[10])/2 +4
    matriz_jacobiana_y[4][5] = lambda W,U: (W[4])/2 -1
    matriz_jacobiana_y[4][10] = lambda W,U: (U[4])/2 -1

    matriz_jacobiana_y[5][4] = lambda W, U: (-W[5]) / 2 - 1
    matriz_jacobiana_y[5][5] = lambda W, U: (U[11]) / 2 + 4
    matriz_jacobiana_y[5][11] = lambda W, U: (U[6]) / 2 - 1

    matriz_jacobiana_y[6][0] = lambda W, U: (-U[6]) / 2 - 1
    matriz_jacobiana_y[6][6] = lambda W, U: (U[12]-U[0]) / 2 + 4
    matriz_jacobiana_y[6][7] = lambda W, U: (W[6]) / 2 - 1
    matriz_jacobiana_y[6][12] = lambda W, U: (U[6]) / 2 - 1

    matriz_jacobiana_y[7][1] = lambda W, U: (-U[7]) / 2 - 1
    matriz_jacobiana_y[7][6] = lambda W, U: (-W[7]) / 2 - 1
    matriz_jacobiana_y[7][7] = lambda W, U: (U[13]-U[1]) / 2 + 4
    matriz_jacobiana_y[7][8] = lambda W, U: (W[7]) / 2 - 1
    matriz_jacobiana_y[7][13] = lambda W,U: (U[7]) / 2 - 1

    matriz_jacobiana_y[8][2] = lambda W, U: (-U[8]) / 2 - 1
    matriz_jacobiana_y[8][7] = lambda W, U: (-W[8]) / 2 - 1
    matriz_jacobiana_y[8][8] = lambda W, U: (U[14]-U[2]) / 2 + 4
    matriz_jacobiana_y[8][9] = lambda W, U: (W[8]) / 2 - 1
    matriz_jacobiana_y[8][14] = lambda W, U: (U[8]) / 2 - 1

    matriz_jacobiana_y[9][3] = lambda W, U: (-U[9]) / 2 - 1
    matriz_jacobiana_y[9][8] = lambda W, U: (-W[9]) / 2 - 1
    matriz_jacobiana_y[9][9] = lambda W, U: (U[15]-U[3]) / 2 + 4
    matriz_jacobiana_y[9][10] = lambda W, U: (W[9]) / 2 - 1
    matriz_jacobiana_y[9][15] = lambda W, U: (U[9]) / 2 - 1

    matriz_jacobiana_y[10][4] = lambda W, U: (-U[10]) / 2 - 1
    matriz_jacobiana_y[10][9] = lambda W, U: (-W[10]) / 2 - 1
    matriz_jacobiana_y[10][10] = lambda W, U: (U[16]-U[4]) / 2 + 4
    matriz_jacobiana_y[10][11] = lambda W, U: (W[10]) / 2 - 1
    matriz_jacobiana_y[10][16] = lambda W, U: (U[10]) / 2 - 1

    matriz_jacobiana_y[11][5] = lambda W, U: (-U[11]) / 2 - 1
    matriz_jacobiana_y[11][10] = lambda W, U: (-W[11]) / 2 - 1
    matriz_jacobiana_y[11][11] = lambda W, U: (U[17]-U[5]) / 2 + 4
    matriz_jacobiana_y[11][17] = lambda W, U: (U[11]) / 2 - 1

    matriz_jacobiana_y[12][6] = lambda W, U: (-U[12]) / 2 - 1
    matriz_jacobiana_y[12][12] = lambda W, U: (U[21]-U[6]) / 2 + 4
    matriz_jacobiana_y[12][13] = lambda W, U: (W[12]) / 2 - 1
    matriz_jacobiana_y[12][21] = lambda W, U: (U[12]) / 2 - 1

    matriz_jacobiana_y[13][7] = lambda W, U: (-U[13]) / 2 - 1
    matriz_jacobiana_y[13][12] = lambda W, U: (-W[13]) / 2 - 1
    matriz_jacobiana_y[13][13] = lambda W, U: (U[22]-U[7]) / 2 + 4
    matriz_jacobiana_y[13][14] = lambda W, U: (W[13]) / 2 - 1
    matriz_jacobiana_y[13][22] = lambda W, U: (U[13]) / 2 - 1

    matriz_jacobiana_y[14][8] = lambda W, U: (-U[14]) / 2 - 1
    matriz_jacobiana_y[14][13] = lambda W, U: (-W[14]) / 2 - 1
    matriz_jacobiana_y[14][14] = lambda W, U: (U[23]-U[8]) / 2 + 4
    matriz_jacobiana_y[14][15] = lambda W, U: (W[14]) / 2 - 1
    matriz_jacobiana_y[14][23] = lambda W, U: (U[14]) / 2 - 1

    matriz_jacobiana_y[15][9] = lambda W, U: (-U[15]) / 2 - 1
    matriz_jacobiana_y[15][14] = lambda W, U: (-W[15]) / 2 - 1
    matriz_jacobiana_y[15][15] = lambda W, U: (-U[9]) / 2 + 4
    matriz_jacobiana_y[15][16] = lambda W, U: (W[15]) / 2 - 1

    matriz_jacobiana_y[16][10] = lambda W, U: (-U[16]) / 2 - 1
    matriz_jacobiana_y[16][15] = lambda W, U: (-W[16]) / 2 - 1
    matriz_jacobiana_y[16][16] = lambda W, U: (-U[10]) / 2 + 4
    matriz_jacobiana_y[16][17] = lambda W, U: (W[16]) / 2 - 1

    matriz_jacobiana_y[17][11] = lambda W, U: (-U[17]) / 2 - 1
    matriz_jacobiana_y[17][16] = lambda W, U: (-W[17]) / 2 - 1
    matriz_jacobiana_y[17][17] = lambda W, U: (-U[11]) / 2 + 4
    matriz_jacobiana_y[17][18] = lambda W, U: (W[17]) / 2 - 1

    matriz_jacobiana_y[18][17] = lambda W, U: (-U[19]) / 2 - 1
    matriz_jacobiana_y[18][18] = lambda W, U: (U[24]) / 2 + 4
    matriz_jacobiana_y[18][19] = lambda W, U: (W[18]) / 2 - 1
    matriz_jacobiana_y[18][24] = lambda W, U: (U[18]) / 2 - 1

    matriz_jacobiana_y[19][18] = lambda W, U: (-W[19]) / 2 - 1
    matriz_jacobiana_y[19][19] = lambda W, U: (U[25]) / 2 + 4
    matriz_jacobiana_y[19][20] = lambda W, U: (W[19]) / 2 - 1
    matriz_jacobiana_y[19][25] = lambda W, U: (U[19]) / 2 - 1

    matriz_jacobiana_y[20][19] = lambda W, U: (-W[21]) / 2 - 1
    matriz_jacobiana_y[20][20] = lambda W, U: (U[26]) / 2 + 4
    matriz_jacobiana_y[20][26] = lambda W, U: (U[20]) / 2 - 1

    matriz_jacobiana_y[21][12] = lambda W, U: (-U[21]) / 2 - 1
    matriz_jacobiana_y[21][21] = lambda W, U: (U[27]-U[12]) / 2 + 4
    matriz_jacobiana_y[21][22] = lambda W, U: (W[21]) / 2 - 1
    matriz_jacobiana_y[21][27] = lambda W, U: (U[21]) / 2 - 1

    matriz_jacobiana_y[22][13] = lambda W, U: (-U[22]) / 2 - 1
    matriz_jacobiana_y[22][21] = lambda W, U: (-W[22]) / 2 - 1
    matriz_jacobiana_y[22][22] = lambda W, U: (U[28]-U[13]) / 2 + 4
    matriz_jacobiana_y[22][23] = lambda W, U: (W[22]) / 2 - 1
    matriz_jacobiana_y[22][28] = lambda W, U: (U[22]) / 2 - 1

    matriz_jacobiana_y[23][14] = lambda W, U: (-U[23]) / 2 - 1
    matriz_jacobiana_y[23][22] = lambda W, U: (-W[23]) / 2 - 1
    matriz_jacobiana_y[23][23] = lambda W, U: (U[29]-U[14]) / 2 + 4
    matriz_jacobiana_y[23][29] = lambda W, U: (U[23]) / 2 - 1

    matriz_jacobiana_y[24][18] = lambda W, U: (-U[24]) / 2 - 1
    matriz_jacobiana_y[24][24] = lambda W, U: (U[30]-U[18]) / 2 + 4
    matriz_jacobiana_y[24][25] = lambda W, U: (W[24]) / 2 - 1
    matriz_jacobiana_y[24][30] = lambda W, U: (U[24]) / 2 - 1

    matriz_jacobiana_y[25][19] = lambda W, U: (-U[25]) / 2 - 1
    matriz_jacobiana_y[25][24] = lambda W, U: (-W[26]) / 2 - 1
    matriz_jacobiana_y[25][25] = lambda W, U: (U[31]-U[19]) / 2 + 4
    matriz_jacobiana_y[25][26] = lambda W, U: (W[25]) / 2 - 1
    matriz_jacobiana_y[25][31] = lambda W, U: (U[25]) / 2 - 1

    matriz_jacobiana_y[26][20] = lambda W, U: (-U[26]) / 2 - 1
    matriz_jacobiana_y[26][25] = lambda W, U: (-W[26]) / 2 - 1
    matriz_jacobiana_y[26][26] = lambda W, U: (U[33]-U[20]) / 2 + 4
    matriz_jacobiana_y[26][32] = lambda W, U: (U[26]) / 2 - 1

    matriz_jacobiana_y[27][21] = lambda W, U: (-U[27]) / 2 - 1
    matriz_jacobiana_y[27][27] = lambda W, U: (U[33]-U[21]) / 2 + 4
    matriz_jacobiana_y[27][28] = lambda W, U: (W[27]) / 2 - 1
    matriz_jacobiana_y[27][33] = lambda W, U: (U[27]) / 2 - 1

    matriz_jacobiana_y[28][22] = lambda W, U: (-U[28]) / 2 - 1
    matriz_jacobiana_y[28][27] = lambda W, U: (-W[28]) / 2 - 1
    matriz_jacobiana_y[28][28] = lambda W, U: (U[34] -U[22]) / 2 + 4
    matriz_jacobiana_y[28][29] = lambda W, U: (W[28]) / 2 - 1
    matriz_jacobiana_y[28][34] = lambda W, U: (U[28]) / 2 - 1

    matriz_jacobiana_y[29][23] = lambda W, U: (-U[29]) / 2 - 1
    matriz_jacobiana_y[29][28] = lambda W, U: (-W[29]) / 2 - 1
    matriz_jacobiana_y[29][29] = lambda W, U: (U[35] - U[23]) / 2 + 4
    matriz_jacobiana_y[29][35] = lambda W, U: (U[29]) / 2 - 1

    matriz_jacobiana_y[30][24] = lambda W, U: (-U[30]) / 2 - 1
    matriz_jacobiana_y[30][30] = lambda W, U: (U[36]-U[24]) / 2 + 4
    matriz_jacobiana_y[30][31] = lambda W, U: (W[30]) / 2 - 1
    matriz_jacobiana_y[30][36] = lambda W, U: (U[30]) / 2 - 1

    matriz_jacobiana_y[31][25] = lambda W, U: (-U[31]) / 2 - 1
    matriz_jacobiana_y[31][30] = lambda W, U: (-W[31]) / 2 - 1
    matriz_jacobiana_y[31][31] = lambda W, U: (U[37]- U[25]) / 2 + 4
    matriz_jacobiana_y[31][32] = lambda W, U: (W[31]) / 2 - 1
    matriz_jacobiana_y[31][37] = lambda W, U: (U[31]) / 2 - 1

    matriz_jacobiana_y[32][26] = lambda W, U: (-U[32]) / 2 - 1
    matriz_jacobiana_y[32][31] = lambda W, U: (-W[32]) / 2 - 1
    matriz_jacobiana_y[32][32] = lambda W, U: (U[38] - U[26]) / 2 + 4
    matriz_jacobiana_y[32][38] = lambda W, U: (U[32]) / 2 - 1

    matriz_jacobiana_y[33][27] = lambda W, U: (-U[33]) / 2 - 1
    matriz_jacobiana_y[33][33] = lambda W, U: (-U[27]) / 2 + 4
    matriz_jacobiana_y[33][34] = lambda W, U: (W[33]) / 2 - 1

    matriz_jacobiana_y[34][28] = lambda W, U: (-U[34]) / 2 - 1
    matriz_jacobiana_y[34][33] = lambda W, U: (-W[34]) / 2 - 1
    matriz_jacobiana_y[34][34] = lambda W, U: (-U[28]) / 2 + 4
    matriz_jacobiana_y[34][35] = lambda W, U: (W[34]) / 2 - 1

    matriz_jacobiana_y[35][29] = lambda W, U: (-U[35]) / 2 - 1
    matriz_jacobiana_y[35][34] = lambda W, U: (-W[35]) / 2 - 1
    matriz_jacobiana_y[35][35] = lambda W, U: (U[29]) / 2 + 4

    matriz_jacobiana_y[36][30] = lambda W, U: (-U[36]) / 2 - 1
    matriz_jacobiana_y[36][36] = lambda W, U: (-U[30]) / 2 + 4
    matriz_jacobiana_y[36][37] = lambda W, U: (W[36]) / 2 - 1

    matriz_jacobiana_y[37][31] = lambda W, U: (-U[37]) / 2 - 1
    matriz_jacobiana_y[37][36] = lambda W, U: (-W[37]) / 2 - 1
    matriz_jacobiana_y[37][37] = lambda W, U: (-U[31]) / 2 + 4
    matriz_jacobiana_y[37][38] = lambda W, U: (W[37]) / 2 - 1

    matriz_jacobiana_y[38][32] = lambda W, U: (-U[38]) / 2 - 1
    matriz_jacobiana_y[38][37] = lambda W, U: (-W[38]) / 2 - 1
    matriz_jacobiana_y[38][38] = lambda W, U: (-U[32]) / 2 + 4

    tolera = 0.0001
    diferencia = np.ones(39, dtype = float)
    errado = 2*tolera
    iter = 0
    iteramax = 13

    X0 = np.ones(39)
    Y0 = np.ones(39)

    while np.linalg.norm(X0) > tolera and np.linalg.norm(Y0) > tolera and iter <= iteramax:
        funciones_pobladas_x = poblar_funciones(matriz_funciones_x, X0, Y0)
        jacobiano_poblado_x = poblar_jacobiano(matriz_jacobiana_x, X0, Y0)
        jacobiano_inverso_x = np.linalg.inv(jacobiano_poblado_x)

        funciones_pobladas_y = poblar_funciones(matriz_funciones_y, X0, Y0)
        jacobiano_poblado_y = poblar_jacobiano(matriz_jacobiana_y, X0, Y0)
        jacobiano_inverso_y = np.linalg.inv(jacobiano_poblado_y)

        X0 = X0 - np.dot(jacobiano_inverso_x, funciones_pobladas_x)
        Y0 = Y0 - np.dot(jacobiano_inverso_y, funciones_pobladas_y)
        iter = iter + 1
        print(f'Iteración {iter}:')
        print(np.linalg.norm(X0))
        print(np.linalg.norm(Y0))
        print(X0)
        print(Y0)
        print('---------------------')


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