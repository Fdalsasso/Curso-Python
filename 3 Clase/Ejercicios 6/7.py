# Escriba un programa Python para leer un archivo de texto completo.

archivo = open("archivo.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)