"""Defining a class."""


from __future__ import annotations


class Point:
    """Point has both an x and a y attribute."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None: 
        """Belongs to the Point class and mutates a Point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Belongs to the Point class and instead of mutating a Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __str__(self) -> str:
        """Print out results in a readable way."""
        result: str = f"x: {self.x}; y: {self.y}"
        return result
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Addition operator."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point