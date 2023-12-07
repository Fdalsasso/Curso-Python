# Top ten de peliculas del 2000 en adelante que tienen mas de 20 actores
select title, count(*) as cant_act from movie
inner join movie_cast ON movie.movie_id=movie_cast.movie_id
inner join person ON person.person_id= movie_cast.person_id
WHERE YEAR(movie.release_date)>=2000
group by title
HAVING cant_act>20
order by cant_act desc
limit 10 offset 1
