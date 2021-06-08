#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Square' class is working correctly.
    """
    def test_square_class(self):
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

    def test_area(self):
        """Testing the area() function"""
        s1 = Square(3)
        self.assertEqual(9, s1.area())
        s2 = Square(5, 0, 0, 12)
        self.assertEqual(25, s2.area())

    def test_update(self):
        """Testing the update() function"""
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(89, s1.id)
        s1.update(79, 2)
        self.assertEqual(79, s1.id)
        self.assertEqual(2, s1.size)
        s1.update(89, 2, 4, 5)
        self.assertEqual(89, s1.id)
        self.assertEqual(2, s1.size)
        self.assertEqual(4, s1.x)
        self.assertEqual(5, s1.y)

        # update with kwargs
        s2 = Square(5, 5, 5, 5)
        s2.update(id=1)
        self.assertEqual(1, s2.id)
        s2.update(x=1, y=3, size=4)
        self.assertEqual(1, s2.x)
        self.assertEqual(3, s2.y)
        self.assertEqual(4, s2.size)

    def test_to_dictionary(self):
        """Testing to-dictionary() function"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 9, 'size': 10})
