#!/usr/bin/env python3
"""
This module contains a function that sums a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats to sum

    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
