#!/usr/bin/python3
"""Module that defines a class and inheritance-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class.
        False otherwise.
    """
    return isinstance(obj, a_class)
