# Obtener la suma de todos los números de una lista

lista = []
suma = 0

while 1:
    a = input("Ingrese un numero para agregar a la lista: ")
    if a.isdigit():
        lista.append(int(a))
    else:
        break

for i in lista:
    suma += i

print("La suma total es: ", suma)