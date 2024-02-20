/* Hacer un listado de todas las películas con todos sus atributos.
    Make a list of all the movies with all their attributes. */

select * from movie

/* Hacer un listado de todas las compañías productoras
    Make a list of all the production companies */

select * from production_company

/* Hacer un listado con ell nombre y apellido de los actores.
    Make a list with the name and surname of the actors. */

select person_name from person

/* Hacer un listado cuyo rating sea mayor a 6.
    Make a list whose rating is greater than 6. */

select * from movie
where vote_average > 6

/* Hacer un listado con las películas con promedio mayor a 9 y que duren menos de 3 horas.
    Make a list of movies with an average greater than 9 and that last less than 3 hours. */

select * from movie
where vote_average > 9 and runtime < 120

/* Hacer un listado con todas las películas que contienen en su título la palabra “Star”
    Make a list of all the movies that contain the word “Star” in their title */

select * from movie
where title like "%Star%"

/* Hacer un listado de las películas desde las que más duran a las que menos duran
    Make a list of the movies from those that last the longest to those that last the least */

select * from movie
order by runtime desc

/* Hacer un top 10 de películas según su puntuación .
    Make a top 10 movies according to their score. */

select * from movie
order by vote_average desc
limit 10

/* Hacer un listado con todas las películas que terminan con “Wars”
    Make a list of all the movies that end with “Wars” */

select * from movie
where title like "%Star"

/* Hacer un listado de todas las películas que se lanzaron antes del 2006
    Make a list of all the movies that were released before 2006 */
    
select * from movie
WHERE YEAR(release_date) <2006