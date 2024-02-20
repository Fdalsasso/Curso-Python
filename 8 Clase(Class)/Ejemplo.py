import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Gaby2612',
            db = 'movies_utn'
        )

        self.cursor = self.connection.cursor() #para saber si funciona
        print("La conexion fue exitosa\n")
        self.cursor.close()
    
    def all_movies(self):
        sql = "SELECT * FROM movie LIMIT 10"

        self.cursor.execute(sql)
        users = self.cursor.fetchall()

        for user in users:
            print(user, "\t")

        self.cursor.close()

    def get_movie(self, title):
        querry = "SELECT * FROM movie WHERE title = UPPER('{}') ".format(title)

        try:
            self.cursor.execute(querry)
            movie = self.cursor.fetchone()
            print(movie)
            self.cursor.close()

        except Exception as e:
            print("No esxiste la pelicula\n")
            raise

    def new_movie(self, title, otrosDatos):
        querry = "INSERT INTO movie (title, otros datos) VALUES ('{}', '{})".format(title, otrosDatos)

        try:
            self.cursor.execute(querry)
            self.connection.commit()
            self.cursor.close()

        except Exception as e:
            print("No se creo la pelicula\n")
            raise
    
    def delete_movie(self,id):
        query="DELETE FROM movie WHERE movie_id='{}' ".format(id)
 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se elmino la pelicula")
            raise
 
    def update_movie(self,id, n_nombre):
        query="UPDATE movie SET title= '{}' WHERE movie_id = '{}'".format(n_nombre,id)
        try:  
            self.cursor.execute(query)
            self.connection.commit()
            self.cursor.close()
        except Exception as e:
            print("No se actualizo la pelicula")
            raise


mydb = Database()
mydb.get_user("Star Wars")