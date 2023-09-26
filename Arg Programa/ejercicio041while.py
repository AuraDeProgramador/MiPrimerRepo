#ANTES
suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0 :
    #DURANTE
    suma += numero
    numero = int(input("Ingrese un numero: "))
#DESPUES
print(f"La suma es: {suma}")

palabra = "perrito perro perrote"
for letra in palabra:
    print(letra)
    
cantidad_letras = len(palabra)
for x in range (cantidad_letras):
    print(palabra[x])
