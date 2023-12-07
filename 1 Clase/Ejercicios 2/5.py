# Escribe un programa en Python que nos diga cuánto pagará un cliente en una tienda que da un descuento de $20 a los clientes que gastan más de $200 y compran más de 2 artículos.

compra = 1
valorTotal = 0
cantidadDeArticulos = -1

while compra != 0:
    compra = int(input("Ingrese valor de compra\n"))
    valorTotal += compra
    cantidadDeArticulos += 1

if valorTotal > 200 and cantidadDeArticulos > 2:
    valorTotal -= 20

print("Valor a pagar: ", valorTotal, "\nCantidad de productos: ", cantidadDeArticulos)