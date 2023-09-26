try:
    Horas = int(input(" Indroduzca Horas "))
    Tarifa = float(input(" Introduzca Tarifa "))

    if Horas > 40 :
        excedente = Horas - 40
        Salario = (40 * Tarifa) + (excedente * Tarifa * 1.5)
    else: 
        Salario = Horas * Tarifa

    print (Salario)
except:
    print ("Error,Introduzca un numero")