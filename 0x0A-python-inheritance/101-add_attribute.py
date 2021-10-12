#!/usr/bin/python3
"""13. Can I?"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible
    Args:
        obj: any object
    attr: the name of the new attribute for the object
    value: the value of `attr`
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
