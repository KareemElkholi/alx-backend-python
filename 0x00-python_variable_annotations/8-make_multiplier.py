#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(f: float) -> float:
        """multiplies a float by multiplier"""
        return f * multiplier
    return multiply
