from random import randint

la_tabla_del = randint(1,10)
for numero in range(1,11):
    #para cada numero en el rango ==> [1,2,3,4,5,6,7,8,9,10]
    print(f"{la_tabla_del} x {numero} = {la_tabla_del*numero}")