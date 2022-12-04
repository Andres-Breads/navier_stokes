from sympy import sin, cos, Matrix
from sympy.abc import rho, phi

X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
Y = Matrix([rho, phi])

jacobian = X.jacobian(Y)
print(jacobian)