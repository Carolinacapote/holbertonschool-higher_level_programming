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
    print_symbol = '#'

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

        print_class = ''
        for i in range(self.__height):
            for j in range(self.__width):
                print_class += '{}'.format(self.print_symbol)
            print_class += '\n'
        return (print_class[:-1])

    def __repr__(self):
        rectangle_size = (self.__width, self.__height)
        repr_str = 'Rectangle' + str(rectangle_size)
        return(repr_str)

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)
