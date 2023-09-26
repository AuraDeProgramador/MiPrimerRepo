import random

numero = random.randint(1,10)
contador = 0
suma = 0
while suma < 100:
    contador += 1
    suma += numero
    print(f"Numero: {numero} Suma: {suma} Cantidad de numero ingresados: {contador}")
    numero = random.randint(1,10)
    print(f"Cantidad de numeros: {contador}")