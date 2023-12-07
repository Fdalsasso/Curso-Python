# 4.Hacer una lista con los estudiantes aprobados y una con los desaprobados. Para estar aprobados la nota tiene que ser mayor o igual a 12

from optparse import Values


df = {"student_1" : 13 , "student_2" : 17 , "student_3" : 9 , "student_4" : 15 , "student_5" : 8 ,
"student_6" : 14 , "student_7" : 16 , "student_8" : 12 , "student_9" : 13 , "student_10" : 15 ,
"student_11" : 14 , "student_112" : 9 , "student_13" : 10 , "student_14" : 12 , "student_15" :
13 , "student_16" : 7 , "student_17" : 12 , "student_18" : 15 , "student_19" : 9 , "student_20"
: 17 }

aprobados = []
desaprobados = []

#for elem in df:
#    if df.get(elem) > 11:
#        aprobados.append(elem)
#    else:
#        desaprobados.append(elem)

for key, value in df.items():
    if value > 11:
        aprobados.append(key)
    else:
        desaprobados.append(key)

print(aprobados)
print(desaprobados)