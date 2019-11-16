import mysql.connector

# Change it to change
# database name to create
DATABASE_NAME = 'Try MySQL'


def check_requirements(cursor):
    cursor.execute('SHOW DATABASES')
    for database in cursor:
        if database[0] == DATABASE_NAME:
            print('Database already exists.')
            exit(0)


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

    command = f'''
CREATE DATABASE `{DATABASE_NAME}`
    '''

    cursor.execute(command)
    for x in cursor:
        print(x)
