-- 1
select * from movie

-- 2
select * from production_company

-- 3
select person_name from person

-- 4
select * from movie
where vote_average > 6

-- 5
select * from movie
where vote_average > 9 and runtime < 120

-- 6
select * from movie
where title like "%Star%"

-- 7
select * from movie
order by runtime desc

-- 8
select * from movie
order by vote_average desc
limit 10

-- 9
select * from movie
where title like "%Star"

-- 10
select * from movie
WHERE YEAR(release_date) <2006