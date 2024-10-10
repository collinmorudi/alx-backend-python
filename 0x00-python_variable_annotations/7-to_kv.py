#!/usr/bin/env python3
"""
This module contains a function that creates a tuple from a
string and an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of an int or float.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): The int or float to be squared and
        become the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the
        string k and the second element is the square of v.
    """
    return (k, float(v ** 2))
