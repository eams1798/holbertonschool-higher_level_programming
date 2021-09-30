#!/usr/bin/python3
"""In this module we defiine a class for a square object"""


def evaluate_size(value):
    """Checks if the value is a positive integer or raises an exception
    Args:
        value (int): The value must be an integer

    Returns:
        int: the checked integer
    """
    if not(type(value) is int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        return value


def evaluate_position(value):
    """Checks if the value is a tuple with 2 positive integers
    Args:
        value (tuple): The value must be a tuple with 2 positive integers

    Returns:
        tuple: the checked tuple
    """
    if type(value) is tuple and len(value) == 2:
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return value
    else:
        raise TypeError("position must be a tuple of 2 positive integers")


class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes an object for a square class.

        Args:
            size (int): The size of the square. Can be 0 if size is not
                        specified.
        """
        self.__size = evaluate_size(size)
        self.__position = evaluate_position(position)

    @property
    def size(self):
        """obj:`int`: returns o changes the value of the attribute`size`"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = evaluate_size(value)

    @property
    def position(self):
        """obj:`int`: returns o changes the value of the attribute`position`"""
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = evaluate_position(value)

    def area(self):
        """Returns the current square area.

        Returns:
            The area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character `#` and positions it
            at the given coordenates

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
