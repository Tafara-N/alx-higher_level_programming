#!/usr/bin/python3

"""
Contains class definition of a City and an
instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Inherits from Base and links to the table `cities`
    """

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Constraint: Foreign Key
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
