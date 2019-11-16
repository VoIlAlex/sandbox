import mysql.connector


DATABASE_NAME = 'Try MySQL'
TABLE_NAME = 'My First MySQL Table'
COLUMNS = {
    'first_name': 'VARCHAR(255)',
    'last_name': 'VARCHAR(255)'
}


def check_requirements(cursor):
    # check database
    cursor.execute('SHOW DATABASES')
    for database in cursor:
        if database[0] == DATABASE_NAME:
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
            print(f'Table "{TABLE_NAME}" already exist.')
            exit(-1)


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

    cursor.execute(f'USE `{DATABASE_NAME}`')

    columns = '(' + ','.join([name + ' ' +
                              data_type for name, data_type in COLUMNS.items()]) + ')'
    command = f'CREATE TABLE `{TABLE_NAME}`' + columns
    cursor.execute(command)

    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)
