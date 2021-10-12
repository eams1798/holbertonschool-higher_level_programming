#!/usr/bin/python3
"""9. Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes a class Rectangle

        Args:
            width: private attribute
            height: private attribute
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """a printable version of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
