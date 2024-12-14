#!/usr/bin/env python3
"""
LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class - implements LIFO caching strategy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.last_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        return self.cache_data.get(key, None)
