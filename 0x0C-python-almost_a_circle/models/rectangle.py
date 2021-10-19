#!/usr/bin/python3
"""A module to define a class for a Rectangle"""

from models.base import Base


def wh_val(value, name_value):
    """Validates if the width and height are integers greater than 0

    Args:
        value: A value of any type
        name_value: The name of the given value
    """
    if type(value) is not int:
        raise TypeError(name_value + " must be an integer")
    elif value <= 0:
        raise ValueError(name_value + " must be > 0")
    else:
        return value


def xy_val(value, name_value):
    """Validates if the coordenates are integers greater or equal than 0

    Args:
        value: A value of any type
        name_value: The name of the given value
    """
    if type(value) is not int:
        raise TypeError(name_value + " must be an integer")
    elif value < 0:
        raise ValueError(name_value + " must be >= 0")
    else:
        return value


class Rectangle(Base):
    """A class for a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an object of the class Rectangle

        Args:
            width: a measure
            height: a measure
            x: horizontal position
            y: vertical position
            id:the id of the object
        """
        self.__width = wh_val(width, "width")
        self.__height = wh_val(height, "height")
        self.__x = xy_val(x, "x")
        self.__y = xy_val(y, "y")
        super().__init__(id)

    def __str__(self):
        """Shows information of the attributes of an object"""
        s_rect = "[Rectangle] "
        s_id = "(" + str(self.id) + ") "
        s_xy = str(self.x) + "/" + str(self.y) + " - "
        s_wh = str(self.width) + "/" + str(self.height)
        return s_rect + s_id + s_xy + s_wh

    @property
    def width(self):
        """returns or changes the value of the attribute `width`"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = wh_val(value, "width")

    @property
    def height(self):
        """returns or changes the value of the attribute `height`"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = wh_val(value, "height")

    @property
    def x(self):
        """returns or changes the value of the attribute `x`"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = xy_val(value, "x")

    @property
    def y(self):
        """returns or changes the value of the attribute `y`"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = xy_val(value, "y")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints a rectangle"""
        spaces = "\n" * self.y
        line = " " * self.x + "#" * self.width
        rect = (line + "\n") * (self.height - 1) + line
        print(spaces + rect)

    def update(self, *args, **kwargs):
        """Set new attributes for a Rectangle through a list or a dictionary

        Args:
            *args: A list of arguments
            **kwargs: A dictionary with an attribute and its new value
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for atr, arg in zip(attributes, args):
                setattr(self, atr, arg)
        elif kwargs is not None:
            for atr, arg in kwargs.items():
                if atr in attributes:
                    setattr(self, atr, arg)
        else:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {}
        keys = ['x', 'y', 'id', 'height', 'width']
        for k in keys:
            dic[k] = getattr(self, k)
        return dic
