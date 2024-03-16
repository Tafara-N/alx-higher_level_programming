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
    cursor.execute("SELECT cities.name \
        FROM `cities` JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %(name)s \
        ORDER BY cities.id ASC", {'name': argv[4]})

    records = cursor.fetchall()

    city_names = [record[0] for record in records]
    city_list = ", ".join(city_names)

    print(city_list)

    # Close the cursor and the database connection
    cur.close()
    db.close()
