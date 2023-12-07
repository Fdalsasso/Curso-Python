# Crear una clase de cálculo con un constructor predeterminado (sin parámetros) que permita realizar varios cálculos en números enteros.
# Crear un método llamado Factorial() que permita calcular el factorial de un entero. Pruebe el método instanciando la clase.
# Crear un método llamado Sum() que permita calcular la suma de los primeros n enteros 1 + 2 + 3 + .. + n. Pruebe este método.
# Cree un método llamado testPrimo() en la clase calculo para probar si un numero es primo o no
# Cree un método tablaDeMultiplicar() que cree y muestre la tabla de multiplicar de un entero dado. Luego cree un método tablaDeMultiplicar() para mostrar todas las tablas de multiplicar de enteros 1, 2, 3, ..., 9.
# Cree un método estático listaDivisores() que obtenga todos los divisores de un entero dado en una nueva lista llamada Ldiv. Cree otro método listaDivisoresPrimos() que obtenga todos los divisores primos de un entero dado.

class calculo():

    def factorial(self, numero):
        for i in range(2, numero):
            numero = numero * i

    def sum(self, numero):
        suma = 0
        for i in range(numero + 1):
            suma += i
        return suma

    def testPrimo(self, numero):
        variable = True
        for i in range(2, numero-1):
            if (numero % i) == 0:
                variable = False

        if variable == True:
            print("Es primo")
        else:
            print("No es primo")

    def tablaDeMultiplicar(self, numero):
        lista = []
        for i in range(1, 11):
            lista.append(i * numero)
            print(lista[i - 1], "\t")

    def tablasDeMultiplicar(self):
        lista = []
        for i in range (1, 11):
            lista.append(self.tablaDeMultiplicar(i))
            print("\n")
    
pepe = calculo()
pepe.tablasDeMultiplicar()