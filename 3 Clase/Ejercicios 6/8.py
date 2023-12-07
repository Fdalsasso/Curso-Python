# Escriba un programa de Python para agregar texto a un archivo y mostrar el texto.
texto = "\nHola que tal tu como estas, dime si eres feliz"

archivo = open("archivo.txt", "a")
archivo.write(texto)
archivo.close()
archivo = open("archivo.txt", "r")
leer = archivo.read()
archivo.close()

print(leer)