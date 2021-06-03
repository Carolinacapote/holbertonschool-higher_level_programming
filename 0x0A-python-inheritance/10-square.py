#!/usr/bin/python3
"""This module contains a class called Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Area of the figure"""
        return(self.__size ** 2)

    def __str__(self):
        """Magic attribute __str__ to return a string"""
        return('[Rectangle] {}/{}'.format(self.__size, self.__size))
