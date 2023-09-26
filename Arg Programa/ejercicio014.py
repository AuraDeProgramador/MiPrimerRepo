ancho = int(input("Ingrese el ancho del terreno: "))
largo = int(input("Ingrese el largo del terreno: "))
valor = int(input("Ingrese el valor del metro cuadrado: "))
valorTotalDelTerreno = (ancho * largo ) * valor
print(f"El valor total del terreno es de: ", valorTotalDelTerreno )
alambre1metro = (2*ancho) + (2*largo)
alambre2metro = (2*ancho) + (2*largo) * 2 
alambre3metro = (2*ancho) + (2*largo) * 3
print(f"La cantidad de metros de alambre que se necesita para un metro de altura es : ", alambre1metro)
print(f"La cantidad de metros de alambre que se necesita para dos metros de altura es : ", alambre2metro)
print(f"La cantidad de metros de alambre que se necesita para tres metros de altura es : ",alambre3metro)