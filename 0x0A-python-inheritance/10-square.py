#!/usr/bin/python3
"""10. Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for a Square. Inherits from Rectangle"""

    def __init__(self, size):
        """initializes a class Square

        Args:
            size: private attribute
        """
        self.__size = super().integer_validator("size", size)
        Rectangle.__init__(self, self.__size, self.__size)
