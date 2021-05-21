#!/usr/bin/python3
"""This module contains the Rectangle class that defines a rectangle."""


class Rectangle:
    """Rectangle class to define rectangles.

    __init__ to initialize the object with those specific attributes.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter and setter of the instance private attribute width."""
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Getter and setter of the instance private attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
