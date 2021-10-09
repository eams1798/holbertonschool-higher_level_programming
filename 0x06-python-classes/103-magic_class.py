#!/usr/bin/python3
"""This module defines a Magic Class for a circle"""


import math

class MagicClass:
    """Magic class that does same as given bytecode output"""

    def __init__(self, radius=0):
        """initialize a circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """returns the area of a circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of a circle"""
        return 2 * math.pi * self._MagicClass__radius
