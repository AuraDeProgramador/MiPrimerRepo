n = (input("Introducir numero: "))
par = 0
impar = 0
for x in n:
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
print(n, "es ", par)
