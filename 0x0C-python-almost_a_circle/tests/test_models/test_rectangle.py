#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Rectangle' class is working correctly.
    """
    def test_rectangle_class(self):
        """Function with some test cases"""
        r1 = Rectangle(10, 3)
        self.assertEqual(3, r1.height)
        self.assertEqual(10, r1.width)

        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(10, r2.width)
        self.assertEqual(2, r2.height)
        self.assertEqual(12, r2.id)
        self.assertEqual(0, r2.x)
        self.assertEqual(0, r2.y)

        r3 = Rectangle(2, 3, 5)
        self.assertEqual(2, r3.width)
        self.assertEqual(3, r3.height)
        self.assertEqual(5, r3.x)

        r4 = Rectangle(4, 3, 5, 2)
        self.assertEqual(4, r4.width)
        self.assertEqual(3, r4.height)
        self.assertEqual(5, r4.x)
        self.assertEqual(2, r4.y)

    def test_data_type(self):
        """Function to make sure Type errors are raised"""
        self.assertRaises(TypeError, Rectangle, 'hello', 3, 2, 1)
        self.assertRaises(TypeError, Rectangle, 3, True, 2, 1)
        self.assertRaises(TypeError, Rectangle, 3, 2, 3.45, 1)
        self.assertRaises(TypeError, Rectangle, 3, 2, 4, [1, 2])

    def test_data_value(self):
        """Make sure Value errors are raised"""
        self.assertRaises(ValueError, Rectangle, 0, 2, 3, 1)
        self.assertRaises(ValueError, Rectangle, -6, 2)
        self.assertRaises(ValueError, Rectangle, 3, -3, 2, 1)
        self.assertRaises(ValueError, Rectangle, 3, 0)
        self.assertRaises(ValueError, Rectangle, 2, 3, -2, 0)
        self.assertRaises(ValueError, Rectangle, 2, 3, 2, -1)

    def test_area(self):
        """Testing the area() function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(6, r1.area())
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r2.area())

    def test_update(self):
        """Testing the update() function"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(89, r1.id)
        r1.update(79, 2)
        self.assertEqual(79, r1.id)
        self.assertEqual(2, r1.width)
        r1.update(54, 2, 3)
        self.assertEqual(54, r1.id)
        self.assertEqual(2, r1.width)
        self.assertEqual(3, r1.height)
        r1.update(56, 5, 2, 3)
        self.assertEqual(56, r1.id)
        self.assertEqual(5, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r1.x)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(89, r1.id)
        self.assertEqual(2, r1.width)
        self.assertEqual(3, r1.height)
        self.assertEqual(4, r1.x)
        self.assertEqual(5, r1.y)

        # update with kwargs
        r2 = Rectangle(5, 5, 5, 5)
        r2.update(id=1)
        self.assertEqual(1, r2.id)
        r2.update(id=2, width=3)
        self.assertEqual(2, r2.id)
        self.assertEqual(3, r2.width)
        r2.update(id=6, width=5, height=1)
        self.assertEqual(6, r2.id)
        self.assertEqual(5, r2.width)
        self.assertEqual(1, r2.height)
        r2.update(x=1, height=2, id=3, width=4)
        self.assertEqual(1, r2.x)
        self.assertEqual(2, r2.height)
        self.assertEqual(3, r2.id)
        self.assertEqual(4, r2.width)
        r2.update(id=1, width=5, height=3, x=2, y=4)
        self.assertEqual(1, r2.id)
        self.assertEqual(5, r2.width)
        self.assertEqual(3, r2.height)
        self.assertEqual(2, r2.x)
        self.assertEqual(4, r2.y)

    def test_to_dictionary(self):
        """Testing to-dictionary() function"""
        r1 = Rectangle(10, 2, 1, 9, 12)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 12,
                                         'height': 2, 'width': 10})

    def test_display(self):
        """Testing display() function"""
        std_out = StringIO()
        sys.stdout = std_out
        r1 = Rectangle(2, 2)
        r1.display()
        output = std_out.getvalue()
        self.assertEqual(output, '##\n##\n')

        # display() function with 'x' and 'y'
        std_out_2 = StringIO()
        sys.stdout = std_out_2
        r2 = Rectangle(2, 2, 1, 2)
        r2.display()
        output = std_out_2.getvalue()
        self.assertEqual(output, '\n\n ##\n ##\n')

        std_out_3 = StringIO()
        sys.stdout = std_out_3
        r2 = Rectangle(3, 2, 2)
        r2.display()
        output = std_out_3.getvalue()
        self.assertEqual(output, '  ###\n  ###\n')

    def test_str_method(self):
        """Testing the __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
