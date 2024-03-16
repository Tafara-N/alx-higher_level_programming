#!/usr/bin/python3

"""
A script that lists all `cities` from the database 'hbtn_0e_4_usa'
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Connects to the 'hbtn_0e_4_usa' database and executes a querry that
    fetches all `cities` from 'hbtn_0e_4_usa'
    """

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
        FROM `cities`\
        JOIN `states` ON cities.state_id = states.id\
        ORDER BY `id` ASC")

    records = cursor.fetchall()

    for record in records:
        print(records)
