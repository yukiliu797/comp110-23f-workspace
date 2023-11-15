"""Write the same function in three ways."""
__author__ = "730571715"


def w_sum(vals: list[float]) -> float:
    """Adding a list into vals."""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Adding a list into vals."""
    sum: float = 0.0
    for items in vals:
        sum += items
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Adding a list into vals."""
    sum: float = 0.0
    for items in range(0, len(vals)):
        sum += vals[items]
    return sum