"""Combining two lists into a dictionary."""

__author__ = "730571715"


list1: list[str] = ["happy", "tuesday"]
list2: list[int] = [1, 2]


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Combine two lists into one dictionary."""
    result: dict[str, int] = {}
    idx: int = 0
    if len(list1) != len(list2):
        return result
    while idx < len(list1):
        result[list1[idx]] = list2[idx]
        idx += 1
    return result