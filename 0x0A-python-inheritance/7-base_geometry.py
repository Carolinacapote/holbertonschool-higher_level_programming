#!/usr/bin/python3
"""This module contains a class called
BaseGeometry.
"""


class BaseGeometry:
    """class BaseGeometry"""
    # Public instance method.
    def area(self):
        """
        Exceptions:
            msg: area() is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function that validates the value
        Args:
            name (str): Name of the object.
            value (int): of the object (name).
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
