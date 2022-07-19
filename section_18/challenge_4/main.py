from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed("fast")
colormode(255)
tim.width(15)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


for i in range(25):
    tim.pencolor(random_color())
    number_of_turns = random.randint(0, 3)
    turn_direction = random.choice(["left", "right"])
    for _ in range(number_of_turns):
        if turn_direction == "left":
            tim.left(90)
        else:
            tim.right(90)
    tim.forward(50)

print(type(random_color()))

screen = Screen()
screen.exitonclick()
