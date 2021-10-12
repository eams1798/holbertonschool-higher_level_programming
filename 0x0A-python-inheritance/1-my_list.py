#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """a list that inherits from a list"""

    def __init__(self):
        """initializer for MyList"""
        pass

    def print_sorted(self):
        """prints a sorted list"""
        lst = self.copy()
        lst.sort()
        print(lst)
        lst.clear()
