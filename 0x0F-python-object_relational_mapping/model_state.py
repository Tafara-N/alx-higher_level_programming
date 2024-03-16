#!/usr/bin/python3

"""
Contains the class definition of a State and an instance
Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    Inherits from Base and links to table `states`
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
