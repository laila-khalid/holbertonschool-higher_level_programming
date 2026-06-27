#!/usr/bin/env python3
"""Module demonstrating the use of Mixins."""


class SwimMixin:
    """A mixin class that provides swimming capability."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying capability."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
