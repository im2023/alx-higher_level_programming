#!/usr/bin/python3
"""
defining the State class and Base
class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """The State class

    Attributes:
        __tablename__ (str): table name of the class
        id (int): State id of class.
        name (str): The State name of class
        cities (obj:"City"): Cities belonging to State

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
