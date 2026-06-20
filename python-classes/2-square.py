#!/usr/bin/python3
"""
Module 2-square
Defines a class Square with a private size attribute and validation.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
