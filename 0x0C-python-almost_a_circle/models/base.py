#!/usr/bin/python3
"""This module contains a superclass called *Base*"""
import json
from os import path


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
        if list_objs:
            for obj in list_objs:
                my_dictionary = obj.to_dictionary()
                my_list.append(my_dictionary)

        with open(cls.__name__ + '.json', mode='w') as my_file:
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):  # static method
        """
        Returns:
            The list of the JSON string representation 'json_string'
        """
        my_list = []
        if json_string is None or len(json_string) == 0:
            return my_list

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns:
            An instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_shape = cls(3, 7, 5, 8)
        if cls.__name__ == 'Square':
            dummy_shape = cls(3, 7, 5)

        dummy_shape.update(dummy_shape, **dictionary)
        return dummy_shape

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            A list of instances.
        """
        instances_list = []
        if path.exists(cls.__name__ + '.json'):
            with open(cls.__name__ + '.json', mode='r') as my_file:
                read_file = my_file.read()
                json_dictionaries = cls.from_json_string(read_file)

                for dictionary in json_dictionaries:
                    instances_list.append(cls.create(**dictionary))

        return instances_list
