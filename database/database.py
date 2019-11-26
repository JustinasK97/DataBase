import sqlite3
from movies.movie import movie
from movies.profit import profit



def open_connection():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

def create_movies_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS movies(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   movie_title TEXT UNIQUE,
                   director TEXT,
                   movie_year TEXT,
                   movie_time REAL)
                """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def create_profit_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS publishers (
                            movie_id integer PRIMARY KEY AUTOINCREMENT,
                            movie_rating TEXT,
                            international_sales TEXT)
                        """

        cursor.execute(query)
    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)

create_movies_table()
create_profit_table()
def create_movie(movie):
    try:
        connection, cursor = open_connection()

        query = "INSERT INTO movies VALUE (?, ?, ?, ?, ?)"
        query_parameters = (movie.id, movie.movie_title, movie.director, movie.movie_year, movie.movie_time)

        cursor.execute(query, query_parameters)

        connection.commit()

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)

movie1 = movie(1, "Toy Story"	"John Lasseter"	1995	81)
create_movie(movie1)
def get_movie(movie)
    try:
        connection, cursor = open_connection()

        query =
