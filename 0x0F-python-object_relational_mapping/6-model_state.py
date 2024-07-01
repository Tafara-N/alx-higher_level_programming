#!/usr/bin/env python3

"""
Start link class to table in database
"""

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

