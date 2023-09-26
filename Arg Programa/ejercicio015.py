nombre_vendedor = input("Ingrese el nombre del vendedor: ")
cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_ventas = float(input("Ingrese el valor total de las ventas: "))
salario_base = 1000  # Se puede ajustar este valor 
comision_venta = 100 
comision_total = valor_ventas * 0.05
salario_total = salario_base + (comision_venta * cantidad_ventas) + comision_total
print(f"Nombre del vendedor: {nombre_vendedor}")
print(f"Salario correspondiente en el mes: {salario_total}")
