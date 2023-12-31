#!/usr/bin/env python3
'''sum up list of floats'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up all the floats in the list

    Parameters:
      input_list(list[floats]): a list of floats

    Rerurn:
      return_type: returns a float
    """
    y = 0
    for x in input_list:
        y += x
    return y
