#!/usr/bin/python3
"""This module contains the Rectangle class that defines a rectangle."""


class Rectangle:
    """Rectangle class to define rectangles.

    __init__ to initialize the object with those specific attributes.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(value) != int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(self.__width * 2 + self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return('')

        row = self.__width * '#'
        for i in range(self.__height - 1):
            print(row)
        return(row)

    def __repr__(self):
        rectangle_size = (self.__width, self.__height)
        repr_str = 'Rectangle' + str(rectangle_size)
        return(repr_str)

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
