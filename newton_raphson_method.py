import numpy as np

# INGRESO
fx = lambda x: x**3 + 4*(x**2) - 10
dfx = lambda x: 3*(x**2) + 8*x

x0 = 2 # Punto inicial
tolera = 0.0001

# PROCEDIMIENTO
xi = x0
tramo = abs(2*tolera)
while not(tramo <= tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo = abs(xnuevo - xi) # Error estimado
    xi = xnuevo

# SALIDA
print(xnuevo)
print(tramo)