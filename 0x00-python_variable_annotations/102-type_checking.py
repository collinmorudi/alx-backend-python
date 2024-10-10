#!/usr/bin/env python3
"""
This module provides a function to zoom in an array by repeating its elements
a specified number of times.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zoom in an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be zoomed in.
        factor (int, optional): The number of times each element is repeated.
                                Defaults to 2.

    Returns:
        Tuple[int, ...]: A new tuple with each element of `lst` repeated factor
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Use tuple instead of list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
