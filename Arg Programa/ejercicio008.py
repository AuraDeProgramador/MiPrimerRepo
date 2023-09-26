valor_hora = int(input("Ingrese el valor monetario de una hora de trabajo: "))
horas_trabajadas_por_dia = int(input("Ingrese horas trabajadas por dia: "))
salario_diario = valor_hora * horas_trabajadas_por_dia
dias_habiles = 5
salario_semanal = salario_diario * dias_habiles
horas_sabado = horas_trabajadas_por_dia / 2
horas_trabajadas_sabado = valor_hora * horas_sabado
Total_semanal = (salario_semanal + horas_trabajadas_sabado)
print("El salario semanal es : ",(Total_semanal))