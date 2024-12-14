#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from typing import Dict

Server = __import__('2-hypermedia_pagination').Server


class Server(Server):
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary for deletion-resilient pagination.
        Args:
            index (int): The starting index of the page.
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary containing pagination metadata.
        """
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        dataset = self.indexed_dataset()
        data = []
        next_index = index

        for _ in range(page_size):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
