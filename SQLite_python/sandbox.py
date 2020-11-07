import sqlite3

from sqlite3 import Error


def create_connection(db_file) -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


if __name__ == "__main__":
    connection = create_connection('SQLite_python/hello_world.db')
    cursor = connection.cursor()
    cursor.execute('')
