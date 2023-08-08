#!/usr/bin/env python3
'''Python async comprehension'''
import random
import asyncio
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """
    first async generator function

    Yields:
        Generator[float, None, None]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
