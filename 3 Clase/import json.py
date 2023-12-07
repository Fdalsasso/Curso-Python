import json

class persona():
    
    def __init__(self, nombre, apellido, mascotas):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascotas

persona1 = persona("Facundo", "Dalsasso", ["Zimba", "Mayra"])
persona2 = persona("Pepe", "Loco", [])
persona3 = persona("Gustavo", "Haite Gullota", "Bruce")

persona1 = persona1.__dict__
persona2 = persona2.__dict__
persona3 = persona3.__dict__

lista = [persona1, persona2, persona3]

cadena_texto = json.dumps(lista) #convierte a texto plano las cosas

print(cadena_texto)
print(type(cadena_texto))

jsonFile = open("jsonTexto.json", "a")
jsonFile.write(cadena_texto)
jsonFile.close()

