#!/usr/bin/python3
"""This module contains a superclass called *Base*"""
import models
import json


class Base:
    """This class will be the "base" of the other classes (Rectangle, Square)
    """
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        Conditionals:
            if "id" is not None, assign the "id" with this argument value.
            Otherwise id equals to __nb_objects
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns:
            The JSON string representation of 'list_dictionaries'
            If 'list_dictionaries' is None or empty, return: []
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of list_objs
        to a file.
        Arguments:
            list_objs (list): list of instances who inherits of Base.
        """
        my_dictionary = {}
        my_list = []
        if list_objs is None:
            with open('Rectangle.json', mode='w') as my_file:
                my_file.write(my_list)

        for obj in list_objs:
            if type(obj) is models.square.Square:
                my_dictionary = cls.to_dictionary(obj)
                my_list.append(my_dictionary)
        
                with open('Square.json', mode='w') as my_file:
                    my_file.write(cls.to_json_string(my_list))

            if type(obj) is models.rectangle.Rectangle:
                my_dictionary = cls.to_dictionary(obj)
                my_list.append(my_dictionary)
        
                with open('Rectangle.json', mode='w') as my_file:
                    my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):  # static method
        """"""
