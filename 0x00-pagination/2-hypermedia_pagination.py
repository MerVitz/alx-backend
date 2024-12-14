#!/usr/bin/env python3
"""
Hypermedia pagination implementation.
"""

import math
from typing import List

Server = __import__('1-simple_pagination').Server


class Server(Server):
    """
    Server class for paginating popular baby names dataset.

    Methods:
        get_hyper(page: int, page_size: int)
        : Returns pagination metadata for the dataset.
    """
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing pagination metadata.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary with the following keys:
                - page_size (int): Length of the returned dataset page.
                - page (int): Current page number.
                - data (List[List]): Dataset page.
                - next_page (int | None): Next page number
                , or None if no more pages.
                - prev_page (int | None): Previous page number
                , or None if on the first page.
                - total_pages (int): Total number of pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': (
                page + 1 if page < total_pages else None
            ),
            'prev_page': (
                page - 1 if page > 1 else None
            ),
            'total_pages': total_pages,
        }
