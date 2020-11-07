import mysql.connector
import config
import os
import sys
from logzero import logger
import re
from mysql.connector import ProgrammingError
from mysql.connector.errors import OperationalError

DATABASE_NAME = 'Try MySQL'
SQL_FILE_NAME = 'sql/select_all.sql'


def exec_sql_file(cursor, sql_file):
    logger.info('Executing the file "{}"'.format(sql_file))
    statement = ""

    for line in open(sql_file):
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            statement = statement.replace(';', '')
            try:
                logger.info(
                    'Execution of the statement \n{}'.format(statement))
                cursor.execute(statement)
                logger.info('Result of the execution: ')
                for line in cursor:
                    print(line)
            except (OperationalError, ProgrammingError) as e:
                logger.error(e.args[0])
            statement = ''


def check_requirements(cursor):
    pass


if __name__ == "__main__":
    # connect to the server
    db = mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        passwd=config.PASSWORD
    )
    cursor = db.cursor()
    check_requirements(cursor)

    ##########
    ## MAIN ##
    ##########

    cursor.execute('USE `{}`'.format(DATABASE_NAME))
    exec_sql_file(cursor, sql_file=SQL_FILE_NAME)
    logger.info('Result of the execution: ')
    for line in cursor:
        print(line)
