#!/usr/bin/python3

"""
Class definition of a City and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    Inherits from Base and links to the table `cities`
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Constraint: Foreign Key
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
