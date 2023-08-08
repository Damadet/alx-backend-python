#!/usr/bin/env python3
'''async generator'''
from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension():
    """ Async Comprehensions  """
    a = [i async for i in async_generator()]
    return a
