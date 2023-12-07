# 5. Escriba un programa en Python para obtener el número de semana.

from datetime import date

anio = int(input("Ingrese un anio\n"))
mes = int(input("Ingrese un mes\n"))
dia = int(input("Ingrese un dia\n"))

print(date(anio, mes, dia).strftime("%U"))