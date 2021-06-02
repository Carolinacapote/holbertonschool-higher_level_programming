#!/usr/bin/python3
"""This module contains a class called Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
