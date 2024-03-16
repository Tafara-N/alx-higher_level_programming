#!/usr/bin/python3

"""
A script that lists all City objects from the 'hbtn_0e_101_usa' database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Connect to 'hbtn_0e_100_usa' database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    for instance in session.query(State).order_by(State.id):
        for city_instance in instance.cities:
            print(city_instance.id, city_instance.name, sep=": ", end="")
            print(" -> " + instance.name)
