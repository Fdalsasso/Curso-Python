# Proyecto Final Capacitacion Capgemini/Capgemini Final Training Project


## Grupo/Group  3: 
Integrantes/Members: Agustina Mercedes Garro, Facundo Nahuel Dalsasso, Juan Pablo Castiglione, Ezequiel Arroyo, Juan Cruz Rey Alvarez.




# Temas y Herramientas Involucrados : 
# Topics and Tools Involved:


### Lenguaje:
### Language:
* Python

### Web Framework:
* Django

### B.D. Relacional:
### Relational D.B.:
* SQL
* Package pymysql

### Arquitectura:
### Architecture:
* Modelo Vista Template (MVT)
* Servidor Liviano/Lightweight Server
* Template Engine: Jinja

### Vistas: 
### Views:
* HTML
* CSS
* JavaScript

### Python Dates:
* DateTime

### Computer Vision:
* Open cv

### Intercambio De Datos:
### Data Exchange:
* Json
	







## Nuestro Proyecto: 

El proyecto elegido fue el desarrollo de un foro donde las personas pueden registrarse mediante distintos roles tales como escritores o comentadores,  una vez registrados los primeros tienen la posibilidad de escribir distintos artículos distinguiendolos por categorías, asignándoles un título y su respectivo desarrollo. En cambio los comentadores complementan a los escritores leyendo sus artículos y realizando comentarios del mismo.
Desde ya una persona puede ser escritor y comentarista a la vez pero deberá iniciar sesión con su cuenta correspondiente.

Los comentaristas tienen la posibilidad de buscar artículos mediante un filtro avanzado donde seleccionan la categoría del artículo que desean leer, tal puede ser Entretenimiento, Historia o Filosofía. A los artículos escritos se les asigna el autor correspondiente y la fecha de creación del mismo. 

En caso de haber cometido un error en la subida del artículo, el escritor tiene la posibilidad de editar su artículo, o en caso de querer eliminarlo también tiene la posibilidad. 

El proyecto fue desarrollado priorizando la mantenibilidad del mismo, en caso de querer desarrollar un nuevo requerimiento, el proyecto se encuentra en buen estado para sufrir mejoras o cualquier tipo de cambio necesario.


Para correr el proyecto:
* En MySQL:
  * Correr el script ScriptBD/Foro.sql
  * Hacer un data import de los contenidos de ScriptBD/Dump data
* En una terminal correr los siguientes comandos:
  * cd .\tp-academiapython-grupo3-foro-main\foro\
  * python manage.py runserver





## Our project:

The chosen project was the development of a forum where people can register through different roles such as writers or commentators. Once registered, the former have the possibility of writing different articles, distinguishing them by categories, assigning them a title and their respective development. On the other hand, the commentators complement the writers by reading their articles and making comments on them.
From now on, a person can be a writer and commentator at the same time but they must log in with their corresponding account.

Commenters have the ability to search for articles using an advanced filter where they select the category of the article they want to read, such as Entertainment, History or Philosophy. Written articles are assigned the corresponding author and the date of creation.

In case of having made a mistake in uploading the article, the writer has the possibility of editing his article, or if he wants to delete it, he also has the possibility.

The project was developed prioritizing its maintainability, in case you want to develop a new requirement, the project is in good condition to undergo improvements or any type of necessary change.


To run the project:
* In MySQL:
  * Run the script ScriptBD/Foro.sql
  * Make a data import of the contents of ScriptBD/Dump data
* In a terminal run the following commands:
  * cd .\tp-academiapython-grupo3-foro-main\foro\
  * python manage.py runserver