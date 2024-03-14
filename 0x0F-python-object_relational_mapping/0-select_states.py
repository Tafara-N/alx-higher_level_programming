#!/usr/bin/python3

"""
A script that lists all states from the database 'hbtn_0e_0_usa'
"""

import MySQLdb
import sys
from sys import argv


if __name__ == '__main__':
    """
    Connects to the 'hbtn_0e_0_usa' database and executes a query
    that fetches all data from the `states` table
    """

    db = MySQLdb.connect(host="localhost",
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
