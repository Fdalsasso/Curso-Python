CREATE DATABASE sistemasalud;
USE sistemasalud;

CREATE TABLE paises (
id_pais TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_pais VARCHAR(45) NOT NULL,
PRIMARY KEY (id_pais));

CREATE TABLE medicos (
id_medico INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_medico VARCHAR (45) NOT NULL, 
telefono VARCHAR(15) NOT NULL,
primary key(id_medico));

CREATE TABLE pacientes (
id_paciente INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_paciente VARCHAR (45) NOT NULL, 
telefono VARCHAR(15) NOT NULL,
nacionalidad TINYINT UNSIGNED NOT NULL,
PRIMARY KEY (id_paciente),
CONSTRAINT fk_pacientes_paises FOREIGN KEY(nacionalidad) REFERENCES paises (id_pais));

CREATE TABLE turnos (
id_turno INT UNSIGNED NOT NULL AUTO_INCREMENT,
id_medico INT UNSIGNED NOT NULL,
id_paciente INT UNSIGNED NOT NULL,
fecha_hora DATETIME NOT NULL,
primary key (id_turno),
CONSTRAINT fk_turnos_pacientes FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
CONSTRAINT fk_turnos_medicos FOREIGN KEY (id_medico) REFERENCES medicos (id_medico))
