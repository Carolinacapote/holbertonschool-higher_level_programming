#!/usr/bin/python3
"""This module contains a class called Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Area of the figure"""
        return(self.__size ** 2)
