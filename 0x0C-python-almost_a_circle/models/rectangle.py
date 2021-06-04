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

    @property
    def width(self):
        """getter and setter of the 'width' attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        else:
            if value <= 0:
                raise ValueError('width must be > 0')
            self.__width = value

    @property
    def height(self):
        """getter and setter of the 'height' attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        else:
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value

    @property
    def x(self):
        """getter and setter of the 'x' attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        else:
            if value < 0:
                raise ValueError('x must be >= 0')
            self.__x = value

    @property
    def y(self):
        """getter and setter of the 'y' attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        else:
            if value < 0:
                raise ValueError('y must be >= 0')
            self.__y = value

    def area(self):  # Public method
        """Function that returns the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):  # Public method
        """This function prints in stdout the Rectangle instance with the
        character '#'
        """
        for j in range(self.__height):
                print('#' * self.__width)

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        str_method = '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return str_method
