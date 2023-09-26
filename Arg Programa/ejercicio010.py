inv_pers1 = float(input("Ingrese la cantidad invertida por la persona 1 : "))
inv_pers2 = float(input("Ingrese la cantidad invertida por la persona 2 : "))
inv_pers3 = float(input("Ingrese la cantidad invertida por la persona 3 : "))
total = inv_pers1 + inv_pers2 + inv_pers3
porcentaje_inv_pers1 = round((inv_pers1 / total) * 100, 2)
porcentaje_inv_pers2 = round((inv_pers2 / total) * 100, 2)
porcentaje_inv_pers3 = round((inv_pers3 / total) * 100, 2)
print(f"La persona 1 invirtio : {porcentaje_inv_pers1},  la persona 2 invirtio : {porcentaje_inv_pers2}, la persona 3 invirtio : {porcentaje_inv_pers3}")
