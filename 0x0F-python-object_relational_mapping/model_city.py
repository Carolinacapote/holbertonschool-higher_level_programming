#!/usr/bin/python3
'''
This module contains the class definition of a City that
inherits from Base imported from model_state.py
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''Class definition of a City that inherits from Base'''

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
