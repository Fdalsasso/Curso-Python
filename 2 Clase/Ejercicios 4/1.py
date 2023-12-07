# Cree una clase de Python llamada BankAccount que represente una cuenta bancaria, que tenga como atributos: número de cuenta (tipo numérico), nombre (nombre del propietario de la cuenta como tipo de cadena), saldo.
# Cree un constructor con parámetros: número de cuenta, nombre, saldo.
# Cree un método deposito() que gestione las acciones de depósito.
# Cree un método de retiro() que administre las acciones de retiro.
# Cree un método comisionBancaria() para aplicar las tarifas bancarias con un porcentaje del 5% del saldo de la cuenta.
# Cree un método display() para mostrar los detalles de la cuenta.

class BankAccount():
    
    def __init__(self, numeroDeCuenta, nombre, saldo):
        self.numeroDeCuenta = numeroDeCuenta
        self.nombre = nombre
        self.saldo = saldo

    def deposito(self, monto):
        self.saldo += monto

    def retiro(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto

    def comisionBancaria(self):
        self.saldo = self.saldo * 0.95

    def display(self):
        print("Cliente ", self.nombre, " su cuenta es la ", self.numeroDeCuenta, " y posee un saldo de ", self.saldo)