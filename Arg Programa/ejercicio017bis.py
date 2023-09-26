# Definir los valores de los billetes y monedas
billetes = [1000, 500, 200, 100, 50, 10, 5, 1]
nombres_billetes = ["billetes de 1000", "billetes de 500", "billetes de 200", "billetes de 100", "billetes de 50", "billetes de 10", "billetes de 5", "billetes de 1"]

# Solicitar al usuario ingresar la cantidad de dinero a convertir
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))

# Mostrar la cantidad de cada billete o moneda requeridos
print("Para la cantidad ingresada se necesitan:")
for i in range(len(billetes)):
    cantidad_billetes = cantidad_total // billetes[i]
    if cantidad_billetes > 0:
        print(f"{cantidad_billetes} {nombres_billetes[i]}")
    cantidad_total %= billetes[i]
