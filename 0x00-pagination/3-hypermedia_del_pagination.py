#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class for paginating a dataset of popular baby names.

    Methods:
        dataset(): Returns the full dataset.
        indexed_dataset(): Returns the dataset indexed by row numbers.
        get_hyper_index(index: int, page_size: int)
        Returns deletion-resilient pagination metadata.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset loader.

        Returns:
            List[List]: Full dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns the dataset indexed by row numbers.

        Returns:
            dict: A dictionary mapping row indices to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns pagination metadata that is resilient to deletions.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary with the following keys:
                - index (int): Current start index of the page.
                - next_index (int): Start index for the next page.
                - page_size (int): Current page size.
                - data (List[List]): The actual page of the dataset.
        """
        assert isinstance(index, int) and index >= 0
        dataset = self.indexed_dataset()

        data = []
        next_index = index

        while len(data) < page_size and next_index < len(dataset):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }
