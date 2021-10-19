#!/usr/bin/python3
"""A module to define a  class Square"""

from models.rectangle import Rectangle, wh_val


class Square(Rectangle):
    """A class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an object of the class Square

        Args:
            size: a measure
            x: horizontal position
            y: vertical position
            id:the id of the object
        """
        sz = wh_val(size, "width")
        super().__init__(sz, sz, x, y, id)

    def __str__(self):
        """Shows information of the attributes of an object"""
        s_rect = "[Square] "
        s_id = "(" + str(self.id) + ") "
        s_xy = str(self.x) + "/" + str(self.y) + " - "
        s_sz = str(self.width)
        return s_rect + s_id + s_xy + s_sz

    @property
    def size(self):
        """returns or changes the value of the attribute `size`"""
        return(self.width)

    @size.setter
    def size(self, value):
        self.width = wh_val(value, "width")
        self.height = value

    def update(self, *args, **kwargs):
        """Set new attributes for a Square through a list or a dictionary

        Args:
            *args: A list of arguments
            **kwargs: A dictionary with an attribute and its new value
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for atr, arg in zip(attributes, args):
                setattr(self, atr, arg)
        elif kwargs is not None:
            for atr, arg in kwargs.items():
                setattr(self, atr, arg)
        else:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {}
        keys = ['id', 'x', 'size', 'y']
        for k in keys:
            dic[k] = getattr(self, k)
        return dic
