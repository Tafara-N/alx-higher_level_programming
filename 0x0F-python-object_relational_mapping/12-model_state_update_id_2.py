#!/usr/bin/python3

"""
A script that changes the name of a State object
from the 'hbtn_0e_6_usa' database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the 'hbtn_0e_6_usa' database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
