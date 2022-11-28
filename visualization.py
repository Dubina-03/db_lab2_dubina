import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

username = 'postgres'
password = 'DubinaOlga2003'
database = 'k_drama'
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
SELECT TRIM(name_series), average_rating, birthday_avg
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
    
    cur.execute(query_1)
    genre = []
    amount_genre = []
    for row in cur:
        genre.append(row[0])
        amount_genre.append(row[1])

    cur.execute(query_2)
    years = []
    amount_season = []
    for row in cur:
        years.append(row[0])
        amount_season.append(row[1])

    cur.execute(query_3)
    series_popularity = []
    birth_year = []
    name = []
    for row in cur:
        if row[1]:
            name.append(row[0])
            series_popularity.append(row[1])
            birth_year.append(row[2])

fig, (bar_ax, pie_ax, dot_ax) = plt.subplots(1, 3)

bar_ax.set_title('Кількість серіалів кожного жанру')
bar_ax.set_xlabel('Жанр')
bar_ax.set_ylabel('Кількість')
bar_ax.bar(genre, amount_genre)
fig.autofmt_xdate(rotation=45)


pie_ax.pie(amount_season, labels=years)
pie_ax.set_title('Кількість серілів відносно року випуску')

data_query_3 = pd.DataFrame({'name':name, 'series_popularity':series_popularity, 'cast_popularity':birth_year})
dot_ax.set_title('Популярність серіалу та середній рік народження акторів')
sns.scatterplot(data = data_query_3, x = 'cast_popularity', y = 'series_popularity', ax = dot_ax, hue='name')
fig.autofmt_xdate(rotation=45)


plt.get_current_fig_manager().resize(1900, 900)
plt.subplots_adjust(left=0.1,
                    bottom=0.321,
                    right=0.9,
                    top=0.967,
                    wspace=0.76,
                    hspace=0.195)
plt.show()