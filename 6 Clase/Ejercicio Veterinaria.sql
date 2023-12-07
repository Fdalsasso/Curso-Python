CREATE DATABASE sistema_veterinario;
USE sistema_veterinario;

CREATE TABLE veterinarios (
id_veterinario INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_veterinario VARCHAR (45) NOT NULL, 
telefono VARCHAR (15) NOT NULL,
PRIMARY KEY (id_veterinario)
);

CREATE TABLE duenios (
id_duenio INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_duenio VARCHAR (45) NOT NULL,
telefono VARCHAR (45) NOT NULL,
cantidad_de_mascotas TINYINT UNSIGNED NOT NULL,
PRIMARY KEY (id_duenio)
);

CREATE TABLE razas (
id_raza INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_raza VARCHAR (45) NOT NULL,
PRIMARY KEY (id_raza)
);

CREATE TABLE mascotas (
id_mascota INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_mascota VARCHAR (45) NOT NULL, 
id_duenio INT UNSIGNED NOT NULL,
id_raza INT UNSIGNED,
PRIMARY KEY (id_mascota),
CONSTRAINT fk_mascota_duenio FOREIGN KEY (id_duenio) REFERENCES duenios (id_duenio),
CONSTRAINT fk_mascota_raza FOREIGN KEY (id_raza) REFERENCES razas (id_raza)
);

CREATE TABLE turnos (
id_turno INT UNSIGNED NOT NULL AUTO_INCREMENT,
id_veterinario INT UNSIGNED NOT NULL,
id_mascota INT UNSIGNED NOT NULL,
id_duenio INT UNSIGNED NOT NULL,
fecha_hora DATETIME NOT NULL,
primary key (id_turno),
CONSTRAINT fk_turnos_veterinarios FOREIGN KEY (id_veterinario) REFERENCES veterinarios (id_veterinario),
CONSTRAINT fk_turnos_duenios FOREIGN KEY (id_duenio) REFERENCES duenios (id_duenio)
)