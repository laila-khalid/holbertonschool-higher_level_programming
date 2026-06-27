#!/usr/bin/env python3
"""Module that defines an abstract class Animal and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for the animal's sound."""
        pass


class Dog(Animal):
    """Subclass representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
