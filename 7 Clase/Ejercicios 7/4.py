# 4. Escriba una función en Python para restar/sumar X días de la fecha actual.

from datetime import datetime, timedelta

now = datetime.now()

opcion = input("Ingrese sumar o restar\n")
valor = timedelta(int(input("Ingrese la cantidad de dias\n")))

if opcion.upper() == "SUMAR":
    now += valor
elif opcion.upper() == "RESTAR":
    now-= valor
else:
    print("Operacion invalida")

print(now)