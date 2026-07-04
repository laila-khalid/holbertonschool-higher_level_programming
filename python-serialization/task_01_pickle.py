#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance to a provided filename.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from a provided filename.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
