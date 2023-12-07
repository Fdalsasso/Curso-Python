# Escribir un programa Python que permite eliminar elementos repetidos dentro de un arreglo y pasarlos a otro arreglo

array = []
array2 = []

while 1:
    a = input("Ingrese un elemento para agregar a la lista o ingrese '0' para finalizar: ")
    if a != "0":
        array.append(a)
    else:
        break

for i in range(0, len(array)):
    for j in range(0, i):
        if array[j] == array[i]:
            array2.append(array[i])

for i in array2:
    array.remove(i)