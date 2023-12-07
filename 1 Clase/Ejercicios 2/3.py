# *Determinar si un estudiante aprueba o reprueba un curso, sabiendo que aprobará si su promedio de tres notas (valores enteros del 1 al 10) es mayor o igual a 6; fallar de otra manera.

nota1 = int(input("Ingrese la primera nota\n"))
nota2 = int(input("Ingrese la segunda nota\n"))
nota3 = int(input("Ingrese la tercera nota\n"))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6:
    print("Aprobo")
else:
    print("Desaprobo")