import sympy as sp

# Definir las variables
x, y = sp.symbols('x y')

# Definir la ecuación
ecuacion = sp.Eq(y, 2*x - 2)

# Calcular la pendiente
pendiente = sp.slope(ecuacion)

# Calcular la intercepción x
intercepcion_x = sp.solve(ecuacion, x)[0]

# Calcular la intercepción y
intercepcion_y = sp.solve(ecuacion, y)[0]

# Imprimir los resultados
print("Pendiente: ", pendiente)
print("Intercepción x: ", intercepcion_x)
print("Intercepción y: ", intercepcion_y)
