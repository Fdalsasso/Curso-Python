# 7Escriba un programa en Python donde el usuario elija una opción (sumar, restar, multiplicar, dividir) e insertar dos números. El programa realizará la operación seleccionada y mostrará el resultado.

operacion = input("Ingrese suma, resta, multiplicacion o division\n")
numero8 = int(input("Ingrese el primer numero\n"))
numero9 = int(input("Ingrese el segundo numero\n"))

if operacion == "suma":
    print(numero8 + numero9)
elif operacion == "resta":
    print(numero8 - numero9)
elif operacion == "multiplicacion":
    print(numero8 * numero9)
elif operacion == "division":
    print(numero8 / numero9)
else:
    print("Operacion no valida")