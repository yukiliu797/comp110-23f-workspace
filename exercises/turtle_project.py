"""EX05 - turtle_tutorial."""

__author__ = "730571715"

from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    graph: Turtle = Turtle()
    wall(graph, -250, 100)
    window(graph, 100, 0)
    window(graph, 50, 0)
    window(graph, 100, -50)
    window(graph, 50, -50)
    door(graph, -150, -300)
    roof(graph, -250, 100)
    done()	


def wall(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw lines that create a wall."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(270.0)
    a_turtle.pendown()
    
    a_turtle.forward(400)
    a_turtle.left(90)
    a_turtle.forward(500)
    a_turtle.left(90)
    a_turtle.forward(400)


def window(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw boxes that create a window."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    i: int = 0
    while i < 4:
        a_turtle.forward(70)
        a_turtle.left(90)
        i += 1


def door(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw lines that create a door."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(90.0)
    a_turtle.pendown()

    a_turtle.forward(200)
    a_turtle.right(90)
    a_turtle.forward(150)
    a_turtle.right(90)
    a_turtle.forward(200)


def roof(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw lines for a roof."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.pencolor("green")
    a_turtle.fillcolor(100, 100, 100)

    a_turtle.begin_fill()
    a_turtle.left(90)
    a_turtle.forward(500)
    a_turtle.left(150)
    a_turtle.forward(288.675)
    a_turtle.left(60)
    a_turtle.forward(288.675)
    a_turtle.end_fill()


if __name__ == "__main__":
    main()