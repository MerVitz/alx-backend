#!/usr/bin/env python3
"""
MRU caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class - implements MRU caching strategy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.most_recent_key:
                    del self.cache_data[self.most_recent_key]
                    print(f"DISCARD: {self.most_recent_key}")
            self.most_recent_key = key

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if key in self.cache_data:
            self.most_recent_key = key
        return self.cache_data.get(key, None)
