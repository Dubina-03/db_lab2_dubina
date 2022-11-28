--Кількість серіалів кожного жанру
SELECT TRIM(name_genre), COUNT(name_genre) as amount_series
FROM genres INNER JOIN genre_series
ON genres.id = genre_series.genre_id
GROUP BY name_genre
ORDER BY amount_series;

--Кількість серілів відносно року випуску
SELECT EXTRACT(YEAR FROM airing_date), COUNT(*) as amount_series
FROM all_series
GROUP BY EXTRACT(YEAR FROM airing_date)
ORDER BY EXTRACT(YEAR FROM airing_date);

--Популярність серіалу та середній рік народження акторів
SELECT name_series, average_rating, birthday_avg
FROM all_series INNER JOIN  (SELECT rating_date.series_id, average_rating, birthday_avg FROM rating_date INNER JOIN 
                                (SELECT cast_series.series_id, AVG(EXTRACT(YEAR FROM birthday)) as birthday_avg 
                                FROM people INNER JOIN cast_series ON people.id = cast_series.actor_id 
					            GROUP BY series_id) AS t 
                            ON rating_date.series_id = t.series_id) AS t1
ON all_series.id = t1.series_id
ORDER BY average_rating;