#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Square' class is working correctly.
    """
    def test_square_class(self):  #task 2
        """Function with some test cases"""
        pass

    def test_data_type(self):
        """Function to make sure Type errors are raised"""
        self.assertRaises(TypeError, Square, 'hello', 3, 2)
        self.assertRaises(TypeError, Square, 3, True, 2)
        self.assertRaises(TypeError, Square, 3, 2, 3.45)

    def test_data_value(self):
        """Make sure Value errors are raised"""
        self.assertRaises(ValueError, Square, 0, 2, 3)
        self.assertRaises(ValueError, Square, 3, -3, 2)
        self.assertRaises(ValueError, Square, 2, 3, -2)
