#!/usr/bin/python3
"""This module contains a class that handles errors."""


class Square:
    """Class that defines a square.

    __init__ initialization of a private instance attribute.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        value1, value2 = value
        self.__position = sha512(value1+value2)

        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
