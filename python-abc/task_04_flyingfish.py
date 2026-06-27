#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Override the flying behavior for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swimming behavior for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat for a flying fish."""
        print("The flying fish lives both in water and the sky!")
