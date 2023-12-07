# Utilizando el archivo JSON brindado:
# busque y muestre el pokemon numero 54
# cree la función Pokédex que le permita buscar por número o nombre un pokemon y le de su información
# contar cuantos pokemones hay de cada tipo(tipo 1) y mostrar por pantalla
# Buscar el pokemon con ataque más poderoso (Attack) que no sea dragón ni legendario

import json

def buscar(lista, pokemon):
    if type(pokemon) == int:
        return lista[pokemon - 1]
    else:
        for i in lista:
            if i['Name'] == pokemon:
                return i
        
def tipos(lista):
    df = {}
    for elem in lista:
        if df.get(elem['Type 1']) == None:
            df[elem['Type 1']] = 1
        else:
            df[elem['Type 1']] += 1
    return df

def masPoderoso(lista):
    primero = lista[0]
    for pokemon in lista:
        if pokemon['Attack'] > primero['Attack'] and pokemon['Type 1'] != 'Dragon' and pokemon['Type 2'] != 'Dragon' and pokemon['Legendary'] == 'FALSO':
            primero = pokemon
    return primero


lista = []
df = {}

with open("poke.json", "r") as pokemones:
    data = json.load(pokemones)
    for i in data:
        lista.append(i)


print(masPoderoso(lista))