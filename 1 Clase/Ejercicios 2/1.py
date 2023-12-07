# Escriba un programa en Python que verifique si un número es mayor, igual o menor que cero.

numero1 = int(input("Ingrese un numero\n"))

if numero1 < 0:
    print("El numero es menor a cero")
elif numero1 > 0:
    print("El numero es mayor a cero")
else:
    print("El numero es igual a cero")