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
        character '#'. x equals to a blank space (' ') before printing the
        columns and y equals to new line before printing the rows.
        """
        for i in range(self.__y):
            print()

        for j in range(self.__height):
                print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        str_method = '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return str_method

    def update(self, *args, **kwargs):  # Public method
        """This function assigns an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

        # kwargs implementation 
        self.id = kwargs.get('id')
        self.__width = kwargs.get('width')
        self.__height = kwargs.get('height')
        self.__x = kwargs.get('x')
        self.__y = kwargs.get('y')
