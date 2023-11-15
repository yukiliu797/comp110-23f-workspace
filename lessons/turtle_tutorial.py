"""Drawing of house and stars."""

__author__ = "730526486"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    outline: Turtle = Turtle()
    roof(outline, -250, 100)
    wall(outline, -200, 100)
    window(outline, -150, 0)
    window(outline, -100, 0)
    window(outline, -150, -50)
    window(outline, -100, -50)
    door(outline, 50, -200)
    done()


def roof(turtle: Turtle, x: float, y: float) -> None:
    """Draw roof outline."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.pencolor("pink")
    turtle.fillcolor(155, 155, 155)

    turtle.begin_fill()
    turtle.forward(500)
    turtle.left(150)
    turtle.forward(288.675)
    turtle.left(60)
    turtle.forward(288.675)
    turtle.end_fill()


def wall(turtle: Turtle, x: float, y: float) -> None:
    """Draw wall outline."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90.0)
    turtle.pendown()

    turtle.forward(300)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(300)


def window(turtle: Turtle, x: float, y: float) -> None:
    """Draw boxes that creates a wiindow."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()

    i: int = 0
    while i < 4:
        turtle.forward(50)
        turtle.left(90)
        i += 1


def door(turtle: Turtle, x: float, y: float) -> None:
    """Draw door outline."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(90.0)
    turtle.pendown()

    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)


if __name__ == "__main__":
    main()