# Escriba un programa Python para leer un archivo línea por línea y almacenarlo en una lista.

archivo = open("archivo.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)