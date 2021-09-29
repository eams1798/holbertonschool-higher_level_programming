#!/usr/bin/python3
"""In this module we defiine a class for a square object"""


class Square:
    """This class defines a square"""
    def positive_int_required(f):
        """Does a function if a condition is true

        Args:
            f (function): a function

        Returns:
            function: A function that will be executed
        """
        def required(self, value=0):
            """Checks if the function is a positive integer or
                raises an exception

            Args:
                value (int): The value must be an integer

            Returns:
                function: A function that will be executed
            """
            if not(type(value) is int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                return f(self, value)
        return required

    @positive_int_required
    def __init__(self, size=0):
        """Initializes an object for a square class.

        Args:
        size (int): The size of the square. Can be 0 if size is not
        specified.
        """
        self.__size = size

    @property
    def size(self):
        """obj:`int`: returns o changes the value of the attribute`size`
        """
        return self.__size

    @size.setter
    @positive_int_required
    def size(self, value):
        self.__size = value

    def area(self):
        """Returns the current square area.

        Returns:
            The area of a square
        """
        return self.__size ** 2
