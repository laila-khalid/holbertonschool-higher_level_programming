#!/usr/bin/env python3
"""Module that defines a VerboseList class."""


class VerboseList(list):
    """A custom list class that prints notifications upon modification."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification."""
        items_added = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        item_to_pop = self[index]
        print("Popped [{}] from the list.".format(item_to_pop))
        return super().pop(index)
