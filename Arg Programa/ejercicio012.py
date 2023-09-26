angulo1 = int(input("Ingrese lado 1 : "))
angulo2 = int(input("Ingrese lado 2 : "))

if angulo1 < 0 or angulo2 < 0:
    print("Los ángulos no pueden ser negativos. Por favor, ingrese valores válidos.")
elif angulo1 + angulo2 >= 180:
    print("La suma de los ángulos ingresados es mayor o igual a 180 grados. Por favor, ingrese valores válidos.")
else:
    angulo_restante = 180 - (angulo1 + angulo2)
    print(f"El ángulo restante es de {angulo_restante} grados.")
