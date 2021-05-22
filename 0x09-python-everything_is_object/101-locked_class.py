#!/usr/bin/python3
"""This module contains an emprty class"""


class LockedClass:
    """Empty class that prevents the user from dynamically creating
    new instances attributes"""
    __slots__ = ['first_name']
