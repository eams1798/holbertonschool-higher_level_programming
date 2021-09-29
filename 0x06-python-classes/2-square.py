#!/usr/bin/python3
"""In this module we defiine a class for a square object"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Initializes an object for a square class.

        Args:
            size (int): The size of the square. Can be 0 if size is not
                specified.
            """
        if not(type(size) is int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
