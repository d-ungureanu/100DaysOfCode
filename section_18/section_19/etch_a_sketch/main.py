from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """Move turtle 10 units forward"""
    tim.forward(10)


def move_backwards():
    """Moe turtle 10 units backward"""
    tim.backward(10)


def turn_counter_clock():
    """Turns turtle 10 units counter-clockwise"""
    tim.left(10)


def turn_clockwise():
    """Turns turtle 10 units clockwise"""
    tim.right(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clock)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
