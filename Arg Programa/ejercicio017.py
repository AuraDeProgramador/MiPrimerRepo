cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
print(f"Para la cantidad de ",(cantidad_total), "se necesitan: ")
lista_numeros =[1000, 200, 100, 50, 10, 5 , 1]
for i in lista_numeros:
    if cantidad_total > i:
        resto = cantidad_total // i
        print((resto),("billete" if resto < 2 else "billetes"),(i),)
        cantidad_total = cantidad_total % i

