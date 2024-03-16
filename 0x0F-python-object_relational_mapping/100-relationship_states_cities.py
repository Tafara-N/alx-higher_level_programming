#!/usr/bin/python3

"""
A script that creates the State “California” with the
City “San Francisco” from the 'hbtn_0e_100_usa' database
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

    # Adding new state
    add_state = State(name='California')
    add_city = City(name='San Francisco')
    add_state.cities.append(add_city)

    session.add(add_state)
    session.commit()
    session.close()
