#!/usr/bin/python3

"""
Script takes arguments and lists all `cities` of that state,
using the database 'hbtn_0e_4_usa'
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Connects to the 'hbtn_0e_4_usa' database and executes a querry that
    fetches all names of a state and lists all cities
    """

    if len(argv) != 5:
        print("Usage: ./script.py <username> <password>\
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
    query = "SELECT cities.name \
        FROM `states` \
        INNER JOIN cities ON states.id = cities.state_id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC"

    cursor.execute(query, (argv[4],))

    records = cursor.fetchall()

    city_names = [record[0] for record in records]

    print(", ".join(city_names))

    # Close the cursor and the database connection
    cur.close()
    db.close()
