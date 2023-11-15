"""EX06 Dictionary Functions."""

__author__ = "730571715"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert key and value."""
    result: dict[str, str] = {}
    for key in input:
        if input[key] in result:
            raise KeyError("Sorry, duplicate input.")
        result[input[key]] = key
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Count for most frequently appeared value."""
    i: int = 0
    color: str = ""
    result: dict[str, int] = {}
    for key in input:
        if input[key] in result:
            result[input[key]] += 1
        else:
            result[input[key]] = 1
    for key in result:
        if result[key] > i:
            i = result[key]
            color = key
    return color


def count(input: list[str]) -> dict[str, int]:
    """Count for the times value appeared."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(input):
        if input[i] in result:
            result[input[i]] += 1
        else:
            result[input[i]] = 1
        i += 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    result: dict[str, list[str]] = {}
    for word in input:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)  
    return result


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Check if the day is already in the dictionary."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log