#!/usr/bin/env python3
"""
FIFO caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class - implements FIFO caching strategy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_order.remove(key)
            self.cache_data[key] = item
            self.keys_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        return self.cache_data.get(key, None)
