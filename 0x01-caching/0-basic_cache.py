#!/usr/bin/env python3
"""
Basic dictionary-based caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class - no size limit for the cache.
    """
    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        return self.cache_data.get(key, None)
