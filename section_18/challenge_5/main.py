import turtle as t
import random


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


tim = t.Turtle()
t.speed("fastest")
t.colormode(255)


for i in range(0, 360, 5):
    t.color(random_color())
    t.setheading(i)
    t.circle(100)

screen = t.Screen()
screen.exitonclick()
