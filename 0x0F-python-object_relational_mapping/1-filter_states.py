#!/usr/bin/python3
"""
A script that lists all states from the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Connects to the 'hbtn_0e_0_usa' database and executes a query
    that fetches all data from the `states` table
    """

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM `states` \
        WHERE `name` LIKE BINARY 'N%' \
        ORDER BY `id` ASC"

    cursor.execute(query)

    records = cursor.fetchall()

    for record in records:
        print(record)

    # Close cursor and database connection
    cursor.close()
    db.close()
