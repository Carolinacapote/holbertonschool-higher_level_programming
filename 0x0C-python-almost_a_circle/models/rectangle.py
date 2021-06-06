#!/usr/bin/python3
"""This module contains a class called *Rectangle*"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from the superclass 'Base'
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class and its attributes"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter and setter of the 'width' attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter and setter of the 'height' attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('height must be > 0')
        if type(value) is not int:
            raise TypeError('height must be an integer')
        self.__height = value

    @property
    def x(self):
        """getter and setter of the 'x' attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter and setter of the 'y' attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError('y must be >= 0')
        if type(value) is not int:
            raise TypeError('y must be an integer')
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
        """This function assigns an argument to each attribute with args
        'kwargs' updates the value of the arguments using the key/value
        method
        """
        args_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, args_list[arg], args[arg])

        for key, value in kwargs.items():  # kwargs implementation
            setattr(self, key, value)

    def to_dictionary(self):  # Public method
        """
        Returns:
            A dictionary representation of a 'Rectangle'
        """
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
