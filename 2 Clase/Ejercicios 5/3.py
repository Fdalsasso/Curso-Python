# Escribir un programa en Python que permita saber si un array es capicua

array = []
i = 0
esCapicua = "Es capicua"

while 1:
    a = input("Ingrese un elemento para agregar a la lista o ingrese '0' para finalizar: ")
    if a != "0":
        array.append(a)
    else:
        break

while esCapicua == "Es capicua" and len(array) > i:
    if array[i] != array[len(array) - i - 1]:
        esCapicua = "No es capicua"
    i += 1

print(esCapicua)