#!/usr/bin/python3
"""3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of a class that inherited from
    the specified class or is just a class instance"""
    return isinstance(obj, a_class)
