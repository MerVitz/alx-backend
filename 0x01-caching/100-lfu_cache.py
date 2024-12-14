#!/usr/bin/env python3
"""
LFU caching system.
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache class - implements LFU caching strategy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.freq = defaultdict(int)
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.freq[key] += 1
            else:
                self.cache_data[key] = item
                self.freq[key] = 1
                self.keys_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_freq = min(self.freq.values())
                least_used_keys = [
                    k for k in self.keys_order if self.freq[k] == least_freq
                ]
                discard_key = least_used_keys[0]
                self.keys_order.remove(discard_key)
                del self.cache_data[discard_key]
                del self.freq[discard_key]
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if key in self.cache_data:
            self.freq[key] += 1
        return self.cache_data.get(key, None)
