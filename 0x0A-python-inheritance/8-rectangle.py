#!/usr/bin/python3
"""8. Rectangle"""


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
