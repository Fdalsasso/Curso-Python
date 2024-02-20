/* Actores que tienen de primer nombre ‘Scarlett’.
    Actors whose first name is 'Scarlett'. */

SELECT * FROM actor
WHERE UPPER(first_name) = 'SCARLETT'

/* Actores que tienen de apellido ‘Johansson’.
    Actors whose last name is 'Johansson'. */

SELECT * FROM actor
WHERE UPPER(last_name) = 'JOHANSSON'

/* Actores que contengan una ‘O’ en su nombre.
    Actors who contain an 'O' in their name. */

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%'

/* Actores que contengan una ‘O’ en su nombre y en una ‘A’ en su apellido.
    Actors who contain an 'O' in their first name and an 'A' in their last name. */

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%' AND UPPER(last_name) LIKE '%A%'

/* Actores que contengan dos ‘O’ en su nombre y en una ‘A’ en su apellido.
    Actors who contain two 'O's in their first name and an 'A' in their last name. */

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%O%' AND UPPER(last_name) LIKE '%A%'

/* Actores donde su tercera letra sea ‘B’. 
    Actors where their third letter is 'B'. */

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '__B%'

/* Ciudades que empiezan por ‘a’.
    Cities that start with 'a'. */

SELECT * FROM city
WHERE UPPER(city) LIKE 'A%'

/* Ciudades que acaban por ‘s’.
    Cities that end with 's'. */

SELECT * FROM city
WHERE UPPER(city) LIKE '%S'

/* Ciudades del country 61.
    Country cities 61. */

SELECT * FROM city
WHERE country_id = 61

/* Ciudades del country ‘Spain’.
    Cities of country 'Spain'. */

SELECT * FROM city
WHERE country_id = (SELECT country_id FROM country WHERE UPPER(country) = 'SPAIN')

/* Ciudades con nombres compuestos.
    Cities with compound names. */

SELECT * FROM city
WHERE city LIKE "% %"

/* Películas con una duración entre 80 y 100.
    Movies with a duration between 80 and 100. */

SELECT * FROM film
WHERE length BETWEEN 80 AND 100

/* Peliculas con un rental_rate entre 1 y 3.
    Movies with a rental_rate between 1 and 3. */

SELECT * FROM film
WHERE rental_rate BETWEEN 1 AND 3

/* Películas con un titulo de más de 12 letras.
    Movies with a title of more than 12 letters. */

SELECT * FROM film
WHERE length(title) > 11

/* Peliculas con un rating de PG o G.
    Movies with a PG or G rating. */

SELECT * FROM film
WHERE UPPER(rating) = 'PG' OR UPPER(rating) = 'G'

/* Peliculas que no tengan un rating de NC-17.
    Movies that do not have a rating of NC-17. */

SELECT * FROM film
WHERE UPPER(rating) != 'NC-17'

/* Peliculas con un rating PG y duracion de más de 120.
    Movies with a PG rating and duration of more than 120. */

SELECT * FROM film
WHERE UPPER(rating) = 'PG' AND length > 119

/* ¿Cuantos actores hay?
    How many actors are there? */

SELECT count(actor_id) as cantidad_de_actores FROM actor

/* ¿Cuántas ciudades tiene el country ‘Spain’?
    How many cities does country 'Spain' have? */

SELECT count(city) as cantidad_de_ciudades FROM city
WHERE country_id = (SELECT country_id FROM country WHERE UPPER(country) = 'SPAIN')

/* ¿Cuántos paises hay que empiezan por ‘a’?
    How many countries are there that start with 'a'? */

SELECT count(country) as cantidad FROM country
WHERE country LiKE "A%"

/* Media de duración de peliculas con PG.
    Average duration of movies with PG. */

SELECT avg(length) as duracion_total FROM film
WHERE UPPER(rating) = "PG"

/* Suma de rental_rate de todas las peliculas.
    Sum of rental_rate of all movies. */

SELECT sum(rental_rate) as suma FROM film

/* Pelicula con mayor duración.
    Movie with the longest duration. */

SELECT max(length) FROM film

/* Película con menor duración.
    Shorter duration movie. */

SELECT min(length) FROM film

/* Mostrar las ciudades del country Spain (multitabla).
    Show the cities of the country Spain (multitable). */

SELECT * FROM city
INNER JOIN country ON country.country_id = city.country_id AND UPPER(country.country) = "SPAIN"

/* Mostrar el nombre de la película y el nombre de los actores.
    Show the name of the movie and the name of the actors. */

SELECT film.title, actor.first_name, actor.last_name FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id

/* Mostrar el nombre de la película y el de sus categorías.
    Show the name of the movie and its categories. */

SELECT film.title, category.name FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id

/* Mostrar el country, la ciudad y dirección de cada miembro del staff.
    Show the country, city and address of each staff member. */

SELECT country.country, c.city, a.address FROM staff as s
INNER JOIN address as a ON a.address_id = s.address_id
INNER JOIN city as c ON a.city_id = c.city_id
INNER JOIN country ON country.country_id = c.country_id

/* Mostrar el country, la ciudad y dirección de cada customer.
    Show the country, city and address of each customer. */

SELECT country.country, c.city, a.address FROM customer
INNER JOIN address as a ON a.address_id = customer.address_id
INNER JOIN city as c ON a.city_id = c.city_id
INNER JOIN country ON country.country_id = c.country_id

/* Numero de películas de cada rating
    Number of movies of each rating */

SELECT rating, count(*) FROM film
GROUP BY rating

/* Cuantas películas ha realizado el actor ED CHASE.
    How many films has actor ED CHASE made. */

SELECT first_name, last_name, count(*) FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
WHERE first_name = 'ED' AND last_name = 'CHASE'
GROUP BY first_name, last_name

/* Media de duración de las películas cada categoría.
    Average length of films in each category. */

SELECT name, avg(film.length) FROM category
INNER JOIN film_category ON film_category.category_id = category.category_id
INNER JOIN film ON film.film_id = film_category.film_id
GROUP BY category.name