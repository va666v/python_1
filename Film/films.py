import sqlite3
import json

db = sqlite3.connect("film_data.db")
sql = db.cursor()


def film_name_with_b():
    select_films = []
    for name in sql.execute("SELECT title FROM film_data"):
        a = name[0]
        b = a.split()
        if b[0][0] == "B":
            select_films.append(a)
        else:
            continue
    print(select_films)
    db.commit()

def max_length_film():
    select_films = []
    for len in sql.execute("SELECT length FROM film_data"):
        select_films.append(len[0])
    max_ = max(select_films)
    # name = sql.execute(f"SELECT title FROM film_data WHERE length = {max_}") haw to print name and length
    print(max_)
    db.commit()


def from_db2json():
    items = []
    for item in sql.execute("SELECT * FROM film_data ORDER BY film_id"):
        items.append(item)
    # for film_id, title, desc, release_year, length, rate, special_fratures in sql.execute("SELECT * FROM film_data ORDER BY film_id"):
    #     json_path = {
    #         'film_id' = film_id,
    #         'title' = title,
    #         "desc" = desc,
    #         'release_year' = release_year,
    #         'length' = length,
    #         'rate' = rate,
    #         'special_fratures' = special_fratures
    #     }
    #
    with open('film_data.json', "a") as fl:
        json.dump(items, fl, indent=4)
    db.commit()


def filtered_film():
    #above 2010 and rate is between 3 and 5
    for item in sql.execute("SELECT * FROM film_data WHERE release_year > 2010 AND 3 < rate < 5"):
        print(item)
    db.commit()






# film_name_with_b()
# max_length_film()
# from_db2json()
# filtered_film()

