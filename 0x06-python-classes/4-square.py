#!/usr/bin/python3
"""This module contains a class that handles errors."""


class Square:
    """Class that defines a square.

    __init__ initialization of a private instance attribute.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size * self.__size)
