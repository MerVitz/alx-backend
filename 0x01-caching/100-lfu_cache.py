#!/usr/bin/env python3
"""
LFU Caching system.
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
        self.freq = defaultdict(int)  # Frequency of access for each key
        self.order = []  # Maintain order of keys for
        # LRU in case of frequency tie

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return

        # If key exists, update its value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            # Update the order to move the key to the most recent position
            self.order.remove(key)
            self.order.append(key)
        else:
            # If key does not exist, add it
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.freq.values())
                least_frequent_keys = (
                        [k for k in self.order if self.freq[k] == min_freq]
                        )

                # Apply LRU to resolve ties
                key_to_discard = least_frequent_keys[0]
                self.order.remove(key_to_discard)
                del self.cache_data[key_to_discard]
                del self.freq[key_to_discard]
                print(f"DISCARD: {key_to_discard}")

            # Add the new key
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if key in self.cache_data:
            self.freq[key] += 1  # Increment frequency on access
            self.order.remove(key)
            self.order.append(key)  # Update the ition
            return self.cache_data[key]
        return None
