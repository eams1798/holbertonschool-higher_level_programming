#!/usr/bin/python3
"""9. Student to JSON"""


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

    def to_json(self):
        """Returns the dictionary description for JSON serialization of an object

        Args:
            obj: An abject

        Returns:
            A dictionary
        """
        return self.__dict__
