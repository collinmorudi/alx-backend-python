#!/usr/bin/env python3
"""
This module contains a function safely_get_value with type annotations.
"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default:
                     Union[T, None] = None) -> Union[T, None]:
    """
    Function that safely gets a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to get the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The default value to return if the key is
        not found.

    Returns:
        Union[T, None]: The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
