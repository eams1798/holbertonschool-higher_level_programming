#!/usr/bin/python3
"""7. Integer validator"""


class BaseGeometry:
    """An class named BaseGeometry"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if `value` is a positive integer
        Args:
            name: name of the value
            value: the checking value
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
        else:
            return value
