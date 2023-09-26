try:
    calif = float(input("Introduzca puntuacion: "))
    if calif >= 0.9 :
        print("Sobresaliente")
    elif calif >= 0.8 :
        print("Notable")
    elif calif >= 0.7:
        print("Bien")
    elif calif >= 0.6:
        print("Suficiente")
    else:
        print("Insuficiente")
except:
    print("Puntuacion incorrecta")