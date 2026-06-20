#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private size attribute.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """
        Initializes a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
