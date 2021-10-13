#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """A class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes an object for a Student class

        Args:
            first_name: a string
            last_name: a string
            age: a string
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description for JSON serialization of an object

        Args:
            obj: An abject

        Returns:
            A dictionary
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        if not (isinstance(attrs[i], str) for i in range(len(attrs))):
            return self.__dict__
        return {key: value for (key, value) in self.__dict__.items()
                if key in attrs}
