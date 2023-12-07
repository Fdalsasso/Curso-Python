# Escriba una secuencia de comandos de Python para mostrar los distintos formatos de fecha y hora:
# a) Fecha y hora actuales
# b) Año actual
# c) Mes del año
# d) Número de semana del año
# e) Día de la semana
# f) Día de año
# g) Día del mes
# h) Día de la semana

import time
from datetime import datetime

#a = datetime.now()    |     time.asctime()
#b = datetime.today().strftime("%Y")    |     time.localtime()[0]
#c = datetime.today().strftime("%B")    |     time.localtime()[1]
#d = datetime.today().strftime("%U")    |     time.strftime("%U")
#e = datetime.today().strftime("%A")    |     time.strftime("%A")
#f = datetime.today().strftime("%j")    |     time.strftime("%j")
#g = datetime.today().strftime("%d")    |     time.strftime("%d")
#h = datetime.today().strftime("%a")    |     time.strftime("%a")