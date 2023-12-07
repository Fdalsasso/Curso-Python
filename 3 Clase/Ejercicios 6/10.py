# Escriba un programa Python para encontrar las palabras más largas.

archivo = open("archivo.txt", "r")
texto = archivo.readlines()
archivo.close()

listaDePalabras = []

for elem in texto:
    palabras = ""
    for palabra in elem:
        if palabra != " " and palabra != "\n":
            palabras += palabra
        else:
            listaDePalabras.append(palabras)
            palabras = ""

palabraMasLarga = listaDePalabras[0]

for elem in listaDePalabras:
    if len(elem) > len(palabraMasLarga):
        palabraMasLarga = elem