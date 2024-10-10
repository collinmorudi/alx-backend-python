#!/usr/bin/env python3
"""
This module provides a function to zoom in an array by repeating its elements
a specified number of times.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in an array by repeating each element a specified number of times.

    Args:
        lst (Tuple): A tuple of elements to be zoomed in.
        factor (int, optional): The number of times each element is repeated.
                                Defaults to 2.

    Returns:
        List: A new list with each element of `lst` repeated factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Use tuple as input

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
