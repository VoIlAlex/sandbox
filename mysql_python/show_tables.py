import mysql.connector

DATABASE_NAME = 'Try MySQL'


def check_requirements(cursor):
    cursor.execute('SHOW DATABASES')
    for database in cursor:
        if database[0] == DATABASE_NAME:
            break
    else:
        print(f'Database {DATABASE_NAME} does not exist.')
        exit(-1)
    # read output
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

    cursor.execute('USE `{}`'.format(DATABASE_NAME))
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)
