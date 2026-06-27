#!/usr/bin/env python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, some_iterable):
        """Initialize the iterator and counter.
        
        Args:
            some_iterable (iterable): The collection to iterate over.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Fetch the next item and increment the counter.
        
        Returns:
            The next item in the iterator.
            
        Raises:
            StopIteration: If there are no more items.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
