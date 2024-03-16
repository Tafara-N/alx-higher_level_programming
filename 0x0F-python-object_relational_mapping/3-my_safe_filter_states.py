#!/usr/bin/python3

"""
Script takes arguments and displays all values in the `states` table
from the database 'hbtn_0e_0_usa' where `name` matches the argument
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Connects to the 'hbtn_0e_0_usa' database and executes a query that
    fetches all data from the `states` table where `name` matches the argument
    """

    if len(argv) != 5:
        print("Usage: ./script.py <username> <password> \
            <database> <name_to_search>")
        exit(1)

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    # String formated to prevent SQL injection
    cursor.execute("SELECT * FROM `states` WHERE `name` LIKE \
        BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    records = cursor.fetchall()

    for record in records:
        print(record)

    # Close cursor and database connection
    cursor.close()
    db.close()
