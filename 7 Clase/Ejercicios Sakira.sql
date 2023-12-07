-- Ejercicio 1. Actores que tienen de primer nombre ‘Scarlett’.

SELECT * FROM actor
WHERE UPPER(first_name) = 'SCARLETT'

-- Ejercicio 2. Actores que tienen de apellido ‘Johansson’.

SELECT * FROM actor
WHERE UPPER(last_name) = 'JOHANSSON'

-- Ejercicio 3. Actores que contengan una ‘O’ en su nombre.

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%'

-- Ejercicio 4. Actores que contengan una ‘O’ en su nombre y en una ‘A’ en su apellido.

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%' AND UPPER(last_name) LIKE '%A%'

-- Ejercicio 5. Actores que contengan dos ‘O’ en su nombre y en una ‘A’ en su apellido.

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '%O%O%' AND UPPER(last_name) LIKE '%A%'

-- Ejercicio 6. Actores donde su tercera letra sea ‘B’.

SELECT * FROM actor
WHERE UPPER(first_name) LIKE '__B%'

-- Ejercicio 7. Ciudades que empiezan por ‘a’.

SELECT * FROM city
WHERE UPPER(city) LIKE 'A%'

-- Ejercicio 8. Ciudades que acaban por ‘s’.

SELECT * FROM city
WHERE UPPER(city) LIKE '%S'

-- Ejercicio 9. Ciudades del country 61.

SELECT * FROM city
WHERE country_id = 61

-- Ejercicio 10. Ciudades del country ‘Spain’.

SELECT * FROM city
WHERE country_id = (SELECT country_id FROM country WHERE UPPER(country) = 'SPAIN')

-- Ejercicio 11. Ciudades con nombres compuestos.

SELECT * FROM city
WHERE city LIKE "% %"

-- Ejercicio 12. Películas con una duración entre 80 y 100.

SELECT * FROM film
WHERE length BETWEEN 80 AND 100

-- Ejercicio 13. Peliculas con un rental_rate entre 1 y 3.

SELECT * FROM film
WHERE rental_rate BETWEEN 1 AND 3

-- Ejercicio 14. Películas con un titulo de más de 12 letras.

SELECT * FROM film
WHERE length(title) > 11

-- Ejercicio 15. Peliculas con un rating de PG o G.

SELECT * FROM film
WHERE UPPER(rating) = 'PG' OR UPPER(rating) = 'G'

-- Ehercicio 16. Peliculas que no tengan un rating de NC-17.

SELECT * FROM film
WHERE UPPER(rating) != 'NC-17'

-- Ejercicio 17. Peliculas con un rating PG y duracion de más de 120.

SELECT * FROM film
WHERE UPPER(rating) = 'PG' AND length > 119

-- Ejercicio 18. ¿Cuantos actores hay?

SELECT count(actor_id) as cantidad_de_actores FROM actor

-- Ejercicio 19. ¿Cuántas ciudades tiene el country ‘Spain’?

SELECT count(city) as cantidad_de_ciudades FROM city
WHERE country_id = (SELECT country_id FROM country WHERE UPPER(country) = 'SPAIN')

-- Ejercicio 20. ¿Cuántos countries hay que empiezan por ‘a’?

SELECT count(country) as cantidad FROM country
WHERE country LiKE "A%"

-- Ejercicio 21. Media de duración de peliculas con PG.

SELECT avg(length) as duracion_total FROM film
WHERE UPPER(rating) = "PG"

-- Ejercicio 22. Suma de rental_rate de todas las peliculas.

SELECT sum(rental_rate) as suma FROM film

-- Ejercicio 23. Pelicula con mayor duración.

SELECT max(length) FROM film

-- Ejercicio 24. Película con menor duración.

SELECT min(length) FROM film

-- Ejercicio 25. Mostrar las ciudades del country Spain (multitabla).

SELECT * FROM city
INNER JOIN country ON country.country_id = city.country_id AND UPPER(country.country) = "SPAIN"

-- Ejercicio 26. Mostrar el nombre de la película y el nombre de los actores.

SELECT film.title, actor.first_name, actor.last_name FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id

-- Ejercicio 27. Mostrar el nombre de la película y el de sus categorías.

SELECT film.title, category.name FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id

-- Ejercicio 28. Mostrar el country, la ciudad y dirección de cada miembro del staff.

SELECT country.country, c.city, a.address FROM staff as s
INNER JOIN address as a ON a.address_id = s.address_id
INNER JOIN city as c ON a.city_id = c.city_id
INNER JOIN country ON country.country_id = c.country_id

-- Ejercicio 29. Mostrar el country, la ciudad y dirección de cada customer.

SELECT country.country, c.city, a.address FROM customer
INNER JOIN address as a ON a.address_id = customer.address_id
INNER JOIN city as c ON a.city_id = c.city_id
INNER JOIN country ON country.country_id = c.country_id

-- Ejercicio 30. Numero de películas de cada rating

SELECT rating, count(*) FROM film
GROUP BY rating

-- Ejercicio 31. Cuantas películas ha realizado el actor ED CHASE.

SELECT first_name, last_name, count(*) FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
WHERE first_name = 'ED' AND last_name = 'CHASE'
GROUP BY first_name, last_name

-- Ejercicio 32. Media de duración de las películas cada categoría.

SELECT name, avg(film.length) FROM category
INNER JOIN film_category ON film_category.category_id = category.category_id
INNER JOIN film ON film.film_id = film_category.film_id
GROUP BY category.name