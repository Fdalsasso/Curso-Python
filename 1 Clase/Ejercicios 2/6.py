# Escribir un programa en Python que nos diga cuánto pagará un cliente en una tienda que da un 25% de descuento a los clientes que gastan más de $500 o compran más de 3 artículos.

compra = 1
valorTotal = 0
cantidadDeArticulos = -1

while compra != 0:
    compra = int(input("Ingrese valor de compra\n"))
    valorTotal += compra
    cantidadDeArticulos += 1

if valorTotal > 500 or cantidadDeArticulos > 3:
    valorTotal = valorTotal * 3 / 4

print("Valor a pagar: ", valorTotal, "\nCantidad de productos: ", cantidadDeArticulos)