#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class that declares the test function to prove if the max_integer()
    funtion is working good and prove the raise of the errors.
    """
    def test_max_integer(self):
        # Test max_ integer when argument is a list of integers
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_types(self):
        # Make sure TypeErrors are raised when necessary
        self.assertRaises(TypeError, max_integer, 3.5)
        self.assertRaises(TypeError, max_integer, 'hello')
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [3, 'hello', 3.5])
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 3, 5)
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, {'value_1': 5, 'value_2': 6})
        self.assertRaises(TypeError, max_integer, (1, 4, 3, 5))
