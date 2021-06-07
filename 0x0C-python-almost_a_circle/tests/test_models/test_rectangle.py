#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Rectangle' class is working correctly.
    """
    def test_rectangle_class(self):  #task 2
        """Function with some test cases"""
        pass

    def test_data_type(self):
        """Function to make sure Type errors are raised"""
        self.assertRaises(TypeError, Rectangle, 'hello', 3, 2, 1)
        self.assertRaises(TypeError, Rectangle, 3, True, 2, 1)
        self.assertRaises(TypeError, Rectangle, 3, 2, 3.45, 1)
        self.assertRaises(TypeError, Rectangle, 3, 2, 4, [1, 2])

    def test_data_value(self):
        """Make sure Value errors are raised"""
        self.assertRaises(ValueError, Rectangle, 0, 2, 3, 1)
        self.assertRaises(ValueError, Rectangle, 3, -3, 2, 1)
        self.assertRaises(ValueError, Rectangle, 2, 3, -2, 0)
        self.assertRaises(ValueError, Rectangle, 2, 3, 2, -1)
