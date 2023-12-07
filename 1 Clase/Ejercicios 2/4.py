# Escribe un programa en Python que nos diga si un número ingresado en el teclado es par o impar.

numero = int(input("Ingrese un numero\n"))

resto = numero % 2

if resto == 0:
    print("El numero es par")
else:
    print("El numero es impar")