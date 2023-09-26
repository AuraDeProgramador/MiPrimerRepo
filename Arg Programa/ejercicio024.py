MINIMA_EDAD_LIMITE = 10
MINIMA_ALTURA = 1.6

nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura: "))

entra_edad = edad >= MINIMA_EDAD_LIMITE
entra_altura = altura > 1.6
entra = entra_edad and entra_altura

cartel = f"{nombre} "
 
if entra:
    cartel += "Entraste!"
else:
    if not entra_altura:
        cartel += "No entras por altura"
    
    if not entra_edad:
        cartel += "No entras por edad"
print(cartel)