#!/usr/bin/python3
"""State class Module for initialize a SQL table from Python"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """This class defines the table 'States' which will work
    with our database"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('State.id'), nullable=False)

    def __str__(self):
        return ('{}: {}'.format(self.id, self.name))
