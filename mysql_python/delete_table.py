import mysql.connector

DATABASE_NAME = 'Try MySQL'
TABLE_NAME = 'My First MySQL Table'


def check_requirements(cursor):
    # check database
    cursor.execute('SHOW DATABASES')
    for table in cursor:
        if table[0] == DATABASE_NAME:
            break
    else:
        print(f'Database {DATABASE_NAME} does not exist.')
        exit(-1)
    list(cursor)

    cursor.execute(f'USE `{DATABASE_NAME}`')

    # check table
    cursor.execute('SHOW TABLES')
    for table in cursor:
        if table[0] == TABLE_NAME:
            break
    else:
        print(f'Table {TABLE_NAME} does not exist.')
        exit(-1)
    list(cursor)


if __name__ == "__main__":
    # connect to the server
    db = mysql.connector.connect(
        host='localhost',
        user='voilalex',
        passwd='VoIlAlex_VoIlAlex_2000'
    )
    cursor = db.cursor()
    check_requirements(cursor)

    ##########
    ## MAIN ##
    ##########

    cursor.execute(f'DROP TABLE `{TABLE_NAME}`')
