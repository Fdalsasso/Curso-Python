# Escribe una función de Python para verificar si un número es perfecto o no.

posibleNumeroPerfecto = int(input("Ingrese un numero\n"))
suma = 0

for i in range(1, posibleNumeroPerfecto - 1):
    if (posibleNumeroPerfecto % i) == 0:
        suma += i

if posibleNumeroPerfecto == suma:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")