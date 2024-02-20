INSERT INTO duenios (nombre_duenio, telefono, cantidad_de_mascotas)
 VALUES ("Gustavo", "11-4071-0744", 1), 
("Facundo", "11-5707-2015", 1), 
("Rodrigo", "11-1234-5678", 4)

INSERT INTO mascotas (nombre_mascota, id_duenio)
VALUES ("Mayra", (SELECT id_duenio FROM duenios
WHERE nombre_duenio = "Facundo"))

SELECT * FROM duenios
INNER JOIN mascotas ON mascotas.id_duenio = duenios.id_duenio