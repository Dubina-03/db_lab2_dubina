import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'DubinaOlga2003'
database = 'KDrama'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(name_genre), COUNT(name_genre) as amount_series
FROM genres INNER JOIN genre_series
ON genres.id = genre_series.genre_id
GROUP BY name_genre
ORDER BY amount_series;
'''
query_2 = '''
SELECT EXTRACT(YEAR FROM airing_date), COUNT(*) as amount_series
FROM all_series
GROUP BY EXTRACT(YEAR FROM airing_date)
ORDER BY EXTRACT(YEAR FROM airing_date);
'''
query_3 = '''
SELECT name_series, average_rating, birthday_avg
FROM all_series INNER JOIN  (SELECT rating_date.series_id, average_rating, birthday_avg FROM rating_date INNER JOIN 
                                (SELECT cast_series.series_id, AVG(EXTRACT(YEAR FROM birthday)) as birthday_avg 
                                FROM people INNER JOIN cast_series ON people.id = cast_series.actor_id 
					            GROUP BY series_id) AS t 
                            ON rating_date.series_id = t.series_id) AS t1
ON all_series.id = t1.series_id
ORDER BY average_rating;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print ("Database opened successfully")
    cur = conn.cursor()
    
    print('1.Кількість серіалів кожного жанру\n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('2.Кількість серілів відносно року випуску\n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('3.Популярність серіалу та середній рік народження акторів\n')
    cur.execute(query_3)
    for row in cur:
        print(row)
