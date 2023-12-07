# 1
texto1 = input("Primer texto\n")
texto2 = input("Segundo texto\n")

print(texto1 + " " + texto2)

# 2

numero1 = input("Primer numero\n")
numero2 = input("Segundo numero\n")

print(int(numero1 + numero2))

# 3

celsius = input("Ingrese grados celsius\n")

kelvin = celsius + 273.15

print(kelvin)

# 4

celsius1 = input("Ingrese grados celsius\n")

fahrenheit = (celsius1 * 9/5) + 32

print(fahrenheit)

# 5

opcion = input("Ingrese 1 para pasar de celsius a kelvin, sino otra tecla\n")
celsius2 = input("Ingrese grados celsius\n")

if opcion == 1:
    resu = celsius2 + 273.15
else:
    resu = (celsius2 * 9/5) + 32

# 6

numero3 = int(input("Numero\n"))

resto = numero3 % 2
if resto == 0:
    print("Es par")
else:
    print("Es impar")

# 7

valorInicial = 0

valorFinal = input("Ingrese un numero\n")

for contador in range (0, valorFinal):
    valorInicial += contador

# 8

numero4 = 1
promedio = 0
cantidadDeNumeros = -1

while numero4 != 0:
    numero4 = int(input("Ingrese valor de compra\n"))
    promedio += numero4
    cantidadDeNumeros += 1

promedio = promedio / cantidadDeNumeros

print(promedio)

# 9

numero5 = int(input("Primer numero\n"))
numero6 = int(input("Segundo numero\n"))

if numero5 < numero6:
    print("El numero " + numero3 + "es mayor")
elif numero5 > numero6:
    print("El numero " + numero2 + "es mayor")
else:
    print("Ambos numeros son iguales, no tenias que ingresar numeros iguales")

# 10

variable = True

numero7 = int(input("Numero\n"))

for i in range(2, numero7-1):
    if (numero7 % i) == 0:
        variable = False

if variable == True:
    print("Es primo")
else:
    print("No es primo")

# 11

numero8 = int(input("Primer numero\n"))
numero9 = int(input("Segundo numero\n"))
numero10 = int(input("Tercer numero\n"))

valor = max(numero8, numero8, numero10)

print(valor)