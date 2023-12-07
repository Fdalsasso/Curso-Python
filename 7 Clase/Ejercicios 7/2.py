# 2. Crear una función que determine si un año es bisiesto o no

def bisiesto(anio):
    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

anio = int(input("Ingrese un anio: "))
bisiesto(anio)