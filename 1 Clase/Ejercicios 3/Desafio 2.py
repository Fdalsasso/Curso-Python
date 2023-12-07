# Escribe una función de Python para calcular el factorial de un número

numeroFinal = 0

while numeroFinal < 1:
    numeroFinal = int(input("Ingrese un numero positivo\n"))

for i in range(2, numeroFinal):
    numeroFinal = numeroFinal * i

print("El factorial del numero es: ", numeroFinal)