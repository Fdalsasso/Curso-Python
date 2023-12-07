# Escriba un programa en Python que acepte la longitud y la altura de un rectángulo del usuario y calcule el área y el perímetro

lado = int(input("Ingrese el largo del lado\n"))
altura = int(input("Ingrese la altura\n"))

perimetro = lado * 2 + altura * 2
area = lado * altura

print(f'{perimetro = }, {area = }')