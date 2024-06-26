#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Annotations"""
    if lst:
        return lst[0]
    else:
        return None
