### Strings ###
name, surname, age = "Matias", "Martinez", 34
print ("Mi nombre es {} {} y mi edad es {}" . format(name, surname, age) )
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age) )
print (f"Mi nombre es {name} {surname} y mi edad es {age}" )
### Desempaquetado de Caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division

language_slice = language[1:]
print(language_slice) 
