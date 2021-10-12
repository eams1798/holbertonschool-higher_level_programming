#!/usr/bin/python3
"""4. Only sub class of"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited from the
    specified class"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
