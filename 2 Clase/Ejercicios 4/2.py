# Defina una clase de nombre “círculo” que permita crear un círculo C (O, r) con centro O(a, b) y radio r
# Defina un método Area() de la clase que calcule el área del círculo.
# Defina un método Perimeter() de la clase que le permita calcular el perímetro del círculo.
# Defina un método testBelongs() de la clase que permita probar si un punto A(x, y) pertenece al círculo C(O, r) o no.

from cmath import pi


class circulo():

    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio

    def area(self):
        area = pi * self.radio ** 2
        return area

    def perimeter(self):
        perimetro = 2 * pi * self.radio
        return perimetro

    def testBelongs(self, x, y):
        if(x - self.x) ** 2 + (y - self.y) ** 2 <= self.radio ** 2:
            print("Pertenece")
        else:
            print("No pertenece")