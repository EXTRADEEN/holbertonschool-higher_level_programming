#!/usr/bin/python3
""" create class State """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ contains the class definition of a State """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
