# Hacer una funcion en Python que diga si una palabra es palindromo o no

i = 0
esCapicua = "Es palindromo"

a = input("Ingrese una palabra: ")

while esCapicua == "Es palindromo" and len(a) > i:
    if a[i] != a[len(a) - i - 1]:
        esCapicua = "No es palindromo"
    i += 1

print(esCapicua)