# Escriba un programa en Python que acepte el radio de un círculo del usuario y calcule el área

from cmath import pi


radio = int(input("Ingrese el radio de la circunferencia\n"))

area = radio ** 2 * pi

print("El area es: ", area)