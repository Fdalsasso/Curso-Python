# Escriba un programa Python para crear un archivo de texto con una cadena.

holaMundo = "Hello World"

archivo = open("archivo.txt", "w")
archivo.write(holaMundo)
archivo.close()