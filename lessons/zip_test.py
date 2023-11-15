"""Test my zip function."""


__author__ = "730571715"


from lessons.zip import zip


def test_length() -> None:
    """Test zip when given lists are different lengths."""
    l1: list[str] = ["my", "brain"]
    l2: list[int] = [1, 2, 3, 4]
    assert zip(l1, l2) == {}


def test_empty() -> None:
    """Test zip when given lists are empty."""
    l1: list[str] = []
    l2: list[int] = []
    assert zip(l1, l2) == {}


def test_random() -> None:
    """Test zip when given random numbers."""
    l1: list[str] = ["my", "brain", "broke"]
    l2: list[int] = [1, 2, 3]
    assert zip(l1, l2) == {"my": 1, "brain": 2, "broke": 3}