#!/usr/bin/env python3
"""
This module contains a function that sums a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
