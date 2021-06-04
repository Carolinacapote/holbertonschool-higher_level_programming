#!/usr/bin/python3
"""This module contains a class called *Rectangle*"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from the superclass 'Base'
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class and its attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
