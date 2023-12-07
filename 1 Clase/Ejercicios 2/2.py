# Escribir un programa en Python que permita leer dos números del teclado (deben ser diferentes) y nos muestre en pantalla cuál de ellos es el mayor

numero1 = int(input("Ingrese el primer numero\n"))
numero2 = int(input("Ingrese el segundo numero\n"))
while numero1 == numero2:
    numero2 = int(input("El segundo numero debe ser diferente al primero\n"))

if numero1 < numero2:
    print("El numero ", numero2, " es mayor")
else:
    print("El numero ", numero1, " es mayor")