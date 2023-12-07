# Obtener el número más alto de una lista

def shellSort(lista):
    global comparaciones
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            val = lista[i]
            j = i
            

            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val

        gap = gap // 2

lista = []

while 1:
    a = input("Ingrese un numero para agregar a la lista: ")
    if a.isdigit():
        lista.append(int(a))
    else:
        break

shellSort(lista)

print("El numero mas alto es: ", lista[len(lista) - 1])