from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.speed("slowest")
colormode(255)


def draw_shape(number_of_sides):
    for j in range(number_of_sides):
        tim.forward(100)
        tim.right(360 / number_of_sides)


for sides_number in range(3, 11):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(sides_number)

screen = Screen()
screen.exitonclick()
