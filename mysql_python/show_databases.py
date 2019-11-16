import mysql.connector


def check_requirements(cursor):
    pass


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

    cursor.execute('SHOW DATABASES')

    for x in cursor:
        print(x)
