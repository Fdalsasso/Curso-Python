# Escriba un programa Python para contar el número de líneas en un archivo de texto.

archivo = open("archivo.txt", "r")
texto = archivo.readlines()
archivo.close()

print(len(texto))