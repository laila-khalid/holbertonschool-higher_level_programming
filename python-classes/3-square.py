#!/usr/bin/python3
"""
Module 3-square
Defines a class Square with a private size attribute and an area method.
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

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
