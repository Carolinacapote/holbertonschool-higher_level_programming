#!/usr/bin/python3
"""This module contains a class called *Square*"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from the class 'Rectangle'
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter of the 'size' attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [Square] (<id>) <x>/<y> - <size>
        """
        str_method = '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)
        return str_method

    def update(self, *args, **kwargs):  # Public method
        """This function assigns an argument to each attribute with args
        'kwargs' updates the value of the arguments using the key/value
        method
        """
        args_list = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, args_list[arg], args[arg])

        for key, value in kwargs.items():  # kwargs implementation
            setattr(self, key, value)

    def to_dictionary(self):  # Public method
        """
        Returns:
            A dictionary representation of a 'Square'
        """
        my_dict = {'id': self.id, 'size': self.width,
                   'x': self.x, 'y': self.y}
        return my_dict
