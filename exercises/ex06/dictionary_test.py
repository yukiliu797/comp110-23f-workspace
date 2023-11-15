"""EX07 Test Dictionary Functions."""


__author__ = "730571715"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_empty() -> None:
    """Test for empty dictionary."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_normal() -> None:
    """Test for normal dictionary."""
    input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_KeyError() -> None:
    """Test for error dictionary."""
    with pytest.raises(KeyError):
        invert({'kris': 'jordan', 'michael': 'jordan'})


def test_favorite_color_empty() -> None:
    """Test for empty dictionary."""
    input: dict[str, str] = {}
    assert favorite_color(input) == ""


def test_favorite_color_normal() -> None:
    """Test for normal dictionary."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(input) == "blue"


def test_favorite_color_normal_2() -> None:
    """Test for normal dictionary."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "yellow"}
    assert favorite_color(input) == "yellow"


def test_count_empty() -> None:
    """Test for empty dictionary."""
    input: list[str] = []
    assert count(input) == {}


def test_count_normal() -> None:
    """Test for normal dictionary."""
    input: list[str] = ["yellow", "yellow", "blue"]
    assert count(input) == {"yellow": 2, "blue": 1}


def test_count_normal_2() -> None:
    """Test for normal dictionary."""
    input: list[str] = ["yellow", "blue", "blue"]
    assert count(input) == {"yellow": 1, "blue": 2}


def test_alphabetizer_empty() -> None:
    """Test for empty dictionary."""
    input: list[str] = []
    assert alphabetizer(input) == {}


def test_alphabetizer_normal() -> None:
    """Test for normal dictionary."""
    input: list[str] = ["yellow", "yes", "blue"]
    assert alphabetizer(input) == {"y": ["yellow", "yes"], "b": ["blue"]}


def test_alphabetizer_normal_2() -> None:
    """Test for normal dictionary."""
    input: list[str] = ["lose", "my", "brain"]
    assert alphabetizer(input) == {"l": ["lose"], "m": ["my"], "b": ["brain"]}


def test_update_attendance_empty() -> None:
    """Test for empty dictionary."""
    attendance_log: dict[str, list[str]] = {}
    day: str = ""
    student: str = ""
    assert update_attendance(attendance_log, day, student) == {'': ['']}


def test_update_attendance_normal() -> None:
    """Test for normal dictionary."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    student: str = "Vrinda"
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_normal_2() -> None:
    """Test for normal dictionary."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Yuki", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Wednesday"
    student: str = "Kate"
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Yuki', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['Kate']}