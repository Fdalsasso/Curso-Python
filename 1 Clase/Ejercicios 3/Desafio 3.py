# Escribe una función de Fibonacci

def fibonacci(numero):
    if numero < 3:
        resu = 1
    else:
        resu = fibonacci(numero-1) + fibonacci(numero - 2)
    return resu

fibo = int(input("Ingrese numero\n"))

resultado = fibonacci(fibo)

print("El resultado es: ", resultado)