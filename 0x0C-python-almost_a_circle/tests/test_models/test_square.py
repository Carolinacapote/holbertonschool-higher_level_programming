#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
import sys
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Square' class is working correctly.
    """
    def test_square_class(self):
        """Function with some test cases"""
        s1 = Square(10)
        self.assertEqual(10, s1.size)

        s2 = Square(10, 2)
        self.assertEqual(10, s2.size)
        self.assertEqual(2, s2.x)

        s3 = Square(3, 5, 2)
        self.assertEqual(3, s3.size)
        self.assertEqual(5, s3.x)
        self.assertEqual(2, s3.y)

        s4 = Square(10, 2, 0, 12)
        self.assertEqual(10, s4.size)
        self.assertEqual(12, s4.id)
        self.assertEqual(2, s4.x)
        self.assertEqual(0, s4.y)

    def test_data_type(self):
        """Function to make sure Type errors are raised"""
        self.assertRaises(TypeError, Square, 'hello', 3, 2)
        self.assertRaises(TypeError, Square, 3, True, 2)
        self.assertRaises(TypeError, Square, 3, 2, 3.45)

    def test_data_value(self):
        """Make sure Value errors are raised"""
        self.assertRaises(ValueError, Square, 0, 2, 3)
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(ValueError, Square, 3, -3, 2)
        self.assertRaises(ValueError, Square, 2, 3, -2)

    def test_area(self):
        """Testing the area() function"""
        s1 = Square(3)
        self.assertEqual(9, s1.area())
        s4 = Square(5, 0, 0, 12)
        self.assertEqual(25, s4.area())

    def test_update(self):
        """Testing the update() function"""
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(89, s1.id)
        s1.update(79, 2)
        self.assertEqual(79, s1.id)
        self.assertEqual(2, s1.size)
        s1.update(9, 1, 3)
        self.assertEqual(9, s1.id)
        self.assertEqual(1, s1.size)
        self.assertEqual(3, s1.x)
        s1.update(89, 2, 4, 5)
        self.assertEqual(89, s1.id)
        self.assertEqual(2, s1.size)
        self.assertEqual(4, s1.x)
        self.assertEqual(5, s1.y)

        # update with kwargs
        s4 = Square(5, 5, 5, 5)
        s4.update(id=1)
        self.assertEqual(1, s4.id)
        s4.update(id=4, size=3)
        self.assertEqual(4, s4.id)
        self.assertEqual(3, s4.size)
        s4.update(x=1, y=3, size=4)
        self.assertEqual(1, s4.x)
        self.assertEqual(3, s4.y)
        self.assertEqual(4, s4.size)
        s4.update(id=3, size=9, x=2, y=2)
        self.assertEqual(3, s4.id)
        self.assertEqual(9, s4.size)
        self.assertEqual(2, s4.x)
        self.assertEqual(2, s4.y)

    def test_to_dictionary(self):
        """Testing to-dictionary() function"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 9, 'size': 10})

    def test_display(self):
        """Testing display() function"""
        std_out = StringIO()
        sys.stdout = std_out
        s1 = Square(2)
        s1.display()
        output = std_out.getvalue()
        self.assertEqual(output, '##\n##\n')

        # display() function with 'x' and 'y'
        std_out_2 = StringIO()
        sys.stdout = std_out_2
        s4 = Square(2, 2, 1)
        s4.display()
        output = std_out_2.getvalue()
        self.assertEqual(output, '\n  ##\n  ##\n')

        std_out_3 = StringIO()
        sys.stdout = std_out_3
        s5 = Square(2, 1)
        s5.display()
        output = std_out_3.getvalue()
        self.assertEqual(output, ' ##\n ##\n')

        def test_str_method(self):
            """Testing the __str__ method"""
            s1 = Square(4, 6, 2, 12)
            self.assertEqual(s1.__str__(), '[Square] (12) 6/2 - 4')
