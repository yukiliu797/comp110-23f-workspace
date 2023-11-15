"""EX07: Dictionary Test."""
__author__ = "730571715"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_keyerror():
    """Test raising key error when having deplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary = {"DUKE": "economics", "WFU": "biology"}
        invert(my_dictionary)


def test_invert_usecase1():
    """Test invert with random dictionary."""
    dict1: dict = {"comp110": "python"}
    assert invert(dict1) == {"python": "comp110"}


def test_invert_usecase2():
    """Test invert with random dictionary."""
    dict1: dict = {"Jack": "Andy", "Evan": "Charlie"}
    assert invert(dict1) == {"Andy": "Jack", "Charlie": "Evan"}


def test_favorite_color_empty():
    """Test favorite color with empty dictionary."""
    dict1: dict = {}
    assert favorite_color(dict1) == ''


def test_favorite_color_usecase1():
    """Test favoritw color with random dictionary."""
    dict1: dict = {"A": "blue", "B": "red", "C": "blue"}
    assert favorite_color(dict1) == "blue"


def test_favorite_color_usecase2():
    """Test favoritw color with random dictionary."""
    dict1: dict = {"alpha": "yellow", "beta": "pink", "gamma": "pink", "delta": "red"}
    assert favorite_color(dict1) == "pink"


def test_count_empty():
    """Test count with empty list."""
    word_list: list = []
    assert count(word_list) == {}


def test_count_usecase1():
    """Test count with random word list."""
    word_list: list = ["unc", "duke", "unc"]
    assert count(word_list) == {"unc": 2, "duke": 1}


def test_count_usecase2():
    """Test count with random word list."""
    word_list: list = ["pink", "red"]
    assert count(word_list) == {"pink": 1, "red": 1}


def test_alphabetizer_empty():
    """Test alphabetizer with empty list."""
    word_list: list = []
    assert alphabetizer(word_list) == {}


def test_alphabetizer_usecase1():
    """Test alphabetizer with random word list."""
    word_list: list = ["cat", "python"]
    assert alphabetizer(word_list) == {"c": ["cat"], "p": ["python"]}


def test_alphabetizer_usecase2():
    """Test alphabetizer with random word list."""
    word_list: list = ["apple", "banana", "car", "bike", "coke"]
    assert alphabetizer(word_list) == {"a": ["apple"], "b": ["banana", "bike"], "c": ["car", "coke"]}


def test_update_attendance_empty():
    """Test update attendane with empty dictionary."""
    dict1: dict = {}
    day_of_week: str = "Monday"
    student: str = "Bob"
    assert update_attendance(dict1, day_of_week, student) == {}


def test_update_attendance_usecase1():
    """Test update attendance with empty dictionary."""
    dict1: dict = {"Monday": ["Wendy, Clare"], "Tuesday": ["Clare"]}
    day_of_week: str = "Tuesday"
    student: str = "David"
    assert update_attendance(dict1, day_of_week, student) == {"Monday": ["Wendy, Clare"], "Tuesday": ["Clare", "David"]}


def test_update_attendance_usecase2():
    """Test update attendance with empty dictionary."""
    dict1: dict = {"Monday": ["Cindy, Clare"], "Tuesday": ["Clare"]}
    day_of_week: str = "Wednesday"
    student: str = "Evan"
    assert update_attendance(dict1, day_of_week, student) == {"Monday": ["Cindy, Clare"], "Tuesday": ["Clare"], "Wednesday": ["Evan"]}