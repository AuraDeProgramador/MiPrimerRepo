segundos = int(input("Ingrese los segundos : "))
dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} equivalen a {dias} dias, {horas} horas, {minutos} minutos, {segundos_restantes} segundos.")