#ANTES (PARA TODOS)
maximo = float('-inf')
minimo = float('inf')
numero = int(input("Numero: "))
datos = False
while numero != 0:
    #DURANTE (PARA CADA DATO)
    datos = True
    if numero > maximo:
        maximo = numero
    if numero > minimo:
        minimo = numero
# LO ULTIMO ES LEER UN NUEVO DATO
    numero = int(input("Numero"))
#DESPUES (TOTALES)
if datos:
    print(f"maximo: {maximo}")
    print(f"minimo: {minimo}")
else:
    print("No se ingresaron datos")