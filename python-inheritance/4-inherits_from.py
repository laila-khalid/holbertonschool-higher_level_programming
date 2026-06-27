#!/usr/bin/python3
"""Module that defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an inherited instance of a_class.
        False if it's exactly the class or not related.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
