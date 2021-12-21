#!/usr/bin/python3
"""State class Module for initialize a SQL table from Python"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This class defines the table 'States' which will work
    with our database"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')

    def __str__(self):
        return ('{}: {}'.format(self.id, self.name))
