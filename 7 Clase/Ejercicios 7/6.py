# 6. Dada la fecha de nacimiento de una persona calcular la cantidad de años que tiene

from datetime import  date, timedelta

var = date(2001, 11, 28)

var = date.today() - timedelta(var)

print(var)