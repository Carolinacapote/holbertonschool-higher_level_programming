#!/usr/bin/python3
"""This module contains a class that handles errors."""


class Square:
    """Class that defines a square.

    __init__ initialization of a private instance attribute.
    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size * self.__size)
