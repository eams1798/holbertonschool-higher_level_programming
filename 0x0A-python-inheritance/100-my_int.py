#!/usr/bin/python3
"""12. My integer"""


class MyInt(int):
    """new definition for an integer"""

    def __eq__(self, other):
        """equal now means not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """not equal now means equal"""
        return int.__eq__(self, other)
