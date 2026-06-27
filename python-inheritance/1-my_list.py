#!/usr/bin/python3
"""Module that defines a custom list class."""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
