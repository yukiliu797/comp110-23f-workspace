"""Ex04 utils."""

__author__ = "730571715"


def all(numbers: list[int], number: int) -> bool:
    """Check if all the number matches all the numbers."""
    if len(numbers) == 0:
        return False
    i: int = 0
    while i < len(numbers):
        if numbers[i] != number:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Find the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_number: int = input[0]
    i: int = 0
    while len(input) > i:
        if largest_number < input[i]:
            largest_number = input[i]
        i += 1
    return largest_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if each number in list1 is equal to the numbers in list2."""
    if len(list1) != len(list2):
        return False 
    i: int = 0
    while len(list1) > i:
        if list1[i] != list2[i]:
            return False
        i += 1
    return True