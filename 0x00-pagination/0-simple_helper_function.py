#!/usr/bin/env python3
'''task 0
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''simple helper function'''
    start = (page-1) * page_size
    end = start + page_size
    return (start, end)
