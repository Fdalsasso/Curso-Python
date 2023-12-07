import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Gaby2612',
            db = 'granelco'
        )
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa\n")
        self.cursor.close()
    
    def all_cuentas(self):
        sql = "SELECT * FROM cuenta"
        self.cursor.execute(sql)
        cuentas = self.cursor.fetchall()
        for cuenta in cuentas:
            print(cuenta, "\t")
        self.cursor.close()

    def get_cuenta(self, id):
        querry = "SELECT * FROM cuenta WHERE idCuenta = '{}' ".format(id)
        try:
            self.cursor.execute(querry)
            cuenta = self.cursor.fetchone()
            print(cuenta)
            self.cursor.close()
        except Exception as e:
            print("No esxiste la cuenta\n")
            raise

    def new_cuenta(self, pin, saldo_pesos, saldo_dolares):
        querry = "INSERT INTO cuenta (pin, saldo_pesos, saldo_dolares) VALUES ('{}', '{}', '{}')".format(pin, saldo_pesos, saldo_dolares)
        try:
            self.cursor.execute(querry)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se creo la cuenta\n")
            raise
    
    def delete_cuenta(self,id):
        query="DELETE FROM cuenta WHERE idCuenta='{}' ".format(id) 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se elmino la cuenta")
            raise
 
    def update_cuenta_pin(self,id, nuevo_pin):
        query="UPDATE cuenta SET pin= '{}' WHERE idCuenta = '{}'".format(nuevo_pin,id)
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se actualizo la cuenta")
            raise

    def all_tarjetas(self):
        sql = "SELECT * FROM tarjeta"
        self.cursor.execute(sql)
        tarjetas = self.cursor.fetchall()
        for tarjeta in tarjetas:
            print(tarjeta, "\t")
        self.cursor.close()

    def get_tarjeta(self, id):
        querry = "SELECT * FROM tarjeta WHERE idTarjeta = '{}' ".format(id)
        try:
            self.cursor.execute(querry)
            tarjeta = self.cursor.fetchone()
            print(tarjeta)
            self.cursor.close()
        except Exception as e:
            print("No esxiste la tarjeta\n")
            raise

    def new_tarjeta(self, numero, vencimiento, codigo, estado):
        querry = "INSERT INTO tarjeta (numero, vencimiento, codigo) VALUES ('{}', '{}', '{}', 'Activo')".format(numero, vencimiento, codigo)
        try:
            self.cursor.execute(querry)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se creo la tarjeta\n")
            raise
    
    def delete_tarjeta(self,id):
        query="DELETE FROM tarjeta WHERE idTarjeta='{}' ".format(id) 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se elmino la tarjeta")
            raise

    def update_tarjeta_estado(self,id, nuevo_estado):
        query="UPDATE tarjeta SET estado= '{}' WHERE idTarjeta = '{}'".format(nuevo_estado,id)
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se actualizo la cuenta")
            raise
    
    def all_personas(self):
        sql = "SELECT * FROM persona"
        self.cursor.execute(sql)
        personas = self.cursor.fetchall()
        for persona in personas:
            print(persona, "\t")
        self.cursor.close()

    def get_persona(self, id):
        querry = "SELECT * FROM persona WHERE idPersona = '{}' ".format(id)
        try:
            self.cursor.execute(querry)
            persona = self.cursor.fetchone()
            print(persona)
            self.cursor.close()
        except Exception as e:
            print("No esxiste la persona\n")
            raise

    def new_persona(self, nombre, DNI, nacimiento, profesion, genero):
        querry = "INSERT INTO persona (nombre, DNI, nacimiento, profesion, genero) VALUES ('{}', '{}', '{}', '{}', '{}')".format(nombre, DNI, nacimiento, profesion, genero)
        try:
            self.cursor.execute(querry)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se creo la persona\n")
            raise
    
    def delete_persona(self,id):
        query="DELETE FROM persona WHERE idPersona='{}' ".format(id) 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se elmino la persona")
            raise
 
    def update_persona_profesion(self,id, nueva_profesion):
        query="UPDATE persona SET profesion= '{}' WHERE idPersona = '{}'".format(nueva_profesion,id)
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se actualizo la persona")
            raise

    def update_persona_profesion(self,id, nuevo_genero):
        query="UPDATE persona SET genero= '{}' WHERE idPersona = '{}'".format(nuevo_genero,id)
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se actualizo la persona")
            raise
    
    def all_movimientos(self):
        sql = "SELECT * FROM movimiento"
        self.cursor.execute(sql)
        movimientos = self.cursor.fetchall()
        for movimiento in movimientos:
            print(movimiento, "\t")
        self.cursor.close()


    def new_movimiento(self, fecha, accion, monto):
        querry = "INSERT INTO movimiento (fecha, accion, monto) VALUES ('{}', '{}', '{}')".format(fecha, accion, monto)
        try:
            self.cursor.execute(querry)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se creo la movimiento\n")
            raise
    
    def delete_movimiento(self,id):
        query="DELETE FROM movimiento WHERE idMovimiento='{}' ".format(id) 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se elmino la movimiento")
            raise

mydb = Database()
mydb.get_user("Star Wars")