#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Base' class is working correctly.
    """
    def test_base_class(self):
        """Function with some test cases"""
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base(12)
        self.assertEqual(12, b2.id)
        b3 = Base()
        self.assertEqual(2, b3.id)

    """def test_to_json_string(self):
        # Testing to_json_string() function
        r1 = Rectangle(10, 7, 2, 8, 3)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 3, "width": 10,
        "height": 7, "x": 2, "y": 8}]')
        """
