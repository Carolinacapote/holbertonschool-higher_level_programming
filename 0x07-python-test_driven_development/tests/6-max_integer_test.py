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
        self.assertEqual(max_integer([5, 1, 3, 2]), 5)
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([1, 3, -4, 2, 5]), 5)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
