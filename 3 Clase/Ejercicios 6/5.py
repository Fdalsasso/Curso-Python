# crear un diccionario a partir de este diccionario con datos, pero que no muestre el array, sino el promedio

df = {'student1': [4, 6, 8], 'students2': [10, 5, 7], 'student3': [6, 6, 9]}

nuevo_df = {}

for elem in df:
    suma = 0
    cont = 0
    for nota in df.get(elem):
        suma += nota
        cont += 1
    nuevo_df[elem] = suma / cont

print(nuevo_df)